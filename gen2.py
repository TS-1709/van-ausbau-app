css = """
:root {
  --bg: #0a0a0a;
  --c1: rgba(28,28,30,0.82);
  --c2: rgba(44,44,46,0.6);
  --c3: rgba(58,58,60,0.4);
  --bdr: rgba(255,255,255,0.08);
  --t: #f5f5f7;
  --t2: rgba(245,245,247,0.55);
  --blue: #0a84ff;
  --green: #30d158;
  --red: #ff453a;
  --orange: #ff9f0a;
  --yellow: #ffd60a;
  --purple: #bf5af2;
  --teal: #64d2ff;
  --pink: #ff6482;
}
* { box-sizing: border-box; margin: 0; padding: 0; -webkit-tap-highlight-color: transparent; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text", system-ui, sans-serif;
  background: var(--bg);
  color: var(--t);
  padding: 0 16px;
  padding-bottom: 88px;
  min-height: 100vh;
  -webkit-font-smoothing: antialiased;
  overscroll-behavior: none;
}
body::before {
  content: '';
  position: fixed;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(circle at 30% 20%, rgba(10,132,255,0.06) 0%, transparent 50%),
              radial-gradient(circle at 70% 80%, rgba(191,90,242,0.04) 0%, transparent 50%);
  pointer-events: none;
  z-index: 0;
}
body > * { position: relative; z-index: 1; }

/* Tabs */
.tabs {
  position: fixed; bottom: 0; left: 0; right: 0; z-index: 50;
  display: flex;
  background: rgba(10,10,10,0.92);
  backdrop-filter: saturate(180%) blur(20px);
  -webkit-backdrop-filter: saturate(180%) blur(20px);
  border-top: 0.5px solid rgba(255,255,255,0.08);
  padding-bottom: max(8px, env(safe-area-inset-bottom));
}
.tab {
  flex: 1; padding: 6px 0 4px; text-align: center;
  font-size: 10px; color: var(--t2); cursor: pointer;
  border: none; background: none; font-weight: 500;
  transition: color 0.2s;
}
.tab .ico { font-size: 22px; display: block; margin-bottom: 0px; }
.tab.on { color: var(--blue); }
.tab.on .ico { transform: scale(1.1); }

/* Pages */
.pg { display: none; padding-bottom: 20px; animation: fadeIn 0.25s ease; }
.pg.on { display: block; }
@keyframes fadeIn { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: none; } }

/* Header */
.hdr {
  position: sticky; top: 0; z-index: 10;
  background: rgba(10,10,10,0.85);
  backdrop-filter: saturate(180%) blur(20px);
  -webkit-backdrop-filter: saturate(180%) blur(20px);
  margin: 0 -16px; padding: 12px 16px 16px;
}
.hdr h1 { font-size: 32px; font-weight: 800; letter-spacing: -0.8px; }
.hdr .sub { font-size: 13px; color: var(--t2); margin-top: 2px; }
.sync-dot {
  position: absolute; top: 16px; right: 16px;
  width: 8px; height: 8px; border-radius: 50%;
  transition: background 0.3s;
}
.sync-dot.ok { background: var(--green); box-shadow: 0 0 8px rgba(48,209,88,0.4); }
.sync-dot.fail { background: var(--red); box-shadow: 0 0 8px rgba(255,69,58,0.4); }

/* Glass Card */
.glass {
  background: var(--c1);
  backdrop-filter: blur(40px);
  -webkit-backdrop-filter: blur(40px);
  border: 1px solid var(--bdr);
  border-radius: 20px;
  padding: 20px;
  margin-bottom: 12px;
}

/* Budget */
.budget-header { display: flex; justify-content: space-between; align-items: flex-start; }
.budget-label { font-size: 11px; color: var(--t2); text-transform: uppercase; letter-spacing: 0.8px; font-weight: 600; }
.budget-value { font-size: 36px; font-weight: 800; letter-spacing: -1px; margin-top: 2px; font-variant-numeric: tabular-nums; }
.budget-remain { text-align: right; }
.budget-bar {
  height: 8px; background: rgba(255,255,255,0.06);
  border-radius: 4px; margin-top: 16px; overflow: hidden;
}
.budget-fill {
  height: 100%; border-radius: 4px;
  transition: width 0.8s cubic-bezier(0.34, 1.56, 0.64, 1);
}
.stats-grid {
  display: grid; grid-template-columns: repeat(4, 1fr);
  gap: 12px; margin-top: 16px;
}
.stat-card {
  text-align: center; padding: 12px 8px;
  background: rgba(255,255,255,0.04);
  border-radius: 14px;
  border: 1px solid rgba(255,255,255,0.04);
}
.stat-val { font-size: 18px; font-weight: 700; }
.stat-lbl { font-size: 10px; color: var(--t2); margin-top: 2px; text-transform: uppercase; letter-spacing: 0.5px; }

/* Segment Control */
.seg {
  display: flex; background: rgba(255,255,255,0.06);
  border-radius: 12px; padding: 3px; margin: 12px 0;
}
.seg button {
  flex: 1; padding: 8px 0; border: none; background: transparent;
  color: var(--t2); font-size: 13px; font-weight: 600;
  border-radius: 9px; cursor: pointer; transition: all 0.25s;
}
.seg button.on {
  background: var(--blue); color: white;
  box-shadow: 0 2px 8px rgba(10,132,255,0.3);
}

/* Category */
.cat-section { margin-top: 14px; }
.cat-header {
  display: flex; justify-content: space-between; align-items: center;
  padding: 8px 4px; cursor: pointer; user-select: none;
  border-radius: 8px; transition: background 0.15s;
}
.cat-header:active { background: rgba(255,255,255,0.04); }
.cat-name { font-size: 16px; font-weight: 700; }
.cat-total {
  font-size: 15px; font-weight: 700; color: var(--t2);
  font-variant-numeric: tabular-nums;
}
.chevron {
  color: var(--t2); font-size: 12px;
  transition: transform 0.25s ease; margin-left: 6px;
  display: inline-block;
}
.cat-header.open .chevron { transform: rotate(90deg); }
.cat-items { overflow: hidden; transition: max-height 0.3s ease; }

/* Item Row */
.item-row {
  display: flex; align-items: center; gap: 12px;
  padding: 14px 12px; margin: 2px 0;
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.04);
  border-radius: 16px;
  cursor: pointer;
  transition: all 0.15s;
}
.item-row:active { transform: scale(0.98); background: rgba(255,255,255,0.06); }
.check-circle {
  width: 26px; height: 26px; border-radius: 50%;
  border: 2.5px solid rgba(255,255,255,0.2);
  display: flex; align-items: center; justify-content: center;
  font-size: 14px; flex-shrink: 0;
  transition: all 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
}
.check-circle.done {
  background: var(--green); border-color: var(--green);
  box-shadow: 0 2px 8px rgba(48,209,88,0.3);
}
.item-info { flex: 1; min-width: 0; }
.item-name { font-size: 16px; font-weight: 500; }
.item-meta {
  font-size: 12px; color: var(--t2); margin-top: 3px;
  display: flex; gap: 6px; align-items: center;
}
.item-price {
  font-size: 18px; font-weight: 700;
  font-variant-numeric: tabular-nums;
  min-width: 70px; text-align: right;
}
.item-price.unpaid { color: var(--orange); }
.item-badge {
  display: inline-block; padding: 2px 8px; border-radius: 6px;
  font-size: 10px; font-weight: 700; letter-spacing: 0.3px;
}
.badge-paid { background: rgba(48,209,88,0.15); color: var(--green); }
.badge-open { background: rgba(255,159,10,0.15); color: var(--orange); }

/* Task Row */
.task-row {
  display: flex; align-items: flex-start; gap: 12px;
  padding: 14px 12px; margin: 2px 0;
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.04);
  border-radius: 16px;
}
.task-row.done .task-text { color: var(--t2); text-decoration: line-through; }
.task-body { flex: 1; }
.task-text { font-size: 16px; line-height: 1.4; }
.task-who {
  font-size: 12px; font-weight: 600; margin-top: 4px;
  display: inline-block; padding: 2px 8px; border-radius: 8px;
}
.who-tobi { background: rgba(10,132,255,0.12); color: var(--blue); }
.who-pauline { background: rgba(191,90,242,0.12); color: var(--purple); }
.who-noel { background: rgba(100,210,255,0.12); color: var(--teal); }
.who-raphael { background: rgba(255,100,130,0.12); color: var(--pink); }

/* Who Filter */
.filter-bar {
  display: flex; gap: 8px; margin: 10px 0;
  overflow-x: auto; -webkit-overflow-scrolling: touch;
  padding: 2px 0;
}
.filter-chip {
  padding: 7px 14px; border-radius: 20px;
  font-size: 13px; font-weight: 600;
  border: 1.5px solid rgba(255,255,255,0.1);
  background: transparent; color: var(--t2);
  cursor: pointer; white-space: nowrap; flex-shrink: 0;
  transition: all 0.2s;
}
.filter-chip.on { border-color: var(--blue); background: rgba(10,132,255,0.12); color: var(--blue); }

/* Packlist */
.pk-section {
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.05);
  border-radius: 20px; padding: 18px; margin-top: 12px;
}
.pk-head { display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; }
.pk-title { font-size: 17px; font-weight: 700; }
.pk-count { font-size: 13px; color: var(--t2); }
.pk-members { display: flex; gap: 4px; margin-bottom: 10px; }
.pk-member-tag {
  padding: 3px 10px; border-radius: 10px;
  font-size: 11px; font-weight: 600;
  background: rgba(191,90,242,0.1); color: var(--purple);
}
.pk-progress { height: 4px; background: rgba(255,255,255,0.06); border-radius: 2px; margin-bottom: 12px; overflow: hidden; }
.pk-progress-fill { height: 100%; background: var(--green); border-radius: 2px; transition: width 0.4s ease; }
.pk-item {
  display: flex; align-items: center; gap: 12px;
  padding: 10px 0; border-bottom: 0.5px solid rgba(255,255,255,0.05);
}
.pk-item:last-child { border: none; }
.pk-check {
  width: 24px; height: 24px; border-radius: 7px;
  border: 2px solid rgba(255,255,255,0.15);
  display: flex; align-items: center; justify-content: center;
  font-size: 13px; cursor: pointer; flex-shrink: 0;
  transition: all 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
}
.pk-check.on { background: var(--green); border-color: var(--green); box-shadow: 0 2px 6px rgba(48,209,88,0.25); }
.pk-item-text { font-size: 15px; flex: 1; }
.pk-item.packed .pk-item-text { color: var(--t2); text-decoration: line-through; }

/* Country Card */
.country-card {
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.05);
  border-radius: 20px; padding: 18px; margin-bottom: 10px;
}
.country-name { font-size: 20px; font-weight: 700; margin-bottom: 12px; }
.country-row { display: flex; gap: 12px; padding: 8px 0; border-bottom: 0.5px solid rgba(255,255,255,0.05); }
.country-row:last-child { border: none; }
.country-label { font-weight: 600; min-width: 80px; color: var(--t2); font-size: 12px; text-transform: uppercase; letter-spacing: 0.5px; }
.country-value { flex: 1; font-size: 14px; line-height: 1.4; }
.emergency { color: var(--red); font-weight: 700; font-size: 16px; }

/* Add Row */
.add-row {
  display: flex; gap: 8px; margin-top: 14px;
  background: rgba(255,255,255,0.03);
  border: 1px solid rgba(255,255,255,0.06);
  border-radius: 16px; padding: 6px;
}
.add-row input {
  flex: 1; padding: 12px 14px;
  background: transparent; border: none;
  color: var(--t); font-size: 16px; font-family: inherit;
}
.add-row input:focus { outline: none; }
.add-row input::placeholder { color: var(--t2); }
.add-row input[type="number"] { max-width: 80px; text-align: right; }
.add-btn {
  padding: 12px 18px; background: var(--green);
  color: white; border: none; border-radius: 12px;
  font-size: 18px; font-weight: 700; cursor: pointer;
  transition: transform 0.15s, box-shadow 0.15s;
}
.add-btn:active { transform: scale(0.92); box-shadow: 0 2px 12px rgba(48,209,88,0.3); }

/* Category Selector */
.cat-select-row {
  display: flex; gap: 8px; margin-top: 8px; align-items: center;
}
.cat-select {
  flex: 1; padding: 10px 14px;
  background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08);
  border-radius: 12px; color: var(--t); font-size: 14px;
  -webkit-appearance: none; font-family: inherit;
}
.new-cat-btn {
  padding: 10px 14px; background: rgba(255,255,255,0.06);
  border: 1px dashed rgba(255,255,255,0.15);
  border-radius: 12px; color: var(--t2); font-size: 13px;
  cursor: pointer; white-space: nowrap; transition: all 0.2s;
}
.new-cat-btn:active { background: rgba(255,255,255,0.1); }

/* Notes */
.notes-area {
  width: 100%; min-height: 180px; padding: 16px;
  background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.06);
  border-radius: 16px; color: var(--t);
  font-size: 16px; font-family: inherit; resize: vertical;
  line-height: 1.6;
}
.notes-area:focus { outline: none; border-color: var(--blue); }

/* Settings Fields */
.settings-group { margin-top: 20px; padding-top: 16px; border-top: 0.5px solid rgba(255,255,255,0.08); }
.field { margin-bottom: 16px; }
.field label {
  display: block; font-size: 12px; color: var(--t2);
  margin-bottom: 6px; font-weight: 600;
  text-transform: uppercase; letter-spacing: 0.5px;
}
.field input, .field textarea {
  width: 100%; padding: 14px 16px;
  background: rgba(255,255,255,0.04); border: 1px solid rgba(255,255,255,0.08);
  border-radius: 14px; color: var(--t); font-size: 16px;
  font-family: inherit; -webkit-appearance: none;
  transition: border-color 0.2s;
}
.field input:focus, .field textarea:focus { outline: none; border-color: var(--blue); }

/* Buttons */
.btn-primary {
  width: 100%; padding: 16px;
  background: var(--blue); color: white;
  border: none; border-radius: 14px;
  font-size: 16px; font-weight: 700; cursor: pointer;
  transition: all 0.2s;
}
.btn-primary:active { transform: scale(0.97); opacity: 0.9; }
.btn-green {
  width: 100%; padding: 14px;
  background: var(--green); color: white;
  border: none; border-radius: 14px;
  font-size: 15px; font-weight: 600; cursor: pointer;
  transition: all 0.2s;
}
.btn-green:active { transform: scale(0.97); }

/* Modal */
.overlay {
  position: fixed; inset: 0; z-index: 100;
  background: rgba(0,0,0,0.6);
  backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px);
  display: none; align-items: flex-end; justify-content: center;
}
.overlay.show { display: flex; }
.sheet {
  background: rgba(28,28,30,0.95);
  backdrop-filter: blur(40px); -webkit-backdrop-filter: blur(40px);
  border-radius: 24px 24px 0 0;
  width: 100%; max-width: 500px; padding: 24px;
  padding-bottom: max(24px, env(safe-area-inset-bottom));
  max-height: 85vh; overflow-y: auto;
  animation: slideUp 0.35s cubic-bezier(0.34, 1.56, 0.64, 1);
  border-top: 0.5px solid rgba(255,255,255,0.1);
}
@keyframes slideUp { from { transform: translateY(100%); } to { transform: none; } }
.sheet h2 { font-size: 20px; font-weight: 700; text-align: center; margin-bottom: 20px; }
.modal-actions { display: flex; gap: 10px; margin-top: 18px; }
.modal-btn {
  flex: 1; padding: 14px; border: none; border-radius: 14px;
  font-size: 16px; font-weight: 600; cursor: pointer;
  transition: all 0.15s;
}
.modal-btn:active { transform: scale(0.95); }
.btn-save { background: var(--green); color: white; }
.btn-cancel { background: rgba(255,255,255,0.08); color: var(--t); }
.btn-delete { background: var(--red); color: white; flex: 0.35; }

/* Toast */
.toast {
  position: fixed; top: 60px; left: 50%; transform: translateX(-50%);
  padding: 12px 24px; border-radius: 24px;
  font-size: 14px; font-weight: 600;
  opacity: 0; transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
  z-index: 200; pointer-events: none; color: white;
  backdrop-filter: blur(10px);
}
.toast.show { opacity: 1; transform: translateX(-50%) translateY(0); }
.toast.success { background: rgba(48,209,88,0.9); box-shadow: 0 4px 20px rgba(48,209,88,0.3); }
.toast.error { background: rgba(255,69,58,0.9); box-shadow: 0 4px 20px rgba(255,69,58,0.3); }

/* Export Button */
.export-row { display: flex; gap: 8px; margin-top: 12px; }
.export-btn {
  flex: 1; padding: 12px;
  background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.08);
  border-radius: 14px; color: var(--t); font-size: 14px; font-weight: 600;
  cursor: pointer; text-align: center; transition: all 0.2s;
}
.export-btn:active { background: rgba(255,255,255,0.1); transform: scale(0.97); }

/* Readiness */
.readiness { text-align: center; padding: 16px; }
.readiness-pct { font-size: 48px; font-weight: 800; letter-spacing: -2px; }
.readiness-lbl { font-size: 13px; color: var(--t2); margin-top: 2px; }
"""

with open("style.css", "w") as f:
    f.write(css)
print(f"CSS: {len(css)} bytes")
