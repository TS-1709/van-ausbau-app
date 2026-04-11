import os

css = open("style.css").read()

html = """<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover,user-scalable=no">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Roadtrip">
<title>🚐 Europa Roadtrip</title>
<style>""" + css + """</style>
</head>
<body>
"""

html += """
<div class="pg on" id="pOv">
<div class="hdr"><h1 id="tripTitle">🚐 Roadtrip</h1><div class="sub" id="subT"></div><div class="sync" id="dot">●</div></div>
<div class="bcard">
<div class="brow"><div><div class="blbl">Budget</div><div class="bval" id="bB">—</div></div><div style="text-align:right"><div class="blbl">Verbleibend</div><div class="bval" id="bR">—</div></div></div>
<div class="bbar"><div class="bfill" id="bBar"></div></div>
<div class="bstats">
<div class="bstat"><div class="v" id="bP">—</div><div class="l">Bezahlt</div></div>
<div class="bstat"><div class="v" id="bO">—</div><div class="l">Offen</div></div>
<div class="bstat"><div class="v" id="bC">—</div><div class="l">Erledigt</div></div>
</div></div>
<div class="seg"><button class="on" onclick="sf('all',this)">Alle</button><button onclick="sf('Anschaffung',this)">📦 Neu</button><button onclick="sf('Reparatur',this)">🔧 Rep.</button></div>
<div id="ilist"></div>
<div style="margin-top:14px">
<div class="add-row"><input type="text" id="addName" placeholder="Neue Position..." onkeydown="if(event.key==='Enter')document.getElementById('addPrice').focus()"><input type="number" id="addPrice" placeholder="€" inputmode="decimal" style="max-width:80px" onkeydown="if(event.key==='Enter')quickAdd()"><button class="add-btn" onclick="quickAdd()">+</button></div>
<div style="margin-top:8px"><select id="addCatSelect" style="width:100%;padding:10px;background:var(--c1);border:1px solid var(--bdr);border-radius:10px;color:var(--t);font-size:14px;-webkit-appearance:none"></select></div>
<div style="margin-top:6px"><button style="background:var(--c2);color:var(--t);border:none;padding:8px 14px;border-radius:8px;font-size:13px;cursor:pointer" onclick="showNewCat()">+ Neue Kategorie</button></div>
</div></div>
"""

html += """
<div class="pg" id="pT">
<div class="hdr"><h1>✅ Aufgaben</h1><div class="sub" id="tsub"></div></div>
<div class="who-bar" id="whoBar"></div>
<div id="tlist"></div>
<div class="add-row"><input type="text" id="tIn" placeholder="Neue Aufgabe..." onkeydown="if(event.key==='Enter')addTask()"><button class="add-btn" onclick="addTask()">+</button></div>
</div>
"""

html += """
<div class="pg" id="pP">
<div class="hdr"><h1>🎒 Packliste</h1><div class="sub" id="psub"></div></div>
<div class="family-chips" id="pkFilter"></div>
<div id="plist"></div>
<div style="margin-top:14px">
<div class="fld"><input type="text" id="pkNewCat" placeholder="Neue Kategorie (z.B. 🛶 Kajak)"></div>
<div class="fld"><input type="text" id="pkNewCatMembers" placeholder="Für wen? (kommagetrennt, leer=alle)"></div>
<button class="mb mb-s" style="width:100%;padding:12px" onclick="addPkCat()">+ Kategorie erstellen</button>
</div></div>
"""

html += """
<div class="pg" id="pC">
<div class="hdr"><h1>🌍 Länder-Infos</h1><div class="sub">Vignetten, Umweltzonen, Notfall</div></div>
<div id="clist"></div>
</div>
"""

html += """
<div class="pg" id="pN">
<div class="hdr"><h1>📝 Mehr</h1></div>
<textarea class="notes" id="nArea" placeholder="Planung, Einkaufsliste, Ideen..."></textarea>
<button class="mb mb-s" style="width:100%;margin-top:12px;padding:12px" onclick="saveNotes()">💾 Notizen speichern</button>
<div style="margin-top:20px;border-top:1px solid var(--bdr);padding-top:16px">
<div class="fld"><label>Reise-Name</label><input type="text" id="fTrip" placeholder="Europa Roadtrip 2026"></div>
<div class="fld"><label>Budget (€)</label><input type="number" id="fBud" inputmode="decimal"></div>
<div class="fld"><label>Familie (Namen, komma-getrennt)</label><input type="text" id="fFam" placeholder="Tobi, Pauline, Noel, Raphael"></div>
<div class="fld"><label>Kategorien (eine pro Zeile)</label><textarea id="fCats" class="notes" rows="5" style="min-height:100px"></textarea></div>
<button class="mb mb-s" style="width:100%;padding:12px" onclick="saveSettings()">💾 Einstellungen</button>
</div></div>
"""

