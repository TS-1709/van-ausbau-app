import os, json

css = """
:root{--bg:#000;--c1:#1c1c1e;--c2:#2c2c2e;--bdr:#38383a;--t:#f5f5f7;--t2:#98989d;--blue:#0a84ff;--green:#30d158;--red:#ff453a;--orange:#ff9f0a;--yellow:#ffd60a;--purple:#bf5af2;--teal:#64d2ff;--pink:#ff6482}
*{box-sizing:border-box;margin:0;padding:0;-webkit-tap-highlight-color:transparent}
body{font-family:-apple-system,BlinkMacSystemFont,sans-serif;background:var(--bg);color:var(--t);padding:0 16px;padding-bottom:80px;min-height:100vh;-webkit-font-smoothing:antialiased}
.tabs{position:fixed;bottom:0;left:0;right:0;z-index:50;display:flex;background:rgba(0,0,0,.92);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border-top:.5px solid var(--bdr);padding-bottom:max(6px,env(safe-area-inset-bottom))}
.tab{flex:1;padding:7px 0 5px;text-align:center;font-size:10px;color:var(--t2);cursor:pointer;border:none;background:none;font-weight:500}
.tab .ico{font-size:20px;display:block;margin-bottom:1px}.tab.on{color:var(--blue)}
.pg{display:none;padding-bottom:70px}.pg.on{display:block}
.hdr{position:sticky;top:0;z-index:10;background:linear-gradient(#000 70%,transparent);padding:12px 0 14px}
.hdr h1{font-size:28px;font-weight:800;letter-spacing:-.5px}.hdr .sub{font-size:12px;color:var(--t2)}
.sync{position:absolute;top:14px;right:0;font-size:11px}.sync.ok{color:var(--green)}.sync.fail{color:var(--red)}
.bcard{background:linear-gradient(135deg,#1a1a2e,#16213e);border:1px solid var(--bdr);border-radius:16px;padding:16px;margin-bottom:12px}
.brow{display:flex;justify-content:space-between}.blbl{font-size:11px;color:var(--t2);text-transform:uppercase;letter-spacing:.5px}.bval{font-size:24px;font-weight:800}
.bbar{height:6px;background:var(--c2);border-radius:3px;margin-top:10px;overflow:hidden}.bfill{height:100%;border-radius:3px;transition:width .5s}
.bstats{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;margin-top:10px}.bstat{text-align:center}.bstat .v{font-size:15px;font-weight:700}.bstat .l{font-size:10px;color:var(--t2)}
.seg{display:flex;background:var(--c1);border-radius:10px;padding:2px;margin:8px 0}
.seg button{flex:1;padding:7px 0;border:none;background:transparent;color:var(--t2);font-size:12px;font-weight:600;border-radius:8px;cursor:pointer}.seg button.on{background:var(--blue);color:#fff}
.cat-sec{margin-top:10px}.cat-hdr{display:flex;justify-content:space-between;padding:5px 2px;cursor:pointer;user-select:none}
.cat-n{font-size:14px;font-weight:700}.cat-t{font-size:14px;font-weight:700;color:var(--t2);font-variant-numeric:tabular-nums}
.chev{color:var(--t2);font-size:11px;transition:transform .2s;margin-left:4px}.cat-hdr.open .chev{transform:rotate(90deg)}
.row{display:flex;align-items:center;gap:8px;padding:10px;margin:1px 0;background:var(--c1);border-radius:12px;cursor:pointer}.row:active{background:var(--c2)}
.chk{width:22px;height:22px;border-radius:50%;border:2px solid var(--bdr);display:flex;align-items:center;justify-content:center;font-size:12px;flex-shrink:0;transition:all .2s}.chk.on{background:var(--green);border-color:var(--green)}
.rb{flex:1;min-width:0}.rn{font-size:15px;font-weight:500;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.rm{font-size:11px;color:var(--t2);margin-top:1px;display:flex;gap:5px;align-items:center;flex-wrap:wrap}
.badge{padding:1px 5px;border-radius:4px;font-size:9px;font-weight:600}.b-r{background:rgba(255,149,10,.2);color:var(--orange)}.b-a{background:rgba(10,132,255,.2);color:var(--blue)}
.rp{font-size:16px;font-weight:700;font-variant-numeric:tabular-nums;min-width:60px;text-align:right}.rp.off{color:var(--orange)}
.task{display:flex;align-items:flex-start;gap:10px;padding:11px;margin:1px 0;background:var(--c1);border-radius:12px}.task .chk{margin-top:2px}
.task-body{flex:1}.task-text{font-size:15px;line-height:1.4}.task-who{font-size:11px;font-weight:600;margin-top:2px}
.task.done .task-text{color:var(--t2);text-decoration:line-through}
.who-bar{display:flex;gap:6px;margin:6px 0;overflow-x:auto;-webkit-overflow-scrolling:touch}
.who-chip{padding:5px 12px;border-radius:16px;font-size:12px;font-weight:600;border:1px solid var(--bdr);background:transparent;color:var(--t2);cursor:pointer;white-space:nowrap;flex-shrink:0}
.who-chip.on{border-color:var(--blue);background:rgba(10,132,255,.12);color:var(--blue)}
.pk-sec{margin-top:14px;background:var(--c1);border-radius:14px;padding:14px;border:1px solid var(--bdr)}
.pk-hdr{display:flex;justify-content:space-between;align-items:center;margin-bottom:10px}
.pk-title{font-size:16px;font-weight:700}.pk-count{font-size:12px;color:var(--t2)}
.pk-bar{height:4px;background:var(--c2);border-radius:2px;margin-bottom:10px;overflow:hidden}.pk-fill{height:100%;background:var(--green);border-radius:2px;transition:width .3s}
.pk-item{display:flex;align-items:center;gap:10px;padding:8px 0;border-bottom:.5px solid var(--bdr)}.pk-item:last-child{border:none}
.pk-item .chk{width:20px;height:20px;font-size:11px}.pk-item .txt{font-size:15px;flex:1}
.pk-item.packed .txt{color:var(--t2);text-decoration:line-through}
.pk-members{display:flex;gap:4px;margin-bottom:8px}
.pk-member{padding:2px 8px;border-radius:8px;font-size:10px;font-weight:600;background:rgba(191,90,242,.15);color:var(--purple)}
.notes{width:100%;min-height:200px;padding:14px;background:var(--c1);border:1px solid var(--bdr);border-radius:12px;color:var(--t);font-size:15px;font-family:inherit;resize:vertical;line-height:1.6}.notes:focus{outline:none;border-color:var(--blue)}
.ov{position:fixed;inset:0;z-index:100;background:rgba(0,0,0,.6);backdrop-filter:blur(10px);display:none;align-items:flex-end}.ov.show{display:flex}
.sh{background:var(--c1);border-radius:20px 20px 0 0;width:100%;max-width:500px;padding:20px;max-height:85vh;overflow-y:auto;animation:up .3s;padding-bottom:max(20px,env(safe-area-inset-bottom))}
@keyframes up{from{transform:translateY(100%)}}
.sh h2{font-size:19px;font-weight:700;text-align:center;margin-bottom:14px}
.fld{margin-bottom:12px}.fld label{display:block;font-size:12px;color:var(--t2);margin-bottom:3px;font-weight:500}
.fld input,.fld select{width:100%;padding:11px 13px;background:var(--bg);border:1px solid var(--bdr);border-radius:10px;color:var(--t);font-size:16px;font-family:inherit;-webkit-appearance:none}
.fld input:focus,.fld select:focus{outline:none;border-color:var(--blue)}
.ma{display:flex;gap:8px;margin-top:14px}
.mb{flex:1;padding:13px;border:none;border-radius:12px;font-size:15px;font-weight:600;cursor:pointer}
.mb-s{background:var(--green);color:#fff}.mb-d{background:var(--red);color:#fff;flex:.35}.mb-c{background:var(--c2);color:var(--t)}
.toast{position:fixed;top:60px;left:50%;transform:translateX(-50%);padding:10px 20px;border-radius:20px;font-size:13px;font-weight:600;opacity:0;transition:opacity .3s;z-index:200;pointer-events:none;color:#fff}.toast.show{opacity:1}.toast.ok{background:var(--green)}.toast.er{background:var(--red)}
.add-row{display:flex;gap:8px;margin-top:10px}.add-row input{flex:1;padding:10px 12px;background:var(--c1);border:1px solid var(--bdr);border-radius:10px;color:var(--t);font-size:15px;font-family:inherit}.add-row input:focus{outline:none;border-color:var(--blue)}
.add-btn{padding:10px 16px;background:var(--green);color:#fff;border:none;border-radius:10px;font-size:14px;font-weight:600;cursor:pointer;white-space:nowrap}
.family-chips{display:flex;gap:6px;flex-wrap:wrap;margin:6px 0}
.fchip{padding:4px 10px;border-radius:12px;font-size:11px;font-weight:600;border:1.5px solid var(--bdr);background:transparent;color:var(--t2);cursor:pointer}.fchip.on{border-color:var(--purple);background:rgba(191,90,242,.12);color:var(--purple)}
.country-card{background:var(--c1);border:1px solid var(--bdr);border-radius:14px;padding:14px;margin-bottom:10px}
.country-name{font-size:18px;font-weight:700;margin-bottom:8px}
.country-row{display:flex;gap:8px;padding:6px 0;border-bottom:.5px solid var(--bdr);font-size:14px}.country-row:last-child{border:none}
.country-label{font-weight:600;min-width:90px;color:var(--t2);font-size:12px;text-transform:uppercase}
.country-val{flex:1}
.section-title{font-size:13px;color:var(--t2);text-transform:uppercase;letter-spacing:.5px;margin:16px 0 8px;padding-left:2px}
"""

# Split HTML into parts for heredoc
print(f"CSS length: {len(css)}")
with open("/root/van-app/style.css","w") as f: f.write(css)
print("CSS written")
