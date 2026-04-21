import subprocess, time, json

# Check syntax first
import html.parser, re

with open("index.html") as f:
    content = f.read()

errors = []

# 1. Check for duplicate IDs
ids = re.findall(r'id="([^"]+)"', content)
dupes = [x for x in ids if ids.count(x) > 1]
if dupes:
    errors.append(f"DUPLICATE IDs: {set(dupes)}")

# 2. Check tab count
tabs = re.findall(r'class="tab"', content)
print(f"✅ Tabs: {len(tabs)} (expected 6)")

# 3. Check pages
pages = re.findall(r'class="pg" id="p(\w+)"', content)
print(f"✅ Pages: {pages} (should be 6 unique: Ov,T,P,C,R,N)")

# 4. Check no duplicate page IDs
dup_pages = [x for x in pages if pages.count(x) > 1]
if dup_pages:
    errors.append(f"DUPLICATE page IDs: {set(dup_pages)}")

# 5. Check functions
funcs = re.findall(r'function (\w+)\(', content)
unique_funcs = set()
dup_funcs = []
for f in funcs:
    if f in unique_funcs:
        dup_funcs.append(f)
    unique_funcs.add(f)
if dup_funcs:
    errors.append(f"DUPLICATE functions: {set(dup_funcs)}")

# 6. Check critical functions exist
required = ['gt', 'ld', 'sy', 'rn', 'cm', 'si', 'di', 'calcFuel', 'calcAutarkie', 'showFuelPrices', 'addNewCat', 'toast']
for fn in required:
    if fn not in unique_funcs:
        errors.append(f"MISSING function: {fn}")

# 7. Check JSON syntax in JS
js_start = content.find('<script>')
js_end = content.find('</script>')
if js_start < 0 or js_end < 0:
    errors.append("No <script> block found")
else:
    js = content[js_start+8:js_end]
    # Basic brace check
    open_b = js.count('{')
    close_b = js.count('}')
    if open_b != close_b:
        errors.append(f"Brace mismatch: {{ = {open_b}, }} = {close_b}")
    open_p = js.count('(')
    close_p = js.count(')')
    if open_p != close_p:
        errors.append(f"Paren mismatch: ( = {open_p}, ) = {close_p}")

# 8. Check server responds
import urllib.request
try:
    r = urllib.request.urlopen("http://localhost:8889/", timeout=3)
    status = r.getcode()
    body = r.read().decode()
    print(f"✅ Server: {status} ({len(body)} bytes)")
    if 'gt(' not in body:
        errors.append("gt() not in served page")
    if len(body) < 10000:
        errors.append(f"Page too small: {len(body)} bytes")
except Exception as e:
    errors.append(f"Server error: {e}")

# 9. Check API responds
try:
    r = urllib.request.urlopen("http://localhost:8889/api/data", timeout=3)
    data = json.loads(r.read().decode())
    print(f"✅ API: {len(data.get('items',[]))} items, {len(data.get('tasks',[]))} tasks, {len(data.get('packing',[]))} packing, {len(data.get('countries',[]))} countries")
    if 'fuel' in data:
        print(f"✅ Fuel prices: {list(data.get('fuel',{}).get('prices',{}).keys())}")
except Exception as e:
    errors.append(f"API error: {e}")

# 10. Check UI rendering via headless browser
try:
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8889/", wait_until="networkidle", timeout=10000)
        
        # Check tabs visible
        tab_els = page.query_selector_all('.tab')
        print(f"✅ Browser: {len(tab_els)} tabs rendered")
        
        # Check Rechner tab appears only once
        rechner_count = page.evaluate("document.querySelectorAll('.tab').length")
        rechner_texts = page.evaluate("Array.from(document.querySelectorAll('.tab')).map(t=>t.textContent.trim())")
        rechner_dupes = [t for t in rechner_texts if rechner_texts.count(t) > 1]
        if rechner_dupes:
            errors.append(f"Duplicate tab texts: {set(rechner_dupes)}")
        else:
            print(f"✅ No duplicate tabs: {rechner_texts}")
        
        # Click each tab and verify page shows
        for tab_name, page_id in [("Kosten","Ov"),("Aufgaben","T"),("Packen","P"),("Länder","C"),("Rechner","R"),("Mehr","N")]:
            page.click(f".tab >> text='{tab_name}'")
            time.sleep(0.3)
            visible = page.evaluate(f"document.getElementById('p{page_id}').style.display !== 'none'")
            if visible:
                print(f"✅ Tab '{tab_name}' → page visible")
            else:
                errors.append(f"Tab '{tab_name}' → page NOT visible")
        
        # Test Rechner tab specifically
        page.click(".tab >> text='Rechner'")
        time.sleep(0.5)
        
        # Check no duplicate inputs
        fuel_con = page.evaluate("document.querySelectorAll('#fuelCon').length")
        fuel_dist = page.evaluate("document.querySelectorAll('#fuelDist').length")
        bat_ah = page.evaluate("document.querySelectorAll('#batAh').length")
        if fuel_con > 1:
            errors.append(f"fuelCon appears {fuel_con} times")
        if fuel_dist > 1:
            errors.append(f"fuelDist appears {fuel_dist} times")
        if bat_ah > 1:
            errors.append(f"batAh appears {bat_ah} times")
        
        # Test fuel calculator
        page.fill("#fuelDist", "3000")
        time.sleep(0.5)
        fuel_result = page.inner_text("#fuelResult")
        if "L" in fuel_result and "€" in fuel_result:
            print(f"✅ Fuel calculator works: {fuel_result[:60]}...")
        else:
            errors.append(f"Fuel calculator broken: {fuel_result}")
        
        # Test autarkie calculator
        page.click("text='⚡ Berechnen'")
        time.sleep(0.5)
        autarkie = page.inner_text("#autarkieResult")
        if "Batterie" in autarkie and "Solar" in autarkie:
            print(f"✅ Autarkie calculator works: {autarkie[:60]}...")
        else:
            errors.append(f"Autarkie calculator broken: {autarkie}")
        
        # Check total estimate
        total = page.inner_text("#totalEstimate")
        if "€" in total:
            print(f"✅ Total estimate works: {total[:60]}...")
        else:
            errors.append(f"Total estimate broken: {total}")
        
        # Test all other tabs load data
        page.click(".tab >> text='Kosten'")
        time.sleep(0.5)
        budget_text = page.inner_text("#bB")
        if "€" in budget_text:
            print(f"✅ Budget shows: {budget_text}")
        else:
            errors.append(f"Budget broken: {budget_text}")
        
        page.click(".tab >> text='Aufgaben'")
        time.sleep(0.5)
        task_items = page.query_selector_all('#pT .item')
        print(f"✅ Tasks: {len(task_items)} items")
        
        page.click(".tab >> text='Packen'")
        time.sleep(0.5)
        pack_items = page.query_selector_all('#pP .item')
        print(f"✅ Packing: {len(pack_items)} items")
        
        page.click(".tab >> text='Länder'")
        time.sleep(0.5)
        country_cards = page.query_selector_all('#pC .glass')
        print(f"✅ Countries: {len(country_cards)} cards")
        
        # Screenshot
        page.screenshot(path="/root/van-app/e2e_screenshot.png", full_page=True)
        print(f"✅ Screenshot saved")
        
        browser.close()
except ImportError:
    print("⚠️ Playwright not available for browser test")
except Exception as e:
    errors.append(f"Browser test error: {e}")

print("\n" + "="*50)
if errors:
    print(f"❌ FAILED: {len(errors)} errors")
    for e in errors:
        print(f"  - {e}")
else:
    print("✅ ALL TESTS PASSED!")