html += """
<div class="tabs">
<div class="tab on" onclick="gt('Ov',this)"><span class="ico">🚐</span>Kosten</div>
<div class="tab" onclick="gt('T',this)"><span class="ico">✅</span>Aufgaben</div>
<div class="tab" onclick="gt('P',this)"><span class="ico">🎒</span>Packen</div>
<div class="tab" onclick="gt('C',this)"><span class="ico">🌍</span>Länder</div>
<div class="tab" onclick="gt('N',this)"><span class="ico">📝</span>Mehr</div>
</div>
"""

html += """
<div class="ov" id="mI"><div class="sh">
<h2 id="mT">Bearbeiten</h2>
<div class="fld"><label>Was?</label><input type="text" id="fN"></div>
<div class="fld"><label>Preis (€)</label><input type="number" id="fPr" inputmode="decimal"></div>
<div class="fld"><label>Kategorie</label><select id="fCat"></select></div>
<div class="fld"><label style="display:flex;align-items:center;gap:8px"><input type="checkbox" id="fPd" style="width:auto"> Bezahlt</label></div>
<div class="fld"><label style="display:flex;align-items:center;gap:8px"><input type="checkbox" id="fDn" style="width:auto"> Erledigt</label></div>
<div class="ma"><button class="mb mb-c" onclick="cm()">Abbrechen</button><button class="mb mb-d" id="dBtn" onclick="di()" style="display:none">🗑</button><button class="mb mb-s" onclick="si()">Speichern</button></div>
</div></div>
"""

html += """
<div class="ov" id="mCat"><div class="sh">
<h2>Neue Kategorie</h2>
<div class="fld"><label>Name (mit Emoji!)</label><input type="text" id="newCatName" placeholder="z.B. 🛶 Kajak"></div>
<div class="ma"><button class="mb mb-c" onclick="document.getElementById('mCat').classList.remove('show')">Abbrechen</button><button class="mb mb-s" onclick="addNewCat()">Erstellen</button></div>
</div></div>
<div class="toast" id="toast"></div>
"""

