// EU-27 shared data and chrome. Figures copied from eu27.cloud on 2026-10-06.
window.EU27 = {
  // iso, name, holdings verified /39, tier 0 verified /9, sourced facts, fact-check withheld
  countries: [["AT","Austria",31,8,65,4],["BE","Belgium",20,8,43,0],["BG","Bulgaria",31,8,46,3],["HR","Croatia",29,9,60,1],["CY","Cyprus",30,6,63,3],["CZ","Czechia",32,9,64,5],["DK","Denmark",28,7,61,1],["EE","Estonia",26,6,53,3],["FI","Finland",16,8,33,0],["FR","France",35,9,73,3],["DE","Germany",27,8,54,1],["EL","Greece",32,9,60,2],["HU","Hungary",31,9,78,8],["IE","Ireland",27,6,62,8],["IT","Italy",27,7,60,1],["LV","Latvia",20,5,49,0],["LT","Lithuania",6,2,21,0],["LU","Luxembourg",5,1,21,0],["MT","Malta",19,8,32,1],["NL","Netherlands",25,8,51,0],["PL","Poland",32,8,49,1],["PT","Portugal",27,9,49,5],["RO","Romania",15,4,28,1],["SK","Slovakia",29,7,51,0],["SI","Slovenia",30,9,68,1],["ES","Spain",30,7,57,1],["SE","Sweden",24,7,45,3]]
    .map(([iso,name,h,t,f,w])=>({iso,name,h,t,f,w})),
  // Rough geographic tile positions [col,row]
  pos:{SE:[4,0],FI:[5,0],IE:[0,1],DK:[3,1],EE:[5,1],NL:[2,2],DE:[3,2],PL:[4,2],LV:[5,2],BE:[1,3],LU:[2,3],CZ:[3,3],SK:[4,3],LT:[5,3],FR:[1,4],AT:[3,4],HU:[4,4],RO:[5,4],PT:[0,5],ES:[1,5],IT:[2,5],SI:[3,5],HR:[4,5],BG:[5,5],MT:[2,6],EL:[5,6],CY:[6,6]}
};

(function(){
  const PAGES=[["index.html","Overview"],["ranking.html","Ranking"],["countries.html","Countries"],["holdings.html","Critical holdings"],["hosting.html","Hosting"],["sources.html","Sources"],["ask.html","Ask"],["methodology.html","Methodology"],["fact-check.html","Fact check"]];
  const here=document.body.dataset.page||"index.html";
  const links=PAGES.map(([h,l])=>`<a href="${h}"${h===here?' aria-current="page"':''}>${l}</a>`).join("");
  const nav=document.createElement("nav");nav.className="nav";nav.setAttribute("aria-label","Primary");
  nav.innerHTML=`<div class="wrap"><a class="brand" href="index.html" aria-label="EU27.CLOUD home"><img class="badge" src="badge.png" alt=""><img class="wm logo-l" src="wordmark.png" alt="EU27.CLOUD"><img class="wm logo-d" src="wordmark-white.png" alt="EU27.CLOUD"></a><div class="links">${links}</div><button class="nav-btn theme-btn" id="themeBtn" type="button"></button><button class="nav-btn menu-btn" id="menuBtn" type="button" aria-expanded="false">Menu</button></div><div class="drawer" id="drawer" hidden><div class="wrap">${links}</div></div>`;
  document.body.prepend(nav);

  const foot=document.createElement("footer");foot.className="foot";
  foot.innerHTML=`<div class="wrap"><a class="foot-brand" href="index.html" aria-label="EU27.CLOUD, European Union Data Sovereignty Initiative"><img class="badge" src="badge.png" alt=""><img class="lockup logo-l" src="lockup.png" alt="EU27.CLOUD, European Union Data Sovereignty Initiative"><img class="lockup logo-d" src="lockup-white.png" alt="EU27.CLOUD, European Union Data Sovereignty Initiative"></a><span>Design mockup · figures from eu27.cloud, 6 October 2026</span></div>`;
  document.body.append(foot);

  const mb=document.getElementById("menuBtn"),dr=document.getElementById("drawer");
  mb.addEventListener("click",()=>{dr.hidden=!dr.hidden;mb.setAttribute("aria-expanded",!dr.hidden)});

  const root=document.documentElement,btn=document.getElementById("themeBtn");
  try{const s=localStorage.getItem("eu27-theme");if(s)root.dataset.theme=s}catch(e){}
  const isDark=()=>root.dataset.theme?root.dataset.theme==="dark":!matchMedia("(prefers-color-scheme: light)").matches;
  const SUN='<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.5v2.2M12 19.3v2.2M2.5 12h2.2M19.3 12h2.2M5.3 5.3l1.6 1.6M17.1 17.1l1.6 1.6M5.3 18.7l1.6-1.6M17.1 6.9l1.6-1.6"/></svg>';
  const MOON='<svg viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><path d="M20.5 14.6A8.5 8.5 0 0 1 9.4 3.5a8.5 8.5 0 1 0 11.1 11.1z"/></svg>';
  // Show the mode you switch to: a sun while dark, a moon while light
  const label=()=>{const d=isDark();btn.innerHTML=d?SUN:MOON;btn.setAttribute("aria-label",d?"Switch to light mode":"Switch to dark mode");btn.title=d?"Light mode":"Dark mode"};
  btn.addEventListener("click",()=>{root.dataset.theme=isDark()?"light":"dark";try{localStorage.setItem("eu27-theme",root.dataset.theme)}catch(e){}label()});
  label();
})();