# Now the JavaScript - this is the big part
html += """
<script>
const API="/api/data";
let D=null,fil="all",who="all",pkF="all",eid=-1;
const icons={"Tobi":"👨","Pauline":"👩","Noel":"🧒","Raphael":"👶"};

async function ld(){
  try{const r=await fetch(API);D=await r.json();dot("ok","● Online")}
  catch(e){dot("fail","● Offline");const s=localStorage.getItem("v5");if(s)D=JSON.parse(s)}
  rn()
}
async function sy(){
  try{await fetch(API,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(D)});
  localStorage.setItem("v5",JSON.stringify(D));dot("ok","●")}
  catch(e){localStorage.setItem("v5",JSON.stringify(D));dot("fail","●")}
}
function dot(c,t){const d=document.getElementById("dot");d.className="sync "+c;d.textContent=t}
function fm(n){return n.toLocaleString("de-DE")+" €"}
function es(s){return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;")}
function ic(n){return(D.familyIcons&&D.familyIcons[n])||(icons[n]||"👤")}

function rn(){
  if(!D)return;
  document.getElementById("tripTitle").textContent="🚐 "+(D.tripName||"Roadtrip");
  const total=D.items.reduce((s,i)=>s+i.price,0);
  const paid=D.items.filter(i=>i.paid).reduce((s,i)=>s+i.price,0);
  const done=D.items.filter(i=>i.done).length;
  const budget=D.budget||5000, remain=budget-total;
  const pct=Math.min(100,(total/budget)*100);
  document.getElementById("bB").textContent=fm(budget);
  const rE=document.getElementById("bR");rE.textContent=fm(remain);rE.style.color=remain<0?"var(--red)":"var(--green)";
  document.getElementById("bP").textContent=fm(paid);
  document.getElementById("bO").textContent=fm(total-paid);
  document.getElementById("bC").textContent=done+"/"+D.items.length;
  const bar=document.getElementById("bBar");
  bar.style.width=pct+"%";
  bar.style.background=pct>90?"var(--red)":pct>70?"var(--orange)":"var(--green)";
  document.getElementById("subT").textContent=D.items.length+" Positionen — "+fm(total);

  const vis=D.items.filter(i=>fil==="all"||i.type===fil);
  const cats={};
  vis.forEach(i=>{if(!cats[i.cat])cats[i.cat]=[];cats[i.cat].push(i)});
  let h="";
  Object.entries(cats).sort(([a],[b])=>a.localeCompare(b)).forEach(([cat,list])=>{
    const ct=list.reduce((s,i)=>s+i.price,0);
    h+='<div class="cat-sec"><div class="cat-hdr open" onclick="tc(this)"><span class="cat-n">'+cat+'</span><span><span class="cat-t">'+fm(ct)+'</span><span class="chev">›</span></span></div><div class="ci">';
    list.forEach(item=>{
      const idx=D.items.indexOf(item);
      h+='<div class="row" onclick="ei('+idx+')">';
      h+='<div class="chk '+(item.done?'on':'')+'" onclick="event.stopPropagation();td('+idx+')">'+(item.done?'✓':'')+'</div>';
      h+='<div class="rb"><div class="rn">'+es(item.name)+'</div><div class="rm">';
      h+=(item.paid?'<span style="color:var(--green)">✅</span>':'<span style="color:var(--orange)">⏳</span>');
      h+='</div></div><div class="rp '+(item.paid?'':'off')+'">'+fm(item.price)+'</div></div>';
    });
    h+='</div></div>';
  });
  if(!vis.length)h='<div style="text-align:center;padding:40px;color:var(--t2)"><div style="font-size:48px">🚐</div>Noch keine Einträge</div>';
  document.getElementById("ilist").innerHTML=h;

  const sel=document.getElementById("addCatSelect");
  sel.innerHTML=(D.categories||[]).map(c=>'<option value="'+c+'">'+c+'</option>').join("");

  // Tasks
  const family=D.family||[];
  let wb='<button class="who-chip '+(who==="all"?'on':'')+'" onclick="sw(\\'all\\',this)">Alle</button>';
  family.forEach(f=>{wb+='<button class="who-chip '+(who===f?'on':'')+'" onclick="sw(\\''+f+'\\',this)">'+ic(f)+' '+es(f)+'</button>'});
  wb+='<button class="who-chip '+(who===""?'on':'')+'" onclick="sw(\\'\\',this)">📋 Niemand</button>';
  document.getElementById("whoBar").innerHTML=wb;

  const tvis=D.tasks.filter(t=>who==="all"||(who===""?!t.who:t.who===who));
  const tdone=tvis.filter(t=>t.done).length;
  document.getElementById("tsub").textContent=tdone+"/"+tvis.length+" erledigt";
  let th="";
  tvis.forEach(task=>{
    const idx=D.tasks.indexOf(task);
    const wo=task.who?'<div class="task-who" style="color:var(--purple)">'+ic(task.who)+' '+es(task.who)+'</div>':'';
    th+='<div class="task '+(task.done?'done':'')+'"><div class="chk '+(task.done?'on':'')+'" onclick="tt('+idx+')">'+(task.done?'✓':'')+'</div><div class="task-body"><div class="task-text">'+es(task.text)+'</div>'+wo+'</div></div>';
  });
  document.getElementById("tlist").innerHTML=th||'<div style="text-align:center;padding:30px;color:var(--t2)">Alles erledigt! 🎉</div>';

  rnPk(); rnC();
  document.getElementById("nArea").value=D.notes||"";
  document.getElementById("fBud").value=D.budget||5000;
  document.getElementById("fFam").value=(D.family||[]).join(", ");
  document.getElementById("fTrip").value=D.tripName||"";
  document.getElementById("fCats").value=(D.categories||[]).join("\\n");
}

function rnPk(){
  if(!D||!D.packlist)return;
  const family=D.family||[];
  let fc='<button class="fchip '+(pkF==="all"?'on':'')+'" onclick="spk(\\'all\\',this)">Alle</button>';
  family.forEach(f=>{fc+='<button class="fchip '+(pkF===f?'on':'')+'" onclick="spk(\\''+f+'\\',this)">'+ic(f)+' '+es(f)+'</button>'});
  document.getElementById("pkFilter").innerHTML=fc;
  let ph="";let tp=0,pp=0;
  Object.entries(D.packlist).forEach(([cat,data])=>{
    const items=data.items||data;const members=data.members||[];
    if(pkF!=="all"&&members.length&&!members.includes(pkF))return;
    const pk=items.filter(i=>i.packed).length;tp+=items.length;pp+=pk;
    const pct2=items.length?Math.round(pk/items.length*100):0;
    const memHtml=members.length?'<div class="pk-members">'+members.map(m=>'<span class="pk-member">'+ic(m)+' '+es(m)+'</span>').join("")+'</div>':'';
    ph+='<div class="pk-sec"><div class="pk-hdr"><div><div class="pk-title">'+cat+'</div>'+memHtml+'</div><span class="pk-count">'+pk+'/'+items.length+'</span></div>';
    ph+='<div class="pk-bar"><div class="pk-fill" style="width:'+pct2+'%"></div></div>';
    items.forEach((item,i)=>{
      ph+='<div class="pk-item '+(item.packed?'packed':'')+'"><div class="chk '+(item.packed?'on':'')+'" onclick="tpk(\\''+cat.replace(/'/g,"\\\\'")+'\\','+i+')">'+(item.packed?'✓':'')+'</div><div class="txt">'+es(item.text)+'</div></div>';
    });
    ph+='<div class="add-row" style="margin-top:8px"><input type="text" placeholder="+ Item..." onkeydown="if(event.key==\\'Enter\\')addPkItem(this,\\''+cat.replace(/'/g,"\\\\'")+'\\')"><button class="add-btn" onclick="addPkItem(this.previousElementSibling,\\''+cat.replace(/'/g,"\\\\'")+'\\')">+</button></div>';
    ph+='</div>';
  });
  document.getElementById("psub").textContent=pp+"/"+tp+" eingepackt";
  document.getElementById("plist").innerHTML=ph||'<div style="text-align:center;padding:30px;color:var(--t2)">Noch keine Listen</div>';
}

function rnC(){
  if(!D||!D.countries)return;
  let h="";
  Object.entries(D.countries).forEach(([name,info])=>{
    h+='<div class="country-card"><div class="country-name">'+name+'</div>';
    h+='<div class="country-row"><div class="country-label">Vignette</div><div class="country-val">'+es(info.vignette||"—")+'</div></div>';
    h+='<div class="country-row"><div class="country-label">Umwelt</div><div class="country-val">'+es(info.umwelt||"—")+'</div></div>';
    h+='<div class="country-row"><div class="country-label">Notfall</div><div class="country-val" style="color:var(--red);font-weight:700">'+es(info.notfall||"—")+'</div></div>';
    h+='<div class="country-row"><div class="country-label">Sprache</div><div class="country-val">'+es(info.sprache||"—")+'</div></div>';
    h+='</div>';
  });
  document.getElementById("clist").innerHTML=h;
}

function gt(n,el){document.querySelectorAll(".pg").forEach(p=>p.classList.remove("on"));document.getElementById("p"+n).classList.add("on");document.querySelectorAll(".tab").forEach(t=>t.classList.remove("on"));el.classList.add("on")}
function sf(f,el){fil=f;document.querySelectorAll("#pOv .seg button").forEach(b=>b.classList.remove("on"));el.classList.add("on");rn()}
function sw(w,el){who=w;document.querySelectorAll(".who-chip").forEach(b=>b.classList.remove("on"));el.classList.add("on");rn()}
function spk(f,el){pkF=f;document.querySelectorAll(".fchip").forEach(b=>b.classList.remove("on"));el.classList.add("on");rnPk()}
function tc(el){el.classList.toggle("open");el.nextElementSibling.style.display=el.classList.contains("open")?"":"none"}
async function td(idx){D.items[idx].done=!D.items[idx].done;if(D.items[idx].done)D.items[idx].paid=true;await sy();rn()}
async function tt(idx){D.tasks[idx].done=!D.tasks[idx].done;await sy();rn()}
async function tpk(cat,i){D.packlist[cat].items[i].packed=!D.packlist[cat].items[i].packed;await sy();rnPk()}
async function addPkItem(input,cat){const t=input.value.trim();if(!t)return;D.packlist[cat].items.push({text:t,packed:false});input.value="";await sy();rnPk();ts("✓","ok")}
async function addPkCat(){const n=document.getElementById("pkNewCat").value.trim();if(!n)return;const m=document.getElementById("pkNewCatMembers").value.split(",").map(s=>s.trim()).filter(Boolean);if(!D.packlist[n])D.packlist[n]={members:m,items:[]};document.getElementById("pkNewCat").value="";document.getElementById("pkNewCatMembers").value="";await sy();rn();ts("✓ "+n,"ok")}

function om(idx){eid=typeof idx==="number"?idx:-1;document.getElementById("mT").textContent=eid>=0?"Bearbeiten":"Neue Position";document.getElementById("dBtn").style.display=eid>=0?"":"none";const s=document.getElementById("fCat");s.innerHTML=(D.categories||[]).map(c=>'<option value="'+c+'">'+c+'</option>').join("");if(eid>=0){const i=D.items[eid];document.getElementById("fN").value=i.name;document.getElementById("fPr").value=i.price;s.value=i.cat;document.getElementById("fPd").checked=i.paid;document.getElementById("fDn").checked=i.done}else{document.getElementById("fN").value="";document.getElementById("fPr").value="";document.getElementById("fPd").checked=false;document.getElementById("fDn").checked=false}document.getElementById("mI").classList.add("show");setTimeout(()=>document.getElementById("fN").focus(),300)}
function ei(idx){om(idx)}
function cm(){document.getElementById("mI").classList.remove("show")}
async function si(){const n=document.getElementById("fN").value.trim();if(!n)return;const p=parseFloat(document.getElementById("fPr").value)||0;const c=document.getElementById("fCat").value;const pd=document.getElementById("fPd").checked;const dn=document.getElementById("fDn").checked;const item={name:n,price:p,cat:c,type:"Anschaffung",paid:pd,done:dn};if(eid>=0){item.id=D.items[eid].id;item.type=D.items[eid].type;D.items[eid]=item}else{item.id=D.nextId||(D.nextId=D.items.length+1);D.nextId++;D.items.push(item)}cm();await sy();rn();ts(eid>=0?"✓ Aktualisiert":"✓ Hinzugefügt","ok")}
async function di(){if(eid<0)return;if(!confirm('"'+es(D.items[eid].name)+'" löschen?'))return;D.items.splice(eid,1);cm();await sy();rn();ts("🗑","er")}
async function quickAdd(){const n=document.getElementById("addName").value.trim();if(!n)return;const p=parseFloat(document.getElementById("addPrice").value)||0;const c=document.getElementById("addCatSelect").value;D.items.push({id:D.nextId||(D.nextId=D.items.length+1),name:n,price:p,cat:c,type:"Anschaffung",paid:false,done:false});D.nextId++;document.getElementById("addName").value="";document.getElementById("addPrice").value="";await sy();rn();ts("✓ "+n,"ok")}
function showNewCat(){document.getElementById("mCat").classList.add("show");setTimeout(()=>document.getElementById("newCatName").focus(),300)}
async function addNewCat(){const n=document.getElementById("newCatName").value.trim();if(!n)return;if(!D.categories.includes(n))D.categories.push(n);document.getElementById("newCatName").value="";document.getElementById("mCat").classList.remove("show");await sy();rn();ts("✓ "+n,"ok")}
async function addTask(){const t=document.getElementById("tIn").value.trim();if(!t)return;D.tasks.push({id:D.nextTaskId||(D.nextTaskId=D.tasks.length+1),text:t,who:"",done:false});D.nextTaskId=(D.nextTaskId||D.tasks.length)+1;document.getElementById("tIn").value="";await sy();rn();ts("✓","ok")}
async function saveNotes(){D.notes=document.getElementById("nArea").value;await sy();ts("💾","ok")}
async function saveSettings(){D.budget=parseFloat(document.getElementById("fBud").value)||5000;D.family=document.getElementById("fFam").value.split(",").map(s=>s.trim()).filter(Boolean);D.tripName=document.getElementById("fTrip").value||"Roadtrip";D.categories=document.getElementById("fCats").value.split("\\n").map(s=>s.trim()).filter(Boolean);await sy();rn();ts("✓","ok")}
function ts(m,c){const t=document.getElementById("toast");t.textContent=m;t.className="toast show "+c;setTimeout(()=>t.className="toast",2000)}
ld();
</script>
</body></html>
"""

with open("index.html","w") as f:
    f.write(html)
print(f"Written {len(html)} bytes")
