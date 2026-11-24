/* hourly.js v82 — hzvideo (muted looping YouTube embed, poster still fallback). v80 — reusable scene library for the hourly day schedules (days/YYYY-MM-DD.json). ES5 only. Requires wow.js helpers (wEl, wCv, wLoop, WOW).
   Data-driven templates: hzphoto (quiet:1 = dim ambient still, tiny caption, fade only) hzquote hzriddle hzsteps hzfact.  Living art: hzpend hzgalton hzharmono hzphyllo hzboids hzfourier hzripple hzmonte hzulam hzfirefly hzsleep.
   Illusions: hzcafe hzebb hzkaniz hzlilac hzstep hzhermann hzafter.  v56: hzpwave hzlangton hzchaos hzmaze hzkoch hzaurora + illusions hzcheck hzdrift.  v58: hzchladni hzsort hzspiro hzrose hzmoire hzkoi + illusion hzzoll.  v59: hzturing hzvoronoi hzcollatz hzsnow + illusions hzpogg hzwhite.  v60: hzdla hzsandpile hzgalaxy hzmoonsea + illusions hzhering hzponzo.  v62: hzlorenz hzlife hztree hzdragon hzrainwin + illusions hzmuller hzjastrow.  v63: group templates hzwelcome hzchoose hzguess + party game hzstroop.  v64: hzmeta hzkaleido hzyakamoz (calm night) + illusions hzmib hzcorn hzfraser.  v66: hzfern hzhilbert hzorrery hzfener + hzshepard hzbezold.  v68: hzflow hzlissa hzrule hzlantern + hzscint hzchecker.  v69: hzmandel hzbuffon hzember (calm night) + illusions hzouchi hzmach hzbarber.  v71: hztimes hzmonty hztsp hzbalikci (calm night) + illusions hzcurve hzpinna.  v73: hzrecaman hzsieve hzhalve hzyayla (calm night) + illusions hzwaterfall hztroxler.  v66: hzfern hzhilbert hzorrery hzfener (calm night) + illusions hzshepard hzbezold.  v75: hzpack hzbenford hzbirthday hztren (calm night) + illusions hzsilence hzsfm.  v76: hzclifford hzperc hzstop hzkoy (calm night) + illusions hzneon hzocclude.  v77: hzphysarum hzaxelrod hzcrowd hzstartrail (calm night) + illusions hzdelboeuf hzwagon.  v78: hzglowworm (calm imagined glowworm cave).  v79: hzdoublepend hzhanoi hzwalk hzwhale (calm night) + illusions hzbenham hzenigma.  v80: hzpenrose (Penrose tiling) + fixes: fitEl waits until the scene is attached; stronger caption gradient on hzphoto.  See README.md "Hourly day schedule". */
(function(){
var s=document.createElement('style');s.innerHTML="@font-face{font-family:HzScript;src:url(f/GreatVibes.ttf)}@font-face{font-family:HzBrush;src:url(f/Dancing.ttf)}"+
".hz{position:absolute;left:5vw;right:5vw;text-align:center;color:#f3f1ec;font-family:Georgia,serif;text-shadow:0 2px 16px rgba(0,0,0,.75);box-sizing:border-box;overflow-wrap:break-word;word-wrap:break-word}"+
".hz .lb{font-family:Helvetica,Arial,sans-serif;letter-spacing:.28em;font-size:1.15vw;color:#8fd3c1;text-transform:uppercase;line-height:1.35;margin:0}"+
".hz .q{font-size:2.85vw;line-height:1.22;margin-top:.45vw}.hz .e{font-size:1.6vw;color:#c3cdd2;font-style:italic;margin-top:.4vw;line-height:1.3}"+
".hz .a{font-size:2.4vw;color:#ff9e7a;line-height:1.22;margin:0}.hz .sm{font-family:Helvetica,Arial,sans-serif;font-size:1.1vw;color:#95a5ad;margin-top:.4vw;letter-spacing:.03em;line-height:1.4}"+
".hzin{opacity:0;animation:hzin 1.8s cubic-bezier(.33,1,.68,1) forwards}@keyframes hzin{from{opacity:0;transform:translateY(1.2vw)}to{opacity:1;transform:none}}"+
".hzw{display:inline-block;clip-path:inset(0 100% 0 0);-webkit-clip-path:inset(0 100% 0 0);animation:hzw 5s linear forwards}@keyframes hzw{to{clip-path:inset(0 0 0 0);-webkit-clip-path:inset(0 0 0 0)}}"+
".hzbox{display:inline-block;background:rgba(4,9,14,.78);padding:1.2vw 2.4vw;border-radius:.7vw;max-width:100%;box-sizing:border-box}"+
".hz-top{top:3.2vh;bottom:auto;max-height:24vh;overflow:hidden}.hz-bot{bottom:3vh;top:auto;max-height:22vh;overflow:hidden}"+
".hz-credit{bottom:1.5vh;top:auto;left:5vw;right:5vw;max-height:5vh;overflow:hidden}.hz-credit .sm{margin:0;font-size:1vw;line-height:1.3}"+
".hz-mid{top:26vh;bottom:24vh;left:5vw;right:5vw;display:flex;flex-direction:column;justify-content:center;gap:1.1vh;overflow:hidden}"+
".hz-qzone{top:6vh;bottom:24vh;left:5vw;right:5vw;display:flex;flex-direction:column;justify-content:center;overflow:hidden}"+
".hz-qzone .qln{font-family:HzScript,Georgia,serif;font-size:4.2vw;line-height:1.7;text-shadow:none;margin:0}";
document.head.appendChild(s);
function u(css){if(!css)return css;return String(css).replace(/(top|bottom|left|right|padding|margin|margin-top|font-size|width|height|line-height):(\s*)(-?[\d.]+)px/g,function(m,prop,sp,n){n=+n;if(prop==='left'||prop==='right'||prop==='width'||prop==='font-size')return prop+':'+sp+(n/1920*100).toFixed(3)+'vw';return prop+':'+sp+(n/1080*100).toFixed(3)+'vh'})}
function uhtml(h){if(!h)return h;return String(h).replace(/font-size:(\s*)(-?[\d.]+)px/g,function(m,sp,n){return 'font-size:'+sp+(+n/1920*100).toFixed(3)+'vw'}).replace(/margin-top:(\s*)(-?[\d.]+)px/g,function(m,sp,n){return 'margin-top:'+sp+(+n/1080*100).toFixed(3)+'vh'})}
function T(L,h,css,dl){var d=wEl('div','hz hzin',uhtml(h),u(css));d.style.animationDelay=(dl||0.4)+'s';L.appendChild(d);return d}
function fitEl(el,maxVh){if(!el)return;if(!document.documentElement.contains(el)){var tr=0;(function w(){if(document.documentElement.contains(el))fitEl(el,maxVh);else if(++tr<60)setTimeout(w,50)})();return}/* rev 80: scenes are built before they are attached; measuring then gave 0, so shrink-to-fit never ran */var max=maxVh/100*(el.ownerDocument.documentElement.clientHeight||1080),g=0;while(el.scrollHeight>max+2&&g<8){g++;var ns=el.querySelectorAll('.q,.e,.a,.sm,div,span');for(var i=0;i<ns.length;i++){var fs=parseFloat(getComputedStyle(ns[i]).fontSize);if(fs>10)ns[i].style.fontSize=(fs*0.88)+'px'}}}

function hd(lb,q,e){return '<div class="lb">'+lb+'</div><div class="q">'+q+'</div>'+(e?'<div class="e">'+e+'</div>':'')}
function ease(t){t=Math.max(0,Math.min(1,t));return t<.5?4*t*t*t:1-Math.pow(-2*t+2,3)/2}
function cl(t){return Math.max(0,Math.min(1,t))}
function grad(L,a,b){L.style.background='radial-gradient(ellipse at 50% 40%,'+a+','+b+' 78%)'}
function stars(n){var S=[];for(var i=0;i<n;i++)S.push([Math.random()*1920,Math.random()*1080,Math.random()*1.7+.3,Math.random()*6.28]);return S}
function drawStars(x,S,t){for(var i=0;i<S.length;i++){x.globalAlpha=.35+.35*Math.sin(t*.7+S[i][3]);x.fillStyle='#fff';x.fillRect(S[i][0],S[i][1],S[i][2],S[i][2])}x.globalAlpha=1}
var W=WOW;

/* ---------- data templates ---------- */
/* still photo (never moves). it: f, lb, tr, en, cr, fact/facte, fit:'contain', cp:'top' */
W.hzphoto=function(L,it){L.style.background='#000';
 if(it.quiet){
  var dim=it.dim==null?0.7:it.dim, con=it.con==null?0.92:it.con;
  var m=wEl('img','');m.src=it.f;
  m.style.cssText='position:absolute;top:0;left:0;width:100%;height:100%;object-fit:'+(it.fit||'cover')+';object-position:'+(it.pos||'50% 50%')+';filter:brightness('+dim+') contrast('+con+')';
  L.appendChild(m);
  var v=wEl('div','');v.style.cssText='position:absolute;inset:0;pointer-events:none;background:radial-gradient(ellipse at 50% 45%,rgba(0,0,0,0) 42%,rgba(0,0,0,.5) 100%)';
  L.appendChild(v);
  if(it.tr||it.cr){
    var op=it.capop==null?0.34:it.capop;
    var html='<div style="opacity:'+op+';font-family:Helvetica,Arial,sans-serif;text-align:left;text-shadow:0 1px 10px rgba(0,0,0,.8)">';
    if(it.tr) html+='<div style="font-size:1.05vw;letter-spacing:.08em;color:#e8eef2;font-weight:400">'+it.tr+(it.en?' <span style="font-style:italic;opacity:.8">· '+it.en+'</span>':'')+'</div>';
    if(it.cr) html+='<div style="font-size:.68vw;color:#c5ced4;margin-top:.35vh;letter-spacing:.04em">'+it.cr+'</div>';
    html+='</div>';
    L.appendChild(wEl('div','',html,'position:absolute;left:3vw;right:3vw;bottom:2.6vh;top:auto;text-align:left;z-index:2'));
  }
  L.tri='fade';L.dur=it.d;L.corner=false;return L}
 if(it.fit=='contain'){var b=wEl('img','');b.src=it.f;b.style.cssText='position:absolute;top:-4vw;left:-4vw;width:108vw;height:108vh;object-fit:cover;filter:blur(30px) brightness(.35)';L.appendChild(b)}
 var m=wEl('img','');m.src=it.f;m.style.cssText='position:absolute;top:0;left:0;width:100%;height:100%;object-fit:'+(it.fit||'cover')+';object-position:'+(it.pos||'50% 50%');L.appendChild(m);
 var top=it.cp=='top';
 L.appendChild(wEl('div','',null,'position:absolute;left:0;right:0;'+(top?'top:0':'bottom:0')+';height:64%;background:linear-gradient('+(top?'rgba(0,0,0,.88),rgba(0,0,0,.56) 48%,transparent':'transparent,rgba(0,0,0,.56) 45%,rgba(0,0,0,.9)')+')'));
 var body='<div class="lb">'+it.lb+'</div><div class="q">'+it.tr+'</div><div class="e">'+it.en+'</div>'+(it.fact?'<div class="sm" style="font-size:1.25vw;color:#dfe6e9;margin-top:.7vw">'+it.fact+'<br><i style="color:#b3bfc5">'+it.facte+'</i></div>':'');
 var cap=T(L,body,(top?'top:4vh;bottom:auto;max-height:36vh':'bottom:7.2vh;top:auto;max-height:36vh'),1.2);cap.style.overflow='hidden';
 T(L,'<div class="sm">'+it.cr+'</div>','',1.6).className+=' hz-credit';
 fitEl(cap,36);return L};

var PAL={ink:['#efe6d3','#d9ccb2','#1f2b3b','#5a4a3a','#7a8a9a'],night:['#13213a','#08101e','#f1ece0','#a9b7c9','#6f86a8'],clay:['#3a2119','#1a0d09','#f6e3cf','#d3b39a','#b0563c'],sea:['#0f3a40','#061a1d','#eef6f2','#a9cfc6','#3f8f88']};
W.hzquote=function(L,it){var p=PAL[it.pal||'ink'],c=wCv(L),x=c.getContext('2d');var g=x.createRadialGradient(960,500,100,960,540,1150);g.addColorStop(0,p[0]);g.addColorStop(1,p[1]);x.fillStyle=g;x.fillRect(0,0,1920,1080);
 for(var i=0;i<14;i++){var bx=Math.random()*1920,by=Math.random()*1080,br=150+Math.random()*380,bg=x.createRadialGradient(bx,by,0,bx,by,br);bg.addColorStop(0,'rgba('+(p[4]=='#7a8a9a'?'120,138,154':p[4]=='#6f86a8'?'111,134,168':p[4]=='#b0563c'?'176,86,60':'63,143,136')+',.10)');bg.addColorStop(1,'rgba(0,0,0,0)');x.fillStyle=bg;x.fillRect(bx-br,by-br,2*br,2*br)}
 for(i=0;i<9000;i++){x.fillStyle='rgba('+(Math.random()<.5?'0,0,0':'255,255,255')+','+(Math.random()*.05)+')';x.fillRect(Math.random()*1920,Math.random()*1080,1+Math.random()*2,1+Math.random()*2)}
 x.strokeStyle=p[4];x.globalAlpha=.55;x.lineWidth=2;x.strokeRect(70,60,1780,960);x.globalAlpha=.3;x.strokeRect(84,74,1752,932);x.globalAlpha=1;
 var ln=it.tr.split('|');
 var nch=ln.join('').length,fs=it.fs? (it.fs/1920*100).toFixed(2)+'vw' : (nch>90?3.4:nch>55?4.0:4.6)+'vw';
 var h='<div class="lb" style="color:'+p[4]+';text-shadow:none;margin-bottom:1.6vh">'+(it.lb||'Mevlânâ’dan · From Rumi')+'</div>';
 for(i=0;i<ln.length;i++)h+='<div class="qln" style="font-size:'+fs+';color:'+p[2]+'"><span class="hzw" style="animation-delay:'+(1.2+i*4)+'s">'+ln[i]+'</span></div>';
 var qz=T(L,h,'',0.2);qz.className+=' hz-qzone';qz.style.textShadow='none';
 var attr=T(L,'<div style="width:6vw;height:2px;background:'+p[4]+';margin:0 auto 1.4vh"></div><div class="e" style="color:'+p[3]+';text-shadow:none;font-size:1.55vw">'+it.en+'</div><div class="sm" style="color:'+p[3]+';text-shadow:none">'+(it.by||'Mevlânâ’ya atfedilir · attributed to Rumi')+' — yazı çizimi · lettering illustration</div>','',1.6);
 attr.className+=' hz-bot';attr.style.maxHeight='20vh';return L};

W.hzriddle=function(L,it){grad(L,it.c1||'#1d2f3c',it.c2||'#05080c');var sec=it.sec||18;
 var q=T(L,hd(it.lb||'Bilmece · Riddle',it.q,it.qe),'',.5);q.className+=' hz-top';q.style.maxHeight='42vh';q.style.top='7vh';fitEl(q,42);
 var bot=T(L,(it.hint?'<div class="sm" id="hzhint" style="font-size:1.3vw;margin-bottom:1.2vh">'+it.hint+'</div>':'')+'<div id="hzcd" class="lb" style="color:#ff9e7a;min-height:2vw"></div><div id="hzans" style="opacity:0;transition:opacity .8s"><div class="a">'+it.a+'</div><div class="e">'+it.ae+'</div></div>','',1);
 bot.className+=' hz-bot';bot.style.maxHeight='36vh';
 wLoop(L,function(t){var r=Math.ceil(sec-t),cd=bot.querySelector('#hzcd'),an=bot.querySelector('#hzans');if(cd)cd.textContent=(r>0&&t>4)?'Cevap · Answer: '+r:'';if(an&&t>=sec+0.6)an.style.opacity=1});return L};

W.hzsteps=function(L,it){var st=it.start||5,gp=it.gap||5,n=it.steps.length;
 if(it.f){var m=wEl('img','');m.src=it.f;m.style.cssText='position:absolute;top:0;left:0;width:100%;height:100%;object-fit:cover;filter:brightness(.28) blur(2px)';L.appendChild(m)}else grad(L,it.c1||'#102233',it.c2||'#03060a');
 if(it.bg=='stars'){var c=wCv(L),x=c.getContext('2d'),S=stars(260);wLoop(L,function(t){x.clearRect(0,0,1920,1080);drawStars(x,S,t)})}
 var hdEl=T(L,hd(it.lb,it.q,it.e),'',.4);hdEl.className+=' hz-top';fitEl(hdEl,22);
 var html='';for(var i=0;i<n;i++){var r=it.steps[i];html+='<div class="hzin" style="animation-delay:'+(st+i*gp)+'s;font-size:1.7vw;line-height:1.3"><span>'+r[0]+'</span> <span style="font-size:1.3vw;color:#a9b6bc;font-style:italic">· '+r[1]+'</span>'+(r[2]?'&nbsp;&nbsp;<span class="a" style="font-size:2.1vw">'+r[2]+'</span>':'')+'</div>'}
 var mid=T(L,html,'',0);mid.className='hz hz-mid';
 if(it.fin){var fn=T(L,'<div class="a" style="font-size:2.1vw">'+it.fin+'</div><div class="e" style="font-size:1.45vw">'+it.fine+'</div>','',st+n*gp+1);fn.className+=' hz-bot';fn.style.maxHeight='20vh'}
 return L};

W.hzfact=function(L,it){if(it.f){var m=wEl('img','');m.src=it.f;m.style.cssText='position:absolute;top:0;left:0;width:100%;height:100%;object-fit:cover;filter:brightness(.3)';L.appendChild(m)}else grad(L,it.c1||'#1a2b36',it.c2||'#04070a');
 var el=T(L,'<div class="lb">'+(it.lb||'Biliyor muydunuz? · Did you know?')+'</div><div class="a" style="font-size:8vw;margin:1.5vh 0 1vh;font-family:Helvetica,Arial,sans-serif;font-weight:200">'+it.big+'</div><div class="q" style="font-size:2.5vw">'+it.tr+'</div><div class="e">'+it.en+'</div><div class="sm">'+(it.src||'')+'</div>','top:8vh;bottom:6vh;left:8vw;right:8vw;display:flex;flex-direction:column;justify-content:center;overflow:hidden',.6);
 fitEl(el,84);return L};

/* ---------- living art & simulations ---------- */
W.hzpend=function(L,it){L.style.background='#04060c';var c=wCv(L),x=c.getContext('2d');
 T(L,hd('Kaos · Chaos — simülasyon · simulation','Kelebek Etkisi','The Butterfly Effect'),'top:40px',.4);
 T(L,'<div class="sm" style="font-size:1.354vw;color:#dfe6e9">İki sarkaç neredeyse aynı başladı: aradaki fark sadece 0,001°<br><i>Two pendulums started almost the same — just 0.001° apart</i></div>','bottom:44px',3);
 function P(a){return {a1:a,a2:a,w1:0,w2:0,tr:[]}}var A=[P(2.4),P(2.4+0.001*Math.PI/180)],col=['#8fd3c1','#ff9e7a'],ox=960,oy=380,l=210,g=9.81;
 function stp(p,dt){var m=1,d=p.a1-p.a2,den=2*m+m-m*Math.cos(2*d);var a1=(-g*(3*m)*Math.sin(p.a1)-m*g*Math.sin(p.a1-2*p.a2)-2*Math.sin(d)*m*(p.w2*p.w2*1+p.w1*p.w1*Math.cos(d)))/(1*den);var a2=(2*Math.sin(d)*(p.w1*p.w1*2*m+g*2*m*Math.cos(p.a1)+p.w2*p.w2*m*Math.cos(d)))/(1*den);p.w1+=a1*dt;p.w2+=a2*dt;p.a1+=p.w1*dt;p.a2+=p.w2*dt}
 var last=0;wLoop(L,function(t){var dt=Math.min(.05,t-last);last=t;for(var k=0;k<A.length;k++){for(var s2=0;s2<10;s2++)stp(A[k],dt*1.4/10);var p=A[k],x1=ox+l*Math.sin(p.a1),y1=oy+l*Math.cos(p.a1),x2=x1+l*Math.sin(p.a2),y2=y1+l*Math.cos(p.a2);p.tr.push([x2,y2]);if(p.tr.length>260)p.tr.shift();p.p=[x1,y1,x2,y2]}
  x.clearRect(0,0,1920,1080);for(k=0;k<A.length;k++){var p=A[k];x.strokeStyle=col[k];x.lineWidth=2.5;x.beginPath();for(var i=0;i<p.tr.length;i++){x.globalAlpha=i/p.tr.length*.8;if(i)x.lineTo(p.tr[i][0],p.tr[i][1]);else x.moveTo(p.tr[i][0],p.tr[i][1])}x.stroke();x.globalAlpha=1;
   x.strokeStyle='rgba(230,236,240,.7)';x.lineWidth=4;x.beginPath();x.moveTo(ox,oy);x.lineTo(p.p[0],p.p[1]);x.lineTo(p.p[2],p.p[3]);x.stroke();x.fillStyle=col[k];x.beginPath();x.arc(p.p[2],p.p[3],14,0,7);x.fill()}
  x.fillStyle='#ddd';x.beginPath();x.arc(ox,oy,7,0,7);x.fill()});return L};

W.hzgalton=function(L,it){grad(L,'#16283a','#04070b');var c=wCv(L),x=c.getContext('2d'),R=13,top=250,dx=56,dy=38,B=[],bins=[],i,mx=0;for(i=0;i<=R;i++)bins.push(0);
 T(L,'<div class="hzbox">'+hd('Akıllı Düşünce · Clever Thinking — simülasyon · simulation','Rastgelelikten düzen çıkar','Order out of randomness')+'</div>','top:30px',.4);
 T(L,'<div class="sm" style="font-size:1.302vw;color:#dfe6e9">Her top her çivide yazı-tura atar: sağ ya da sol. Yine de hep aynı çan eğrisi oluşur — Galton tahtası, 1889<br><i>Each ball flips a coin at every peg. Yet the same bell curve always appears — Galton board, 1889</i></div>','bottom:30px',8);
 var last=0,acc=0;wLoop(L,function(t){var dt=Math.min(.05,t-last);last=t;acc+=dt;while(acc>.07){acc-=.07;if(B.length<120)B.push({r:0,k:0,p:0})}
  x.clearRect(0,0,1920,1080);x.fillStyle='#9fb3bf';for(var r=0;r<R;r++)for(var k=0;k<=r;k++){x.beginPath();x.arc(960+(k-r/2)*dx,top+r*dy,5,0,7);x.fill()}
  for(i=B.length-1;i>=0;i--){var b=B[i];b.p+=dt*4.2;if(b.p>=1){b.p=0;b.r++;if(Math.random()<.5)b.k++;if(b.r>=R){bins[b.k]++;B.splice(i,1);continue}}
   var x0=960+(b.k-b.r/2)*dx,y0=top+b.r*dy-14,k2=b.k+(b.dir=(b.dir===undefined||b.p<.05)?(Math.random()<.5?0:1):b.dir);x.fillStyle='#ff9e7a';x.beginPath();x.arc(x0,y0+b.p*dy,8,0,7);x.fill()}
  var by=950;mx=0;for(i=0;i<=R;i++)mx=Math.max(mx,bins[i]);var sc=mx>0?Math.min(6,240/mx):6;
  for(i=0;i<=R;i++){var bx=960+(i-R/2)*dx;x.fillStyle='#8fd3c1';x.fillRect(bx-dx/2+5,by-bins[i]*sc,dx-10,bins[i]*sc)}
  if(t>20){x.globalAlpha=cl((t-20)/3);x.strokeStyle='#fff';x.lineWidth=3;x.beginPath();var tot=0;for(i=0;i<=R;i++)tot+=bins[i];for(var u=-R/2-.5;u<=R/2+.5;u+=.1){var yy=by-tot*sc*Math.exp(-u*u/(2*R/4))/Math.sqrt(2*Math.PI*R/4);if(u==-R/2-.5)x.moveTo(960+u*dx,yy);else x.lineTo(960+u*dx,yy)}x.stroke();x.globalAlpha=1}});return L};

W.hzharmono=function(L,it){L.style.background='#05070c';var c=wCv(L),x=c.getContext('2d');var f1=2+Math.random()*.02,f2=3+Math.random()*.02,f3=3+Math.random()*.02,f4=2+Math.random()*.02,p1=Math.random()*6,p2=Math.random()*6,d=.0025,tt=0,lx=null,ly,hue=Math.random()*360;
 T(L,hd('Canlı Sanat · Living Art — çizim · illustration','Harmonograf: sarkaçların çizdiği resim','Harmonograph: a picture drawn by pendulums'),'top:40px',.4);
 T(L,'<div class="sm" style="font-size:1.250vw">1840’larda iki sarkaç bir kalemi oynatarak bu desenleri çizerdi · In the 1840s two pendulums moved a pen to draw patterns like this</div>','bottom:40px',5);
 wLoop(L,function(t){for(var k=0;k<40;k++){tt+=.02;var e=Math.exp(-d*tt),X=960+e*(380*Math.sin(f1*tt+p1)+120*Math.sin(f2*tt)),Y=590+e*(300*Math.sin(f3*tt+p2)+90*Math.sin(f4*tt));
  if(lx!==null){x.strokeStyle='hsla('+((hue+tt*.8)%360)+',70%,66%,.55)';x.lineWidth=1.4;x.beginPath();x.moveTo(lx,ly);x.lineTo(X,Y);x.stroke()}lx=X;ly=Y}});return L};

W.hzphyllo=function(L,it){grad(L,'#1c2a1a','#050804');var c=wCv(L),x=c.getContext('2d'),N=0;
 T(L,'<div class="hzbox">'+hd('Doğadaki Matematik · Nature’s Maths — çizim · illustration','Ayçiçeği neden 137,5° sever?','Why do sunflowers love 137.5°?')+'</div>','top:30px',.4);
 T(L,'<div class="hzbox"><div class="sm" style="font-size:1.302vw;color:#e6ece6">Her yeni tohum bir öncekinden 137,5° döner — altın açı. Böylece hiç boşluk kalmaz.<br><i>Each new seed turns 137.5° from the last — the golden angle — so no space is wasted.</i></div></div>','bottom:30px',10);
 wLoop(L,function(t){var tg=Math.min(900,Math.floor(t*34));for(;N<tg;N++){var a=N*137.508*Math.PI/180,r=11*Math.sqrt(N),sz=4+N/120;x.fillStyle='hsl('+(30+N%34*1.4)+','+(60+N%13)+'%,'+(32+(N%21))+'%)';x.beginPath();x.arc(960+r*Math.cos(a),600+r*Math.sin(a)*.98,sz,0,7);x.fill()}});return L};

W.hzboids=function(L,it){var c=wCv(L),x=c.getContext('2d'),N=240,B=[],i,j;for(i=0;i<N;i++)B.push([200+Math.random()*1500,250+Math.random()*500,Math.random()*4-2,Math.random()*2-1]);
 var sky=x.createLinearGradient(0,0,0,1080);sky.addColorStop(0,'#2b3a5c');sky.addColorStop(.55,'#c98a7a');sky.addColorStop(.75,'#f2c19a');sky.addColorStop(1,'#3a3040');
 T(L,hd('Canlı Sanat · Living Art — simülasyon · simulation','Sığırcık sürüsü: lider yok, yine de dans','A starling murmuration: no leader, still a dance'),'top:40px',.4);
 T(L,'<div class="sm" style="font-size:1.302vw;color:#fff">Her kuş sadece en yakın 7 komşusuna bakar · Each bird watches only its 7 nearest neighbours</div>','bottom:40px',6);
 wLoop(L,function(t){x.fillStyle=sky;x.fillRect(0,0,1920,1080);x.fillStyle='#1b1a26';x.beginPath();x.moveTo(0,1080);for(var k=0;k<=1920;k+=40)x.lineTo(k,900+Math.sin(k*.003)*50+Math.sin(k*.011)*16);x.lineTo(1920,1080);x.fill();
  var tx=960+520*Math.sin(t*.23),ty=480+160*Math.sin(t*.37);
  for(i=0;i<N;i++){var b=B[i],cx=0,cy=0,vx=0,vy=0,sx=0,sy=0,n=0;for(j=0;j<N;j++){if(i==j)continue;var o=B[j],dx=o[0]-b[0],dy=o[1]-b[1],d2=dx*dx+dy*dy;if(d2<4900){n++;cx+=o[0];cy+=o[1];vx+=o[2];vy+=o[3];if(d2<1100){sx-=dx/d2*40;sy-=dy/d2*40}}}
   if(n){b[2]+=(cx/n-b[0])*.0012+(vx/n-b[2])*.05+sx*.05+(Math.random()-.5)*.25;b[3]+=(cy/n-b[1])*.0012+(vy/n-b[3])*.05+sy*.05+(Math.random()-.5)*.25}b[2]+=(tx-b[0])*.00035;b[3]+=(ty-b[1])*.00035;
   var sp=Math.sqrt(b[2]*b[2]+b[3]*b[3]),m=Math.max(2.2,Math.min(5,sp));b[2]=b[2]/sp*m;b[3]=b[3]/sp*m}
  x.fillStyle='#14121c';for(i=0;i<N;i++){var b=B[i];b[0]+=b[2];b[1]+=b[3];x.beginPath();x.ellipse(b[0],b[1],5,2.2,Math.atan2(b[3],b[2]),0,7);x.fill()}});return L};

W.hzfourier=function(L,it){L.style.background='#050a12';var c=wCv(L),x=c.getContext('2d'),N=160,P=[],F=[],i,k;
 for(i=0;i<N;i++){var u=i/N*2*Math.PI;P.push([16*Math.pow(Math.sin(u),3)*15,-(13*Math.cos(u)-5*Math.cos(2*u)-2*Math.cos(3*u)-Math.cos(4*u))*15])}
 for(k=0;k<N;k++){var re=0,im=0;for(i=0;i<N;i++){var a=2*Math.PI*k*i/N;re+=P[i][0]*Math.cos(a)+P[i][1]*Math.sin(a);im+=P[i][1]*Math.cos(a)-P[i][0]*Math.sin(a)}var fr=k<N/2?k:k-N;F.push([fr,Math.sqrt(re*re+im*im)/N,Math.atan2(im,re)])}
 F.sort(function(a,b){return b[1]-a[1]});F=F.slice(0,40);var path=[];
 T(L,hd('Akıllı Düşünce · Clever Thinking — çizim · illustration','Dönen daireler bir kalp çiziyor','Spinning circles are drawing a heart'),'top:40px',.4);
 T(L,'<div class="sm" style="font-size:1.302vw;color:#dfe6e9">Fourier (1807): her şekil, dönen dairelerin toplamıyla çizilebilir<br><i>Fourier (1807): any shape can be drawn by adding spinning circles</i></div>','bottom:40px',5);
 wLoop(L,function(t){var ph=(t*.16)%1*2*Math.PI;x.clearRect(0,0,1920,1080);var X=960,Y=610;
  for(var j=0;j<F.length;j++){var f=F[j],r=f[1];x.strokeStyle='rgba(143,211,193,.25)';x.lineWidth=1.5;x.beginPath();x.arc(X,Y,r,0,7);x.stroke();var nx=X+r*Math.cos(f[0]*ph+f[2]),ny=Y+r*Math.sin(f[0]*ph+f[2]);x.strokeStyle='rgba(220,235,240,.55)';x.beginPath();x.moveTo(X,Y);x.lineTo(nx,ny);x.stroke();X=nx;Y=ny}
  path.push([X,Y]);if(path.length>420)path.shift();x.strokeStyle='#ff7a6a';x.lineWidth=5;x.beginPath();for(j=0;j<path.length;j++){if(j)x.lineTo(path[j][0],path[j][1]);else x.moveTo(path[j][0],path[j][1])}x.stroke()});return L};

W.hzripple=function(L,it){var c=wCv(L),x=c.getContext('2d'),D=[];
 T(L,hd('Canlı Sanat · Living Art — çizim · illustration','Yağmur halkaları','Rain rings'),'top:40px',.4);
 T(L,'<div class="sm" style="font-size:1.302vw;color:#dfe6e9">Dalgalar birbirine çarpmaz — birbirinin içinden geçer<br><i>Waves don’t collide — they pass right through each other</i></div>','bottom:40px',5);
 var last=0;wLoop(L,function(t){var dt=t-last;last=t;if(Math.random()<dt*2.2)D.push([200+Math.random()*1520,260+Math.random()*640,t]);
  var g=x.createLinearGradient(0,0,0,1080);g.addColorStop(0,'#0b2a33');g.addColorStop(1,'#04121a');x.fillStyle=g;x.fillRect(0,0,1920,1080);
  for(var i=D.length-1;i>=0;i--){var d=D[i],a=t-d[2];if(a>7){D.splice(i,1);continue}for(var r=0;r<4;r++){var rr=a*95-r*26;if(rr<=0)continue;x.strokeStyle='rgba(190,230,235,'+(.5*(1-a/7)*(1-r*.22))+')';x.lineWidth=2.5-r*.4;x.beginPath();x.ellipse(d[0],d[1],rr,rr*.42,0,0,7);x.stroke()}}});return L};

W.hzmonte=function(L,it){grad(L,'#1a2433','#04060a');var c=wCv(L),x=c.getContext('2d'),S=620,X0=660,Y0=300,inn=0,tot=0;x.strokeStyle='#9fb3bf';x.lineWidth=3;x.strokeRect(X0,Y0,S,S);x.beginPath();x.arc(X0,Y0+S,S,-Math.PI/2,0);x.stroke();
 T(L,hd('Akıllı Düşünce · Clever Thinking — simülasyon · simulation','Rastgele noktalarla π bulmak','Finding π with random dots'),'top:40px',.4);
 var V=T(L,'','top:420px;left:1340px;right:auto;text-align:left',1);
 T(L,'<div class="sm" style="font-size:1.250vw;color:#dfe6e9">Çeyrek dairenin içine düşenlerin oranı × 4 ≈ π · Share inside the quarter circle × 4 ≈ π</div>','bottom:40px',4);
 wLoop(L,function(t){var n=Math.min(40,Math.floor(t*3)+2);for(var i=0;i<n&&tot<30000;i++){var u=Math.random(),v=Math.random(),ins=u*u+v*v<=1;if(ins)inn++;tot++;x.fillStyle=ins?'rgba(255,158,122,.85)':'rgba(143,211,193,.85)';x.fillRect(X0+u*S-2,Y0+S-v*S-2,4,4)}
  V.innerHTML='<div class="lb">Nokta · Dots</div><div style="font-size:2.708vw">'+tot.toLocaleString('tr-TR')+'</div><div class="lb" style="margin-top:30px">π ≈</div><div class="a" style="font-size:4.375vw">'+(tot?(4*inn/tot).toFixed(4):'—')+'</div><div class="sm">Gerçek · Real: 3,1416</div>'});return L};

W.hzulam=function(L,it){L.style.background='#04070b';var c=wCv(L),x=c.getContext('2d'),N=0,px=960,py=600,dir=0,len=1,cnt=0,turns=0,STEP=7;
 function pr(n){if(n<2)return false;if(n%2==0)return n==2;for(var d=3;d*d<=n;d+=2)if(n%d==0)return false;return true}
 T(L,'<div class="hzbox">'+hd('Sayı Sırrı · Number Secret — çizim · illustration','Asal sayılar rastgele mi?','Are prime numbers random?')+'</div>','top:24px',.4);
 T(L,'<div class="hzbox"><div class="sm" style="font-size:1.250vw;color:#dfe6e9">1963: Stanislaw Ulam sıkıcı bir konuşmada sayıları spiral yazıp asalları işaretledi — çapraz çizgiler belirdi<br><i>1963: bored in a talk, Ulam wrote numbers in a spiral and marked the primes — diagonal lines appeared</i></div></div>','bottom:24px',12);
 wLoop(L,function(t){var tg=Math.min(26000,Math.floor(t*t*22+t*60));for(;N<tg;N++){var n=N+1;if(pr(n)){x.fillStyle='hsl('+(170+(n%40))+',60%,'+(60+(n%15))+'%)';x.fillRect(px-2.5,py-2.5,5,5)}
   if(dir==0)px+=STEP;else if(dir==1)py-=STEP;else if(dir==2)px-=STEP;else py+=STEP;cnt++;if(cnt==len){cnt=0;dir=(dir+1)%4;turns++;if(turns%2==0)len++}}});return L};

W.hzfirefly=function(L,it){var c=wCv(L),x=c.getContext('2d'),N=90,F=[],i,K=it.k2||0.9;for(i=0;i<N;i++)F.push({x:Math.random()*1920,y:450+Math.random()*520,p:Math.random()*6.283,w:1.0+Math.random()*.12,dx:Math.random()*.4-.2,dy:Math.random()*.3-.15});
 T(L,hd('Doğa · Nature — çizim · illustration','Ateşböcekleri yavaş yavaş birlikte yanıp sönmeye başlıyor','Fireflies slowly begin to blink together'),'top:50px',.6);
 T(L,'<div class="sm" style="font-size:1.302vw;color:#cfd8de">Bazı ormanlarda binlercesi aynı anda ışık yakar — kimse yönetmeden<br><i>In some forests thousands flash in unison — with no one in charge</i></div>','bottom:44px',6);
 var last=0;wLoop(L,function(t){var dt=Math.min(.05,t-last);last=t;var sx=0,sy=0;for(i=0;i<N;i++){sx+=Math.cos(F[i].p);sy+=Math.sin(F[i].p)}var R=Math.sqrt(sx*sx+sy*sy)/N,ps=Math.atan2(sy,sx),k=t<8?0:K*cl((t-8)/20);
  var g=x.createLinearGradient(0,0,0,1080);g.addColorStop(0,'#030612');g.addColorStop(.7,'#0a1424');g.addColorStop(1,'#050a0c');x.fillStyle=g;x.fillRect(0,0,1920,1080);
  x.fillStyle='#02040a';x.beginPath();x.moveTo(0,1080);for(var u=0;u<=1920;u+=30)x.lineTo(u,600+Math.sin(u*.0021)*70+Math.sin(u*.009)*20);x.lineTo(1920,1080);x.fill();
  for(i=0;i<N;i++){var f=F[i];f.p+=dt*(f.w+k*R*Math.sin(ps-f.p));f.x+=f.dx;f.y+=f.dy+Math.sin(t+i)*.1;if(f.x<0)f.x=1920;if(f.x>1920)f.x=0;var b=Math.pow(Math.max(0,Math.cos(f.p)),8);if(b>.02){var rg=x.createRadialGradient(f.x,f.y,0,f.x,f.y,26);rg.addColorStop(0,'rgba(220,255,150,'+b+')');rg.addColorStop(1,'rgba(220,255,150,0)');x.fillStyle=rg;x.fillRect(f.x-26,f.y-26,52,52)}}});return L};

W.hzsleep=function(L,it){var c=wCv(L),x=c.getContext('2d'),S=stars(380),C=[];for(var i=0;i<5;i++)C.push([Math.random()*1920,140+Math.random()*320,300+Math.random()*300]);
 T(L,'<div class="q" style="font-size:5.000vw;font-family:HzScript,Georgia,serif">İyi uykular</div><div class="e" style="font-size:2.188vw">Sleep well</div><div class="sm">Sessiz tepeler, hilal ay — çizim · illustration</div>','top:200px',2);
 wLoop(L,function(t){var g=x.createLinearGradient(0,0,0,1080);g.addColorStop(0,'#03050d');g.addColorStop(.7,'#0f1a33');g.addColorStop(1,'#141d34');x.fillStyle=g;x.fillRect(0,0,1920,1080);drawStars(x,S,t*.4);
  x.fillStyle='#eef0f8';x.beginPath();x.arc(1500,230,70,0,7);x.fill();x.fillStyle='#070b18';x.beginPath();x.arc(1530,210,64,0,7);x.fill();
  for(i=0;i<C.length;i++){var cx=(C[i][0]+t*6)%2400-240,cg=x.createRadialGradient(cx,C[i][1],0,cx,C[i][1],C[i][2]);cg.addColorStop(0,'rgba(140,160,200,.10)');cg.addColorStop(1,'rgba(140,160,200,0)');x.fillStyle=cg;x.fillRect(cx-C[i][2],C[i][1]-C[i][2],C[i][2]*2,C[i][2]*2)}
  var H=[[760,.0018,60,'#0a1122'],[840,.0026,45,'#070c19'],[930,.0035,30,'#04070f']];for(var h=0;h<H.length;h++){x.fillStyle=H[h][3];x.beginPath();x.moveTo(0,1080);for(var u=0;u<=1920;u+=30)x.lineTo(u,H[h][0]+Math.sin(u*H[h][1]+h*2)*H[h][2]);x.lineTo(1920,1080);x.fill()}});return L};

/* ---------- optical illusions ---------- */
W.hzcafe=function(L,it){L.style.background='#0b0f12';var c=wCv(L),x=c.getContext('2d'),s=96,R=7,off=[0,32,64,32];
 T(L,hd('Göz Oyunu · Optical Illusion','Bu yatay çizgiler eğri mi?','Are these horizontal lines tilted?'),'top:40px',.4);
 T(L,'<div class="a">Hepsi tamamen düz ve paralel!</div><div class="e">They are perfectly straight and parallel.</div><div class="sm">Kafe Duvarı illüzyonu · Café Wall illusion (Bristol, 1979)</div>','bottom:36px',15);
 wLoop(L,function(t){x.clearRect(0,0,1920,1080);x.save();x.beginPath();x.rect(80,0,1760,1080);x.clip();var y0=290;for(var r=0;r<R;r++){var y=y0+r*(s*.56+6);x.fillStyle='#777';x.fillRect(80,y-6,1760,6);for(var k=-1;k<20;k++){var xx=80+k*s+off[r%4];x.fillStyle=k%2==0?'#111':'#f4f4f4';x.fillRect(xx,y,s,s*.56)}}x.restore();
  x.fillStyle='#777';x.fillRect(80,y0+R*(s*.56+6)-6,1760,6);var a=ease((t-14)/2);if(a>0){x.globalAlpha=a;x.strokeStyle='#ff6a5a';x.lineWidth=4;for(r=0;r<=R;r++){var yy=y0+r*(s*.56+6)-3;x.beginPath();x.moveTo(60,yy);x.lineTo(1860,yy);x.stroke()}x.globalAlpha=1}});return L};

W.hzebb=function(L,it){L.style.background='#0d141a';var c=wCv(L),x=c.getContext('2d');
 T(L,hd('Göz Oyunu · Optical Illusion','Hangi turuncu daire daha büyük?','Which orange circle is bigger?'),'top:40px',.4);
 T(L,'<div class="a">İkisi de aynı boyutta!</div><div class="e">They are exactly the same size.</div><div class="sm">Ebbinghaus illüzyonu · Ebbinghaus illusion</div>','bottom:40px',15);
 function dot(X,Y,r,col){x.fillStyle=col;x.beginPath();x.arc(X,Y,r,0,7);x.fill()}
 wLoop(L,function(t){x.clearRect(0,0,1920,1080);var a=ease((t-13)/3),fade=1-a,cy=600,Lx=560+a*260,Rx=1360-a*260;
  x.globalAlpha=fade;for(var i=0;i<6;i++){var an=i/6*6.283;dot(560+Math.cos(an)*200,cy+Math.sin(an)*200,95,'#7f97a8')}for(i=0;i<8;i++){an=i/8*6.283;dot(1360+Math.cos(an)*92,cy+Math.sin(an)*92,24,'#7f97a8')}x.globalAlpha=1;
  dot(Lx,cy,58,'#ff8a5c');dot(Rx,cy,58,'#ff8a5c')});return L};

W.hzkaniz=function(L,it){L.style.background='#f2f0ea';var c=wCv(L),x=c.getContext('2d'),cx=960,cy=600,R=270,r=90;
 var d1=T(L,hd('<span style="color:#2a7f74">Göz Oyunu · Optical Illusion</span>','<span style="color:#1b2328;text-shadow:none">Ortadaki beyaz üçgeni görüyor musun?</span>','<span style="color:#56636b;text-shadow:none">Do you see the white triangle in the middle?</span>'),'top:40px;text-shadow:none',.4);
 T(L,'<div class="a" style="color:#c2492f;text-shadow:none">Hiç çizilmedi — beynin tamamladı!</div><div class="e" style="color:#56636b;text-shadow:none">It was never drawn — your brain filled it in.</div><div class="sm" style="color:#6d7a82;text-shadow:none">Kanizsa üçgeni, 1955 · Kanizsa triangle</div>','bottom:36px',15);
 wLoop(L,function(t){x.clearRect(0,0,1920,1080);var rot=t>14?ease((t-14)/2)*Math.PI*(t>24?1-ease((t-24)/2):1):0;
  for(var i=0;i<3;i++){var a=-Math.PI/2+i*2*Math.PI/3,px=cx+R*Math.cos(a),py=cy+20+R*Math.sin(a),to=a+Math.PI+rot;x.fillStyle='#1b2328';x.beginPath();x.moveTo(px,py);x.arc(px,py,r,to+Math.PI/6,to-Math.PI/6+2*Math.PI);x.closePath();x.fill();
   var b=-Math.PI/2+Math.PI/3+i*2*Math.PI/3,qx=cx+R*.95*Math.cos(b+Math.PI),qy=cy+20+R*.95*Math.sin(b+Math.PI);}
  x.strokeStyle='#1b2328';x.lineWidth=7;for(i=0;i<3;i++){var a2=Math.PI/2+i*2*Math.PI/3,vx=cx+R*Math.cos(a2),vy=cy+20+R*Math.sin(a2);var l1=a2+Math.PI+Math.PI/6+Math.PI/2*0,ax=vx+Math.cos(a2+Math.PI-Math.PI/6)*0;
   var p1=[cx+R*Math.cos(a2+2*Math.PI/3),cy+20+R*Math.sin(a2+2*Math.PI/3)],p2=[cx+R*Math.cos(a2-2*Math.PI/3),cy+20+R*Math.sin(a2-2*Math.PI/3)];
   x.beginPath();x.moveTo(vx+(p1[0]-vx)*.22,vy+(p1[1]-vy)*.22);x.lineTo(vx,vy);x.lineTo(vx+(p2[0]-vx)*.22,vy+(p2[1]-vy)*.22);x.stroke()}});return L};

W.hzlilac=function(L,it){L.style.background='#bdbdbd';var c=wCv(L),x=c.getContext('2d'),cx=960,cy=600,R=320;
 T(L,'<div class="lb" style="color:#2b4e48;text-shadow:none">Göz Oyunu · Optical Illusion</div><div class="q" style="color:#1c2226;text-shadow:none;font-size:2.812vw">Sadece ortadaki artıya bak, gözünü ayırma…</div><div class="e" style="color:#3d474d;text-shadow:none">Stare only at the cross in the middle…</div>','top:36px',.4);
 T(L,'<div class="a" style="color:#1f6b3a;text-shadow:none;font-size:2.396vw">Yeşil bir nokta dönüyor ve pembeler kayboluyor mu?</div><div class="e" style="color:#3d474d;text-shadow:none">Does a green dot circle round while the pink ones vanish?</div><div class="sm" style="color:#444;text-shadow:none">Leylak Kovalayıcı · Lilac Chaser — Jeremy Hinton, 2005</div>','bottom:30px',20);
 wLoop(L,function(t){x.fillStyle='#bdbdbd';x.fillRect(0,0,1920,1080);var miss=Math.floor(t/0.1)%12;for(var i=0;i<12;i++){if(i==miss)continue;var a=i/12*6.283,px=cx+R*Math.cos(a),py=cy+R*Math.sin(a),g=x.createRadialGradient(px,py,0,px,py,70);g.addColorStop(0,'rgba(222,90,205,1)');g.addColorStop(.45,'rgba(214,130,200,.75)');g.addColorStop(1,'rgba(189,189,189,0)');x.fillStyle=g;x.fillRect(px-72,py-72,144,144)}
  x.fillStyle='#111';x.fillRect(cx-16,cy-2,32,4);x.fillRect(cx-2,cy-16,4,32)});return L};

W.hzstep=function(L,it){L.style.background='#0c1014';var c=wCv(L),x=c.getContext('2d');
 T(L,hd('Göz Oyunu · Optical Illusion','İki kutu adım adım mı yürüyor?','Are the two blocks walking step by step?'),'top:40px',.4);
 T(L,'<div class="a">Hayır! Hızları hiç değişmiyor.</div><div class="e">No! Their speed never changes — the stripes fool you.</div><div class="sm">“Adım atan ayaklar” · Stepping feet illusion (Anstis, 2001)</div>','bottom:36px',18);
 wLoop(L,function(t){var fade=t>18?1-ease((t-18)/3)*(t<30?1:1-ease((t-30)/2)):1;x.fillStyle='#808080';x.fillRect(0,300,1920,560);x.globalAlpha=fade;for(var k=0;k<1920;k+=40){x.fillStyle='#000';x.fillRect(k,300,20,560);x.fillStyle='#fff';x.fillRect(k+20,300,20,560)}x.globalAlpha=1;
  var p=(t*70)%1400,X=260+(p<700?p:1400-p);x.fillStyle='#1f3fbf';x.fillRect(X,450,160,60);x.fillStyle='#f5e24a';x.fillRect(X,650,160,60)});return L};

W.hzhermann=function(L,it){L.style.background='#000';var c=wCv(L),x=c.getContext('2d');
 T(L,'<div class="hzbox">'+hd('Göz Oyunu · Optical Illusion','Kesişimlerde siyah noktalar görüyor musun?','Do you see dark dots flashing at the crossings?')+'</div>','top:30px',.4);
 T(L,'<div class="hzbox"><div class="a" style="font-size:2.292vw">Tüm noktalar beyaz — siyahlar sadece gözünde!</div><div class="e">Every dot is white — the dark ones exist only in your eyes.</div><div class="sm">Parıldayan ızgara · Scintillating grid (1994)</div></div>','bottom:30px',14);
 x.fillStyle='#000';x.fillRect(0,0,1920,1080);var s=96,w=14;x.fillStyle='#6b6b6b';for(var k=-s;k<1920+s;k+=s){x.fillRect(k,0,w,1080)}for(k=-s;k<1080+s;k+=s){x.fillRect(0,k,1920,w)}x.fillStyle='#fff';for(var i=-s;i<1920+s;i+=s)for(var j=-s;j<1080+s;j+=s){x.beginPath();x.arc(i+w/2,j+w/2,10,0,7);x.fill()}return L};

/* afterimage: inverted still photo, then greyscale. it: f, cr, place, placee */
W.hzafter=function(L,it){L.style.background='#000';var m=wEl('img','');m.src=it.f;m.style.cssText='position:absolute;top:0;left:0;width:100%;height:100%;object-fit:cover;filter:invert(1)';L.appendChild(m);
 var dt=wEl('div','',null,'position:absolute;left:50%;top:50%;width:22px;height:22px;margin:-11px 0 0 -11px;border-radius:50%;background:#ff2a2a;box-shadow:0 0 0 4px #fff;z-index:5');L.appendChild(dt);
 var a=T(L,'<div class="hzbox"><div class="lb">Göz Oyunu · Optical Illusion — gerçek fotoğraf · real photo</div><div class="q" style="font-size:2.604vw">Kırmızı noktaya 25 saniye bak, kıpırdama…</div><div class="e">Stare at the red dot for 25 seconds, don’t move…</div><div class="lb" id="hzc" style="margin-top:14px;color:#ff9e7a"></div></div>','top:40px',.4);
 var st=it.sec||25,sw=false;wLoop(L,function(t){var r=Math.ceil(st-t),cc=a.querySelector('#hzc');if(cc)cc.innerHTML=r>0?r:'';
  if(t>=st&&!sw){sw=true;m.style.filter='grayscale(1)';a.innerHTML='';T(L,'<div class="hzbox"><div class="q" style="font-size:2.708vw">Siyah-beyaz fotoğrafta renkleri görüyor musun?</div><div class="e">Do you see colours in a black-and-white photo?</div><div class="sm">Gözün yorulan hücreleri zıt rengi üretir · Tired cells in your eye create the opposite colours</div><div class="sm">'+it.place+' — '+it.cr+'</div></div>','bottom:40px',.1)}
  if(t>=st+12&&m.style.filter!='none'){m.style.filter='none'}});return L};
/* ---------- v56 additions: hzpwave hzlangton hzchaos hzmaze hzkoch hzaurora (art/sims), hzcheck hzdrift (illusions) ---------- */
/* pendulum wave: 15 pendulums, n-th does 51+n swings per 60 s */
W.hzpwave=function(L,it){grad(L,'#13202b','#030508');var c=wCv(L),x=c.getContext('2d'),N=15,P=60,i;
 T(L,hd('Canlı Sanat · Living Art — simülasyon · simulation','Sarkaç Dalgası','The Pendulum Wave'),'top:36px',.4);
 T(L,'<div class="sm" style="font-size:1.302vw;color:#dfe6e9">15 sarkaç, her biri bir öncekinden biraz daha uzun ve yavaş. Yaklaşık 60 saniyede hepsi yeniden aynı hizaya gelir<br><i>15 pendulums, each a little longer and slower than the last. After about 60 seconds they all line up again</i></div>','bottom:34px',5);
 wLoop(L,function(t){x.clearRect(0,0,1920,1080);var pts=[];
  for(i=0;i<N;i++){var y=300+i*40,w=2*Math.PI*(51+i)/P,X=960+430*Math.cos(w*t);pts.push([X,y]);
   x.strokeStyle='rgba(159,179,191,.18)';x.lineWidth=2;x.beginPath();x.moveTo(530,y);x.lineTo(1390,y);x.stroke()}
  x.strokeStyle='rgba(143,211,193,.35)';x.lineWidth=3;x.beginPath();for(i=0;i<N;i++){if(i)x.lineTo(pts[i][0],pts[i][1]);else x.moveTo(pts[i][0],pts[i][1])}x.stroke();
  for(i=0;i<N;i++){var h=170+i*9,g=x.createRadialGradient(pts[i][0]-5,pts[i][1]-5,2,pts[i][0],pts[i][1],17);g.addColorStop(0,'hsl('+h+',70%,85%)');g.addColorStop(1,'hsl('+h+',55%,45%)');x.fillStyle=g;x.beginPath();x.arc(pts[i][0],pts[i][1],16,0,7);x.fill()}});return L};

/* Langton's ant */
W.hzlangton=function(L,it){L.style.background='#0a1117';var c=wCv(L),x=c.getContext('2d'),S=8,GW=240,GH=135,G=new Uint8Array(GW*GH),ax=Math.floor(GW/2)+10,ay=Math.floor(GH/2)+6,dir=0,n=0,shown=false,DX=[0,1,0,-1],DY=[-1,0,1,0];
 T(L,'<div class="hzbox">'+hd('Akıllı Düşünce · Clever Thinking — simülasyon · simulation','Langton’un Karıncası: iki basit kural','Langton’s Ant: two simple rules')+'<div class="sm" style="font-size:1.198vw;color:#dfe6e9">Boş karede sağa, dolu karede sola dön · kareyi çevir · bir adım ilerle<br><i>Empty square: turn right · filled square: turn left · flip it · step forward</i></div></div>','top:24px',.4);
 var V=T(L,'','bottom:30px;left:40px;right:auto;text-align:left',1);var M=null;
 wLoop(L,function(t){var tg=Math.min(15500,Math.floor(t<6?t*15:90+(t-6)*360));
  for(;n<tg;n++){var k=ay*GW+ax,s=G[k];dir=(dir+(s?3:1))%4;G[k]=s?0:1;x.fillStyle=G[k]?'#d9e4e1':'#0a1117';x.fillRect(ax*S,ay*S,S,S);ax=(ax+DX[dir]+GW)%GW;ay=(ay+DY[dir]+GH)%GH}
  x.fillStyle='#ff6a4a';x.fillRect(ax*S-1,ay*S-1,S+2,S+2);
  V.innerHTML='<div class="hzbox" style="padding:12px 28px"><div class="lb">Adım · Steps</div><div style="font-size:2.396vw">'+n.toLocaleString('tr-TR')+'</div></div>';
  if(n>10400&&!shown){shown=true;T(L,'<div class="hzbox"><div class="a" style="font-size:2.083vw">≈10.000 adım kaos… sonra birden düzenli bir “otoyol”!</div><div class="e" style="font-size:1.458vw">≈10,000 steps of chaos… then suddenly an orderly “highway”!</div><div class="sm">Chris Langton, 1986 — kimse nedenini tam kanıtlayamadı · nobody has fully proved why</div></div>','bottom:30px;left:auto;right:40px;width:1080px',.1)}});return L};

/* chaos game -> Sierpinski triangle */
W.hzchaos=function(L,it){grad(L,'#161a2c','#030407');var c=wCv(L),x=c.getContext('2d'),V=[[960,235],[575,880],[1345,880]],col=['#8fd3c1','#ff9e7a','#a9b8ff'],px=900,py=700,n=0,ov=wCv(L),o=ov.getContext('2d'),last=[];
 T(L,'<div class="hzbox">'+hd('Kaos Oyunu · The Chaos Game — simülasyon · simulation','Rastgele bir köşe seç, oraya yarı yoldan nokta koy, tekrarla…','Pick a random corner, jump halfway there, repeat…')+'</div>','top:24px',.4);
 for(var i=0;i<3;i++){x.fillStyle=col[i];x.beginPath();x.arc(V[i][0],V[i][1],12,0,7);x.fill()}
 var R=T(L,'','bottom:34px;left:40px;right:auto;text-align:left;width:420px',1),done=false;
 wLoop(L,function(t){var tg=t<14?Math.floor(t*1.6):Math.min(90000,Math.floor(22+(t-14)*(t-14)*60));o.clearRect(0,0,1920,1080);
  for(;n<tg;n++){var k=Math.floor(Math.random()*3),nx=(px+V[k][0])/2,ny=(py+V[k][1])/2;if(t<14)last.push([px,py,nx,ny,k]);px=nx;py=ny;if(n>3){x.fillStyle=col[k];x.globalAlpha=t<14?1:.75;x.fillRect(px-(t<14?4:1),py-(t<14?4:1),t<14?8:2,t<14?8:2);x.globalAlpha=1}}
  if(t<15&&last.length){var l=last[last.length-1];o.strokeStyle='rgba(255,255,255,.7)';o.setLineDash([10,8]);o.lineWidth=2;o.beginPath();o.moveTo(l[0],l[1]);o.lineTo(V[l[4]][0],V[l[4]][1]);o.stroke();o.setLineDash([])}
  R.innerHTML='<div class="hzbox" style="padding:12px 28px"><div class="lb">Nokta · Dots</div><div style="font-size:2.292vw">'+n.toLocaleString('tr-TR')+'</div></div>';
  if(t>30&&!done){done=true;T(L,'<div class="hzbox"><div class="a" style="font-size:2.188vw">Rastgelelikten Sierpiński üçgeni çıktı!</div><div class="e" style="font-size:1.458vw">Randomness drew a Sierpiński triangle!</div><div class="sm">Her parçası bütünün küçük bir kopyası — bir fraktal · Every part is a tiny copy of the whole — a fractal</div></div>','bottom:14px',.1)}});return L};

/* maze: carve with depth-first backtracking, then flood-fill (BFS) the shortest path */
W.hzmaze=function(L,it){grad(L,'#1a2a24','#040806');var c=wCv(L),x=c.getContext('2d'),CW=45,RH=17,S=36,X0=960-CW*S/2,Y0=270,i,
 vis=new Uint8Array(CW*RH),E=[],st=[0],steps=0,phase=0,dist=null,Q=null,qi=0,path=null,pl=0;vis[0]=1;for(i=0;i<CW*RH;i++)E.push([0,0,0,0]);
 T(L,hd('Akıllı Düşünce · Clever Thinking — simülasyon · simulation','Bilgisayar önce labirenti kazıyor, sonra çıkışı buluyor','The computer carves a maze, then finds the way out'),'top:30px',.4);
 var B=T(L,'','bottom:34px',1);B.innerHTML='<div class="sm" style="font-size:1.302vw;color:#dfe6e9">1) Rastgele ilerle, çıkmaza girince geri dön · Wander randomly, back up at dead ends</div>';
 var D=[[0,-1],[1,0],[0,1],[-1,0]];
 function cell(k,col){var cx=k%CW,cy=Math.floor(k/CW);x.fillStyle=col;x.fillRect(X0+cx*S+5,Y0+cy*S+5,S-10,S-10);var e=E[k];if(e[1])x.fillRect(X0+cx*S+S-5,Y0+cy*S+5,10,S-10);if(e[2])x.fillRect(X0+cx*S+5,Y0+cy*S+S-5,S-10,10)}
 x.fillStyle='#07100c';x.fillRect(X0,Y0,CW*S,RH*S);
 var acc=0,lt=0;wLoop(L,function(t){acc+=Math.min(.1,t-lt)*(phase==0?95:phase==1?70:60);lt=t;
  while(acc>=1){acc--;
   if(phase==0){if(!st.length){phase=1;dist=new Int32Array(CW*RH);for(i=0;i<dist.length;i++)dist[i]=-1;dist[0]=0;Q=[0];B.innerHTML='<div class="sm" style="font-size:1.302vw;color:#dfe6e9">2) Su gibi her yöne aynı anda yayıl — çıkışa ilk varan yol en kısasıdır<br><i>Spread like water in every direction at once — the first route to reach the exit is the shortest</i></div>';break}
    var k=st[st.length-1],cx=k%CW,cy=Math.floor(k/CW),opt=[];for(var d=0;d<4;d++){var nx=cx+D[d][0],ny=cy+D[d][1];if(nx>=0&&ny>=0&&nx<CW&&ny<RH&&!vis[ny*CW+nx])opt.push(d)}
    if(opt.length){var d2=opt[Math.floor(Math.random()*opt.length)],nk=(cy+D[d2][1])*CW+cx+D[d2][0];E[k][d2]=1;E[nk][(d2+2)%4]=1;vis[nk]=1;st.push(nk);cell(k,'#b9c9c2');cell(nk,'#ff9e7a')}else{st.pop();cell(k,'#b9c9c2')}}
   else if(phase==1){var lim=4;while(lim--&&qi<Q.length){var k=Q[qi++],cx=k%CW,cy=Math.floor(k/CW);var hh=170+Math.min(80,dist[k]/5);cell(k,'hsl('+hh+',45%,52%)');for(var d=0;d<4;d++)if(E[k][d]){var nk=(cy+D[d][1])*CW+cx+D[d][0];if(dist[nk]<0){dist[nk]=dist[k]+1;Q.push(nk)}}}
    if(qi>=Q.length){phase=2;path=[];var k=CW*RH-1;while(k!==0){path.push(k);var cx=k%CW,cy=Math.floor(k/CW);for(var d=0;d<4;d++)if(E[k][d]){var nk=(cy+D[d][1])*CW+cx+D[d][0];if(dist[nk]==dist[k]-1){k=nk;break}}}path.push(0);path.reverse()}}
   else if(phase==2&&pl<path.length){var k=path[pl++],cx=k%CW,cy=Math.floor(k/CW);x.fillStyle='#ffffff';x.beginPath();x.arc(X0+cx*S+S/2,Y0+cy*S+S/2,9,0,7);x.fill();if(pl==path.length)B.innerHTML='<div class="a" style="font-size:2.083vw">Çıkış bulundu: '+path.length+' adım</div><div class="e" style="font-size:1.458vw">Exit found: '+path.length+' steps — the shortest possible</div>'}}
  x.fillStyle='#8fd3c1';x.fillRect(X0-14,Y0+6,10,S-12);x.fillStyle='#ff6a4a';x.fillRect(X0+CW*S+4,Y0+(RH-1)*S+6,10,S-12)});return L};

/* Koch snowflake: perimeter grows forever, area stays finite */
W.hzkoch=function(L,it){grad(L,'#122236','#03060b');var c=wCv(L),x=c.getContext('2d'),R=265,cx=960,cy=575,LV=[],i;
 var p=[];for(i=0;i<3;i++){var a=-Math.PI/2+i*2*Math.PI/3;p.push([cx+R*Math.cos(a),cy+R*Math.sin(a)])}p.push(p[0]);LV.push(p);
 for(var l=1;l<=5;l++){var q=[],o=LV[l-1];for(i=0;i<o.length-1;i++){var A=o[i],B=o[i+1],dx=(B[0]-A[0])/3,dy=(B[1]-A[1])/3,P1=[A[0]+dx,A[1]+dy],P2=[A[0]+2*dx,A[1]+2*dy],ang=-Math.PI/3,Px=[P1[0]+dx*Math.cos(ang)-dy*Math.sin(ang),P1[1]+dx*Math.sin(ang)+dy*Math.cos(ang)];q.push(A,P1,Px,P2)}q.push(o[o.length-1]);LV.push(q)}
 T(L,'<div class="hzbox">'+hd('Fraktal · Fractal — çizim · illustration','Koch kar tanesi: her kenarın ortasına küçük bir üçgen ekle','The Koch snowflake: add a small triangle to the middle of every edge')+'</div>','top:22px',.4);
 var V=T(L,'','top:430px;left:1390px;right:auto;text-align:left',1);
 T(L,'<div class="hzbox"><div class="a" style="font-size:1.979vw">Çevre her adımda ⁴⁄₃ katına çıkar ve sonsuza gider — alan ise ilk üçgenin 1,6 katını hiç geçmez</div><div class="e" style="font-size:1.406vw">The perimeter grows by 4/3 each step, forever — yet the area never exceeds 1.6× the first triangle</div></div>','bottom:26px',33);
 wLoop(L,function(t){var lv=Math.min(5,Math.floor(t/5.5)),q=LV[lv];x.clearRect(0,0,1920,1080);x.beginPath();x.moveTo(q[0][0],q[0][1]);for(i=1;i<q.length;i++)x.lineTo(q[i][0],q[i][1]);x.closePath();x.fillStyle='rgba(159,224,255,.10)';x.fill();x.strokeStyle='#bfe9ff';x.lineWidth=2.5;x.stroke();
  V.innerHTML='<div class="lb">Adım · Step</div><div style="font-size:2.917vw">'+lv+'</div><div class="lb" style="margin-top:22px">Kenar · Edges</div><div style="font-size:2.292vw">'+(3*Math.pow(4,lv)).toLocaleString('tr-TR')+'</div><div class="lb" style="margin-top:22px">Çevre · Perimeter</div><div class="a" style="font-size:2.708vw">×'+Math.pow(4/3,lv).toFixed(2).replace('.',',')+'</div>'});return L};

/* aurora (calm night) */
W.hzaurora=function(L,it){var c=wCv(L),x=c.getContext('2d'),S=stars(320),BD=[[300,.0021,.33,150,250],[380,.0016,.21,175,200],[250,.0029,.27,200,160]],gr=[];
 for(var b=0;b<BD.length;b++){var g=x.createLinearGradient(0,0,0,1);g.addColorStop(0,'rgba(120,90,200,0)');g.addColorStop(.25,'hsla('+(BD[b][3]-40)+',70%,60%,.20)');g.addColorStop(.6,'hsla(140,80%,58%,.32)');g.addColorStop(1,'rgba(60,255,160,0)');gr.push(g)}
 T(L,hd('Gece · Night — çizim · illustration','Kuzey Işıkları','The Northern Lights'),'top:60px',2);
 T(L,'<div class="sm" style="font-size:1.302vw;color:#cfd8de">Güneş’ten gelen parçacıklar havaya çarpınca gökyüzü parlar — yeşil renk oksijenden gelir<br><i>Particles from the Sun strike the air and the sky glows — the green comes from oxygen</i></div>','bottom:44px',8);
 wLoop(L,function(t){var g0=x.createLinearGradient(0,0,0,1080);g0.addColorStop(0,'#02040b');g0.addColorStop(.75,'#06121c');g0.addColorStop(1,'#081a1e');x.fillStyle=g0;x.fillRect(0,0,1920,1080);drawStars(x,S,t*.3);
  x.globalCompositeOperation='lighter';for(var b=0;b<BD.length;b++){var d=BD[b];x.fillStyle=gr[b];for(var u=0;u<1920;u+=6){var y=d[0]+Math.sin(u*d[1]+t*d[2])*70+Math.sin(u*d[1]*2.7-t*d[2]*1.3)*30,h=d[4]+Math.sin(u*.01+t*.4+b)*60,a=.55+.45*Math.sin(u*.004-t*.25+b*2);x.globalAlpha=Math.max(0,a);x.save();x.translate(u,y);x.scale(1,h+120);x.fillRect(0,0,7,1);x.restore()}}x.globalAlpha=1;x.globalCompositeOperation='source-over';
  x.fillStyle='#03070a';x.beginPath();x.moveTo(0,1080);for(var v=0;v<=1920;v+=30)x.lineTo(v,820+Math.sin(v*.004)*60+Math.sin(v*.013)*22);x.lineTo(1920,1080);x.fill()});return L};

/* Adelson checker-shadow: tiles A and B are the same grey */
W.hzcheck=function(L,it){L.style.background='#1a1d20';var c=wCv(L),x=c.getContext('2d'),N=7,S=88,X0=652,Y0=226,scx=1048,scy=622;
 var im=x.createImageData(N*S,N*S),dd=im.data;for(var yy=0;yy<N*S;yy++)for(var xx=0;xx<N*S;xx++){var r=Math.floor(yy/S),cc=Math.floor(xx/S),base=((r+cc)%2==0)?200:120,dx=X0+xx-scx,dy=Y0+yy-scy,ds=Math.sqrt(dx*dx*.7+dy*dy),f=ds<130?.6:ds>265?1:.6+.4*((ds-130)/135),v=Math.round(base*f),k=(yy*N*S+xx)*4;dd[k]=dd[k+1]=dd[k+2]=v;dd[k+3]=255}
 x.putImageData(im,X0,Y0);
 x.fillStyle='#3f8f6a';x.fillRect(1165,430,100,200);x.beginPath();x.ellipse(1215,630,50,16,0,0,7);x.fill();x.fillStyle='#62b48c';x.beginPath();x.ellipse(1215,430,50,16,0,0,7);x.fill();
 x.font='bold 52px Helvetica,Arial';x.textAlign='center';x.textBaseline='middle';x.fillStyle='#e8e8e8';x.fillText('A',X0+2*S+S/2,Y0+1*S+S/2);x.fillStyle='#2a2a2a';x.fillText('B',X0+4*S+S/2,Y0+4*S+S/2);
 T(L,hd('Göz Oyunu · Optical Illusion','A karesi mi daha koyu, B mi?','Which square is darker, A or B?'),'top:36px',.4);
 T(L,'<div class="a" style="font-size:2.292vw">İkisi tamamen aynı gri tonda!</div><div class="e" style="font-size:1.562vw">They are exactly the same shade of grey.</div><div class="sm">Beynin gölgeyi hesaba katıp “düzeltir” · Your brain corrects for the shadow — Edward Adelson, 1995</div>','bottom:20px',17);
 var sh=false;wLoop(L,function(t){if(t>16&&!sh){sh=true;x.fillStyle='rgb(120,120,120)';x.fillRect(X0+2*S+S/2-16,Y0+2*S,32,2*S+S/2+16);x.fillRect(X0+2*S+S/2-16,Y0+4*S+S/2-16,S*1.5+16,32);x.fillStyle='#e8e8e8';x.fillText('A',X0+2*S+S/2,Y0+1*S+S/2);x.fillStyle='#2a2a2a';x.fillText('B',X0+4*S+S/2,Y0+4*S+S/2)}});return L};

/* peripheral drift: a completely still picture that seems to turn */
W.hzdrift=function(L,it){L.style.background='#d8d6cf';var c=wCv(L),x=c.getContext('2d'),seq=['#000000','#2f4fae','#ffffff','#9fd8cb'];
 function wheel(cx,cy,R,dir){for(var ring=0;ring<5;ring++){var r1=R*(1-ring*.19),r0=r1-R*.17,n=24+ring*-3;for(var s2=0;s2<n;s2++){var a0=s2/n*2*Math.PI+ring*.3,a1=(s2+1)/n*2*Math.PI+ring*.3;for(var q=0;q<4;q++){var b0=a0+(a1-a0)*q/4,b1=a0+(a1-a0)*(q+1)/4;x.fillStyle=seq[dir>0?q:3-q];x.beginPath();x.arc(cx,cy,r1,b0,b1+.003);x.arc(cx,cy,r0,b1+.003,b0,true);x.closePath();x.fill()}}}}
 var P=[[440,410,1],[960,410,-1],[1480,410,1],[700,710,-1],[1220,710,1]];for(var i=0;i<P.length;i++)wheel(P[i][0],P[i][1],145,P[i][2]);
 T(L,'<div class="hzbox" style="background:rgba(20,24,28,.82)">'+hd('Göz Oyunu · Optical Illusion','Bu resim tamamen durağan. Çarklar dönüyor mu?','This picture is completely still. Are the wheels turning?')+'</div>','top:20px',.4);
 T(L,'<div class="hzbox" style="background:rgba(20,24,28,.82)"><div class="a" style="font-size:1.979vw">Tek bir çarkın ortasına sabit bak — o çark durur, kenardakiler döner</div><div class="e" style="font-size:1.406vw">Stare at the centre of one wheel — it stops, while the others keep turning</div><div class="sm">Çevresel kayma illüzyonu · Peripheral drift illusion — Akiyoshi Kitaoka’nın çalışmalarından esinlenildi · inspired by Akiyoshi Kitaoka</div></div>','bottom:16px',14);return L};


/* ---------- v58 additions: hzchladni hzsort hzspiro hzrose hzmoire hzkoi (art/sims), hzzoll (illusion) ---------- */
/* Chladni figures: sand leaves the vibrating parts of a plate and gathers on the still (nodal) lines */
W.hzchladni=function(L,it){grad(L,'#1d1a16','#050403');var c=wCv(L),x=c.getContext('2d'),N=7000,P=[],i,S=600,X0=660,Y0=300,M=[[1,4],[2,5],[3,5],[2,7],[4,7],[3,8]],mi=-1,n=1,m=4,PI=Math.PI,lab=null;
 for(i=0;i<N;i++)P.push([Math.random(),Math.random()]);
 T(L,hd('Ses ve Şekil · Sound & Shape — simülasyon · simulation','Chladni levhası: kum, sesin resmini çiziyor','A Chladni plate: sand draws a picture of sound'),'top:30px',.4);
 lab=T(L,'','top:450px;left:1330px;right:auto;width:470px;text-align:left',1);
 T(L,'<div class="sm" style="font-size:1.302vw;color:#e6dfd2">Titreşen yerlerden kaçan kum, hiç kıpırdamayan çizgilerde toplanır. Nota yükseldikçe desen karmaşıklaşır<br><i>Sand is shaken off the vibrating parts and gathers on the lines that stay still. The higher the note, the richer the pattern</i></div>','bottom:30px',6);
 wLoop(L,function(t){var k=Math.floor(t/11)%M.length;if(k!==mi){mi=k;n=M[k][0];m=M[k][1];for(i=0;i<N;i++){P[i][0]=Math.random();P[i][1]=Math.random()}
   lab.innerHTML='<div class="lb">Titreşim · Mode</div><div style="font-size:2.6vw">n = '+n+' · m = '+m+'</div><div class="sm">Nota '+(k+1)+' / '+M.length+' · Note '+(k+1)+' of '+M.length+'</div>'}
  x.clearRect(0,0,1920,1080);x.fillStyle='#14110d';x.fillRect(X0-10,Y0-10,S+20,S+20);x.fillStyle='#2b2620';x.fillRect(X0,Y0,S,S);x.fillStyle='rgba(240,230,205,.85)';
  for(i=0;i<N;i++){var p=P[i],f=Math.cos(n*PI*p[0])*Math.cos(m*PI*p[1])-Math.cos(m*PI*p[0])*Math.cos(n*PI*p[1]),a=Math.abs(f)*0.012+0.0004;
   p[0]+=(Math.random()-.5)*a;p[1]+=(Math.random()-.5)*a;if(p[0]<0)p[0]=-p[0];if(p[0]>1)p[0]=2-p[0];if(p[1]<0)p[1]=-p[1];if(p[1]>1)p[1]=2-p[1];
   x.fillRect(X0+p[0]*S,Y0+p[1]*S,2,2)}});return L};

/* sorting race: bubble sort vs quicksort on the same bars, same speed */
W.hzsort=function(L,it){grad(L,'#151d26','#030508');var c=wCv(L),x=c.getContext('2d'),N=44,A=[],i,j;
 for(i=0;i<N;i++)A.push(i+1);for(i=N-1;i>0;i--){j=Math.floor(Math.random()*(i+1));var tt=A[i];A[i]=A[j];A[j]=tt}
 function bub(a){var o=[],n=a.length,s=a.slice();for(var i=0;i<n-1;i++){var sw=false;for(var j=0;j<n-1-i;j++){o.push(['c',j,j+1]);if(s[j]>s[j+1]){var t=s[j];s[j]=s[j+1];s[j+1]=t;o.push(['s',j,j+1]);sw=true}}if(!sw)break}return o}
 function qs(a){var o=[],s=a.slice();function part(lo,hi){var p=s[hi],k=lo;for(var j=lo;j<hi;j++){o.push(['c',j,hi]);if(s[j]<p){if(k!==j){var t=s[k];s[k]=s[j];s[j]=t;o.push(['s',k,j])}k++}}if(k!==hi){var t2=s[k];s[k]=s[hi];s[hi]=t2;o.push(['s',k,hi])}return k}
  (function r(lo,hi){if(lo<hi){var p=part(lo,hi);r(lo,p-1);r(p+1,hi)}})(0,s.length-1);return o}
 var R=[{n:'Kabarcık Sıralaması · Bubble sort',a:A.slice(),o:bub(A),k:0,x0:110,col:'#ff9e7a'},{n:'Hızlı Sıralama · Quicksort',a:A.slice(),o:qs(A),k:0,x0:1010,col:'#8fd3c1'}];
 T(L,hd('Akıllı Algoritmalar · Clever Algorithms — simülasyon · simulation','Aynı karışık çubuklar, aynı hız: hangi yöntem önce bitirir?','Same shuffled bars, same speed: which method finishes first?'),'top:28px',.4);
 var lb=[T(L,'','top:252px;left:110px;right:auto;width:800px;text-align:left',1),T(L,'','top:252px;left:1010px;right:auto;width:800px;text-align:left',1)],fin=false;
 wLoop(L,function(t){var tg=Math.max(0,Math.floor((t-3)*24));x.clearRect(0,0,1920,1080);
  for(var r=0;r<2;r++){var Q=R[r],hl=null;while(Q.k<Math.min(tg,Q.o.length)){var op=Q.o[Q.k++];hl=op;if(op[0]=='s'){var t1=Q.a[op[1]];Q.a[op[1]]=Q.a[op[2]];Q.a[op[2]]=t1}}
   if(!hl&&Q.k<Q.o.length&&Q.k>0)hl=Q.o[Q.k-1];var done=Q.k>=Q.o.length,bw=800/N;
   for(i=0;i<N;i++){var h=Q.a[i]*11;x.fillStyle=done?Q.col:(hl&&(i==hl[1]||i==hl[2]))?'#ffffff':'rgba(200,214,222,.55)';x.fillRect(Q.x0+i*bw+1,860-h,bw-3,h)}
   lb[r].innerHTML='<div class="lb" style="color:'+Q.col+'">'+Q.n+'</div><div class="sm" style="font-size:1.2vw;color:#dfe6e9">Adım · Steps: '+Q.k.toLocaleString('tr-TR')+(done?' &nbsp;✓ Bitti · Done':'')+'</div>'}
  if(!fin&&R[0].k>=R[0].o.length){fin=true}
  if(t>4&&R[1].k>=R[1].o.length&&!R.sh){R.sh=1;T(L,'<div class="hzbox"><div class="a" style="font-size:1.9vw">Hızlı sıralama ≈'+R[1].o.length+' adımda bitti — kabarcık ≈'+R[0].o.length+' adım istiyor</div><div class="e" style="font-size:1.35vw">Quicksort finished in ≈'+R[1].o.length+' steps — bubble sort needs ≈'+R[0].o.length+'. Böl ve yönet · Divide and conquer (Tony Hoare, 1959)</div></div>','bottom:20px',.1)}});return L};

/* spirograph: a small wheel rolling inside a big ring draws a rosette */
W.hzspiro=function(L,it){L.style.background='#0b0f14';var c=wCv(L),x=c.getContext('2d'),ov=wCv(L),o=ov.getContext('2d'),SP=[[300,105,80,'#8fd3c1'],[300,186,150,'#ff9e7a'],[300,72,120,'#a9b8ff'],[300,130,95,'#e6c3ff']],cur=-1,cx=960,cy=575,lp=null;
 T(L,hd('Canlı Sanat · Living Art — çizim · illustration','Spirograf: büyük çemberin içinde dönen küçük bir tekerlek','Spirograph: a little wheel rolling inside a big ring'),'top:30px',.4);
 var V=T(L,'','bottom:30px',1);
 wLoop(L,function(t){var k=Math.min(SP.length-1,Math.floor(t/17)),p=SP[k],R=p[0],r=p[1],d=p[2];if(k!==cur){cur=k;x.globalAlpha=1;x.fillStyle='rgba(11,15,20,.82)';x.fillRect(0,0,1920,1080);lp=null;
   V.innerHTML='<div class="sm" style="font-size:1.25vw;color:#dfe6e9">Halka '+R+' · tekerlek '+r+' · kalem '+d+' — oran sadeleşince desen kaç yaprak olacağını söyler<br><i>Ring '+R+' · wheel '+r+' · pen '+d+' — the simplified ratio tells you how many petals it will have</i></div>'}
  var lt=(t-k*17),a=lt*2.4;o.clearRect(0,0,1920,1080);
  for(var s=0;s<12;s++){var aa=a-0.2+s*0.2/12,X=cx+(R-r)*Math.cos(aa)+d*Math.cos((R-r)/r*aa),Y=cy+(R-r)*Math.sin(aa)-d*Math.sin((R-r)/r*aa);if(lp){x.strokeStyle=p[3];x.lineWidth=2;x.globalAlpha=.9;x.beginPath();x.moveTo(lp[0],lp[1]);x.lineTo(X,Y);x.stroke()}lp=[X,Y]}
  var gx=cx+(R-r)*Math.cos(a),gy=cy+(R-r)*Math.sin(a);o.strokeStyle='rgba(255,255,255,.18)';o.lineWidth=2;o.beginPath();o.arc(cx,cy,R,0,7);o.stroke();o.beginPath();o.arc(gx,gy,r,0,7);o.stroke();o.beginPath();o.moveTo(gx,gy);o.lineTo(lp[0],lp[1]);o.stroke();o.fillStyle='#fff';o.beginPath();o.arc(lp[0],lp[1],6,0,7);o.fill()});return L};

/* Earth and Venus: a line between them every few days draws a five-petal rose over 8 years */
W.hzrose=function(L,it){var c=wCv(L),x=c.getContext('2d'),ov=wCv(L),o=ov.getContext('2d'),S=stars(260),cx=960,cy=580,RE=300,RV=RE*0.723,day=0,lastD=-99;
 x.fillStyle='#03050b';x.fillRect(0,0,1920,1080);
 T(L,hd('Gezegen Dansı · Dance of the Planets — simülasyon · simulation','Dünya ile Venüs’ü birkaç günde bir çizgiyle birleştir…','Join Earth and Venus with a line every few days…'),'top:28px',.4);
 var V=T(L,'','top:470px;left:1420px;right:auto;width:420px;text-align:left',1),sh=false;
 wLoop(L,function(t){var tg=Math.min(2922,Math.max(0,(t-2)*62));o.clearRect(0,0,1920,1080);drawStars(o,S,t);
  while(day<tg){day+=1;var ae=2*Math.PI*day/365.25,av=2*Math.PI*day/224.7,E=[cx+RE*Math.cos(ae),cy-RE*Math.sin(ae)],Vn=[cx+RV*Math.cos(av),cy-RV*Math.sin(av)];
   if(day-lastD>=4){lastD=day;x.strokeStyle='hsla('+(170+day/2922*80)+',60%,70%,.22)';x.lineWidth=1.2;x.beginPath();x.moveTo(E[0],E[1]);x.lineTo(Vn[0],Vn[1]);x.stroke()}}
  var ae2=2*Math.PI*day/365.25,av2=2*Math.PI*day/224.7;o.fillStyle='#ffd27a';o.beginPath();o.arc(cx,cy,16,0,7);o.fill();
  o.fillStyle='#6fb6ff';o.beginPath();o.arc(cx+RE*Math.cos(ae2),cy-RE*Math.sin(ae2),11,0,7);o.fill();o.fillStyle='#f1e3c8';o.beginPath();o.arc(cx+RV*Math.cos(av2),cy-RV*Math.sin(av2),9,0,7);o.fill();
  V.innerHTML='<div class="lb">Yıl · Year</div><div style="font-size:2.8vw">'+(day/365.25).toFixed(1).replace('.',',')+'</div><div class="sm"><span style="color:#6fb6ff">●</span> Dünya · Earth &nbsp; <span style="color:#f1e3c8">●</span> Venüs · Venus</div>';
  if(day>=2920&&!sh){sh=true;T(L,'<div class="hzbox"><div class="a" style="font-size:1.9vw">8 yılda 5 yapraklı bir gül! Dünya 8 tur atarken Venüs neredeyse tam 13 tur atar</div><div class="e" style="font-size:1.35vw">A five-petal rose in 8 years — while Earth goes round 8 times, Venus goes round almost exactly 13</div></div>','bottom:20px',.1)}});return L};

/* moiré: two sets of rings drifting over each other */
W.hzmoire=function(L,it){L.style.background='#0c1014';var c=wCv(L),x=c.getContext('2d');
 T(L,'<div class="hzbox">'+hd('Canlı Sanat · Living Art — çizim · illustration','Hareli desen: iki basit halka deseni üst üste kayıyor','Moiré: two plain ring patterns sliding over each other')+'</div>','top:22px',.4);
 T(L,'<div class="hzbox"><div class="sm" style="font-size:1.25vw;color:#dfe6e9">Dalgalanan çiçek şekilleri aslında hiç çizilmedi — gözün iki deseni birlikte okuyunca kendisi görüyor<br><i>The rippling flower shapes are never drawn — your eye creates them by reading both patterns together</i></div></div>','bottom:22px',7);
 wLoop(L,function(t){x.clearRect(0,0,1920,1080);var C=[[960+150*Math.cos(t*.23),560+90*Math.sin(t*.31)],[960-150*Math.cos(t*.19),560-90*Math.sin(t*.27)]],col=['rgba(143,211,193,.85)','rgba(255,158,122,.85)'];
  x.lineWidth=5;for(var k=0;k<2;k++){x.strokeStyle=col[k];for(var r=10;r<900;r+=15){x.beginPath();x.arc(C[k][0],C[k][1],r,0,7);x.stroke()}}});return L};

/* calm night pond with koi */
W.hzkoi=function(L,it){var c=wCv(L),x=c.getContext('2d'),F=[],i,RP=[],PAD=[[300,330,70],[1600,260,90],[1450,820,60],[420,860,80],[1050,190,50]];
 var cols=[['#f2efe8','#e0582e'],['#f6a04d','#f6a04d'],['#f4f1ea','#222'],['#e9e4da','#d9452b'],['#ffcf8a','#ffcf8a']];
 for(i=0;i<6;i++)F.push({a:Math.random()*6.28,cx:960+(Math.random()-.5)*700,cy:560+(Math.random()-.5)*300,rx:220+Math.random()*260,ry:120+Math.random()*140,sp:(.05+Math.random()*.05)*(i%2?1:-1),c:cols[i%5],L:70+Math.random()*30});
 T(L,hd('Gece Havuzu · Night Pond — çizim · illustration (sakin · calm)','Ay ışığında koi balıkları','Koi under the moonlight'),'top:40px',2);
 T(L,'<div class="sm" style="font-size:1.25vw;color:#cdd6dc">Japonya’da koi sabrın ve azmin sembolüdür; bazıları 50 yıldan uzun yaşar<br><i>In Japan koi stand for patience and perseverance; some live for more than 50 years</i></div>','bottom:40px',9);
 wLoop(L,function(t){var g=x.createRadialGradient(1300,300,50,960,540,1200);g.addColorStop(0,'#16303a');g.addColorStop(1,'#02080c');x.fillStyle=g;x.fillRect(0,0,1920,1080);
  x.fillStyle='rgba(220,235,240,.06)';x.beginPath();x.ellipse(1300,300,220,60,0,0,7);x.fill();
  if(Math.random()<.012)RP.push([Math.random()*1920,250+Math.random()*700,t]);
  for(i=RP.length-1;i>=0;i--){var age=t-RP[i][2];if(age>7){RP.splice(i,1);continue}x.strokeStyle='rgba(200,225,235,'+(.25*(1-age/7))+')';x.lineWidth=2;x.beginPath();x.ellipse(RP[i][0],RP[i][1],age*28,age*10,0,0,7);x.stroke()}
  for(i=0;i<F.length;i++){var f=F[i],a=f.a+t*f.sp,X=f.cx+f.rx*Math.cos(a),Y=f.cy+f.ry*Math.sin(a),dx=-f.rx*Math.sin(a)*f.sp,dy=f.ry*Math.cos(a)*f.sp,ang=Math.atan2(dy,dx),w=Math.sin(t*3+i)*.35;
   x.save();x.translate(X,Y);x.rotate(ang);x.globalAlpha=.9;
   x.fillStyle=f.c[0];x.beginPath();x.ellipse(0,0,f.L*.5,f.L*.17,0,0,7);x.fill();
   x.fillStyle=f.c[1];x.beginPath();x.ellipse(f.L*.12,0,f.L*.16,f.L*.11,0,0,7);x.fill();
   x.save();x.translate(-f.L*.45,0);x.rotate(w);x.fillStyle=f.c[0];x.globalAlpha=.7;x.beginPath();x.moveTo(0,0);x.lineTo(-f.L*.32,-f.L*.16);x.lineTo(-f.L*.28,0);x.lineTo(-f.L*.32,f.L*.16);x.closePath();x.fill();x.restore();
   x.restore()}x.globalAlpha=1;
  for(i=0;i<PAD.length;i++){var p=PAD[i];x.fillStyle='rgba(46,92,60,.92)';x.beginPath();x.moveTo(p[0],p[1]);x.arc(p[0],p[1],p[2],.3+i,6.0+i);x.closePath();x.fill();if(i%2==0){x.fillStyle='rgba(240,200,215,.9)';x.beginPath();x.arc(p[0]+p[2]*.2,p[1]-p[2]*.2,p[2]*.18,0,7);x.fill()}}});return L};

/* Zöllner illusion: parallel lines look tilted because of short cross-hatches */
W.hzzoll=function(L,it){L.style.background='#e9e6df';var c=wCv(L),x=c.getContext('2d'),A=Math.PI/4;
 T(L,'<div class="hzbox" style="background:rgba(20,24,28,.85)">'+hd('Göz Oyunu · Optical Illusion','Bu uzun çizgiler birbirine paralel mi?','Are these long lines parallel?')+'</div>','top:20px',.4);
 T(L,'<div class="hzbox" style="background:rgba(20,24,28,.85)"><div class="a" style="font-size:1.95vw">Hepsi tamamen paralel! Kısa çizgiler kaybolunca kendin gör</div><div class="e" style="font-size:1.35vw">They are perfectly parallel — watch as the short marks fade away</div><div class="sm">Zöllner illüzyonu · Zöllner illusion — Johann Zöllner, 1860</div></div>','bottom:18px',16);
 wLoop(L,function(t){var ha=t<17?1:Math.max(0,1-(t-17)/4);if(t>34)ha=Math.min(1,(t-34)/3);x.clearRect(0,0,1920,1080);x.save();x.beginPath();x.rect(300,240,1320,600);x.clip();
  for(var k=0;k<9;k++){var ox=180+k*190;x.strokeStyle='#111';x.lineWidth=5;x.beginPath();x.moveTo(ox,240);x.lineTo(ox+600,840);x.stroke();
   x.globalAlpha=ha;x.lineWidth=4;for(var s=0;s<14;s++){var px=ox+s*45,py=240+s*45,dr=(k%2?1:-1);x.beginPath();if(dr>0){x.moveTo(px-26,py);x.lineTo(px+26,py)}else{x.moveTo(px,py-26);x.lineTo(px,py+26)}x.stroke()}x.globalAlpha=1}
  x.restore()});return L};

/* ---------- v59 additions: hzturing hzvoronoi hzcollatz hzsnow (art/sims), hzpogg hzwhite (illusions) ---------- */
/* Turing patterns: Gray-Scott reaction-diffusion grows leopard-like spots, then a coral/zebra labyrinth */
W.hzturing=function(L,it){L.style.background='#0b0a09';var c=wCv(L),x=c.getContext('2d'),GW=128,GH=72,N=GW*GH,A,B,A2,B2,off=document.createElement('canvas');off.width=GW;off.height=GH;var o=off.getContext('2d'),im=o.createImageData(GW,GH),dd=im.data,mode=-1,i;
 var PR=[{f:.0367,k:.0649,c0:[28,18,12],c1:[226,196,150],n:'Benekler · Spots — f 0,037 · k 0,065'},{f:.0545,k:.062,c0:[10,24,30],c1:[214,232,228],n:'Labirent · Labyrinth — f 0,055 · k 0,062'}];
 function seed(){A=new Float32Array(N);B=new Float32Array(N);A2=new Float32Array(N);B2=new Float32Array(N);for(i=0;i<N;i++)A[i]=1;for(var s=0;s<26;s++){var cx=4+Math.floor(Math.random()*(GW-8)),cy=4+Math.floor(Math.random()*(GH-8));for(var yy=-2;yy<=2;yy++)for(var xx=-2;xx<=2;xx++)B[(cy+yy)*GW+cx+xx]=1}}
 function step(p){for(var y=0;y<GH;y++){var yu=((y+GH-1)%GH)*GW,yd=((y+1)%GH)*GW,yc=y*GW;for(var xx=0;xx<GW;xx++){var xl=(xx+GW-1)%GW,xr=(xx+1)%GW,k=yc+xx,a=A[k],b=B[k];
  var la=.2*(A[yc+xl]+A[yc+xr]+A[yu+xx]+A[yd+xx])+.05*(A[yu+xl]+A[yu+xr]+A[yd+xl]+A[yd+xr])-a,lb=.2*(B[yc+xl]+B[yc+xr]+B[yu+xx]+B[yd+xx])+.05*(B[yu+xl]+B[yu+xr]+B[yd+xl]+B[yd+xr])-b,abb=a*b*b;
  A2[k]=a+(la-abb+p.f*(1-a));B2[k]=b+(.5*lb+abb-(p.k+p.f)*b)}}var t1=A;A=A2;A2=t1;t1=B;B=B2;B2=t1}
 T(L,'<div class="hzbox">'+hd('Turing’in Desenleri · Turing Patterns — simülasyon · simulation','İki kimyasal yarışıyor: biri yayılıyor, biri frenliyor…','Two chemicals race: one spreads, one holds it back…')+'</div>','top:22px',.4);
 var V=T(L,'','bottom:22px',1);
 wLoop(L,function(t){var m=t<36?0:1;if(m!==mode){mode=m;seed();V.innerHTML='<div class="hzbox"><div class="sm" style="font-size:1.25vw;color:#e8e2d8">Alan Turing, 1952: leoparın benekleri ve zebranın çizgileri böyle basit kurallarla oluşabilir · Leopard spots and zebra stripes can arise from simple rules like these<br><i style="color:#b9c4c9">'+PR[m].n+'</i></div></div>'}
  var p=PR[mode];for(var s=0;s<12;s++)step(p);
  for(i=0;i<N;i++){var v=Math.max(0,Math.min(1,(A[i]-B[i]-.1)*1.6)),q=i*4;dd[q]=p.c0[0]+(p.c1[0]-p.c0[0])*v;dd[q+1]=p.c0[1]+(p.c1[1]-p.c0[1])*v;dd[q+2]=p.c0[2]+(p.c1[2]-p.c0[2])*v;dd[q+3]=255}
  o.putImageData(im,0,0);x.imageSmoothingEnabled=true;x.drawImage(off,0,0,1920,1080)});return L};

/* Voronoi: every point of the plane belongs to its nearest seed. Cells grow at the same speed and meet on straight borders */
W.hzvoronoi=function(L,it){L.style.background='#0c0b0a';var c=wCv(L),x=c.getContext('2d'),GW=384,GH=216,N=GW*GH,off=document.createElement('canvas');off.width=GW;off.height=GH;var o=off.getContext('2d'),im=o.createImageData(GW,GH),dd=im.data,rnd=-1,R=null;
 var PAL=[{edge:[236,226,206],cols:[[122,62,34],[140,74,40],[104,52,30],[150,86,48],[118,70,44]],n:'Zürafa derisi gibi · Like a giraffe’s coat'},{edge:[18,20,24],cols:[[54,92,110],[120,150,120],[170,90,70],[200,190,170],[70,110,90],[140,70,80],[90,120,160]],n:'Vitray gibi · Like stained glass'}];
 function build(r){var p=PAL[r],S=[],i,k;for(i=0;i<42;i++)S.push([Math.random()*GW,Math.random()*GH,p.cols[i%p.cols.length]]);
  var D1=new Float32Array(N),D2=new Float32Array(N),ID=new Uint8Array(N),mx=0;for(var y=0;y<GH;y++)for(var xx=0;xx<GW;xx++){var a=1e9,b=1e9,id=0;for(k=0;k<S.length;k++){var dx=S[k][0]-xx,dy=S[k][1]-y,d=dx*dx+dy*dy;if(d<a){b=a;a=d;id=k}else if(d<b)b=d}var j=y*GW+xx;D1[j]=Math.sqrt(a);D2[j]=Math.sqrt(b);ID[j]=id;if(D1[j]>mx)mx=D1[j]}
  var nb=Math.ceil(mx)+1,cnt=new Int32Array(nb+1);for(i=0;i<N;i++)cnt[Math.floor(D1[i])+1]++;for(i=1;i<=nb;i++)cnt[i]+=cnt[i-1];var ord=new Int32Array(N),pos=new Int32Array(cnt);for(i=0;i<N;i++)ord[pos[Math.floor(D1[i])]++]=i;
  for(i=0;i<N*4;i+=4){dd[i]=12;dd[i+1]=11;dd[i+2]=10;dd[i+3]=255}return {S:S,D1:D1,D2:D2,ID:ID,ord:ord,p:0,mx:mx,pal:p}}
 T(L,'<div class="hzbox">'+hd('Hücrelerin Geometrisi · Geometry of Cells — çizim · illustration','Her nokta en yakın tohuma ait: Voronoi hücreleri','Every point belongs to its nearest seed: Voronoi cells')+'</div>','top:22px',.4);
 var V=T(L,'','bottom:22px',1);
 wLoop(L,function(t){var r=t<34?0:1;if(r!==rnd){rnd=r;R=build(r);V.innerHTML='<div class="hzbox"><div class="sm" style="font-size:1.25vw;color:#e8e2d8">Hücreler aynı hızla büyür ve buluştukları yerde düz bir sınır çizer — zürafa derisi, yusufçuk kanadı, kuruyan çamur<br><i style="color:#b9c4c9">Cells grow at the same speed and meet on straight borders — giraffe skin, dragonfly wings, drying mud · '+R.pal.n+'</i></div></div>'}
  var rad=Math.max(0,(t-r*34-2))*12.8;while(R.p<N&&R.D1[R.ord[R.p]]<=rad){var j=R.ord[R.p++],q=j*4,col=R.S[R.ID[j]][2],e=R.D2[j]-R.D1[j]<1.35,sh=1-.18*Math.min(1,R.D1[j]/72);
   if(e){dd[q]=R.pal.edge[0];dd[q+1]=R.pal.edge[1];dd[q+2]=R.pal.edge[2]}else{dd[q]=col[0]*sh;dd[q+1]=col[1]*sh;dd[q+2]=col[2]*sh}}
  o.putImageData(im,0,0);x.imageSmoothingEnabled=true;x.drawImage(off,0,0,1920,1080);x.fillStyle='rgba(255,255,255,.9)';for(var k=0;k<R.S.length;k++){x.beginPath();x.arc(R.S[k][0]*5,R.S[k][1]*5,4,0,7);x.fill()}});return L};

/* Collatz coral: draw every number's path back to 1, turning one way on even steps and the other way on odd steps */
W.hzcollatz=function(L,it){grad(L,'#10202a','#03070a');var c=wCv(L),x=c.getContext('2d'),n=1,MAXN=4000,EA=.08,OA=-.096,SL=7.5;
 T(L,'<div class="hzbox">'+hd('Sayıların Gizemi · Mystery of Numbers — çizim · illustration','Çiftse ikiye böl, tekse 3’le çarp 1 ekle… Hep 1’e mi varır?','If even, halve it; if odd, triple it and add 1… Does it always reach 1?')+'</div>','top:22px',.4);
 var V=T(L,'','top:430px;left:60px;right:auto;width:420px;text-align:left',1);
 T(L,'<div class="hzbox"><div class="sm" style="font-size:1.22vw;color:#dfe6e9">Her sayının 1’e giden yolu çiziliyor: çift adımda sağa, tek adımda sola dön. Ortaya bir deniz yosunu çıkıyor<br><i>Each number’s path to 1 is drawn — turn right on even steps, left on odd ones. A seaweed appears. Collatz sanısı, 1937 — hâlâ kanıtlanamadı · still unproven</i></div></div>','bottom:20px',6);
 wLoop(L,function(t){var tg=Math.min(MAXN,Math.floor(t<10?t*3:30+Math.pow(t-10,2)*2.4));
  for(;n<=tg;n++){var s=[],v=n;while(v!=1){s.push(v);v=(v%2==0)?v/2:(3*v+1)/2}s.push(1);var px=1200,py=900,a=-Math.PI/2;x.strokeStyle='hsla('+(165+Math.min(120,s.length*1.1))+',55%,'+(58+n%10)+'%,'+(n<40?.8:.13)+')';x.lineWidth=n<40?2.2:1.2;x.beginPath();x.moveTo(px,py);
   for(var i=s.length-2;i>=0;i--){a+=(s[i]%2==0)?EA:OA;px+=SL*Math.cos(a);py+=SL*Math.sin(a);x.lineTo(px,py)}x.stroke()}
  var m=Math.max(1,n-1),st=0,v2=m,mxv=m;while(v2!=1){v2=(v2%2==0)?v2/2:3*v2+1;st++;if(v2>mxv)mxv=v2}
  V.innerHTML='<div class="hzbox" style="padding:14px 26px"><div class="lb">Sayı · Number</div><div style="font-size:2.4vw">'+m.toLocaleString('tr-TR')+'</div><div class="lb" style="margin-top:12px">1’e kadar adım · Steps to 1</div><div class="a" style="font-size:2.1vw">'+st+'</div><div class="sm">en yüksek · peak: '+mxv.toLocaleString('tr-TR')+'</div></div>'});return L};

/* calm night: first snow over a quiet hillside house (illustration) */
W.hzsnow=function(L,it){var c=wCv(L),x=c.getContext('2d'),F=[],i,TR=[];for(i=0;i<420;i++)F.push([Math.random()*1920,Math.random()*1080,.4+Math.random()*1.6,Math.random()*6.28]);
 for(i=0;i<38;i++)TR.push([Math.random()*1920,0,30+Math.random()*40]);for(i=0;i<TR.length;i++){var u=TR[i][0];TR[i][1]=760+Math.sin(u*.0021+1)*60+Math.sin(u*.006)*18}
 T(L,hd('Sessiz Gece · Quiet Night — çizim · illustration, hayal ürünü · imagined (sakin · calm)','Yaylaya ilk kar düşüyor','The first snow falls on the highlands'),'top:44px',2);
 T(L,'<div class="sm" style="font-size:1.25vw;color:#cdd6dc">Taze kar sesi yutar: kar tanelerinin arasındaki hava, sünger gibi sesleri emer<br><i>Fresh snow swallows sound — the air between the flakes soaks it up like a sponge</i></div>','bottom:40px',9);
 wLoop(L,function(t){var g=x.createLinearGradient(0,0,0,1080);g.addColorStop(0,'#060a16');g.addColorStop(.6,'#142036');g.addColorStop(1,'#1c2a40');x.fillStyle=g;x.fillRect(0,0,1920,1080);
  var mg=x.createRadialGradient(1480,250,10,1480,250,260);mg.addColorStop(0,'rgba(220,228,245,.55)');mg.addColorStop(.2,'rgba(200,210,235,.18)');mg.addColorStop(1,'rgba(200,210,235,0)');x.fillStyle=mg;x.fillRect(1180,0,600,560);x.fillStyle='#e6ebf5';x.beginPath();x.arc(1480,250,46,0,7);x.fill();
  x.fillStyle='#2a3a52';x.beginPath();x.moveTo(0,1080);for(var u=0;u<=1920;u+=30)x.lineTo(u,650+Math.sin(u*.0016+2)*80);x.lineTo(1920,1080);x.fill();
  x.fillStyle='#d5dceb';x.beginPath();x.moveTo(0,1080);for(u=0;u<=1920;u+=30)x.lineTo(u,760+Math.sin(u*.0021+1)*60+Math.sin(u*.006)*18);x.lineTo(1920,1080);x.fill();
  for(i=0;i<TR.length;i++){var tx=TR[i][0],ty=TR[i][1]+6,h=TR[i][2]*2.2;x.fillStyle='#0d1626';x.beginPath();x.moveTo(tx,ty-h);x.lineTo(tx-h*.32,ty);x.lineTo(tx+h*.32,ty);x.fill();x.fillStyle='rgba(225,232,245,.8)';x.beginPath();x.moveTo(tx,ty-h);x.lineTo(tx-h*.1,ty-h*.68);x.lineTo(tx+h*.1,ty-h*.68);x.fill()}
  var hx=760,hy=772;x.fillStyle='#3a2c24';x.fillRect(hx,hy-80,170,80);x.fillStyle='#e8edf6';x.beginPath();x.moveTo(hx-22,hy-78);x.lineTo(hx+85,hy-150);x.lineTo(hx+192,hy-78);x.fill();
  var fl=.85+.08*Math.sin(t*1.3);x.fillStyle='rgba(255,214,160,'+fl+')';x.fillRect(hx+30,hy-58,34,30);x.fillRect(hx+106,hy-58,34,30);var wg=x.createRadialGradient(hx+85,hy-40,5,hx+85,hy-40,190);wg.addColorStop(0,'rgba(255,200,140,.16)');wg.addColorStop(1,'rgba(255,200,140,0)');x.fillStyle=wg;x.fillRect(hx-120,hy-240,410,360);
  x.fillStyle='rgba(180,190,205,.18)';for(i=0;i<5;i++){var sy=hy-170-i*40-(t*14)%40;x.beginPath();x.arc(hx+130+Math.sin(t*.5+i)*10,sy,10+i*4,0,7);x.fill()}
  x.fillStyle='#fff';for(i=0;i<F.length;i++){var f=F[i];f[1]+=f[2]*.55;f[0]+=Math.sin(t*.4+f[3])*.35;if(f[1]>1085){f[1]=-5;f[0]=Math.random()*1920}x.globalAlpha=.35+f[2]*.3;x.beginPath();x.arc(f[0],f[1],f[2]*1.4,0,7);x.fill()}x.globalAlpha=1});return L};

/* Poggendorff illusion: which line on the right continues the line on the left? */
W.hzpogg=function(L,it){L.style.background='#e9e6df';var c=wCv(L),x=c.getContext('2d'),BX0=840,BX1=1080,BY0=300,BY1=880,sl=-.42,X0=420,Y0=850;
 function yAt(X,off){return Y0+(X-X0)*sl+(off||0)}
 T(L,'<div class="hzbox" style="background:rgba(20,24,28,.85)">'+hd('Göz Oyunu · Optical Illusion','Soldaki çizgi, sağdaki hangi çizgiyle devam ediyor: A, B ya da C?','Which line on the right continues the line on the left: A, B or C?')+'</div>','top:20px',.4);
 T(L,'<div class="hzbox" style="background:rgba(20,24,28,.85)"><div class="a" style="font-size:1.95vw">Doğru cevap B — çoğu gözü yanılır!</div><div class="e" style="font-size:1.35vw">The answer is B — most eyes get it wrong. Kutunun kenarları açıyı yanlış okutur · The band’s edges trick your sense of angle</div><div class="sm">Poggendorff illüzyonu · Poggendorff illusion — 1860</div></div>','bottom:18px',18);
 x.font='bold 46px Helvetica,Arial';x.textAlign='left';x.textBaseline='middle';
 wLoop(L,function(t){var r=t<17?0:Math.min(1,(t-17)/3);x.clearRect(0,0,1920,1080);x.lineCap='round';
  x.strokeStyle='#1b2328';x.lineWidth=7;x.beginPath();x.moveTo(X0,Y0);x.lineTo(BX0,yAt(BX0));x.stroke();
  var offs=[-70,0,70],nm=['A','B','C'];for(var k=0;k<3;k++){x.strokeStyle='#1b2328';x.beginPath();x.moveTo(BX1,yAt(BX1,offs[k]));x.lineTo(1380,yAt(1380,offs[k]));x.stroke();x.fillStyle='#1b2328';x.fillText(nm[k],1405,yAt(1395,offs[k]))}
  if(r>0){x.globalAlpha=r;x.strokeStyle='#d0432c';x.lineWidth=4;x.setLineDash([16,12]);x.beginPath();x.moveTo(X0,Y0);x.lineTo(1380,yAt(1380));x.stroke();x.setLineDash([]);x.globalAlpha=1}
  x.fillStyle='rgba(120,138,150,'+(1-r*.7)+')';x.fillRect(BX0,BY0,BX1-BX0,BY1-BY0)});return L};

/* White's illusion: the grey bars are identical */
W.hzwhite=function(L,it){L.style.background='#808080';var c=wCv(L),x=c.getContext('2d'),X0=360,Y0=290,H=40,NR=14,W2=1200;
 T(L,'<div class="hzbox" style="background:rgba(20,24,28,.85)">'+hd('Göz Oyunu · Optical Illusion','Hangi gri çubuklar daha açık: soldakiler mi, sağdakiler mi?','Which grey bars are lighter: the left ones or the right ones?')+'</div>','top:20px',.4);
 T(L,'<div class="hzbox" style="background:rgba(20,24,28,.85)"><div class="a" style="font-size:1.95vw">Hepsi tamamen aynı gri! Çizgiler kaybolunca kendin gör</div><div class="e" style="font-size:1.35vw">They are all exactly the same grey — watch as the stripes fade</div><div class="sm">White illüzyonu · White’s illusion — Michael White, 1979</div></div>','bottom:18px',17);
 wLoop(L,function(t){var f=t<17?1:Math.max(0,1-(t-17)/4);if(t>36)f=Math.min(1,(t-36)/3);x.clearRect(0,0,1920,1080);
  for(var r=0;r<NR;r++){var blk=r%2==0,v=Math.round(blk?128-128*f:128+127*f);x.fillStyle='rgb('+v+','+v+','+v+')';x.fillRect(X0,Y0+r*H,W2,H)}
  x.fillStyle='rgb(128,128,128)';for(r=3;r<NR-3;r++){if(r%2==0)x.fillRect(X0+170,Y0+r*H,200,H);else x.fillRect(X0+W2-370,Y0+r*H,200,H)}});return L};


/* ---------- v60 additions: hzdla hzsandpile hzgalaxy hzmoonsea (art/sims), hzhering hzponzo (illusions) ---------- */
/* time-budgeted work helper: run fn() repeatedly for at most ms milliseconds */
function budget(ms,fn){var t0=Date.now(),n=0;while(Date.now()-t0<ms){if(fn()===false)break;n++}return n}

/* Diffusion-limited aggregation: random walkers stick to a growing crystal (frost, coral, lightning scars) */
W.hzdla=function(L,it){L.style.background='#05080d';var c=wCv(L),x=c.getContext('2d'),GW=480,GH=270,N=GW*GH,G=new Uint8Array(N),off=document.createElement('canvas');off.width=GW;off.height=GH;var o=off.getContext('2d'),im=o.createImageData(GW,GH),dd=im.data,CX=240,CY=140,rmax=2,cnt=1,RL=92,wx=0,wy=0,alive=false,i;
 for(i=0;i<N*4;i+=4){dd[i]=5;dd[i+1]=8;dd[i+2]=13;dd[i+3]=255}
 function put(px,py){var j=py*GW+px;G[j]=1;var q=j*4,h=Math.min(1,cnt/5200);dd[q]=235-h*170;dd[q+1]=245-h*60;dd[q+2]=255-h*40;cnt++;var r=Math.sqrt((px-CX)*(px-CX)+(py-CY)*(py-CY));if(r>rmax)rmax=r}
 put(CX,CY);
 function spawn(){var a=Math.random()*6.2832,r=rmax+4;wx=Math.round(CX+r*Math.cos(a));wy=Math.round(CY+r*Math.sin(a));alive=true}
 T(L,'<div class="hzbox">'+hd('Kristallerin Büyümesi · How Crystals Grow — simülasyon · simulation','Rastgele dolaşan her parçacık, ilk değdiği yere yapışıyor…','Each randomly wandering particle sticks to the first thing it touches…')+'</div>','top:22px',.4);
 var V=T(L,'','top:430px;left:60px;right:auto;width:400px;text-align:left',1);
 T(L,'<div class="hzbox"><div class="sm" style="font-size:1.22vw;color:#dfe6e9">Kural bu kadar basit — ama ortaya buz çiçekleri, mercanlar, şimşek izleri ve taşlardaki maden dendritleri gibi dallar çıkıyor<br><i>That is the whole rule — yet it grows branches like frost, coral, lightning scars and mineral dendrites. Difüzyonla sınırlı büyüme · Diffusion-limited aggregation (Witten &amp; Sander, 1981)</i></div></div>','bottom:20px',6);
 wLoop(L,function(t){if(rmax<RL){budget(14,function(){for(var s=0;s<400;s++){if(!alive)spawn();var m=Math.random()*4|0;if(m==0)wx++;else if(m==1)wx--;else if(m==2)wy++;else wy--;
    var dx=wx-CX,dy=wy-CY,r2=dx*dx+dy*dy;if(r2>(rmax+14)*(rmax+14)||wx<1||wy<1||wx>=GW-1||wy>=GH-1){alive=false;continue}
    var j=wy*GW+wx;if(G[j-1]||G[j+1]||G[j-GW]||G[j+GW]){put(wx,wy);alive=false;if(rmax>=RL)return false}}})}
  o.putImageData(im,0,0);x.imageSmoothingEnabled=false;x.clearRect(0,0,1920,1080);x.drawImage(off,0,0,1920,1080);
  V.innerHTML='<div class="hzbox" style="padding:14px 26px"><div class="lb">Parçacık · Particles</div><div style="font-size:2.4vw">'+cnt.toLocaleString('tr-TR')+'</div></div>'});return L};

/* Abelian sandpile: add grains to one cell; any cell with 4 grains gives one to each neighbour. A fractal appears */
W.hzsandpile=function(L,it){L.style.background='#070a10';var c=wCv(L),x=c.getContext('2d'),S=181,N=S*S,G=new Int32Array(N),off=document.createElement('canvas');off.width=S;off.height=S;var o=off.getContext('2d'),im=o.createImageData(S,S),dd=im.data,C=(S>>1)*S+(S>>1),added=0,TOT=40000,lo=S>>1,hi=S>>1;
 var COL=[[12,18,30],[38,104,124],[214,182,128],[238,236,228]];
 T(L,'<div class="hzbox">'+hd('Kum Yığını · Sandpile — simülasyon · simulation','Ortaya tek tek kum tanesi ekleniyor. 4 tane biriken kare, komşularına birer tane dağıtıyor…','Grains are dropped in the middle. Any square with 4 grains hands one to each neighbour…')+'</div>','top:22px',.4);
 var V=T(L,'','top:430px;left:60px;right:auto;width:400px;text-align:left',1);
 T(L,'<div class="hzbox"><div class="sm" style="font-size:1.22vw;color:#dfe6e9">Tek bir tane bazen hiçbir şey yapmaz, bazen bütün yığını kaydırır: kendiliğinden kritiklik. Depremler, çığlar ve orman yangınları da böyle davranır<br><i>One grain may do nothing — or set off an avalanche across the whole pile: self-organised criticality, like earthquakes, snow slides and forest fires. Bak–Tang–Wiesenfeld, 1987</i></div></div>','bottom:20px',6);
 function sweep(){var any=false;for(var y=lo;y<=hi;y++){var r=y*S;for(var xx=lo;xx<=hi;xx++){var j=r+xx,v=G[j];if(v>=4){var q=v>>2;G[j]=v-4*q;G[j-1]+=q;G[j+1]+=q;G[j-S]+=q;G[j+S]+=q;any=true;if(xx-1<lo)lo=Math.max(1,xx-1);if(xx+1>hi)hi=Math.min(S-2,xx+1);if(y-1<lo)lo=Math.max(1,y-1);if(y+1>hi)hi=Math.min(S-2,y+1)}}}return any}
 wLoop(L,function(t){var target=Math.min(TOT,Math.floor(t<4?0:Math.pow((t-4)/44,1.4)*TOT));if(target>added){G[C]+=target-added;added=target}
  budget(14,function(){return sweep()});
  for(var j=0;j<N;j++){var v=G[j],q=j*4,cc=v>3?[255,255,255]:COL[v];dd[q]=cc[0];dd[q+1]=cc[1];dd[q+2]=cc[2];dd[q+3]=255}
  o.putImageData(im,0,0);x.imageSmoothingEnabled=false;x.clearRect(0,0,1920,1080);x.drawImage(off,960-362+80,560-362+20,724,724);
  V.innerHTML='<div class="hzbox" style="padding:14px 26px"><div class="lb">Kum tanesi · Grains</div><div style="font-size:2.4vw">'+added.toLocaleString('tr-TR')+'</div><div class="sm">0 · 1 · 2 · 3 tane: lacivert · camgöbeği · kum · beyaz<br>navy · teal · sand · white</div></div>'});return L};

/* Spiral galaxy from tilted ellipses: stars on ellipses, each ellipse turned a little more — arms appear (density wave) */
W.hzgalaxy=function(L,it){L.style.background='#020308';var c=wCv(L),x=c.getContext('2d'),ST=[],i,BG=stars(240);
 for(i=0;i<11000;i++){var a=Math.round((Math.pow(Math.random(),.8)*400+18)/4)*4;ST.push([a,Math.random()*6.2832,i<14])}
 T(L,'<div class="hzbox">'+hd('Galaksiler · Galaxies — simülasyon · simulation','Her yıldız kendi oval yolunda dönüyor. Ovaller biraz biraz döndürülünce…','Every star circles on its own oval path. Turn each oval a little more than the last…')+'</div>','top:22px',.4);
 T(L,'<div class="hzbox"><div class="sm" style="font-size:1.22vw;color:#dfe6e9">…sarmal kollar belirir. Kollar sabit değildir: kırmızı yıldızlar kollara girip çıkar — tıpkı otoyoldaki trafik sıkışıklığı gibi<br><i>…spiral arms appear. The arms are not fixed: the red stars drift into them and out again — like a traffic jam on a motorway. Yoğunluk dalgası · Density wave theory (Lin &amp; Shu, 1964)</i></div></div>','bottom:20px',12);
 wLoop(L,function(t){x.fillStyle='#020308';x.fillRect(0,0,1920,1080);drawStars(x,BG,t);
  var tw=t<8?0:Math.min(1,(t-8)/14)*.0105,cx=960,cy=575,tl=.78,rot=t*.03;x.globalCompositeOperation='lighter';
  for(var k=0;k<ST.length;k++){var s=ST[k],a=s[0],b=a*.62,ph=a*tw+rot,th=s[1]+t*3.2/Math.sqrt(a+40);
   var ex=a*Math.cos(th),ey=b*Math.sin(th),px=ex*Math.cos(ph)-ey*Math.sin(ph),py=(ex*Math.sin(ph)+ey*Math.cos(ph))*tl;
   if(s[2]){x.fillStyle='#ff5a4a';x.beginPath();x.arc(cx+px,cy+py,5,0,7);x.fill();continue}
   var f=Math.max(0,1-a/420);x.fillStyle='rgba('+(150+105*f|0)+','+(180+60*f|0)+',255,'+(.28+.35*f)+')';x.fillRect(cx+px-1,cy+py-1,2.2,2.2)}
  var g=x.createRadialGradient(cx,cy,0,cx,cy,110);g.addColorStop(0,'rgba(255,240,220,.4)');g.addColorStop(1,'rgba(255,240,220,0)');x.fillStyle=g;x.fillRect(cx-110,cy-110,220,220);x.globalCompositeOperation='source-over'});return L};

/* calm night: moonlight draws a silver road on the Black Sea (illustration) */
W.hzmoonsea=function(L,it){var c=wCv(L),x=c.getContext('2d'),S=stars(200),GL=[],i,HZ=600,MX=1260;
 for(i=0;i<900;i++){var d=Math.pow(Math.random(),1.6);GL.push([d,(Math.random()-.5),Math.random()*6.28,.4+Math.random()*1.2])}
 T(L,hd('Gece Denizi · Night Sea — çizim · illustration, hayal ürünü · imagined (sakin · calm)','Ay ışığı denizde gümüş bir yol çiziyor','Moonlight draws a silver road across the sea'),'top:44px',2);
 T(L,'<div class="sm" style="font-size:1.25vw;color:#cdd6dc">Bu yol aslında yok: her dalga, ayı sana yansıtan minik bir ayna. Kıyıdaki herkes yolu kendi önünde görür<br><i>The road isn’t really there: every wave is a tiny mirror tilting the moon towards you — everyone on the shore sees the path leading to themselves</i></div>','bottom:40px',9);
 wLoop(L,function(t){var g=x.createLinearGradient(0,0,0,HZ);g.addColorStop(0,'#03060f');g.addColorStop(1,'#16223a');x.fillStyle=g;x.fillRect(0,0,1920,HZ);drawStars(x,S.filter(function(s){return s[1]<HZ-40}),t);
  var mg=x.createRadialGradient(MX,250,10,MX,250,300);mg.addColorStop(0,'rgba(230,236,250,.5)');mg.addColorStop(.25,'rgba(200,212,240,.14)');mg.addColorStop(1,'rgba(200,212,240,0)');x.fillStyle=mg;x.fillRect(MX-300,0,600,560);x.fillStyle='#eef1f8';x.beginPath();x.arc(MX,250,52,0,7);x.fill();
  var sg=x.createLinearGradient(0,HZ,0,1080);sg.addColorStop(0,'#0e1a2e');sg.addColorStop(1,'#04080f');x.fillStyle=sg;x.fillRect(0,HZ,1920,480);
  x.fillStyle='#070b14';x.beginPath();x.moveTo(0,HZ);for(var u=0;u<=760;u+=20)x.lineTo(u,HZ-26-Math.sin(u*.008)*22-Math.sin(u*.03)*5);x.lineTo(760,HZ);x.fill();
  x.fillStyle='rgba(255,206,150,.85)';for(i=0;i<14;i++){var lx=40+i*50+(i*37%23),ly=HZ-8-(i*13%11);x.fillRect(lx,ly,2.4,2.4)}
  for(i=0;i<GL.length;i++){var p=GL[i],yy=HZ+4+p[0]*470,wd=40+p[0]*420,xx=MX+p[1]*wd*(1+.15*Math.sin(t*.3+p[2])),al=Math.max(0,Math.sin(t*p[3]+p[2]))*(.25+.6*(1-p[0]*.6));
   x.fillStyle='rgba(225,232,248,'+al.toFixed(3)+')';x.fillRect(xx,yy,6+p[0]*30,1.2+p[0]*2.2)}
  x.strokeStyle='rgba(120,140,170,.10)';x.lineWidth=1;for(i=0;i<12;i++){var wy=HZ+20+i*i*3.4+((t*6)%14);x.beginPath();for(u=0;u<=1920;u+=40)x.lineTo(u,wy+Math.sin(u*.01+t*.4+i)*2);x.stroke()}});return L};

/* Hering illusion: two straight red lines look bowed by the rays behind them */
W.hzhering=function(L,it){L.style.background='#ece8e0';var c=wCv(L),x=c.getContext('2d');
 T(L,'<div class="hzbox" style="background:rgba(20,24,28,.85)">'+hd('Göz Oyunu · Optical Illusion','Kırmızı çizgiler düz mü, yoksa dışa doğru eğri mi?','Are the red lines straight, or do they bow outwards?')+'</div>','top:20px',.4);
 T(L,'<div class="hzbox" style="background:rgba(20,24,28,.85)"><div class="a" style="font-size:1.95vw">İkisi de dümdüz ve birbirine paralel! Işınlar kaybolunca kendin gör</div><div class="e" style="font-size:1.35vw">Both are perfectly straight and parallel — watch as the rays fade</div><div class="sm">Hering illüzyonu · Hering illusion — Ewald Hering, 1861</div></div>','bottom:18px',17);
 wLoop(L,function(t){var f=t<17?1:Math.max(0,1-(t-17)/4);if(t>36)f=Math.min(1,(t-36)/3);x.clearRect(0,0,1920,1080);var cx=960,cy=560;
  x.save();x.beginPath();x.rect(380,230,1160,660);x.clip();x.globalAlpha=f;x.strokeStyle='#1d252b';x.lineWidth=2.2;for(var k=0;k<40;k++){var a=k*Math.PI/40;x.beginPath();x.moveTo(cx-Math.cos(a)*900,cy-Math.sin(a)*900);x.lineTo(cx+Math.cos(a)*900,cy+Math.sin(a)*900);x.stroke()}x.restore();x.globalAlpha=1;
  x.strokeStyle='#c8372a';x.lineWidth=7;x.beginPath();x.moveTo(cx-150,240);x.lineTo(cx-150,880);x.moveTo(cx+150,240);x.lineTo(cx+150,880);x.stroke()});return L};

/* Ponzo illusion: two identical bars on railway tracks — the upper one looks longer */
W.hzponzo=function(L,it){L.style.background='#d9d4c8';var c=wCv(L),x=c.getContext('2d');
 T(L,'<div class="hzbox" style="background:rgba(20,24,28,.85)">'+hd('Göz Oyunu · Optical Illusion','Hangi kırmızı çubuk daha uzun: üstteki mi, alttaki mi?','Which red bar is longer: the top one or the bottom one?')+'</div>','top:20px',.4);
 T(L,'<div class="hzbox" style="background:rgba(20,24,28,.85)"><div class="a" style="font-size:1.95vw">İkisi de tam olarak aynı uzunlukta!</div><div class="e" style="font-size:1.35vw">They are exactly the same length — your brain thinks the top one is farther away, so it “stretches” it</div><div class="sm">Ponzo illüzyonu · Ponzo illusion — Mario Ponzo, 1911</div></div>','bottom:18px',17);
 function rx(y,s){var k=(1000-y)/780;return s<0?560+k*360:1360-k*360}
 wLoop(L,function(t){var f=t<17?1:Math.max(.12,1-(t-17)/4);if(t>36)f=Math.min(1,(t-36)/3);x.clearRect(0,0,1920,1080);
  x.save();x.beginPath();x.rect(0,220,1920,860);x.clip();x.globalAlpha=f;x.strokeStyle='#4a4038';
  for(var k=0;k<16;k++){var y=1000-780*(1-Math.pow(.86,k));x.lineWidth=2+9*Math.pow(.86,k);x.beginPath();x.moveTo(rx(y,-1)-40*Math.pow(.86,k),y);x.lineTo(rx(y,1)+40*Math.pow(.86,k),y);x.stroke()}
  x.strokeStyle='#2a2622';x.lineWidth=9;x.beginPath();x.moveTo(560,1000);x.lineTo(920,220);x.moveTo(1360,1000);x.lineTo(1000,220);x.stroke();x.restore();x.globalAlpha=1;
  x.fillStyle='#c8372a';x.fillRect(850,370,220,22);x.fillRect(850,790,220,22);
  if(t>19&&t<36){var a=Math.min(1,(t-19)/2);x.globalAlpha=a;x.strokeStyle='#1f6f8b';x.lineWidth=3;x.setLineDash([12,10]);x.beginPath();x.moveTo(850,330);x.lineTo(850,850);x.moveTo(1070,330);x.lineTo(1070,850);x.stroke();x.setLineDash([]);x.globalAlpha=1}});return L};

/* ---------- v62 additions: hzlorenz hzlife hztree hzdragon hzrainwin (art/sims; hzrainwin = calm night), hzmuller hzjastrow (illusions) ---------- */
/* Lorenz attractor: three paths that start almost exactly together drift apart — the butterfly effect */
W.hzlorenz=function(L,it){L.style.background='#04060c';var c=wCv(L),x=c.getContext('2d'),hc=wCv(L),h=hc.getContext('2d'),P=[[1,1,1],[1.00001,1,1],[1.00002,1,1]],COL=['#8fd3c1','#ff9e7a','#a9b8ff'],PR=[null,null,null],dt=.005,done=0,SPS=120;
 T(L,'<div class="hzbox">'+hd('Kelebek Etkisi · The Butterfly Effect — simülasyon · simulation','Üç nokta neredeyse aynı yerden yola çıkıyor: aralarındaki fark yüz binde bir…','Three points start from almost the same place — just one hundred-thousandth apart…')+'</div>','top:22px',.4);
 var V=T(L,'','top:430px;left:60px;right:auto;width:420px;text-align:left',1);
 T(L,'<div class="hzbox"><div class="sm" style="font-size:1.22vw;color:#dfe6e9">…bir süre birlikte giderler, sonra bambaşka yollara ayrılırlar. Hava durumu da böyledir: en küçük ölçüm hatası büyür, bu yüzden iki haftadan uzun tahmin yapılamaz<br><i>…they travel together for a while, then split onto completely different paths. Weather works the same way: the tiniest measuring error grows, so forecasts beyond about two weeks are impossible. Lorenz çekicisi · Lorenz attractor (Edward Lorenz, 1963)</i></div></div>','bottom:20px',22);
 function st(p){var dx=10*(p[1]-p[0]),dy=p[0]*(28-p[2])-p[1],dz=p[0]*p[1]-8/3*p[2];p[0]+=dx*dt;p[1]+=dy*dt;p[2]+=dz*dt}
 function sp(p){return [1010+p[0]*24,945-p[2]*13.2]}
 x.lineWidth=2.2;x.lineCap='round';
 wLoop(L,function(t){x.fillStyle='rgba(4,6,12,.008)';x.fillRect(0,0,1920,1080);var want=Math.min(Math.floor(t*SPS),done+40);
  while(done<want){done++;for(var k=0;k<3;k++){st(P[k]);var q=sp(P[k]);if(PR[k]){x.strokeStyle=COL[k];x.globalAlpha=.85;x.beginPath();x.moveTo(PR[k][0],PR[k][1]);x.lineTo(q[0],q[1]);x.stroke()}PR[k]=q}}
  x.globalAlpha=1;h.clearRect(0,0,1920,1080);for(k=0;k<3;k++){if(!PR[k])continue;h.fillStyle=COL[k];h.beginPath();h.arc(PR[k][0],PR[k][1],7,0,7);h.fill()}
  var dd=Math.sqrt(Math.pow(P[0][0]-P[2][0],2)+Math.pow(P[0][1]-P[2][1],2)+Math.pow(P[0][2]-P[2][2],2));
  V.innerHTML='<div class="hzbox" style="padding:14px 26px"><div class="lb">Aradaki fark · Gap</div><div style="font-size:2.3vw">'+(dd<.01?dd.toFixed(5):dd.toFixed(2))+'</div><div class="sm">başta · at start: 0.00002</div></div>'});return L};

/* Conway's Game of Life: four simple rules, living patterns */
W.hzlife=function(L,it){L.style.background='#060a0f';var c=wCv(L),x=c.getContext('2d'),CW=160,CH=90,S=12,N=CW*CH,G=new Uint8Array(N),H=new Float32Array(N),gen=0,last=0,seedT=0,i;
 function seed(){for(i=0;i<N;i++){var cx=(i%CW)-80,cy=((i/CW)|0)-50;G[i]=(Math.abs(cx)<46&&Math.abs(cy)<24&&Math.random()<.34)?1:0}
  var gl=[[1,0],[2,1],[0,2],[1,2],[2,2]];for(var r=0;r<6;r++){var ox=6+r*24,oy=26;gl.forEach(function(p){G[(oy+p[1])*CW+ox+p[0]]=1})}gen=0}
 seed();
 T(L,'<div class="hzbox">'+hd('Yaşam Oyunu · The Game of Life — simülasyon · simulation','Her kare canlı ya da ölü. Komşu sayısına bakarak her adımda yeniden karar veriyor…','Every square is alive or dead — and decides again at every step by counting its neighbours…')+'</div>','top:22px',.4);
 var V=T(L,'','top:430px;left:40px;right:auto;width:330px;text-align:left',1);
 T(L,'<div class="hzbox"><div class="sm" style="font-size:1.2vw;color:#dfe6e9">2 ya da 3 komşu: yaşar · 3 komşu: doğar · gerisi: ölür. Bu kadar basit kurallardan “uçan” desenler, saatler, hatta bilgisayarlar kurulabilir<br><i>2 or 3 neighbours: it lives · 3 neighbours: a birth · otherwise it dies. From rules this simple come gliders, clocks — even working computers. John Conway, 1970</i></div></div>','bottom:20px',8);
 function step(){var nG=new Uint8Array(N);for(var y=0;y<CH;y++)for(var xx=0;xx<CW;xx++){var n=0;for(var dy=-1;dy<=1;dy++)for(var dx=-1;dx<=1;dx++){if(!dx&&!dy)continue;var yy=(y+dy+CH)%CH,x2=(xx+dx+CW)%CW;n+=G[yy*CW+x2]}var j=y*CW+xx;nG[j]=(n==3||(n==2&&G[j]))?1:0;if(G[j]&&!nG[j])H[j]=1}G=nG;gen++}
 wLoop(L,function(t){if(t>2&&t-last>.13){last=t;step();if(gen>420){seed()}}
  x.fillStyle='#060a0f';x.fillRect(0,0,1920,1080);var pop=0;
  for(var j=0;j<N;j++){var px=(j%CW)*S,py=((j/CW)|0)*S;if(G[j]){pop++;x.fillStyle='#8fd3c1';x.fillRect(px+1,py+1,S-2,S-2)}else if(H[j]>.02){x.fillStyle='rgba(255,158,122,'+(H[j]*.45).toFixed(2)+')';x.fillRect(px+2,py+2,S-4,S-4);H[j]*=.93}}
  V.innerHTML='<div class="hzbox" style="padding:14px 26px"><div class="lb">Kuşak · Generation</div><div style="font-size:2.2vw">'+gen+'</div><div class="lb" style="margin-top:.6vw">Canlı · Alive</div><div style="font-size:2.2vw">'+pop+'</div></div>'});return L};

/* Fractal tree: one rule (split in two, a little shorter) repeated — and it sways in the wind */
W.hztree=function(L,it){var c=wCv(L),x=c.getContext('2d'),R=[],i,MAXD=11,PET=[];for(i=0;i<4096;i++)R.push(Math.random());
 for(i=0;i<70;i++)PET.push([Math.random()*1920,Math.random()*1080,Math.random()*6.28,1+Math.random()*1.5]);
 T(L,'<div class="hzbox">'+hd('Yaşayan Sanat · Living Art — çizim · illustration, hayal ürünü · imagined','Tek bir kural: “İkiye ayrıl, biraz kısal.” Sonra aynısını tekrar et…','One rule: “split in two, get a little shorter.” Then do it again…')+'</div>','top:22px',.4);
 T(L,'<div class="hzbox"><div class="sm" style="font-size:1.22vw;color:#dfe6e9">11 tekrarda 2.048 dal uç verir. Ağaçlar, damarlarımız, nehir ağları ve şimşek aynı “dallanma” fikrini kullanır<br><i>Eleven repeats give 2,048 branch tips. Trees, our blood vessels, river networks and lightning all use the same branching idea — a fractal</i></div></div>','bottom:20px',14);
 wLoop(L,function(t){var g=x.createLinearGradient(0,0,0,1080);g.addColorStop(0,'#0b1626');g.addColorStop(1,'#1c2a2a');x.fillStyle=g;x.fillRect(0,0,1920,1080);
  x.fillStyle='#14201c';x.beginPath();x.ellipse(960,1070,700,70,0,0,7);x.fill();
  var grow=Math.min(MAXD+1,t<1?0:(t-1)/1.1),wind=Math.sin(t*.55)*.05+Math.sin(t*1.3)*.015,idx=0;x.lineCap='round';
  function br(x0,y0,a,len,d,id){if(d>grow)return;var f=Math.min(1,grow-d),sw=wind*(d+1)*.35,x1=x0+Math.cos(a+sw)*len*f,y1=y0+Math.sin(a+sw)*len*f;
   x.strokeStyle=d<6?'rgb('+(70+d*6)+','+(52+d*8)+','+(44+d*6)+')':'rgb('+(80+d*6)+','+(110+d*6)+','+(90+d*4)+')';x.lineWidth=Math.max(1,22*Math.pow(.68,d));x.beginPath();x.moveTo(x0,y0);x.lineTo(x1,y1);x.stroke();
   if(d==MAXD&&f>=1){x.fillStyle='rgba(246,206,220,.85)';x.beginPath();x.arc(x1,y1,3.4,0,7);x.fill();return}
   if(f<1)return;var r1=R[id%4096],r2=R[(id*7+3)%4096];br(x1,y1,a-.32-r1*.22,len*(.7+r2*.08),d+1,id*2+1);br(x1,y1,a+.30+r2*.22,len*(.7+r1*.08),d+1,id*2+2)}
  br(960,1060,-Math.PI/2,190,0,0);
  if(grow>MAXD){x.fillStyle='rgba(246,206,220,.75)';for(i=0;i<PET.length;i++){var p=PET[i];p[1]+=p[3]*.6;p[0]+=Math.sin(t*.7+p[2])*.8+.4;if(p[1]>1080){p[1]=300;p[0]=500+Math.random()*900}x.beginPath();x.ellipse(p[0],p[1],4,2.4,p[2]+t,0,7);x.fill()}}});return L};

/* Dragon curve: fold a paper strip in half again and again, unfold every crease to 90° */
W.hzdragon=function(L,it){L.style.background='#070b12';var c=wCv(L),x=c.getContext('2d'),P=[[0,0],[1,0]],lvl=0,MAXL=13,LT=3.6,T0=3;
 T(L,'<div class="hzbox">'+hd('Kâğıt Katlama · Paper Folding — simülasyon · simulation','Bir kâğıt şeridini hep aynı yöne ikiye katla, sonra her kıvrımı dik açıyla aç…','Fold a paper strip in half, always the same way — then open every crease to a right angle…')+'</div>','top:22px',.4);
 var V=T(L,'','top:430px;left:60px;right:auto;width:330px;text-align:left',1);
 T(L,'<div class="hzbox"><div class="sm" style="font-size:1.22vw;color:#dfe6e9">Çizgi hiçbir zaman kendini kesmez ama düzlemi doldurur: Ejderha eğrisi. NASA fizikçileri bunu 1960’larda böyle buldu<br><i>The line never crosses itself, yet it fills the plane: the Dragon curve, discovered by NASA physicists in the 1960s — and Jurassic Park’s chapter pages show it</i></div></div>','bottom:20px',10);
 function rot(p,c0,a){var dx=p[0]-c0[0],dy=p[1]-c0[1],cs=Math.cos(a),sn=Math.sin(a);return [c0[0]+dx*cs-dy*sn,c0[1]+dx*sn+dy*cs]}
 wLoop(L,function(t){var want=Math.min(MAXL,Math.max(0,Math.floor((t-T0)/LT)));while(lvl<want){var pv=P[P.length-1],n=P.length;for(var i=n-2;i>=0;i--){var q=rot(P[i],pv,Math.PI/2);P.push([Math.round(q[0]),Math.round(q[1])])}lvl++}
  var pr=lvl<MAXL&&t>T0?ease(((t-T0)/LT)-lvl):0,pv2=P[P.length-1],A=[];
  if(pr>0){for(var j=P.length-2;j>=0;j--)A.push(rot(P[j],pv2,Math.PI/2*pr))}
  var mnx=1e9,mny=1e9,mxx=-1e9,mxy=-1e9,all=[P,A];all.forEach(function(Z){Z.forEach(function(p){if(p[0]<mnx)mnx=p[0];if(p[0]>mxx)mxx=p[0];if(p[1]<mny)mny=p[1];if(p[1]>mxy)mxy=p[1]})});
  var sc=Math.min(1240/Math.max(1,mxx-mnx),560/Math.max(1,mxy-mny),260),ox=1080-(mnx+mxx)/2*sc,oy=575-(mny+mxy)/2*sc;
  x.clearRect(0,0,1920,1080);x.lineWidth=Math.max(1.3,Math.min(8,sc*.28));x.lineCap='round';x.lineJoin='round';
  function draw(Z,col){if(Z.length<2)return;var CH=Math.max(1,Math.ceil(Z.length/40));for(var k=0;k<Z.length-1;k+=CH){x.strokeStyle=col(k/Z.length);x.beginPath();x.moveTo(ox+Z[k][0]*sc,oy+Z[k][1]*sc);for(var m=k+1;m<=Math.min(Z.length-1,k+CH);m++)x.lineTo(ox+Z[m][0]*sc,oy+Z[m][1]*sc);x.stroke()}}
  draw(P,function(f){return 'hsl('+(175+f*120|0)+',55%,66%)'});draw(A,function(f){return 'hsl('+(10+f*20|0)+',85%,70%)'});
  V.innerHTML='<div class="hzbox" style="padding:14px 26px"><div class="lb">Katlama · Folds</div><div style="font-size:2.3vw">'+lvl+'</div><div class="lb" style="margin-top:.6vw">Parça · Segments</div><div style="font-size:2.3vw">'+(P.length-1).toLocaleString('tr-TR')+'</div></div>'});return L};

/* calm night: rain on a window, harbour lights blurred behind (illustration) */
W.hzrainwin=function(L,it){var c=wCv(L),x=c.getContext('2d'),B=[],D=[],S=[],i;
 for(i=0;i<46;i++)B.push([Math.random()*1920,560+Math.random()*360,30+Math.random()*90,Math.random()<.7?[255,196,140]:[170,200,255],Math.random()*6.28]);
 for(i=0;i<520;i++)S.push([Math.random()*1920,Math.random()*1080,1+Math.random()*3.2]);
 for(i=0;i<26;i++)D.push([Math.random()*1920,Math.random()*1080,3+Math.random()*4,.4+Math.random()*1.6,Math.random()*30]);
 T(L,hd('Yağmurlu Gece · Rainy Night — çizim · illustration, hayal ürünü · imagined (sakin · calm)','Cama vuran yağmur, ötede limanın ışıkları','Rain on the glass, harbour lights beyond'),'top:44px',2);
 T(L,'<div class="sm" style="font-size:1.25vw;color:#cdd6dc">Her damla küçük bir mercek: içine bakarsan dışarıdaki dünyayı ters dönmüş görürsün<br><i>Every drop is a tiny lens — look closely and you see the world outside upside down</i></div>','bottom:40px',9);
 wLoop(L,function(t){var g=x.createLinearGradient(0,0,0,1080);g.addColorStop(0,'#060a14');g.addColorStop(.55,'#0d1628');g.addColorStop(1,'#080c16');x.fillStyle=g;x.fillRect(0,0,1920,1080);
  for(i=0;i<B.length;i++){var b=B[i],a=.10+.05*Math.sin(t*.4+b[4]),rg=x.createRadialGradient(b[0],b[1],0,b[0],b[1],b[2]);rg.addColorStop(0,'rgba('+b[3]+','+(a*2.2).toFixed(3)+')');rg.addColorStop(1,'rgba('+b[3]+',0)');x.fillStyle=rg;x.fillRect(b[0]-b[2],b[1]-b[2],2*b[2],2*b[2])}
  x.fillStyle='rgba(200,215,235,.16)';for(i=0;i<S.length;i++){var s=S[i];x.beginPath();x.arc(s[0],s[1],s[2],0,7);x.fill()}
  for(i=0;i<D.length;i++){var d=D[i];if(t>d[4]){d[1]+=d[3]*(.6+.4*Math.sin(t*2+i));d[0]+=Math.sin(t*1.7+i)*.15}if(d[1]>1100){d[1]=-20;d[0]=Math.random()*1920;d[4]=t+Math.random()*12}
   var tg=x.createLinearGradient(d[0],d[1]-160,d[0],d[1]);tg.addColorStop(0,'rgba(190,210,235,0)');tg.addColorStop(1,'rgba(190,210,235,.16)');x.strokeStyle=tg;x.lineWidth=d[2]*.7;x.beginPath();x.moveTo(d[0],d[1]-160);x.lineTo(d[0],d[1]);x.stroke();
   x.fillStyle='rgba(215,228,245,.35)';x.beginPath();x.arc(d[0],d[1],d[2],0,7);x.fill();x.fillStyle='rgba(255,255,255,.5)';x.beginPath();x.arc(d[0]-d[2]*.35,d[1]-d[2]*.35,d[2]*.3,0,7);x.fill()}});return L};

/* Müller-Lyer illusion: arrow fins change how long a line looks */
W.hzmuller=function(L,it){L.style.background='#e6e2d8';var c=wCv(L),x=c.getContext('2d');
 T(L,'<div class="hzbox" style="background:rgba(20,24,28,.85)">'+hd('Göz Oyunu · Optical Illusion','Hangi yatay çizgi daha uzun: üstteki mi, alttaki mi?','Which horizontal line is longer: the top one or the bottom one?')+'</div>','top:20px',.4);
 T(L,'<div class="hzbox" style="background:rgba(20,24,28,.85)"><div class="a" style="font-size:1.95vw">İkisi de tam olarak aynı uzunlukta!</div><div class="e" style="font-size:1.35vw">They are exactly the same length — the fins make the brain read corners of a room</div><div class="sm">Müller-Lyer illüzyonu · Müller-Lyer illusion — Franz Müller-Lyer, 1889</div></div>','bottom:18px',17);
 function fin(px,py,dir,f){x.globalAlpha=f;x.beginPath();x.moveTo(px,py);x.lineTo(px+dir*80,py-62);x.moveTo(px,py);x.lineTo(px+dir*80,py+62);x.stroke();x.globalAlpha=1}
 wLoop(L,function(t){var f=t<17?1:Math.max(0,1-(t-17)/4);if(t>36)f=Math.min(1,(t-36)/3);x.clearRect(0,0,1920,1080);x.strokeStyle='#1b2328';x.lineWidth=9;x.lineCap='round';
  var X0=660,X1=1260,Y1=440,Y2=770;x.beginPath();x.moveTo(X0,Y1);x.lineTo(X1,Y1);x.moveTo(X0,Y2);x.lineTo(X1,Y2);x.stroke();
  fin(X0,Y1,-1,f);fin(X1,Y1,1,f);fin(X0,Y2,1,f);fin(X1,Y2,-1,f);
  if(t>19&&t<36){x.globalAlpha=Math.min(1,(t-19)/2);x.strokeStyle='#c8372a';x.lineWidth=3;x.setLineDash([12,10]);x.beginPath();x.moveTo(X0,360);x.lineTo(X0,850);x.moveTo(X1,360);x.lineTo(X1,850);x.stroke();x.setLineDash([]);x.globalAlpha=1}});return L};

/* Jastrow illusion: two identical curved blocks — the lower one looks bigger */
W.hzjastrow=function(L,it){L.style.background='#e9e5dc';var c=wCv(L),x=c.getContext('2d');
 T(L,'<div class="hzbox" style="background:rgba(20,24,28,.85)">'+hd('Göz Oyunu · Optical Illusion','Hangi kavisli parça daha büyük: mavi mi, kırmızı mı?','Which curved piece is bigger: the blue one or the red one?')+'</div>','top:20px',.4);
 T(L,'<div class="hzbox" style="background:rgba(20,24,28,.85)"><div class="a" style="font-size:1.95vw">İkisi de tıpatıp aynı! Üst üste konunca kendin gör</div><div class="e" style="font-size:1.35vw">They are identical — watch them slide on top of each other. The brain compares the short inner edge with the long outer edge next to it</div><div class="sm">Jastrow illüzyonu · Jastrow illusion — Joseph Jastrow, 1889</div></div>','bottom:18px',17);
 function arc(cx,cy,col,al){var R1=520,R2=330,a0=-Math.PI/2-.62,a1=-Math.PI/2+.62;x.globalAlpha=al;x.fillStyle=col;x.beginPath();x.arc(cx,cy,R1,a0,a1);x.arc(cx,cy,R2,a1,a0,true);x.closePath();x.fill();x.globalAlpha=1}
 wLoop(L,function(t){x.clearRect(0,0,1920,1080);var m=t<19?0:t<23?ease((t-19)/4):t<31?1:t<35?1-ease((t-31)/4):0;
  var cyA=820,cyB=1040,cy=cyA+(cyB-cyA)*m;arc(960,cyB,'#c8372a',1);arc(960,cy,'#2a6f9b',m>0?.8:1)});return L};


/* ---------- v63: group / friends templates ---------- */
/* hzwelcome: still photo + painted script lettering. it: f, pos, lb, lines[[text,fs_vw],...], names, tr, en, cr */
W.hzwelcome=function(L,it){L.style.background='#000';
 var m=wEl('img','');m.src=it.f;m.style.cssText='position:absolute;top:0;left:0;width:100%;height:100%;object-fit:cover;object-position:'+(it.pos||'50% 50%');L.appendChild(m);
 L.appendChild(wEl('div','',null,'position:absolute;top:0;left:0;right:0;bottom:0;background:radial-gradient(ellipse at 50% 42%,rgba(6,12,18,.62),rgba(6,12,18,.28) 62%,rgba(0,0,0,.55))'));
 L.appendChild(wEl('div','',null,'position:absolute;left:0;right:0;bottom:0;height:40%;background:linear-gradient(transparent,rgba(0,0,0,.78))'));
 var lb=T(L,'<div class="lb" style="color:#bfe9dd">'+it.lb+'</div>','top:3.5vh;bottom:auto;max-height:7vh;overflow:hidden',.3);
 var h='';for(var i=0;i<it.lines.length;i++){var ln=it.lines[i];h+='<div style="font-family:HzScript,Georgia,serif;font-size:'+ln[1]+'vw;line-height:1.18;color:#fbf8f2;text-shadow:0 0.3vw 2.2vw rgba(0,0,0,.85)"><span class="hzw" style="animation-delay:'+(0.8+i*3.2)+'s;padding:.42em .5em .28em;margin:-.42em 0 -.28em">'+ln[0]+'</span></div>'}
 var sz=T(L,h,'top:10vh;bottom:'+(it.names?'37vh':'30vh')+';display:flex;flex-direction:column;justify-content:center;overflow:hidden',.1);
 if(it.names){var nm=T(L,'<div style="font-family:HzBrush,Georgia,serif;font-size:3.1vw;color:#c9f0e4;letter-spacing:.04em;line-height:1.2">'+it.names+'</div>','top:65vh;bottom:auto;max-height:10vh;overflow:hidden',6.5)}
 var sub=T(L,'<div class="q" style="font-size:2.2vw">'+it.tr+'</div><div class="e" style="font-size:1.45vw">'+it.en+'</div>','bottom:7.5vh;top:auto;max-height:16vh;overflow:hidden',it.names?8.5:7);fitEl(sub,16);
 T(L,'<div class="sm">'+it.cr+'</div>','',1.6).className+=' hz-credit';return L};

/* hzchoose: “which would you pick?” two still photos side by side. it: q, qe, a:{f,t,e,tag,pos}, b:{...}, p, pe, cr */
W.hzchoose=function(L,it){grad(L,it.c1||'#16232c',it.c2||'#04070a');
 var hdEl=T(L,'<div class="lb">'+(it.lb||'Hangisini Seçerdin? · Which Would You Pick?')+'</div><div class="q" style="font-size:2.5vw">'+it.q+'</div><div class="e" style="font-size:1.4vw">'+it.qe+'</div>','top:3vh;bottom:auto;max-height:17vh;overflow:hidden',.3);fitEl(hdEl,17);
 var S=[it.a,it.b];for(var i=0;i<2;i++){var o=S[i],x=i?51.5:4;
  var fr=wEl('div','',null,'position:absolute;top:21.5vh;height:49vh;left:'+x+'vw;width:44.5vw;border-radius:.8vw;overflow:hidden;box-shadow:0 1vw 3vw rgba(0,0,0,.6);opacity:0;animation:hzin 1.6s '+(0.8+i*1.2)+'s forwards');
  var im=wEl('img','');im.src=o.f;im.style.cssText='width:100%;height:100%;object-fit:cover;object-position:'+(o.pos||'50% 50%');fr.appendChild(im);L.appendChild(fr);
  var badge=T(L,'<div style="font-family:Helvetica,Arial,sans-serif;font-weight:300;font-size:2.4vw;color:#fff;line-height:1">'+(i?'B':'A')+'</div>','top:23vh;bottom:auto;left:'+(x+1.2)+'vw;right:auto;width:4.2vw;padding:.7vw 0;background:rgba(4,9,14,.72);border-radius:.6vw;text-shadow:none',1+i*1.2);
  var cap=T(L,'<div class="lb" style="font-size:.85vw;letter-spacing:.2em">'+o.tag+'</div><div class="q" style="font-size:2.05vw;margin-top:.3vw">'+o.t+'</div><div class="e" style="font-size:1.25vw;margin-top:.2vw">'+o.e+'</div>','top:72.5vh;bottom:auto;max-height:13.5vh;overflow:hidden;left:'+x+'vw;right:auto;width:44.5vw',1.4+i*1.2);fitEl(cap,13.5)}
 if(it.p){var pr=T(L,'<div style="font-family:HzBrush,Georgia,serif;font-size:2vw;color:#ff9e7a;line-height:1.15">'+it.p+'</div><div class="sm" style="margin-top:.1vw;font-size:1.05vw;color:#c3cdd2">'+it.pe+'</div>','top:86.6vh;bottom:auto;max-height:7vh;overflow:hidden',5);fitEl(pr,7)}
 T(L,'<div class="sm">'+it.cr+'</div>','',1.6).className+=' hz-credit';return L};

/* hzguess: guess together over a still photo; answer after sec. No a = conversation question. it: f, pos, lb, q, qe, hint, a, ae, sec, cr */
W.hzguess=function(L,it){L.style.background='#000';var sec=it.sec||20;
 var m=wEl('img','');m.src=it.f;m.style.cssText='position:absolute;top:0;left:0;width:100%;height:100%;object-fit:'+(it.fit||'cover')+';object-position:'+(it.pos||'50% 50%');L.appendChild(m);
 L.appendChild(wEl('div','',null,'position:absolute;left:0;right:0;top:0;height:42%;background:linear-gradient(rgba(0,0,0,.7),transparent)'));
 L.appendChild(wEl('div','',null,'position:absolute;left:0;right:0;bottom:0;height:42%;background:linear-gradient(transparent,rgba(0,0,0,.75))'));
 var q=T(L,'<div class="hzbox"><div class="lb">'+(it.lb||'Birlikte Tahmin · Guess Together')+'</div><div class="q" style="font-size:2.6vw">'+it.q+'</div><div class="e" style="font-size:1.45vw">'+it.qe+'</div></div>','top:4vh;bottom:auto;max-height:31vh;overflow:hidden',.5);fitEl(q,31);
 var b='';if(it.hint)b+='<div class="sm" style="font-size:1.25vw;color:#dfe6e9;margin-bottom:.8vh">'+it.hint+'</div>';
 if(it.a){b+='<div id="hzcd" class="lb" style="color:#ff9e7a;min-height:1.6vw"></div><div id="hzans" style="opacity:0;transition:opacity .8s"><div class="a" style="font-size:2.3vw">'+it.a+'</div><div class="e" style="font-size:1.35vw">'+it.ae+'</div></div>'}
 else b+='<div style="font-family:HzBrush,Georgia,serif;font-size:2.2vw;color:#ff9e7a">'+(it.p||'Sırayla anlatın! · Take turns!')+'</div>';
 var bot=T(L,'<div class="hzbox">'+b+'</div>','bottom:7.5vh;top:auto;max-height:30vh;overflow:hidden',2);fitEl(bot,30);
 T(L,'<div class="sm">'+it.cr+'</div>','',1.6).className+=' hz-credit';
 if(it.a)wLoop(L,function(t){var r=Math.ceil(sec-t),cd=bot.querySelector('#hzcd'),an=bot.querySelector('#hzans');if(cd)cd.textContent=(r>0&&t>3)?'Cevap · Answer: '+r:'';if(an&&t>=sec+0.6)an.style.opacity=1});return L};

/* hzstroop: Stroop colour game for a group. Round 1 words match colours, round 2 they don't. */
W.hzstroop=function(L,it){grad(L,'#1b2230','#05070b');
 var C=[['KIRMIZI','#ff5252'],['MAVİ','#4fa8ff'],['YEŞİL','#3ddc84'],['SARI','#fff04d'],['MOR','#b884ff'],['PEMBE','#ff86cf']];
 var A=[0,3,1,5,2,4,1,0,4,3,5,2],B=[[1,0],[2,3],[0,4],[5,1],[3,2],[4,5],[2,0],[1,4],[0,3],[4,1],[3,5],[5,2]];
 var hdEl=T(L,hd('Oyun · Party Game','Kelimeyi okuma — rengini yüksek sesle söyle!','Don’t read the word — say its colour out loud!'),'',.4);hdEl.className+=' hz-top';hdEl.style.maxHeight='21vh';fitEl(hdEl,21);
 function grid(r2){var h='<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:3.2vh 2vw;align-items:center">';for(var i=0;i<12;i++){var w=r2?C[B[i][0]][0]:C[A[i]][0],c=r2?C[B[i][1]][1]:C[A[i]][1];h+='<div style="font-family:Helvetica,Arial,sans-serif;font-weight:700;font-size:3.1vw;letter-spacing:.04em;color:'+c+';text-shadow:none">'+w+'</div>'}return h+'</div>'}
 var mid=T(L,'<div class="lb" id="hzrd" style="margin-bottom:2.4vh;color:#ff9e7a">1. Tur: ısınma · Round 1: warm-up</div>'+grid(0),'top:25vh;bottom:25vh;display:flex;flex-direction:column;justify-content:center;overflow:hidden',1.2);
 var bt=T(L,'<div class="e" style="font-size:1.45vw;color:#dfe6e9">Stroop etkisi (1935): beyin okumayı otomatik yapar, bu yüzden renk söylemek yavaşlar. En hızlı kim?</div><div class="sm">The Stroop effect (1935): the brain reads automatically, so naming the colour slows you down. Who is fastest?</div>','',3);bt.className+=' hz-bot';bt.style.maxHeight='19vh';
 var sw=0;wLoop(L,function(t){if(!sw&&t>22){sw=1;mid.innerHTML='<div class="lb" style="margin-bottom:2.4vh;color:#ff9e7a">2. Tur: şimdi zor! · Round 2: now it gets hard!</div>'+grid(1)}});return L};


/* ---------- v64 additions: hzmeta hzkaleido hzyakamoz (living art; hzyakamoz = calm night), hzmib hzcorn hzfraser (illusions) ---------- */
/* Lava lamp: wax blobs warm up, rise, cool and sink (metaballs) */
W.hzmeta=function(L,it){L.style.background='#070a18';var c=wCv(L),x=c.getContext('2d'),FW=192,FH=108,oc=document.createElement('canvas');oc.width=FW;oc.height=FH;var o=oc.getContext('2d'),img=o.createImageData(FW,FH),B=[],i;
 for(i=0;i<9;i++)B.push({x:40+Math.random()*112,ph:Math.random()*6.28,sp:.05+Math.random()*.05,r:5.5+Math.random()*4.5,w:Math.random()*6.28});
 T(L,'<div class="hzbox">'+hd('Yaşayan Sanat · Living Art — simülasyon · simulation','Lav lambası: ısınan mum hafifler ve yükselir; tepede soğuyunca ağırlaşıp geri iner…','A lava lamp: warm wax gets lighter and rises — at the top it cools, grows heavier and sinks again…')+'</div>','top:22px',.4);
 T(L,'<div class="hzbox"><div class="sm" style="font-size:1.2vw;color:#dfe6e9">Hiçbir şekil iki kez tekrarlanmaz. İlk lav lambası 1963’te İngiltere’de Edward Craven Walker tarafından yapıldı; içinde yalnızca mum, su ve bir ampulün ısısı var<br><i>No shape ever repeats. The first lava lamp was made in England in 1963 by Edward Craven Walker — just wax, water and the warmth of a bulb</i></div></div>','bottom:20px',14);
 var C1=[255,104,96],C2=[90,60,190];
 wLoop(L,function(t){var d=img.data,k=0,j;
  for(i=0;i<B.length;i++){var b=B[i];b.cy=FH*.55-Math.sin(t*b.sp*2.2+b.ph)*FH*.42;b.cx=b.x+Math.sin(t*.13+b.w)*14}
  for(var y=0;y<FH;y++)for(var xx=0;xx<FW;xx++){var f=0;for(j=0;j<B.length;j++){var dx=xx-B[j].cx,dy=(y-B[j].cy)*1.15;f+=B[j].r*B[j].r/(dx*dx+dy*dy+1)}
   var m=f<.85?0:f<1?(f-.85)/.15:1,gl=Math.min(1,f*.5),yy=y/FH;
   d[k]=7+C2[0]*gl*.25+(C1[0]*(1-yy*.3)-7)*m;d[k+1]=10+C2[1]*gl*.2+(C1[1]*(1-yy*.2)-10)*m;d[k+2]=24+C2[2]*gl*.35+(C1[2]+yy*30-24)*m;d[k+3]=255;k+=4}
  o.putImageData(img,0,0);x.imageSmoothingEnabled=true;x.drawImage(oc,0,0,1920,1080)});return L};

/* Kaleidoscope: drifting coloured pieces in one wedge, mirrored twelve times */
W.hzkaleido=function(L,it){L.style.background='#05070c';var c=wCv(L),x=c.getContext('2d'),P=[],i,N=12,CX=960,CY=575,R=500,COL=['#8fd3c1','#ff9e7a','#a9b8ff','#f2efe6','#5fa8d3','#e07a9a','#7fd18b'];
 for(i=0;i<34;i++)P.push({r:40+Math.random()*(R-60),a:Math.random(),s:8+Math.random()*34,c:COL[i%COL.length],vr:(Math.random()-.5)*14,va:(Math.random()-.5)*.03,sh:i%3,rot:Math.random()*6.28});
 T(L,'<div class="hzbox">'+hd('Yaşayan Sanat · Living Art — canlı çizim · live drawing','Birkaç renkli parça ve aynalar: kaleydoskopta aynı desen asla iki kez gelmez','A few coloured pieces and mirrors — a kaleidoscope never shows the same pattern twice')+'</div>','top:22px',.4);
 T(L,'<div class="hzbox"><div class="sm" style="font-size:1.2vw;color:#dfe6e9">David Brewster, 1816. Adı Yunanca: kalos (güzel) + eidos (biçim) + skopein (bakmak) — “güzel biçimleri seyretmek”<br><i>David Brewster, 1816. The name is Greek: kalos (beautiful) + eidos (form) + skopein (to look) — “watching beautiful forms”</i></div></div>','bottom:20px',12);
 var WA=Math.PI*2/N;
 function piece(p){var a=p.a*WA,px=Math.cos(a)*p.r,py=Math.sin(a)*p.r;x.save();x.translate(px,py);x.rotate(p.rot);x.fillStyle=p.c;x.globalAlpha=.55;x.beginPath();
  if(p.sh==0)x.arc(0,0,p.s,0,7);else if(p.sh==1){x.moveTo(0,-p.s*1.4);x.quadraticCurveTo(p.s,0,0,p.s*1.4);x.quadraticCurveTo(-p.s,0,0,-p.s*1.4)}else{x.moveTo(0,-p.s);x.lineTo(p.s*.9,p.s*.6);x.lineTo(-p.s*.9,p.s*.6);x.closePath()}x.fill();x.restore()}
 wLoop(L,function(t){x.fillStyle='rgba(5,7,12,.16)';x.fillRect(0,0,1920,1080);
  for(i=0;i<P.length;i++){var p=P[i];p.r+=p.vr*.016;p.a+=p.va*.3;p.rot+=.004;if(p.r<30||p.r>R-20)p.vr*=-1;if(p.a<0||p.a>1)p.va*=-1}
  x.save();x.translate(CX,CY);x.rotate(t*.02);x.beginPath();x.arc(0,0,R,0,7);x.clip();
  for(var k=0;k<N;k++){x.save();x.rotate(k*WA);if(k%2){x.rotate(WA);x.scale(1,-1)}x.beginPath();x.moveTo(0,0);x.arc(0,0,R,-.002,WA+.002);x.closePath();x.save();x.clip();for(i=0;i<P.length;i++)piece(P[i]);x.restore();x.restore()}
  x.restore();x.globalAlpha=1;x.strokeStyle='rgba(200,215,225,.25)';x.lineWidth=3;x.beginPath();x.arc(CX,CY,R+4,0,7);x.stroke()});return L};

/* Motion-induced blindness: stare at the centre — the still yellow dots vanish */
W.hzmib=function(L,it){L.style.background='#000';var c=wCv(L),x=c.getContext('2d'),CX=960,CY=560,D=[[960,330],[760,700],[1160,700]];
 T(L,'<div class="hzbox">'+hd('Göz Oyunu · Optical Illusion — şimdi dene · try it now','Ortadaki yanıp sönen noktaya 15–20 saniye gözünü ayırmadan bak…','Stare at the blinking dot in the centre for 15–20 seconds without looking away…')+'</div>','top:20px',.4);
 T(L,'<div class="hzbox"><div class="a" style="font-size:1.8vw">Sarı noktalar teker teker kayboldu mu? Hiçbiri yerinden oynamadı!</div><div class="e" style="font-size:1.3vw">Did the yellow dots vanish one by one? None of them ever moved. The brain “deletes” still details when strong motion surrounds them</div><div class="sm">Harekete bağlı körlük · Motion-induced blindness — Bonneh, Cooperman &amp; Sagi, 2001</div></div>','bottom:18px',26);
 wLoop(L,function(t){x.clearRect(0,0,1920,1080);x.save();x.translate(CX,CY);x.rotate(t*.9);x.strokeStyle='#2f5bff';x.lineWidth=5;
  for(var gx=-9;gx<=9;gx++)for(var gy=-9;gy<=9;gy++){var px=gx*58,py=gy*58;if(px*px+py*py>520*520)continue;x.beginPath();x.moveTo(px-13,py);x.lineTo(px+13,py);x.moveTo(px,py-13);x.lineTo(px,py+13);x.stroke()}
  x.restore();x.fillStyle='#ffe23a';for(var i=0;i<3;i++){x.beginPath();x.arc(D[i][0],D[i][1],12,0,7);x.fill()}
  x.fillStyle=(Math.floor(t*2.5)%2)?'#3ddc84':'#0c3';x.beginPath();x.arc(CX,CY,9,0,7);x.fill()});return L};

/* Cornsweet illusion: two halves of the same grey look different because of a thin edge */
W.hzcorn=function(L,it){L.style.background='#343434';var c=wCv(L),x=c.getContext('2d'),im=x.createImageData(1920,1080),d=im.data,X0=360,X1=1560,Y0=300,Y1=830,MID=960,RW=170,i,y,xx;
 for(y=0;y<1080;y++)for(xx=0;xx<1920;xx++){var v=52,k=(y*1920+xx)*4;if(y>=Y0&&y<Y1&&xx>=X0&&xx<X1){v=127;if(xx<MID&&xx>MID-RW)v=127-42*Math.pow((xx-(MID-RW))/RW,2);else if(xx>=MID&&xx<MID+RW)v=127+42*Math.pow(1-(xx-MID)/RW,2)}d[k]=d[k+1]=d[k+2]=v;d[k+3]=255}
 T(L,'<div class="hzbox" style="background:rgba(20,24,28,.85)">'+hd('Göz Oyunu · Optical Illusion','Sol taraf sağdan daha koyu, değil mi?','The left half looks darker than the right, doesn’t it?')+'</div>','top:20px',.4);
 T(L,'<div class="hzbox" style="background:rgba(20,24,28,.85)"><div class="a" style="font-size:1.9vw">İki taraf da tam olarak aynı gri! Fark yalnızca ortadaki ince kenarda</div><div class="e" style="font-size:1.3vw">Both sides are exactly the same grey — the only difference is a thin edge in the middle. Cover it and the halves match</div><div class="sm">Cornsweet illüzyonu · Cornsweet illusion — Tom Cornsweet, 1970</div></div>','bottom:18px',17);
 wLoop(L,function(t){x.putImageData(im,0,0);var m=t<18?0:t<21?ease((t-18)/3):t<34?1:t<37?1-ease((t-34)/3):0;
  if(m>0){x.fillStyle='#1b2328';x.fillRect(MID-RW-10,Y0-40-(1-m)*600,2*RW+20,(Y1-Y0+80))}});return L};

/* Fraser spiral: perfect circles that look like a spiral */
W.hzfraser=function(L,it){L.style.background='#8fa39c';var c=wCv(L),x=c.getContext('2d'),CX=960,CY=575,RR=[],r;for(r=70;r<=470;r+=50)RR.push(r);
 function scene(){x.fillStyle='#8fa39c';x.fillRect(0,0,1920,1080);
  for(var a=0;a<24;a++){x.fillStyle=a%2?'#7d948c':'#a3b5ae';x.beginPath();x.moveTo(CX,CY);x.arc(CX,CY,560,a*Math.PI/12,(a+1)*Math.PI/12);x.closePath();x.fill()}
  for(var q=0;q<RR.length;q++){var R=RR[q],n=Math.round(2*Math.PI*R/26);for(var s=0;s<n;s++){var an=s/n*Math.PI*2;x.save();x.translate(CX+Math.cos(an)*R,CY+Math.sin(an)*R);x.rotate(an+Math.PI/2+.42);x.fillStyle=s%2?'#111':'#f4f4f0';x.fillRect(-12,-5,24,10);x.restore()}}}
 T(L,'<div class="hzbox" style="background:rgba(20,24,28,.85)">'+hd('Göz Oyunu · Optical Illusion','Ortaya doğru dönen bir sarmal görüyorsun, değil mi?','You see a spiral winding into the centre, right?')+'</div>','top:20px',.4);
 T(L,'<div class="hzbox" style="background:rgba(20,24,28,.85)"><div class="a" style="font-size:1.9vw">Sarmal yok: hepsi iç içe kusursuz çemberler!</div><div class="e" style="font-size:1.3vw">There is no spiral — they are all perfect, separate circles. The tilted “twisted cord” pieces fool the brain. Follow the coral line</div><div class="sm">Fraser sarmalı · Fraser spiral illusion — James Fraser, 1908</div></div>','bottom:18px',18);
 wLoop(L,function(t){scene();if(t>19){var p=Math.min(1,(t-19)/6),R=RR[5];x.strokeStyle='#ff6b4a';x.lineWidth=7;x.beginPath();x.arc(CX,CY,R,-Math.PI/2,-Math.PI/2+p*Math.PI*2);x.stroke()}});return L};

/* Yakamoz: glowing plankton on night waves (calm night) */
W.hzyakamoz=function(L,it){var c=wCv(L),x=c.getContext('2d'),S=stars(170),SP=[],i,HY=500;
 T(L,hd('Yakamoz · Sea Sparkle — çizim · illustration, hayal ürünü · imagined (sakin · calm)','Dalgalar kıyıya varınca deniz mavi bir ışıkla parlıyor','As the waves reach the shore, the sea lights up blue'),'top:44px',2);
 T(L,'<div class="sm" style="font-size:1.25vw;color:#cdd6dc">Bu ışığı minicik plankton canlıları yapar: dalga onları sarstığında bir an parlarlar. Karadeniz’de de yaz gecelerinde görülür<br><i>Tiny plankton make this light — they glow for a moment when a wave shakes them. It can be seen on Black Sea summer nights too</i></div>','bottom:40px',9);
 wLoop(L,function(t){var g=x.createLinearGradient(0,0,0,HY);g.addColorStop(0,'#03050c');g.addColorStop(1,'#0b1424');x.fillStyle=g;x.fillRect(0,0,1920,HY);drawStars(x,S.filter(function(s){return s[1]<HY-20}),t);
  x.fillStyle='rgba(225,232,245,.85)';x.beginPath();x.arc(1500,170,34,0,7);x.fill();x.fillStyle='#050810';x.beginPath();x.arc(1514,160,32,0,7);x.fill();
  var sg=x.createLinearGradient(0,HY,0,1080);sg.addColorStop(0,'#081220');sg.addColorStop(1,'#02040a');x.fillStyle=sg;x.fillRect(0,HY,1920,1080-HY);
  x.fillStyle='#120f0d';x.beginPath();x.moveTo(0,1080);x.lineTo(0,930);for(var sx=0;sx<=1920;sx+=60)x.lineTo(sx,930+Math.sin(sx*.004)*20);x.lineTo(1920,1080);x.fill();
  for(var w=0;w<7;w++){var ph=((t*.05+w/7)%1),y=HY+12+Math.pow(ph,1.7)*420,amp=2+ph*9,glow=ph>.72?Math.min(1,(ph-.72)/.12)*(1-Math.max(0,(ph-.94)/.06)):0;
   x.lineWidth=1+ph*3;x.strokeStyle='rgba(120,140,170,'+(.12+ph*.15).toFixed(3)+')';x.shadowBlur=0;
   if(glow>0){x.strokeStyle='rgba(70,220,255,'+(.25+.6*glow).toFixed(3)+')';x.shadowColor='#39d4ff';x.shadowBlur=26*glow;x.lineWidth=3+5*glow;if(Math.random()<.5*glow)SP.push([Math.random()*1920,y+Math.random()*10,1])}
   x.beginPath();for(var px=0;px<=1920;px+=24){var yy=y+Math.sin(px*.006+t*.6+w)*amp+Math.sin(px*.017-t*.4)*amp*.4;if(px)x.lineTo(px,yy);else x.moveTo(px,yy)}x.stroke()}
  x.shadowBlur=0;for(i=SP.length-1;i>=0;i--){var p=SP[i];p[2]-=.012;if(p[2]<=0){SP.splice(i,1);continue}x.fillStyle='rgba(120,235,255,'+(p[2]*.8).toFixed(3)+')';x.beginPath();x.arc(p[0],p[1],2.2,0,7);x.fill()}});return L};

/* ---------- v66 additions: hzfern hzhilbert hzorrery hzfener (living art / explainers; hzfener = calm night), hzshepard hzbezold (illusions) ---------- */
/* Barnsley fern: four tiny rules picked at random grow a real-looking fern */
W.hzfern=function(L,it){grad(L,'#0f1d16','#020504');var c=wCv(L),x=c.getContext('2d'),px=0,py=0,n=0,R=T(L,'','bottom:30px;left:40px;right:auto;text-align:left;width:440px',1),done=false;
 T(L,'<div class="hzbox">'+hd('Yaşayan Sanat · Living Art — simülasyon · simulation','Dört küçük kural, rastgele seçiliyor… ve bir eğrelti otu büyüyor','Four tiny rules, picked at random… and a fern grows')+'</div>','top:22px',.4);
 wLoop(L,function(t){var tg=t<8?Math.floor(t*40):Math.min(160000,Math.floor(320+(t-8)*(t-8)*90));
  for(;n<tg;n++){var r=Math.random(),nx,ny;if(r<.01){nx=0;ny=.16*py}else if(r<.86){nx=.85*px+.04*py;ny=-.04*px+.85*py+1.6}else if(r<.93){nx=.2*px-.26*py;ny=.23*px+.22*py+1.6}else{nx=-.15*px+.28*py;ny=.26*px+.24*py+.44}px=nx;py=ny;
   var sx=720+px*84,sy=1050-py*84,g=Math.floor(120+py*12);x.fillStyle='rgba('+Math.floor(60+py*6)+','+Math.min(235,g)+','+Math.floor(90+py*4)+','+(t<8?1:.8)+')';var s=t<8?5:1.6;x.fillRect(sx-s/2,sy-s/2,s,s)}
  R.innerHTML='<div class="hzbox" style="padding:12px 28px"><div class="lb">Nokta · Points</div><div style="font-size:2.292vw">'+n.toLocaleString('tr-TR')+'</div><div class="sm">%85 büyüt · grow &nbsp; %7 sol yaprak · left leaf<br>%7 sağ yaprak · right leaf &nbsp; %1 sap · stem</div></div>';
  if(t>34&&!done){done=true;T(L,'<div class="hzbox" style="max-width:40vw"><div class="a" style="font-size:1.7vw">Her yaprak, bütün eğrelti otunun küçük bir kopyası</div><div class="e" style="font-size:1.3vw">Every frond is a small copy of the whole fern — Michael Barnsley, 1988: the whole plant hides in just 28 numbers</div></div>','bottom:20px;left:auto;right:40px;width:40vw',.1)}});return L};

/* Hilbert curve: one unbroken line that fills a square, order by order */
W.hzhilbert=function(L,it){grad(L,'#171a2a','#040509');var c=wCv(L),x=c.getContext('2d'),S=680,X0=440,Y0=240,cache={};
 function d2xy(n,d){var rx,ry,s,t=d,xx=0,yy=0;for(s=1;s<n;s*=2){rx=1&(t/2);ry=1&(t^rx);if(ry==0){if(rx==1){xx=s-1-xx;yy=s-1-yy}var tm=xx;xx=yy;yy=tm}xx+=s*rx;yy+=s*ry;t=Math.floor(t/4)}return[xx,yy]}
 function pts(o){if(cache[o])return cache[o];var n=1<<o,P=[];for(var d=0;d<n*n;d++){var p=d2xy(n,d);P.push([X0+(p[0]+.5)*S/n,Y0+(p[1]+.5)*S/n])}return cache[o]=P}
 T(L,'<div class="hzbox">'+hd('Zekice Düşünce · Clever Thinking — canlı çizim · live drawing','Kalemi hiç kaldırmadan, tek bir çizgiyle bir kareyi doldurabilir misin?','Can you fill a whole square with one line, without ever lifting the pen?')+'</div>','top:20px',.4);
 var R=T(L,'','bottom:30px;left:40px;right:auto;text-align:left;width:380px',1),done=false;
 wLoop(L,function(t){var o=Math.min(6,1+Math.floor(t/8)),f=Math.min(1,(t-(o-1)*8)/6.5);if(o==6)f=Math.min(1,(t-40)/9);var P=pts(o),m=Math.max(2,Math.floor(P.length*f));
  x.clearRect(0,0,1920,1080);x.strokeStyle='rgba(255,255,255,.08)';x.lineWidth=2;x.strokeRect(X0,Y0,S,S);x.lineWidth=o<4?6:o<5?4:2.6;x.lineJoin='round';
  for(var i=1;i<m;i++){x.strokeStyle='hsl('+Math.floor(170+i/P.length*190)+',70%,68%)';x.beginPath();x.moveTo(P[i-1][0],P[i-1][1]);x.lineTo(P[i][0],P[i][1]);x.stroke()}
  R.innerHTML='<div class="hzbox" style="padding:12px 28px"><div class="lb">Aşama · Order '+o+'</div><div style="font-size:1.6vw">'+(P.length).toLocaleString('tr-TR')+' kare · squares</div><div class="sm">Her aşamada çizgi 2 kat uzar<br>The line doubles in length each step</div></div>';
  if(t>49&&!done){done=true;T(L,'<div class="hzbox" style="max-width:40vw"><div class="a" style="font-size:1.6vw">David Hilbert, 1891: sonsuz aşamada çizgi karenin her noktasından geçer</div><div class="e" style="font-size:1.25vw">At infinite order the line passes through every point of the square. Points close on the line stay close on the map — used today to sort map data and pixels</div></div>','bottom:20px;left:auto;right:40px;width:40vw',.1)}});return L};

/* Orrery: the inner planets with their true speed ratios (1 Earth year = 12 s) */
W.hzorrery=function(L,it){var c=wCv(L),x=c.getContext('2d'),S=stars(220),CX=960,CY=610,K=.42,Y=12,
 PL=[['Merkür · Mercury',87.97,135,7,'#b9b2a8'],['Venüs · Venus',224.7,210,11,'#e9d8b0'],['Dünya · Earth',365.26,290,12,'#5fa8d3'],['Mars',686.98,380,9,'#d77a55'],['Jüpiter · Jupiter',4332.6,540,22,'#d8b99a']],TR=[];
 T(L,'<div class="hzbox">'+hd('Ölçek Yolculuğu · Scale Journey — simülasyon · simulation','Gezegenler gerçek hız oranlarıyla dönüyor: 1 Dünya yılı = 12 saniye','The planets turning at their true relative speeds — 1 Earth year = 12 seconds')+'</div>','top:20px',.4);
 var R=T(L,'','bottom:30px;left:40px;right:auto;text-align:left;width:400px',1),done=false;
 wLoop(L,function(t){x.fillStyle='#03050b';x.fillRect(0,0,1920,1080);drawStars(x,S,t);var days=t/Y*365.26;
  var g=x.createRadialGradient(CX,CY,0,CX,CY,70);g.addColorStop(0,'#fff6d8');g.addColorStop(.35,'#ffc966');g.addColorStop(1,'rgba(255,150,60,0)');x.fillStyle=g;x.beginPath();x.arc(CX,CY,70,0,7);x.fill();
  for(var i=0;i<PL.length;i++){var p=PL[i],a=-days/p[1]*Math.PI*2+i,px=CX+Math.cos(a)*p[2],py=CY+Math.sin(a)*p[2]*K;
   x.strokeStyle='rgba(160,180,200,.18)';x.lineWidth=1.5;x.beginPath();x.ellipse(CX,CY,p[2],p[2]*K,0,0,7);x.stroke();
   if(i==2){TR.push([px,py]);if(TR.length>90)TR.shift();x.strokeStyle='rgba(95,168,211,.5)';x.lineWidth=3;x.beginPath();for(var j=0;j<TR.length;j++){if(j)x.lineTo(TR[j][0],TR[j][1]);else x.moveTo(TR[j][0],TR[j][1])}x.stroke()}
   x.fillStyle=p[4];x.beginPath();x.arc(px,py,p[3],0,7);x.fill();x.fillStyle='rgba(230,236,240,.75)';x.font='20px Helvetica,Arial';x.fillText(p[0],px+p[3]+8,py+6)}
  R.innerHTML='<div class="hzbox" style="padding:12px 28px"><div class="lb">Geçen süre · Time passed</div><div style="font-size:2vw">'+(days/365.26).toFixed(1).replace('.',',')+' yıl · years</div><div class="sm">Uzaklıklar ölçeksiz · distances not to scale</div></div>';
  if(t>30&&!done){done=true;T(L,'<div class="hzbox" style="max-width:58vw"><div class="a" style="font-size:1.8vw">Merkür 88 günde, Mars 687 günde, Jüpiter neredeyse 12 yılda bir tur atar</div><div class="e" style="font-size:1.25vw">Mercury laps the Sun in 88 days, Mars in 687, Jupiter in almost 12 years — at this speed one Jupiter year would take 2.4 minutes</div></div>','bottom:20px;left:auto;right:40px;width:58vw',.1)}});return L};

/* Shepard tables: two table tops that are exactly the same shape */
W.hzshepard=function(L,it){L.style.background='#ece6da';var c=wCv(L),x=c.getContext('2d'),E1=[150,-300],E2=[120,45];
 function rot(v,a){return[v[0]*Math.cos(a)-v[1]*Math.sin(a),v[0]*Math.sin(a)+v[1]*Math.cos(a)]}
 function top(cx,cy,a){var e1=rot(E1,a),e2=rot(E2,a),p0=[cx-(e1[0]+e2[0])/2,cy-(e1[1]+e2[1])/2];return[p0,[p0[0]+e1[0],p0[1]+e1[1]],[p0[0]+e1[0]+e2[0],p0[1]+e1[1]+e2[1]],[p0[0]+e2[0],p0[1]+e2[1]]]}
 function poly(P,f,s,w){x.beginPath();x.moveTo(P[0][0],P[0][1]);for(var i=1;i<P.length;i++)x.lineTo(P[i][0],P[i][1]);x.closePath();if(f){x.fillStyle=f;x.fill()}if(s){x.strokeStyle=s;x.lineWidth=w||3;x.stroke()}}
 function table(P){var th=22,LG=150;var lo=P.slice().sort(function(a,b){return b[1]-a[1]});
  for(var i=0;i<4;i++){var q=P[i];x.fillStyle='#5a3b26';x.fillRect(q[0]-9,q[1],18,LG)}
  for(i=0;i<4;i++){var a=P[i],b=P[(i+1)%4];if(a[1]+b[1]>lo[2][1]+lo[3][1]-1)poly([a,b,[b[0],b[1]+th],[a[0],a[1]+th]],'#7a5034')}
  poly(P,'#b5835a','#4b311f',3)}
 var A=top(640,600,0),B=top(1290,620,Math.PI/2),done=false;
 T(L,'<div class="hzbox" style="background:rgba(20,24,28,.85)">'+hd('Göz Oyunu · Optical Illusion','Hangi masanın üstü daha uzun ve ince?','Which table top is longer and thinner?')+'</div>','top:20px',.4);
 T(L,'<div class="hzbox" style="background:rgba(20,24,28,.85)"><div class="a" style="font-size:1.9vw">İki masa üstü birebir aynı! Biri yalnızca döndürülmüş</div><div class="e" style="font-size:1.3vw">The two table tops are exactly the same shape — one is just turned. The brain “corrects” for depth and stretches the one going away</div><div class="sm">Shepard masaları · Shepard tables — Roger Shepard, 1990</div></div>','bottom:18px',20);
 wLoop(L,function(t){x.fillStyle='#ece6da';x.fillRect(0,0,1920,1080);table(A);table(B);
  var m=t<20?0:t<26?ease((t-20)/6):t<34?1:t<38?1-ease((t-34)/4):0;
  if(m>0){var cx=640+(1290-640)*m,cy=600+20*m,P=top(cx,cy,Math.PI/2*m);poly(P,'rgba(255,107,74,.35)','#ff6b4a',5)}});return L};

/* Bezold / Munker effect: the same red looks orange on yellow stripes and purple on blue stripes */
W.hzbezold=function(L,it){L.style.background='#14171c';var c=wCv(L),x=c.getContext('2d'),RED='#e8433a',SW=10;
 T(L,'<div class="hzbox">'+hd('Göz Oyunu · Optical Illusion','Ortadaki iki karenin rengi aynı mı?','Are the two squares in the middle the same colour?')+'</div>','top:20px',.4);
 T(L,'<div class="hzbox"><div class="a" style="font-size:1.9vw">Evet: ikisi de aynı kırmızı! Komşu çizgiler rengi kendine çekiyor</div><div class="e" style="font-size:1.3vw">Yes — both are the very same red. The neighbouring stripes pull the colour towards themselves (colour assimilation)</div><div class="sm">Bezold etkisi · Bezold effect — Wilhelm von Bezold, 1874 · Munker illüzyonu · Munker illusion</div></div>','bottom:18px',20);
 function panel(X,col,fade){for(var y=0;y<520;y+=SW){var k=(y/SW)%2,inSq=y>=130&&y<390;var px0=X,px1=X+600;
  if(k==0){x.fillStyle=col;x.globalAlpha=1-fade;x.fillRect(px0,280+y,600,SW);x.globalAlpha=1}else{x.fillStyle='#14171c';x.fillRect(px0,280+y,600,SW)}
  if(inSq&&k==1){x.fillStyle=RED;x.fillRect(X+170,280+y,260,SW)}
  if(inSq&&k==0&&fade>0){x.fillStyle='#14171c';x.globalAlpha=fade;x.fillRect(X+170,280+y,260,SW);x.globalAlpha=1}}}
 wLoop(L,function(t){var f=t<20?0:t<24?ease((t-20)/4):t<34?1:t<38?1-ease((t-34)/4):0;x.fillStyle='#14171c';x.fillRect(0,0,1920,1080);panel(250,'#ffd21f',f);panel(1070,'#2f55ff',f)});return L};

/* Lighthouse: a slow beam turning over the night sea (calm night) */
W.hzfener=function(L,it){var c=wCv(L),x=c.getContext('2d'),S=stars(200),HY=620,LX=1450,LY=360,P=10;
 T(L,hd('Deniz Feneri · Lighthouse — çizim · illustration, hayal ürünü · imagined (sakin · calm)','Gece boyunca usulca dönen bir deniz feneri','A lighthouse turning slowly through the night'),'top:44px',2);
 T(L,'<div class="sm" style="font-size:1.25vw;color:#cdd6dc">Her fenerin kendine özgü bir çakma düzeni vardır; denizciler feneri ışığının ritminden tanır. Bu hayalî fener her 10 saniyede bir döner<br><i>Every lighthouse has its own flash pattern — sailors recognise it by the rhythm of its light. This imagined one turns once every 10 seconds</i></div>','bottom:40px',9);
 wLoop(L,function(t){var g=x.createLinearGradient(0,0,0,HY);g.addColorStop(0,'#02040a');g.addColorStop(1,'#0c1626');x.fillStyle=g;x.fillRect(0,0,1920,HY);drawStars(x,S.filter(function(s){return s[1]<HY-10}),t);
  var sg=x.createLinearGradient(0,HY,0,1080);sg.addColorStop(0,'#0a1424');sg.addColorStop(1,'#02040a');x.fillStyle=sg;x.fillRect(0,HY,1920,1080-HY);
  var a=(t%P)/P*Math.PI*2,cs=Math.cos(a),sn=Math.sin(a),len=1900,vis=.5+.5*sn;
  x.save();x.globalCompositeOperation='lighter';var w=.07+.05*(1-Math.abs(cs));var bx=LX+cs*len,by=LY+Math.abs(sn)*40-30;
  var bg=x.createLinearGradient(LX,LY,bx,by);bg.addColorStop(0,'rgba(255,244,214,'+(.35+.25*vis).toFixed(3)+')');bg.addColorStop(1,'rgba(255,244,214,0)');x.fillStyle=bg;x.beginPath();x.moveTo(LX,LY);x.lineTo(bx,by-len*w);x.lineTo(bx,by+len*w);x.closePath();x.fill();
  var gl=x.createRadialGradient(LX,LY,0,LX,LY,60+140*Math.pow(vis,6));gl.addColorStop(0,'rgba(255,248,226,.95)');gl.addColorStop(1,'rgba(255,240,200,0)');x.fillStyle=gl;x.beginPath();x.arc(LX,LY,220,0,7);x.fill();
  for(var r=0;r<26;r++){var yy=HY+10+r*r*.62,ww=6+r*3.2,al=(.22-r*.007)*(.4+.6*vis);if(al<=0)break;x.fillStyle='rgba(255,236,190,'+al.toFixed(3)+')';x.fillRect(LX-ww/2+Math.sin(t*.8+r)*6,yy,ww,2)}x.restore();
  x.fillStyle='#07090d';x.beginPath();x.moveTo(1180,HY+4);x.quadraticCurveTo(1320,520,1420,505);x.lineTo(1500,500);x.quadraticCurveTo(1640,520,1800,HY+4);x.closePath();x.fill();
  x.fillStyle='#d9dde2';x.beginPath();x.moveTo(1428,505);x.lineTo(1436,385);x.lineTo(1464,385);x.lineTo(1472,505);x.closePath();x.fill();
  x.fillStyle='#9a3b34';x.fillRect(1434,440,32,18);x.fillRect(1431,475,38,14);x.fillStyle='#1b2028';x.fillRect(1438,346,24,34);x.beginPath();x.moveTo(1432,348);x.lineTo(1450,326);x.lineTo(1468,348);x.closePath();x.fill();
  for(var wv=0;wv<5;wv++){var wy=HY+40+wv*80+Math.sin(t*.4+wv)*4;x.strokeStyle='rgba(120,140,170,.10)';x.lineWidth=2;x.beginPath();for(var px=0;px<=1920;px+=40){var q=wy+Math.sin(px*.005+t*.5+wv)*4;if(px)x.lineTo(px,q);else x.moveTo(px,q)}x.stroke()}});return L};


/* ---------- v68 additions: hzflow hzlissa hzrule (living art), hzscint hzchecker (illusions), hzlantern (calm night) ---------- */
/* flow field: thousands of tiny particles drifting along an invisible, slowly changing wind map */
W.hzflow=function(L,it){L.style.background='#070d14';var c=wCv(L),x=c.getContext('2d'),P=[],N=1400,i;
 x.fillStyle='#070d14';x.fillRect(0,0,1920,1080);
 for(i=0;i<N;i++)P.push([Math.random()*1920,Math.random()*1080,Math.random()*200]);
 T(L,'<div class="hzbox">'+hd('Yaşayan Sanat · Living Art — simülasyon · simulation','Görünmez bir rüzgâr haritası; binlerce nokta ona uyuyor','An invisible wind map — and thousands of dots obey it')+'</div>','top:22px',.4);
 T(L,'<div class="hzbox" style="max-width:56vw"><div class="sm" style="font-size:1.2vw;color:#dfe6e9">Her noktanın tek kuralı var: bulunduğu yerdeki oku izle. Haritayı yavaşça değiştirince çizgiler nehir gibi akıyor<br><i>Each dot has a single rule: follow the arrow where you are. Change the map slowly and the lines flow like rivers</i></div></div>','bottom:20px;left:40px;right:auto;text-align:left',6);
 function ang(px,py,t){return (Math.sin(px*.0032+t*.07)+Math.cos(py*.0041-t*.05)+Math.sin((px+py)*.0019+t*.04))*1.6}
 wLoop(L,function(t){x.fillStyle='rgba(7,13,20,.06)';x.fillRect(0,0,1920,1080);
  for(i=0;i<N;i++){var p=P[i],a=ang(p[0],p[1],t),nx=p[0]+Math.cos(a)*2.4,ny=p[1]+Math.sin(a)*2.4;
   var h=190+60*Math.sin(a)+(p[2]%40);x.strokeStyle='hsla('+h+',70%,'+(58+10*Math.cos(a))+'%,.55)';x.lineWidth=1.3;x.beginPath();x.moveTo(p[0],p[1]);x.lineTo(nx,ny);x.stroke();
   p[0]=nx;p[1]=ny;p[2]+=1;if(p[0]<0||p[0]>1920||p[1]<0||p[1]>1080||p[2]>420){p[0]=Math.random()*1920;p[1]=Math.random()*1080;p[2]=Math.random()*60}}});return L};

/* Lissajous table: a grid of curves from two simple oscillations with different frequency ratios */
W.hzlissa=function(L,it){grad(L,'#16202e','#04070b');var c=wCv(L),x=c.getContext('2d'),G=5,CW=300,OX=(1920-G*CW)/2+CW/2,OY=335;
 T(L,'<div class="hzbox">'+hd('Sesin Şekli · The Shape of Sound — simülasyon · simulation','İki basit titreşim, bir araya gelince dans eden eğriler','Two simple vibrations, combined, become dancing curves')+'</div>','top:20px',.4);
 T(L,'<div class="hzbox" style="max-width:62vw"><div class="sm" style="font-size:1.2vw;color:#dfe6e9">Yatayda bir titreşim, dikeyde bir başkası. Frekans oranı 1:2 ise sekiz, 2:3 ise bir düğüm çıkar — müzikteki oktav ve beşli aralıklar böyle görünür<br><i>One vibration sideways, another up and down. A 1:2 ratio gives a figure eight, 2:3 a knot — this is how an octave and a fifth look</i></div></div>','bottom:16px',6);
 wLoop(L,function(t){x.clearRect(0,0,1920,1080);
  for(var a=0;a<4;a++)for(var b=0;b<G;b++){var cx=OX+b*CW,cy=OY+a*150,fx=b+1,fy=a+1;
   x.strokeStyle='rgba(143,211,193,.9)';x.lineWidth=2;x.beginPath();var ph=t*.35;
   for(var k=0;k<=240;k++){var u=k/240*Math.PI*2,px=cx+Math.sin(fx*u+ph)*105,py=cy+Math.sin(fy*u)*55;if(k)x.lineTo(px,py);else x.moveTo(px,py)}x.stroke();
   var u2=t*1.4;x.fillStyle='#fff';x.beginPath();x.arc(cx+Math.sin(fx*u2+ph)*105,cy+Math.sin(fy*u2)*55,5,0,7);x.fill();
   x.fillStyle='rgba(180,195,205,.7)';x.font='22px Helvetica,Arial';x.textAlign='center';x.fillText(fx+' : '+fy,cx,cy+80)}});return L};

/* elementary cellular automata: Rule 30, Rule 90 (Sierpinski) and Rule 110, one line at a time */
W.hzrule=function(L,it){L.style.background='#0a0d12';var c=wCv(L),x=c.getContext('2d'),CS=6,NC=320,TOP=175,NR=Math.floor((1080-TOP-125)/CS),RULES=[30,90,110],NOTE=[
 ['Kural 30: kaotik görünür; bir zamanlar Mathematica’nın rastgele sayı üretecinde kullanıldı','Rule 30 looks chaotic — it was once used as the random-number generator in Mathematica'],
 ['Kural 90: aynı kuraldan bir Sierpinski üçgeni doğuyor','Rule 90: the very same game draws a Sierpinski triangle'],
 ['Kural 110: sonsuza kadar tam bir bilgisayar gibi hesap yapabilir','Rule 110 can compute anything a computer can — it is “Turing complete”']];
 var hdr=T(L,'<div class="hzbox">'+hd('Yaşayan Sanat · Living Art — simülasyon · simulation','Her satır, bir üsttekinin üç komşusuna bakıp renk seçiyor','Each row looks at three neighbours above it and chooses its colour')+'</div>','top:20px',.4);
 var cap=T(L,'','bottom:14px;left:5vw;right:5vw',1),ri=-1,row,cells,y=0,last=-9,seg=19;
 function start(k){ri=k;cells=new Uint8Array(NC);cells[NC>>1]=1;y=0;x.fillStyle='#0a0d12';x.fillRect(0,TOP,1920,1080-TOP);cap.innerHTML='<div class="hzbox" style="padding:.5vw 1.6vw"><div class="a" style="font-size:1.5vw">'+NOTE[k][0]+'</div><div class="e" style="font-size:1.1vw">'+NOTE[k][1]+'</div></div>'}
 wLoop(L,function(t){var k=Math.min(2,Math.floor(t/seg));if(k!=ri)start(k);var want=Math.min(NR,Math.floor((t-k*seg)*10));
  while(y<want){for(var i=0;i<NC;i++)if(cells[i]){x.fillStyle=ri==0?'#8fd3c1':ri==1?'#9db8ff':'#ffb38a';x.fillRect(i*CS,TOP+y*CS,CS-1,CS-1)}
   var n=new Uint8Array(NC);for(i=0;i<NC;i++){var l=cells[(i+NC-1)%NC],m=cells[i],r=cells[(i+1)%NC];n[i]=(RULES[ri]>>(l*4+m*2+r))&1}cells=n;y++}});return L};

/* scintillating grid: dark dots seem to flash at the crossings you are not looking at */
W.hzscint=function(L,it){L.style.background='#000';var c=wCv(L),x=c.getContext('2d');x.fillStyle='#000';x.fillRect(0,0,1920,1080);
 var SP=96,NX=14,NY=7,X0=(1920-SP*(NX-1))/2,Y0=250,i,j;
 x.fillStyle='#46468a';for(i=0;i<NX;i++)x.fillRect(X0+i*SP-8,Y0-SP*.6,16,SP*(NY-1)+SP*1.2);for(j=0;j<NY;j++)x.fillRect(X0-SP*.6,Y0+j*SP-8,SP*(NX-1)+SP*1.2,16);
 x.fillStyle='#fff';for(i=0;i<NX;i++)for(j=0;j<NY;j++){x.beginPath();x.arc(X0+i*SP,Y0+j*SP,13,0,7);x.fill()}
 T(L,'<div class="hzbox">'+hd('Göz Oyunu · Optical Illusion','Beyaz noktaların arasında koyu noktalar yanıp sönüyor mu?','Do dark dots flicker among the white ones?')+'</div>','top:12px',.4);
 T(L,'<div class="hzbox"><div class="a" style="font-size:1.8vw">Hayır! Ekranda hiç koyu nokta yok; kıvılcımları beynin yaratıyor</div><div class="e" style="font-size:1.25vw">No — there are no dark dots at all. Your visual system makes the flashes. Look at one crossing and the others twinkle (scintillating grid, Schrauf 1993)</div></div>','bottom:14px',16);return L};

/* Adelson checker shadow: squares A and B are exactly the same grey */
W.hzchecker=function(L,it){L.style.background='#2a2d33';var c=wCv(L),x=c.getContext('2d'),S=80,OX=(1920-S*8)/2,OY=250,LT=205,DK=112,K=DK/LT;
 T(L,'<div class="hzbox">'+hd('Göz Oyunu · Optical Illusion','A ve B karelerinden hangisi daha açık gri?','Which is lighter grey, square A or square B?')+'</div>','top:14px',.4);
 T(L,'<div class="hzbox"><div class="a" style="font-size:1.8vw">İkisi tamamen aynı gri! Beyin gölgeyi “hesaplayıp” çıkarıyor</div><div class="e" style="font-size:1.25vw">They are exactly the same grey. Your brain discounts the shadow (Adelson’s checker-shadow illusion, 1995). Ekranda ölçerseniz hem A hem B = %44 parlaklık · measure it: both A and B are 44 % brightness</div></div>','bottom:12px',22);
 function g(v){v=Math.round(v);return 'rgb('+v+','+v+','+v+')'}
 var SX=OX+S*4.2,SY=OY+S*3.6;
 function inSh(cx,cy){var dx=(cx-SX)/(S*2.3),dy=(cy-SY)/(S*1.15);return dx*dx+dy*dy<1||(cx>SX&&cx<SX+S*2.7&&Math.abs(cy-SY)<S*.75&&false)}
 var A=[0,4],B=[3,4];
 wLoop(L,function(t){for(var r=0;r<8;r++)for(var q=0;q<8;q++){var light=(r+q)%2==1,cx=OX+q*S+S/2,cy=OY+r*S+S/2,sh=inSh(cx,cy)||(Math.abs(cy-SY)<S*.7&&cx>SX-S*.2&&cx<SX+S*3.3);var v=light?LT:DK;if(sh)v*=K;x.fillStyle=g(v);x.fillRect(OX+q*S,OY+r*S,S,S)}
  var sq=function(r,q,l){x.fillStyle='rgba(255,60,60,0)';x.strokeStyle='#ff5a4a';x.lineWidth=4;x.strokeRect(OX+q*S+6,OY+r*S+6,S-12,S-12);x.fillStyle='#ff5a4a';x.font='bold 40px Helvetica,Arial';x.textAlign='center';x.fillText(l,OX+q*S+S/2,OY+r*S+S/2+14)};
  sq(A[1],A[0],'A');sq(B[1],B[0],'B');
  if(t>14){var al=Math.min(1,(t-14)/3),ya=OY+A[1]*S+S/2;x.globalAlpha=al;x.fillStyle=g(DK);x.fillRect(OX+A[0]*S+S/2,ya-S*.18,(B[0]-A[0])*S,S*.36);x.fillStyle='#ff5a4a';x.font='bold 40px Helvetica,Arial';x.fillText('A',OX+A[0]*S+S/2,ya+14);x.fillText('B',OX+B[0]*S+S/2,ya+14);x.globalAlpha=1}});return L};

/* floating lanterns: calm night, slow warm lights drifting up over dark water and distant hills */
W.hzlantern=function(L,it){var c=wCv(L),x=c.getContext('2d'),S=stars(160),N=26,P=[],i;
 for(i=0;i<N;i++)P.push([Math.random()*1920,Math.random()*1000+60,.14+Math.random()*.3,Math.random()*6.28,.6+Math.random()*.9]);
 T(L,hd('Gece Kandilleri · Night Lanterns — çizim · illustration, hayal ürünü · imagined (sakin · calm)','Karanlık bir gökte yavaşça yükselen kandiller','Lanterns slowly rising into a dark sky'),'top:44px',2);
 T(L,'<div class="sm" style="font-size:1.25vw;color:#cdd6dc">Kandil, bayram ve anma gecelerinde dileklerin göğe bırakıldığı en eski ışıklardandır; her biri küçük bir niyet taşır<br><i>Lanterns are among the oldest lights for letting wishes drift to the sky — each carries one small intention</i></div>','bottom:40px',9);
 wLoop(L,function(t){var HY=760,g=x.createLinearGradient(0,0,0,HY);g.addColorStop(0,'#02030a');g.addColorStop(1,'#101a2e');x.fillStyle=g;x.fillRect(0,0,1920,HY);drawStars(x,S.filter(function(s){return s[1]<HY-20}),t);
  x.fillStyle='#050912';x.beginPath();x.moveTo(0,HY);x.lineTo(0,640);for(var px=0;px<=1920;px+=40)x.lineTo(px,640+Math.sin(px*.004+1)*46+Math.sin(px*.011)*18);x.lineTo(1920,HY);x.fill();
  var wg=x.createLinearGradient(0,HY,0,1080);wg.addColorStop(0,'#0b1424');wg.addColorStop(1,'#02040a');x.fillStyle=wg;x.fillRect(0,HY,1920,320);
  for(i=0;i<N;i++){var p=P[i];p[1]-=p[2]*.6;p[0]+=Math.sin(t*.3+p[3])*.25;if(p[1]<-40){p[1]=HY-30;p[0]=Math.random()*1920}
   var fl=.82+.18*Math.sin(t*2.2+p[3]*3),r=15*p[4];
   for(var m=0;m<2;m++){var yy=m?HY+(HY-p[1])*.9+20:p[1],al=(m?.18:1)*Math.min(1,(HY-p[1])/80)*fl;if(m&&yy>1070)continue;
    var gl=x.createRadialGradient(p[0],yy,0,p[0],yy,r*7);gl.addColorStop(0,'rgba(255,214,170,'+(.55*al).toFixed(3)+')');gl.addColorStop(1,'rgba(255,190,150,0)');x.fillStyle=gl;x.beginPath();x.arc(p[0],yy,r*7,0,7);x.fill();
    x.fillStyle='rgba(255,236,214,'+(.95*al).toFixed(3)+')';x.beginPath();x.ellipse(p[0],yy,r*.7,r,0,0,7);x.fill()}}});return L};

/* ---------- v69 additions: hzmandel hzbuffon (living art / clever thinking), hzouchi hzmach hzbarber (illusions), hzember (calm night) ---------- */
/* Mandelbrot set: z → z² + c, drawn row by row, zooming into "Seahorse Valley" */
W.hzmandel=function(L,it){L.style.background='#03060c';var c=wCv(L),x=c.getContext('2d'),RW=480,RH=270,o=document.createElement('canvas');o.width=RW;o.height=RH;var ox=o.getContext('2d'),img=ox.createImageData(RW,RH),D=img.data,bg=document.createElement('canvas');bg.width=1920;bg.height=1080;var bx=bg.getContext('2d');
 var CX=-0.743643887,CY=0.131825904,st=-1,row=0,sc=3.2,mi=80,SEG=it.seg||9,zoomLab=T(L,'','bottom:16px;left:auto;right:40px;width:auto;text-align:right',1);
 T(L,'<div class="hzbox">'+hd('Yaşayan Sanat · Living Art — hesaplama · computation','Mandelbrot kümesi: tek bir kısa formül, sonsuz bir kıyı','The Mandelbrot set — one short formula, an endless coastline')+'</div>','top:20px',.4);
 T(L,'<div class="hzbox" style="max-width:52vw"><div class="sm" style="font-size:1.15vw;color:#dfe6e9">Her nokta için z → z² + c tekrar edilir; sonsuza kaçmayan noktalar kümeye aittir. Ne kadar yaklaşırsan yaklaş, yeni ayrıntı çıkar (Benoit Mandelbrot, 1980’ler)<br><i>For every point, repeat z → z² + c; points that never escape belong to the set. However far you zoom, new detail appears</i></div></div>','bottom:16px;left:40px;right:auto;text-align:left',5);
 function col(n,zr,zi){if(n>=mi)return [4,8,16];var s=n+1-Math.log(Math.log(Math.sqrt(zr*zr+zi*zi)))/Math.LN2,t=s/40;
  return [Math.round(15+80*(.5+.5*Math.sin(t*6.28+4.2))),Math.round(60+150*(.5+.5*Math.sin(t*6.28+2.6))),Math.round(120+130*(.5+.5*Math.sin(t*6.28+1.3)))]}
 function start(k){st=k;row=0;sc=3.2/Math.pow(3.2,k);mi=Math.min(1400,90+k*120);
  bx.fillStyle='#03060c';bx.fillRect(0,0,1920,1080);if(k>0){bx.save();bx.translate(960,540);bx.scale(3.2,3.2);bx.translate(-960,-540);bx.drawImage(c,0,0);bx.restore()}
  zoomLab.innerHTML='<div class="hzbox" style="padding:.4vw 1.2vw"><div class="sm" style="font-size:1.1vw;color:#dfe6e9">Yakınlaştırma · Zoom ×'+Math.round(Math.pow(3.2,k)).toLocaleString('tr-TR')+'</div></div>'}
 wLoop(L,function(t){var k=Math.floor(t/SEG)%9;if(k!=st)start(k);if(row>=RH)return;
  var end=Math.min(RH,row+10),asp=RW/RH;for(var py=row;py<end;py++){var ci=CY+(py/RH-.5)*sc/asp;for(var px=0;px<RW;px++){var cr=CX+(px/RW-.5)*sc,zr=0,zi=0,n=0,r2;
    while(n<mi){r2=zr*zr;var i2=zi*zi;if(r2+i2>16)break;zi=2*zr*zi+ci;zr=r2-i2+cr;n++}
    var cc=col(n,zr,zi),q=(py*RW+px)*4;D[q]=cc[0];D[q+1]=cc[1];D[q+2]=cc[2];D[q+3]=255}}
  ox.putImageData(img,0,0,0,row,RW,end-row);row=end;x.imageSmoothingEnabled=true;x.drawImage(bg,0,0);x.drawImage(o,0,0,RW,row,0,0,1920,row*4)});return L};

/* Buffon's needle: drop needles on a striped floor; the share that cross a line estimates π */
W.hzbuffon=function(L,it){L.style.background='#1a140f';var c=wCv(L),x=c.getContext('2d'),D=120,X0=120,X1=1800,Y0=215,Y1=900,N=0,C=0,last=0;
 function floor(){x.fillStyle='#2b2118';x.fillRect(X0,Y0,X1-X0,Y1-Y0);for(var gx=X0;gx<=X1;gx+=D){x.fillStyle='#d8d2c4';x.fillRect(gx-1.5,Y0,3,Y1-Y0)}}
 floor();
 T(L,'<div class="hzbox">'+hd('Zekice Düşünce · Clever Thinking — simülasyon · simulation','Yere rastgele iğne atarak π sayısını bulmak','Finding π by dropping needles at random')+'</div>','top:16px',.4);
 var box=T(L,'','bottom:14px',1);
 wLoop(L,function(t){var k=t<3?0:t<10?1:t<20?3:t<35?6:10;x.fillStyle='rgba(43,33,24,.035)';x.fillRect(X0,Y0,X1-X0,Y1-Y0);for(var gx=X0;gx<=X1;gx+=D){x.fillStyle='#d8d2c4';x.fillRect(gx-1.5,Y0,3,Y1-Y0)}
  for(var i=0;i<k;i++){var cx=X0+D/2+Math.random()*(X1-X0-D),cy=Y0+D/2+Math.random()*(Y1-Y0-D),a=Math.random()*Math.PI,dx=Math.cos(a)*D/2,dy=Math.sin(a)*D/2;
   var xa=cx-dx,xb=cx+dx,hit=Math.floor((xa-X0)/D)!=Math.floor((xb-X0)/D);N++;if(hit)C++;
   x.strokeStyle=hit?'rgba(255,140,110,.85)':'rgba(143,211,193,.55)';x.lineWidth=2;x.beginPath();x.moveTo(xa,cy-dy);x.lineTo(xb,cy+dy);x.stroke()}
  if(N>200000){N=0;C=0;floor()}
  if(t-last>.3){last=t;var est=C?(2*N/C):0;box.innerHTML='<div class="hzbox" style="padding:.6vw 1.8vw"><div class="a" style="font-size:1.7vw">İğne · Needles: '+N.toLocaleString('tr-TR')+' · çizgiye değen · crossing: '+C.toLocaleString('tr-TR')+' · π ≈ '+(C?est.toFixed(4):'…')+'</div><div class="e" style="font-size:1.1vw">İğne boyu = çizgi aralığı ise, değme olasılığı 2/π. Yani π ≈ 2 × atılan ÷ değen (Buffon, 1777) · If the needle is as long as the line gap, the chance of crossing is 2/π — so π ≈ 2 × thrown ÷ crossing</div></div>'}});return L};

/* Ouchi illusion: a disc of vertical bricks inside a field of horizontal bricks seems to float and slide */
W.hzouchi=function(L,it){L.style.background='#000';var c=wCv(L),x=c.getContext('2d'),BW=44,BH=11,R=230,CX=960,CY=575;
 function bricks(vert){for(var yy=0;yy<1080;yy+=(vert?BW:BH))for(var xx=0;xx<1920;xx+=(vert?BH:BW)){var on=((xx/(vert?BH:BW))+(yy/(vert?BW:BH)))%2<1;x.fillStyle=on?'#f2f2f2':'#111';x.fillRect(xx,yy,vert?BH:BW,vert?BW:BH)}}
 function draw(ox,oy){x.save();x.translate(ox,oy);bricks(false);x.beginPath();x.arc(CX,CY,R,0,7);x.clip();bricks(true);x.restore()}
 T(L,'<div class="hzbox">'+hd('Göz Oyunu · Optical Illusion','Gözlerini resmin üzerinde gezdir: ortadaki daire ayrı bir katman gibi kayıyor mu?','Let your eyes wander over the picture — does the central disc slide like a separate layer?')+'</div>','top:12px',.4);
 T(L,'<div class="hzbox"><div class="a" style="font-size:1.7vw">Daire basılı ve hareketsiz; kaymayı beyin üretiyor</div><div class="e" style="font-size:1.2vw">The disc is printed flat and does not move — your brain judges the motion of vertical and horizontal edges differently (Ouchi illusion, Hajime Ouchi, 1977)</div></div>','bottom:12px',18);
 wLoop(L,function(t){var a=t*.9;draw(Math.round(Math.cos(a)*6),Math.round(Math.sin(a)*6))});return L};

/* Mach bands: each grey band is perfectly even, yet the edges seem to glow light and dark */
W.hzmach=function(L,it){L.style.background='#202428';var c=wCv(L),x=c.getContext('2d'),N=8,X0=160,BW=200,Y0=250,Y1=760;
 T(L,'<div class="hzbox">'+hd('Göz Oyunu · Optical Illusion','Her gri şeridin içi düz mü, yoksa kenarlarına doğru açılıp koyulaşıyor mu?','Is each grey band even inside — or does it get lighter and darker towards its edges?')+'</div>','top:12px',.4);
 T(L,'<div class="hzbox"><div class="a" style="font-size:1.7vw">Her şerit baştan sona tek bir gri! Kenarlardaki parlak ve koyu çizgileri gözün ekliyor</div><div class="e" style="font-size:1.2vw">Every band is a single flat grey. The light and dark lines at the edges are added by your retina, which sharpens contrast (Mach bands, Ernst Mach, 1865). Alttaki çizgi gerçek parlaklık · the line below is the real brightness</div></div>','bottom:12px',16);
 wLoop(L,function(t){for(var i=0;i<N;i++){var v=Math.round(40+i*26);x.fillStyle='rgb('+v+','+v+','+v+')';x.fillRect(X0+i*BW,Y0,BW,Y1-Y0)}
  if(t>16){var al=Math.min(1,(t-16)/3);x.fillStyle='#202428';x.fillRect(X0-20,Y1+6,N*BW+40,80);x.globalAlpha=al;x.strokeStyle='#ff9e7a';x.lineWidth=4;x.beginPath();
   for(i=0;i<N;i++){var yy=Y1+76-i*9;if(i)x.lineTo(X0+i*BW,yy);else x.moveTo(X0,yy);x.lineTo(X0+(i+1)*BW,yy)}x.stroke();x.globalAlpha=1}});return L};

/* Barber pole illusion: the same diagonal stripes move sideways, but a tall window makes them look like they climb */
W.hzbarber=function(L,it){grad(L,'#1c2430','#05070a');var c=wCv(L),x=c.getContext('2d'),A=[560,250,170,560],B=[940,370,620,190],SP=46;
 T(L,'<div class="hzbox">'+hd('Göz Oyunu · Optical Illusion','İki pencerede aynı çizgiler aynı yöne gidiyor. Hangi yöne?','Both windows show the same stripes moving the same way. Which way?')+'</div>','top:12px',.4);
 T(L,'<div class="hzbox"><div class="a" style="font-size:1.7vw">İkisinde de çizgiler sağa kayıyor! Uzun pencerede aşağı, geniş pencerede yana gidiyor gibi görünüyor</div><div class="e" style="font-size:1.2vw">In both, the stripes slide to the right. In the tall window they seem to fall, in the wide one to slide sideways: the brain reads motion along the longer side of the window — the “aperture problem” behind the barber-pole illusion (Hans Wallach, 1935)</div></div>','bottom:12px',20);
 function win(r,off){x.save();x.beginPath();x.rect(r[0],r[1],r[2],r[3]);x.clip();x.fillStyle='#f3f1ec';x.fillRect(r[0],r[1],r[2],r[3]);x.fillStyle='#c8452f';
  for(var k=-40;k<40;k++){var bx=r[0]+k*SP*2+off;x.beginPath();x.moveTo(bx,r[1]+r[3]);x.lineTo(bx+SP,r[1]+r[3]);x.lineTo(bx+SP+r[3],r[1]);x.lineTo(bx+r[3],r[1]);x.fill()}
  x.restore();x.strokeStyle='#8fd3c1';x.lineWidth=4;x.strokeRect(r[0],r[1],r[2],r[3])}
 wLoop(L,function(t){x.clearRect(0,0,1920,1080);var off=(t*60)%(SP*2);win(A,off);win(B,off);
  if(t>20){x.fillStyle='rgba(255,158,122,'+Math.min(1,(t-20)/2)+')';x.font='bold 54px Helvetica,Arial';x.textAlign='center';x.fillText('→',A[0]+A[2]/2,A[1]+A[3]+60);x.fillText('→',B[0]+B[2]/2,B[1]+B[3]+60)}});return L};

/* calm night: a small campfire under the stars, sparks drifting slowly upward (illustration) */
W.hzember=function(L,it){var c=wCv(L),x=c.getContext('2d'),S=stars(170),P=[],i,FX=960,FY=900;
 T(L,hd('Kamp Ateşi · Campfire — çizim · illustration, hayal ürünü · imagined (sakin · calm)','Yıldızların altında küçük bir ateş','A small fire under the stars'),'top:44px',2);
 T(L,'<div class="sm" style="font-size:1.25vw;color:#cdd6dc">Kıvılcımlar neden yukarı çıkar? Ateşin ısıttığı hava hafifler ve yükselir; minik köz parçalarını da beraberinde taşır<br><i>Why do sparks rise? Air warmed by the fire becomes lighter and rises, carrying tiny embers with it</i></div>','bottom:34px;left:5vw;right:auto;width:42vw;text-align:left',9);
 wLoop(L,function(t){var g=x.createLinearGradient(0,0,0,1080);g.addColorStop(0,'#02030a');g.addColorStop(.75,'#0b1222');g.addColorStop(1,'#120c0a');x.fillStyle=g;x.fillRect(0,0,1920,1080);drawStars(x,S.filter(function(s){return s[1]<640}),t);
  x.fillStyle='#04060b';x.beginPath();x.moveTo(0,1080);x.lineTo(0,700);for(var px=0;px<=1920;px+=40)x.lineTo(px,700+Math.sin(px*.003+2)*60+Math.sin(px*.013)*14);x.lineTo(1920,1080);x.fill();
  var fl=.85+.1*Math.sin(t*7.3)+.05*Math.sin(t*13.1),gl=x.createRadialGradient(FX,FY,0,FX,FY,520*fl);gl.addColorStop(0,'rgba(255,150,90,.38)');gl.addColorStop(1,'rgba(255,120,70,0)');x.fillStyle=gl;x.beginPath();x.arc(FX,FY,520,0,7);x.fill();
  x.strokeStyle='#1a120e';x.lineWidth=16;x.lineCap='round';x.beginPath();x.moveTo(FX-90,FY+40);x.lineTo(FX+70,FY+5);x.moveTo(FX+90,FY+40);x.lineTo(FX-70,FY+5);x.stroke();
  for(var f=0;f<5;f++){var fh=(110+30*Math.sin(t*5+f*1.7))*fl,fw=26+f%2*10,fx=FX-50+f*25;var fg=x.createLinearGradient(0,FY+20,0,FY-fh);fg.addColorStop(0,'rgba(255,120,60,.9)');fg.addColorStop(.6,'rgba(255,170,110,.55)');fg.addColorStop(1,'rgba(255,220,190,0)');x.fillStyle=fg;
   x.beginPath();x.moveTo(fx-fw,FY+20);x.quadraticCurveTo(fx-fw*.6,FY-fh*.5,fx+6*Math.sin(t*3+f),FY-fh);x.quadraticCurveTo(fx+fw*.6,FY-fh*.5,fx+fw,FY+20);x.fill()}
  if(Math.random()<.35)P.push([FX-40+Math.random()*80,FY-30,(Math.random()-.5)*.5,.6+Math.random()*.9,0]);
  for(i=P.length-1;i>=0;i--){var p=P[i];p[0]+=p[2]+Math.sin(t+p[1]*.02)*.3;p[1]-=p[3];p[4]+=1/60;var al=Math.max(0,1-p[4]/7);if(al<=0){P.splice(i,1);continue}
   x.fillStyle='rgba(255,'+(170+Math.round(60*al))+',130,'+al.toFixed(2)+')';x.fillRect(p[0],p[1],2.4,2.4)}});return L};

/* ---------- v71 additions: hztimes (living art), hzmonty hztsp (clever thinking), hzcurve hzpinna (illusions), hzbalikci (calm night) ---------- */
/* times tables on a circle: join point i to point i×k (mod N); k=2 draws a cardioid, k=3 a nephroid… */
W.hztimes=function(L,it){grad(L,'#141c2a','#03050a');var c=wCv(L),x=c.getContext('2d'),N=it.n||240,R=372,CX=960,CY=600,HOLD=it.hold||7,K0=it.k0||2,lab=T(L,'','top:250px;left:auto;right:150px;width:auto;text-align:right',1);
 T(L,'<div class="hzbox">'+hd('Yaşayan Sanat · Living Art — matematik · mathematics','Çemberde çarpım tablosu: her noktayı, kendisinin k katına bağla','A times table on a circle — join every point to k times itself')+'</div>','top:16px',.4);
 T(L,'<div class="hzbox" style="max-width:38vw"><div class="sm" style="font-size:1.1vw;color:#dfe6e9">Çembere '+N+' nokta koy. 1’i k’ya, 2’yi 2k’ya, 3’ü 3k’ya bağla (sayı '+N+'’ü geçerse başa dön). k=2 kalp biçimli bir “kardioid”, k=3 iki yapraklı bir “nefroid” çizer<br><i>Put '+N+' points on a circle. Join 1 to k, 2 to 2k, 3 to 3k (wrapping round past '+N+'). k=2 draws a heart-shaped cardioid, k=3 a two-lobed nephroid</i></div></div>','bottom:16px;left:40px;right:auto;text-align:left',5);
 var NM={2:['kardioid','cardioid'],3:['nefroid','nephroid'],4:['3 yapraklı · 3 cusps','3 cusps'],5:['4 yapraklı · 4 cusps','4 cusps']},lastK=-1;
 wLoop(L,function(t){var u=t/HOLD,n=Math.floor(u),f=u-n,e=f<.55?0:ease((f-.55)/.45),k=K0+n+e;x.clearRect(0,0,1920,1080);x.lineWidth=1.1;
  for(var i=0;i<N;i++){var a=i/N*6.2832-1.5708,b=(i*k)%N/N*6.2832-1.5708,h=(i/N*300+t*6)%360;x.strokeStyle='hsla('+h.toFixed(0)+',70%,68%,.55)';x.beginPath();x.moveTo(CX+Math.cos(a)*R,CY+Math.sin(a)*R);x.lineTo(CX+Math.cos(b)*R,CY+Math.sin(b)*R);x.stroke()}
  x.strokeStyle='rgba(220,230,235,.25)';x.lineWidth=2;x.beginPath();x.arc(CX,CY,R,0,7);x.stroke();
  var kk=K0+n;if(kk!==lastK){lastK=kk;var nm=NM[kk];lab.innerHTML='<div class="hzbox" style="padding:.6vw 1.6vw"><div class="a" style="font-size:2.4vw">k = '+kk+'</div>'+(nm?'<div class="e" style="font-size:1.2vw">'+nm[0]+(nm[0]==nm[1]?'':' · '+nm[1])+'</div>':'')+'</div>'}});return L};

/* Monty Hall: three doors, one car. Stay or switch? Simulate thousands of games */
W.hzmonty=function(L,it){grad(L,'#1d2430','#05070b');var c=wCv(L),x=c.getContext('2d'),G=0,SW=0,ST=0,acc=0,game=null,box=T(L,'','bottom:14px',1),last=0;
 T(L,'<div class="hzbox">'+hd('Zekice Düşünce · Clever Thinking — simülasyon · simulation','Üç kapı, bir araba. Bir kapı seçtin; sunucu keçili bir kapıyı açtı. Kapını değiştirir misin?','Three doors, one car. You pick a door; the host opens one with a goat. Do you switch?')+'</div>','top:14px',.4);
 function newGame(){var car=Math.floor(Math.random()*3),pick=Math.floor(Math.random()*3),opts=[0,1,2].filter(function(d){return d!=pick&&d!=car}),open=opts[Math.floor(Math.random()*opts.length)],sw=[0,1,2].filter(function(d){return d!=pick&&d!=open})[0];return {car:car,pick:pick,open:open,sw:sw}}
 function play(g){G++;if(g.pick==g.car)ST++;if(g.sw==g.car)SW++}
 function door(i,g,ph){var X=560+i*280,Y=330,Wd=200,H=300;x.fillStyle='#3a2c22';x.fillRect(X-8,Y-8,Wd+16,H+16);
  var opened=(ph>=2&&i==g.open)||ph>=3;x.fillStyle=opened?'#11161c':'#7c5a3e';x.fillRect(X,Y,Wd,H);
  if(opened){x.font='120px serif';x.textAlign='center';x.fillText(i==g.car?'🚗':'🐐',X+Wd/2,Y+H/2+40)}else{x.fillStyle='#e8dcc8';x.font='bold 64px Helvetica,Arial';x.textAlign='center';x.fillText(String(i+1),X+Wd/2,Y+H/2+22)}
  if(ph>=1&&i==g.pick){x.strokeStyle='#8fd3c1';x.lineWidth=8;x.strokeRect(X-14,Y-14,Wd+28,H+28);x.fillStyle='#8fd3c1';x.font='28px Helvetica,Arial';x.fillText('Seçimin · Your pick',X+Wd/2,Y+H+56)}}
 function bars(){var p1=G?ST/G:0,p2=G?SW/G:0,X=560,Wb=760,Y=760;x.font='26px Helvetica,Arial';x.textAlign='left';
  [[p1,'Kalırsan kazanma · Win if you stay','#c3cdd2'],[p2,'Değiştirirsen kazanma · Win if you switch','#ff9e7a']].forEach(function(r,j){var y=Y+j*70;x.fillStyle='rgba(255,255,255,.08)';x.fillRect(X,y,Wb,40);x.fillStyle=r[2];x.fillRect(X,y,Wb*r[0],40);x.fillStyle='#f3f1ec';x.fillText(r[1]+' — %'+(r[0]*100).toFixed(1),X,y-10)});
  x.strokeStyle='rgba(255,255,255,.5)';x.lineWidth=2;[1/3,2/3].forEach(function(q){x.beginPath();x.moveTo(X+Wb*q,Y-4);x.lineTo(X+Wb*q,Y+114);x.stroke()})}
 wLoop(L,function(t){x.clearRect(0,0,1920,1080);var slow=t<24,ph;
  if(slow){var gi=Math.floor(t/8),tt=t-gi*8;if(!game||game.i!==gi){if(game&&game.g)play(game.g);game={i:gi,g:newGame()}}ph=tt<1.5?0:tt<3.5?1:tt<5.5?2:3;[0,1,2].forEach(function(i){door(i,game.g,ph)})}
  else{acc+=t<40?1:t<55?6:25;while(acc>=1){acc--;play(newGame())}var g=newGame();[0,1,2].forEach(function(i){door(i,g,3)})}
  bars();if(t-last>.4){last=t;box.innerHTML='<div class="hzbox" style="padding:.6vw 1.8vw"><div class="a" style="font-size:1.6vw">Oyun · Games: '+G.toLocaleString('tr-TR')+(t>45?' — değiştirmek kazandırır: ⅔ · switching wins ⅔ of the time':'')+'</div>'+(t>45?'<div class="e" style="font-size:1.05vw">İlk seçimin 1/3 ihtimalle doğru. Sunucu arabanın yerini bildiği için kalan ⅔ ihtimal tek kapalı kapıda toplanır (Monty Hall problemi, 1975) · Your first pick is right 1/3 of the time; the host knows where the car is, so the other ⅔ collects on the one door left closed</div>':'')+'</div>'}});return L};

/* travelling salesman: nearest-neighbour tour, then 2-opt untangles the crossings */
W.hztsp=function(L,it){grad(L,'#13202a','#04080b');var c=wCv(L),x=c.getContext('2d'),N=it.n||70,P,tour,stage,k,t0,box=T(L,'','bottom:14px',1),last=0;
 T(L,'<div class="hzbox">'+hd('Zekice Düşünce · Clever Thinking — algoritma · algorithm','Gezgin satıcı: '+N+' şehrin hepsine uğrayıp eve dönen en kısa yol hangisi?','The travelling salesman: what is the shortest route that visits all '+N+' cities and comes home?')+'</div>','top:14px',.4);
 function d(a,b){var dx=P[a][0]-P[b][0],dy=P[a][1]-P[b][1];return Math.sqrt(dx*dx+dy*dy)}
 function len(){var s=0;for(var i=0;i<tour.length;i++)s+=d(tour[i],tour[(i+1)%tour.length]);return s}
 function reset(t){P=[];for(var i=0;i<N;i++)P.push([260+Math.random()*1400,250+Math.random()*560]);tour=[0];stage=0;k=0;t0=t}
 function nnStep(){var a=tour[tour.length-1],best=-1,bd=1e9;for(var i=0;i<N;i++)if(tour.indexOf(i)<0){var dd=d(a,i);if(dd<bd){bd=dd;best=i}}if(best<0)return false;tour.push(best);return true}
 function optStep(){var n=tour.length;for(var tries=0;tries<n*n;tries++){var i=k%n,j=Math.floor(k/n)%n;k++;if(j<=i+1)continue;var a=tour[i],b=tour[i+1],cc=tour[j],dd=tour[(j+1)%n];if(d(a,cc)+d(b,dd)<d(a,b)-1e-9+d(cc,dd)-1e-9){var s=tour.slice(i+1,j+1).reverse();Array.prototype.splice.apply(tour,[i+1,s.length].concat(s));k=0;return true}if(k>=n*n)return false}return true}
 reset(0);var L0=0,Lnn=0,lo=0;
 wLoop(L,function(t){if(stage==0){if(t-t0>.15*(tour.length)/1.5){if(!nnStep()){stage=1;Lnn=len();k=0}}}else if(stage==1){if(t-lo>.2){lo=t;if(!optStep()){stage=2;t0=t}}}else if(t-t0>10)reset(t);
  x.clearRect(0,0,1920,1080);x.strokeStyle=stage==0?'rgba(195,205,210,.8)':'rgba(255,158,122,.95)';x.lineWidth=3;x.beginPath();for(var i=0;i<tour.length;i++){var p=P[tour[i]];if(i)x.lineTo(p[0],p[1]);else x.moveTo(p[0],p[1])}if(stage>0)x.closePath();x.stroke();
  for(i=0;i<N;i++){x.fillStyle=i==0?'#8fd3c1':'#f3f1ec';x.beginPath();x.arc(P[i][0],P[i][1],i==0?11:6,0,7);x.fill()}
  if(t-last>.4){last=t;var s=stage==0?'1. Adım: hep en yakın şehre git · Step 1: always go to the nearest city':stage==1?'2. Adım: kesişen iki yolu bul, aradaki parçayı ters çevir (2-opt) · Step 2: find two crossing roads and reverse the piece between them (2-opt)':'Bitti · Done — '+(Lnn?Math.round((1-len()/Lnn)*100):0)+'% daha kısa · shorter than the greedy route';
   box.innerHTML='<div class="hzbox" style="padding:.6vw 1.8vw;max-width:80vw"><div class="a" style="font-size:1.5vw">'+s+'</div><div class="e" style="font-size:1.05vw">'+N+' şehir için olası tur sayısı 100 basamaklı bir sayıdan büyüktür; hepsini denemek imkânsız, bu yüzden akıllı kısayollar kullanılır · For '+N+' cities the number of possible tours has over 100 digits — far too many to try, so clever shortcuts are used</div></div>'}});return L};

/* curvature blindness (Takahashi, 2017): identical gentle waves look zigzag or curved depending on where the shading changes */
W.hzcurve=function(L,it){L.style.background='#7f7f7f';var c=wCv(L),x=c.getContext('2d'),A=30,WL=180,X0=170,X1=1750;
 T(L,'<div class="hzbox">'+hd('Göz Oyunu · Optical Illusion','Hangi çizgiler yumuşak dalga, hangileri sivri zikzak?','Which lines are smooth waves, and which are sharp zigzags?')+'</div>','top:12px',.4);
 T(L,'<div class="hzbox"><div class="a" style="font-size:1.7vw">Hepsi aynı yumuşak dalga! Renk tepe noktalarında değişince beyin köşe görüyor</div><div class="e" style="font-size:1.2vw">Every line is the same smooth wave. Where light and dark switch at the peaks, the brain reads a corner; where they switch on the slopes, it reads a curve (curvature blindness, Kohske Takahashi, 2017). Arada bir hepsi tek renge döner · Now and then they all turn one colour</div></div>','bottom:12px',18);
 function wave(y,off,uni){var ph=off?WL/4:0;for(var xx=X0;xx<X1;xx+=2){var s=Math.floor((xx-X0+ph)/(WL/2)),col=uni?'#222':(s%2?'#f0f0f0':'#151515');x.strokeStyle=col;x.lineWidth=7;x.beginPath();x.moveTo(xx,y+A*Math.sin((xx-X0)/WL*6.2832));x.lineTo(xx+2.4,y+A*Math.sin((xx+2.4-X0)/WL*6.2832));x.stroke()}}
 wLoop(L,function(t){x.fillStyle='#7f7f7f';x.fillRect(0,0,1920,1080);var uni=t>22&&Math.floor((t-22)/4)%2==0;
  x.fillStyle='#b4b4b4';x.fillRect(X0-40,240,X1-X0+80,280);x.fillStyle='#4c4c4c';x.fillRect(X0-40,540,X1-X0+80,280);
  for(var r=0;r<4;r++){wave(290+r*64,r%2,uni);wave(590+r*64,(r+1)%2,uni)}});return L};

/* Pinna–Brelstaff rings: as the picture slowly grows and shrinks, the two rings seem to turn in opposite directions */
W.hzpinna=function(L,it){L.style.background='#8a8a8a';var c=wCv(L),x=c.getContext('2d'),CX=960,CY=580;
 T(L,'<div class="hzbox">'+hd('Göz Oyunu · Optical Illusion','Ortadaki noktaya bak. Resim büyüyüp küçülürken halkalar dönüyor mu?','Look at the centre dot. As the picture grows and shrinks, do the rings turn?')+'</div>','top:12px',.4);
 T(L,'<div class="hzbox"><div class="a" style="font-size:1.7vw">Hiçbir şey dönmüyor! Sadece büyüyüp küçülüyor</div><div class="e" style="font-size:1.2vw">Nothing rotates — the picture only grows and shrinks. The tilted light and dark edges of each square fool motion detectors in the eye into reading a twist, and the two rings seem to turn in opposite directions (Pinna–Brelstaff illusion, 2000)</div></div>','bottom:12px',22);
 function ring(R,n,tilt,inv){for(var i=0;i<n;i++){var a=i/n*6.2832,S=R*.11;x.save();x.translate(Math.cos(a)*R,Math.sin(a)*R);x.rotate(a+tilt);x.fillStyle='#8a8a8a';x.fillRect(-S/2,-S/2,S,S);x.lineWidth=S*.16;
  x.strokeStyle=inv?'#111':'#fafafa';x.beginPath();x.moveTo(-S/2,S/2);x.lineTo(-S/2,-S/2);x.lineTo(S/2,-S/2);x.stroke();x.strokeStyle=inv?'#fafafa':'#111';x.beginPath();x.moveTo(S/2,-S/2);x.lineTo(S/2,S/2);x.lineTo(-S/2,S/2);x.stroke();x.restore()}}
 wLoop(L,function(t){x.fillStyle='#8a8a8a';x.fillRect(0,0,1920,1080);var s=1+.3*Math.sin(t*1.1);x.save();x.translate(CX,CY);x.scale(s,s);ring(300,48,.785,0);ring(200,32,-.785,1);x.restore();
  x.fillStyle='#000';x.beginPath();x.arc(CX,CY,8,0,7);x.fill()});return L};

/* calm night: a dark sea with distant fishing-boat lights rocking gently on the horizon (illustration) */
W.hzbalikci=function(L,it){var c=wCv(L),x=c.getContext('2d'),S=stars(150),HY=640,B=[],i;
 for(i=0;i<7;i++)B.push([180+i*240+Math.random()*120,.6+Math.random()*.6,Math.random()*6.28,Math.random()<.4]);
 T(L,hd('Gece Balıkçıları · Night Fishermen — çizim · illustration, hayal ürünü · imagined (sakin · calm)','Ufukta, karanlık denizin üstünde balıkçı ışıkları','Fishing-boat lights on the horizon of a dark sea'),'top:44px',2);
 T(L,'<div class="sm" style="font-size:1.25vw;color:#cdd6dc">Bazı balıkçılar geceleri güçlü lambalar yakar: küçük balıklar ışığa doğru yüzeye çıkar. Buna “ışıkla avcılık” denir<br><i>Some fishermen light strong lamps at night — small fish rise towards the light. It is called light fishing</i></div>','bottom:40px',9);
 wLoop(L,function(t){var g=x.createLinearGradient(0,0,0,HY);g.addColorStop(0,'#02030a');g.addColorStop(1,'#0e1626');x.fillStyle=g;x.fillRect(0,0,1920,HY);drawStars(x,S.filter(function(s){return s[1]<HY-30}),t);
  var mg=x.createRadialGradient(1520,190,0,1520,190,160);mg.addColorStop(0,'rgba(225,230,240,.9)');mg.addColorStop(.25,'rgba(200,210,230,.25)');mg.addColorStop(1,'rgba(200,210,230,0)');x.fillStyle=mg;x.beginPath();x.arc(1520,190,160,0,7);x.fill();
  for(var k=0;k<3;k++){var cx=((t*6+k*700)%2600)-340,cy=150+k*70;x.fillStyle='rgba(20,26,40,.55)';x.beginPath();x.ellipse(cx,cy,260,34,0,0,7);x.fill()}
  var wg=x.createLinearGradient(0,HY,0,1080);wg.addColorStop(0,'#08101c');wg.addColorStop(1,'#010206');x.fillStyle=wg;x.fillRect(0,HY,1920,440);
  for(i=0;i<B.length;i++){var b=B[i],bob=Math.sin(t*.6+b[2])*3,bx=b[0]+Math.sin(t*.05+b[2])*20,by=HY-6+bob,col=b[3]?'200,255,220':'255,240,215';
   var gl=x.createRadialGradient(bx,by,0,bx,by,60*b[1]);gl.addColorStop(0,'rgba('+col+',.55)');gl.addColorStop(1,'rgba('+col+',0)');x.fillStyle=gl;x.beginPath();x.arc(bx,by,60*b[1],0,7);x.fill();
   x.fillStyle='rgba('+col+',.95)';x.beginPath();x.arc(bx,by,3.4*b[1],0,7);x.fill();
   for(var yy=HY+6;yy<HY+200*b[1];yy+=7){var w=(3+Math.sin(t*1.3+yy*.15+b[2])*2.5)*b[1]*(1+(yy-HY)/90),al=.35*(1-(yy-HY)/(200*b[1]));x.fillStyle='rgba('+col+','+Math.max(0,al).toFixed(3)+')';x.fillRect(bx-w+Math.sin(t+yy*.2)*3,yy,w*2,2.5)}}
  for(var yy2=HY+10;yy2<1080;yy2+=11){x.fillStyle='rgba(150,170,200,.035)';x.fillRect(0,yy2+Math.sin(t*.5+yy2)*2,1920,1)}});return L};

/* ---------- v73 additions: hzrecaman (living art), hzsieve hzhalve (clever thinking), hzwaterfall hztroxler (illusions), hzyayla (calm night) ---------- */
function ablTR(n){n=Math.round(n);var U=['','den','den','ten','ten','ten','dan','den','den','dan'],Tn=['','dan','den','dan','tan','den','tan','ten','den','dan'];if(n%10)return U[n%10];if(n%100)return Tn[(n/10|0)%10];if(n%1000)return 'den';if(n%1000000)return 'den';return 'dan'}
function nTR(n){var s=String(Math.round(n));return s.replace(/\B(?=(\d{3})+(?!\d))/g,'.')}
/* Recamán sequence: step back by n if that number is new and positive, otherwise forward; each step drawn as a half-circle arc */
W.hzrecaman=function(L,it){grad(L,'#141a2a','#03050a');var c=wCv(L),x=c.getContext('2d'),N=it.n||66,A=[0],seen={0:1},i,mx=0,SP=it.sp||.55,HOLD=10,CY=640,lab=T(L,'','bottom:16px',1),lastN=-1;
 for(i=1;i<=N;i++){var p=A[i-1],v=p-i;if(v<0||seen[v])v=p+i;A.push(v);seen[v]=1;if(v>mx)mx=v}
 var sc=Math.min(1760/mx,2*400/N),X0=(1920-mx*sc)/2,TOT=N*SP+HOLD+3;
 T(L,'<div class="hzbox">'+hd('Yaşayan Sanat · Living Art — matematik · mathematics','Recamán dizisi: geri gidebiliyorsan geri git, gidemiyorsan ileri','The Recamán sequence — step back if you can, otherwise step forward')+'</div>','top:16px',.4);
 wLoop(L,function(t){var u=t%TOT,k=Math.min(N,u/SP),n=Math.floor(k),f=k-n,fade=u>N*SP+HOLD?1-(u-N*SP-HOLD)/3:1;x.clearRect(0,0,1920,1080);x.globalAlpha=Math.max(0,fade);
  x.strokeStyle='rgba(220,230,235,.18)';x.lineWidth=1.5;x.beginPath();x.moveTo(X0-20,CY);x.lineTo(X0+mx*sc+20,CY);x.stroke();
  for(var j=1;j<=Math.min(N,n+1);j++){var a=A[j-1],b=A[j],cx=X0+(a+b)/2*sc,r=Math.abs(b-a)/2*sc,up=j%2==1,fr=j<=n?1:f;if(fr<=0)continue;
   var h=(200+j/N*160)%360;x.strokeStyle='hsla('+h.toFixed(0)+',65%,'+(j>n-1?78:64)+'%,.9)';x.lineWidth=j>n-1?3.2:2.2;x.beginPath();
   var s0=b>a?Math.PI:0,dir=(b>a)==up?(b>a?1:-1):(b>a?-1:1);if(up){if(b>a)x.arc(cx,CY,r,Math.PI,Math.PI+Math.PI*fr,false);else x.arc(cx,CY,r,0,-Math.PI*fr,true)}else{if(b>a)x.arc(cx,CY,r,Math.PI,Math.PI-Math.PI*fr,true);else x.arc(cx,CY,r,0,Math.PI*fr,false)}x.stroke()}
  x.globalAlpha=1;
  if(n!==lastN){lastN=n;var sh=A.slice(Math.max(0,n-9),n+1).join(', ');lab.innerHTML='<div class="hzbox" style="padding:.6vw 1.8vw;max-width:84vw"><div class="a" style="font-size:1.6vw">'+(n<N?(n+1)+'. adım · step '+(n+1)+': '+A[n]+(A[n+1]<A[n]?' − ':' + ')+(n+1)+' = '+A[n+1]:'Kural hiç değişmedi; desen kendiliğinden çıktı · The rule never changed — the pattern made itself')+'</div><div class="e" style="font-size:1.1vw">… '+sh+' — her yay bir adım; üstte tek, altta çift adımlar · each arc is one step: odd steps above, even steps below. Her sayı bir gün mutlaka gelir mi? Kimse kanıtlayamadı · Does every number eventually appear? Nobody has proved it</div></div>'}});return L};

/* Sieve of Eratosthenes on 1–200 */
W.hzsieve=function(L,it){grad(L,'#16202c','#04070b');var c=wCv(L),x=c.getContext('2d'),M=200,COLS=20,CW=84,RH=60,X0=(1920-COLS*CW)/2,Y0=262,PR=[2,3,5,7,11,13],COL={2:'#ff9e7a',3:'#8fd3c1',5:'#f2d06b',7:'#b9a3ff',11:'#7fb8ff',13:'#ff8fb8'},ev=[],box=T(L,'','bottom:12px',1),lastS='';
 T(L,'<div class="hzbox">'+hd('Zekice Düşünce · Clever Thinking — algoritma · algorithm','Eratosthenes’in kalburu: 1’den 200’e kadar bütün asal sayıları bul','The Sieve of Eratosthenes — find every prime from 1 to 200')+'</div>','top:12px',.4);
 var tt=2;PR.forEach(function(p){ev.push([tt,p,p,1]);tt+=1.2;for(var m=p*p;m<=M;m+=p){ev.push([tt,p,m,0]);tt+=.09}tt+=1});var TEND=tt,TOT=TEND+14;
 wLoop(L,function(t){var u=t%TOT,cross={},cur=0,i;for(i=0;i<ev.length&&ev[i][0]<=u;i++){var e=ev[i];if(e[3])cur=e[1];else if(!cross[e[2]])cross[e[2]]=e[1]}var done=u>=TEND;
  x.clearRect(0,0,1920,1080);x.textAlign='center';x.textBaseline='middle';
  for(var n=1;n<=M;n++){var r=Math.floor((n-1)/COLS),cc=(n-1)%COLS,X=X0+cc*CW+CW/2,Y=Y0+r*RH+RH/2,cr=cross[n],isP=!cr&&n>1&&(PR.indexOf(n)>=0||done||n<cur*cur);
   if(isP&&(done||PR.indexOf(n)>=0&&n<=cur)){x.fillStyle=done?'rgba(143,211,193,.28)':'rgba(255,255,255,.08)';x.beginPath();x.arc(X,Y,25,0,7);x.fill()}
   if(n==cur&&!done){x.strokeStyle=COL[cur];x.lineWidth=4;x.beginPath();x.arc(X,Y,27,0,7);x.stroke()}
   x.font=(isP&&done?'bold 30px':'28px')+' Georgia';x.fillStyle=n==1?'rgba(200,210,215,.25)':cr?'rgba(200,210,215,.22)':(done?'#f3f1ec':'rgba(243,241,236,.9)');x.fillText(n,X,Y);
   if(cr){x.strokeStyle=COL[cr];x.globalAlpha=.85;x.lineWidth=3;x.beginPath();x.moveTo(X-22,Y+14);x.lineTo(X+22,Y-14);x.stroke();x.globalAlpha=1}}
  var s=done?'done':cur?'p'+cur:'start';if(s!==lastS){lastS=s;var a,e;
   if(done){a='Geriye kalan 46 sayının hepsi asal!';e='The 46 numbers left are all prime. We could stop at 13, because 14 × 14 = 196 and every non-prime up to 200 has a factor smaller than 14';}
   else if(cur){a=cur+' asal. Şimdi '+cur+'’ün bütün katlarını sil';e=cur+' is prime — now cross out all its multiples (starting from '+cur+' × '+cur+' = '+cur*cur+', the smaller ones are already gone)';}
   else{a='1 asal değil. Silinmemiş ilk sayı: 2';e='1 is not prime. The first number not crossed out is 2';}
   box.innerHTML='<div class="hzbox" style="padding:.6vw 1.8vw;max-width:86vw"><div class="a" style="font-size:1.6vw">'+a+'</div><div class="e" style="font-size:1.1vw">'+e+'</div></div>'}});return L};

/* 20 questions: binary search finds any number from 1 to 1,000,000 in at most 20 yes/no questions */
W.hzhalve=function(L,it){grad(L,'#1a2230','#04060a');var c=wCv(L),x=c.getContext('2d'),M=1000000,lo,hi,sec,q,hist,t0,ST=it.st||2.3,state,box=T(L,'','bottom:12px',1),lastK='';
 T(L,'<div class="hzbox">'+hd('Zekice Düşünce · Clever Thinking — ikiye bölme · halving','1 ile 1.000.000 arasında bir sayı tuttum. Yalnızca evet/hayır sorularıyla kaç soruda bulursun?','I am thinking of a number from 1 to 1,000,000. With yes/no questions only, how many do you need?')+'</div>','top:12px',.4);
 function reset(t){lo=1;hi=M;sec=1+Math.floor(Math.random()*M);q=0;hist=[];t0=t;state=0}
 reset(0);var lastStep=-1;
 wLoop(L,function(t){var el=t-t0;if(state==0&&el>3){state=1;lastStep=t}
  if(state==1&&t-lastStep>ST){lastStep=t;if(lo<hi){var mid=Math.floor((lo+hi)/2),yes=sec>mid;q++;hist.push([mid,yes]);if(yes)lo=mid+1;else hi=mid}if(lo>=hi){state=2;t0=t}}
  if(state==2&&t-t0>9)reset(t);
  x.clearRect(0,0,1920,1080);var BX=160,BW=1600,Y1=360;
  x.fillStyle='rgba(220,230,235,.12)';x.fillRect(BX,Y1,BW,34);var a=(lo-1)/M*BW,b=hi/M*BW;x.fillStyle='rgba(255,158,122,.9)';x.fillRect(BX+a,Y1,Math.max(3,b-a),34);
  x.fillStyle='#c3cdd2';x.font='24px Helvetica';x.textAlign='left';x.fillText('1',BX,Y1+66);x.textAlign='right';x.fillText('1.000.000',BX+BW,Y1+66);
  var Y2=520,span=hi-lo+1;x.fillStyle='rgba(143,211,193,.18)';x.fillRect(BX,Y2,BW,70);x.strokeStyle='rgba(143,211,193,.8)';x.lineWidth=2;x.strokeRect(BX,Y2,BW,70);
  x.strokeStyle='rgba(255,158,122,.55)';x.beginPath();x.moveTo(BX+a,Y1+34);x.lineTo(BX,Y2);x.moveTo(BX+a+Math.max(3,b-a),Y1+34);x.lineTo(BX+BW,Y2);x.stroke();
  x.fillStyle='#f3f1ec';x.font='30px Georgia';x.textAlign='left';x.fillText(nTR(lo),BX,Y2+112);x.textAlign='right';x.fillText(nTR(hi),BX+BW,Y2+112);
  if(state==2){x.textAlign='center';x.font='bold 64px Georgia';x.fillStyle='#ff9e7a';x.fillText(nTR(sec),960,Y2+50)}else{x.strokeStyle='#f3f1ec';x.setLineDash([8,8]);x.beginPath();x.moveTo(BX+BW/2,Y2-14);x.lineTo(BX+BW/2,Y2+84);x.stroke();x.setLineDash([])}
  x.textAlign='center';x.font='40px Georgia';x.fillStyle='#8fd3c1';x.fillText('Soru · Question  '+q+' / 20',960,Y2+190);
  var k=state+':'+q;if(k!==lastK){lastK=k;var h=hist[hist.length-1],A,E;
   if(state==0){A='Tahmin et: 1.000 mi, 100 mü, 20 mi?';E='Guess first: 1,000 questions? 100? 20?'}
   else if(state==2){A='Buldum: '+nTR(sec)+' — yalnızca '+q+' soruda!';E='Found it in just '+q+' questions. Each question halves the candidates; 2 multiplied by itself 20 times is 1,048,576 — more than a million. Sözlükte bir kelime ararken de aynısını yaparsın · You do the same when you look up a word in a dictionary'}
   else if(h){A=nTR(h[0])+'’'+ablTR(h[0])+' büyük mü? → '+(h[1]?'Evet':'Hayır');E='Is it bigger than '+nTR(h[0]).replace(/\./g,',')+'? → '+(h[1]?'Yes':'No')+' · Kalan aday · candidates left: '+nTR(hi-lo+1)}
   else{A='Her soruda kalan aralığın tam ortasını sor';E='Always ask about the exact middle of what is left'}
   box.innerHTML='<div class="hzbox" style="padding:.6vw 1.8vw;max-width:86vw"><div class="a" style="font-size:1.6vw">'+A+'</div><div class="e" style="font-size:1.1vw">'+E+'</div></div>'}});return L};

/* motion aftereffect ("waterfall illusion", Addams 1834): stare at a turning spiral, then it stops — and seems to flow the other way */
W.hzwaterfall=function(L,it){L.style.background='#0b0d10';var c=wCv(L),x=c.getContext('2d'),CX=960,CY=585,R=330,RUN=it.run||28,STOP=it.stop||14,TOT=RUN+STOP+3,cd=T(L,'','bottom:12px',1),lastK='';
 T(L,'<div class="hzbox">'+hd('Göz Oyunu · Optical Illusion — hareket sonrası etkisi · motion aftereffect','Ortadaki kırmızı noktaya bak ve gözünü ayırma. Spiral durunca ne oluyor?','Stare at the red dot and keep looking. What happens when the spiral stops?')+'</div>','top:12px',.4);
 function spiral(rot){x.save();x.translate(CX,CY);x.beginPath();x.arc(0,0,R,0,7);x.fillStyle='#f2f2f2';x.fill();x.clip();x.rotate(rot);x.fillStyle='#111';var B=R/(4*Math.PI),k,th;
  for(k=0;k<2;k++){x.beginPath();for(th=0;th<=9*Math.PI;th+=.08){var r=B*th,a=th+k*Math.PI;x.lineTo(Math.cos(a)*r,Math.sin(a)*r)}for(th=9*Math.PI;th>=0;th-=.08){var r2=Math.max(0,B*(th-Math.PI/2)),a2=th+k*Math.PI;x.lineTo(Math.cos(a2-0)*r2,Math.sin(a2)*r2)}x.closePath();x.fill()}
  x.restore();x.strokeStyle='rgba(255,255,255,.25)';x.lineWidth=3;x.beginPath();x.arc(CX,CY,R+4,0,7);x.stroke();x.fillStyle='#e0302a';x.beginPath();x.arc(CX,CY,9,0,7);x.fill()}
 var rot=0,lt=0;
 wLoop(L,function(t){var u=t%TOT,dt=Math.min(.1,t-lt);lt=t;if(u>1.5&&u<RUN)rot+=dt*2.2;x.clearRect(0,0,1920,1080);spiral(rot);
  var ph=u<1.5?'w':u<RUN?'r'+Math.ceil(RUN-u):u<RUN+STOP?'s':'e';if(ph!==lastK){lastK=ph;var A,E;
   if(ph[0]=='r'){A='Noktaya bak… '+Math.ceil(RUN-u);E='Keep looking at the dot… '+Math.ceil(RUN-u)}
   else if(ph=='s'){A='Spiral durdu. Ama sana tersine akıyor gibi mi görünüyor?';E='The spiral has stopped — yet does it seem to flow the other way? Motion cells in your brain got tired of one direction, so for a few seconds the balance tips the other way. First described in 1834 at the Falls of Foyers, Scotland: after watching the waterfall, the rocks seemed to rise'}
   else{A='Hazır mısın? · Ready?';E='Bir kez daha · One more time'}
   cd.innerHTML='<div class="hzbox" style="padding:.6vw 1.8vw;max-width:86vw"><div class="a" style="font-size:1.6vw">'+A+'</div><div class="e" style="font-size:1.1vw">'+E+'</div></div>'}});return L};

/* Troxler fading (1804): soft, blurry colour spots vanish while you fix your gaze on the centre */
W.hztroxler=function(L,it){L.style.background='#b9b6c0';var c=wCv(L),x=c.getContext('2d'),CX=960,CY=590,B=[],i,cols=['255,120,150','120,170,255','140,215,160','255,190,110','190,140,255','110,210,220','255,150,120','150,190,120'];
 for(i=0;i<8;i++){var a=i/8*6.2832+.2;B.push([CX+Math.cos(a)*300,CY+Math.sin(a)*230,cols[i]])}
 T(L,'<div class="hzbox">'+hd('Göz Oyunu · Optical Illusion','Ortadaki küçük artıya bak ve gözlerini hiç kıpırdatma. Renkli lekelere ne oluyor?','Fix your eyes on the little cross and do not move them. What happens to the coloured spots?')+'</div>','top:12px',.4);
 T(L,'<div class="hzbox"><div class="a" style="font-size:1.7vw">Lekeler yavaş yavaş griye karışıp kayboluyor!</div><div class="e" style="font-size:1.2vw">The spots slowly melt into the grey and disappear. The eye stops reporting things that do not change and have soft edges — the brain fills the gap with the background. Gözünü bir an oynat: hepsi geri gelir · Move your eyes for a moment and they all come back (Troxler fading, 1804)</div></div>','bottom:12px',26);
 x.fillStyle='#b9b6c0';x.fillRect(0,0,1920,1080);for(i=0;i<B.length;i++){var g=x.createRadialGradient(B[i][0],B[i][1],0,B[i][0],B[i][1],120);g.addColorStop(0,'rgba('+B[i][2]+',.55)');g.addColorStop(.5,'rgba('+B[i][2]+',.25)');g.addColorStop(1,'rgba('+B[i][2]+',0)');x.fillStyle=g;x.beginPath();x.arc(B[i][0],B[i][1],120,0,7);x.fill()}
 x.strokeStyle='#222';x.lineWidth=4;x.beginPath();x.moveTo(CX-16,CY);x.lineTo(CX+16,CY);x.moveTo(CX,CY-16);x.lineTo(CX,CY+16);x.stroke();return L};

/* calm night: mist drifting through dark, layered highland hills with a few warm house lights (illustration) */
W.hzyayla=function(L,it){var c=wCv(L),x=c.getContext('2d'),S=stars(170),LAY=[],i,j,HL=[];
 function rnd(s){return function(){s=(s*9301+49297)%233280;return s/233280}}var R=rnd(7);
 for(i=0;i<5;i++){var base=430+i*120,amp=70-i*6,ph1=R()*6,ph2=R()*6,pts=[];for(j=0;j<=96;j++){var xx=j*20;pts.push(base-amp*Math.sin(xx/310+ph1)-amp*.5*Math.sin(xx/123+ph2)-18*Math.sin(xx/47+i))}LAY.push(pts)}
 for(i=0;i<14;i++){var li=1+Math.floor(R()*4),jj=2+Math.floor(R()*92);HL.push([jj*20,LAY[li][jj]+14+R()*30,li,R()*6.28])}
 T(L,hd('Yaylada Gece · Night in the Highlands — çizim · illustration, hayal ürünü · imagined (sakin · calm)','Sis, sırtların arasından usulca geçiyor; uzakta birkaç sıcak pencere','Mist drifts softly between the ridges; a few warm windows far away'),'top:44px',2);
 T(L,'<div class="sm" style="font-size:1.25vw;color:#cdd6dc">Gece hava soğuyunca vadilerdeki nem yoğunlaşır ve sis çukurlara çöker. Sabah güneşi onu yavaşça yukarı, bir bulut denizine dönüştürür<br><i>When the night air cools, moisture in the valleys condenses and the fog settles into the hollows. The morning sun slowly lifts it into a sea of clouds</i></div>','bottom:40px',9);
 wLoop(L,function(t){var g=x.createLinearGradient(0,0,0,700);g.addColorStop(0,'#03050c');g.addColorStop(1,'#152033');x.fillStyle=g;x.fillRect(0,0,1920,1080);drawStars(x,S.filter(function(s){return s[1]<420}),t);
  x.fillStyle='rgba(235,238,245,.92)';x.beginPath();x.arc(1480,170,34,0,7);x.fill();x.fillStyle='#070b16';x.beginPath();x.arc(1494,160,32,0,7);x.fill();
  for(var l=0;l<LAY.length;l++){var p=LAY[l],sh=10+l*5;x.fillStyle='rgb('+(sh)+','+(sh+5)+','+(sh+14)+')';x.beginPath();x.moveTo(0,1080);for(var k=0;k<p.length;k++)x.lineTo(k*20,p[k]);x.lineTo(1920,1080);x.closePath();x.fill();
   for(var h=0;h<HL.length;h++)if(HL[h][2]==l){var fl=.75+.25*Math.sin(t*.8+HL[h][3]),gl=x.createRadialGradient(HL[h][0],HL[h][1],0,HL[h][0],HL[h][1],22);gl.addColorStop(0,'rgba(255,214,160,'+(.55*fl).toFixed(2)+')');gl.addColorStop(1,'rgba(255,214,160,0)');x.fillStyle=gl;x.beginPath();x.arc(HL[h][0],HL[h][1],22,0,7);x.fill();x.fillStyle='rgba(255,226,180,'+(.9*fl).toFixed(2)+')';x.fillRect(HL[h][0]-2,HL[h][1]-2,4,4)}
   if(l<LAY.length-1){for(var m=0;m<4;m++){var w=900,mx=((t*(6+l*2)+m*640+l*300)%(1920+w))-w/2,my=p[48]+40+m%2*20,mg=x.createRadialGradient(mx,my,0,mx,my,w/2);mg.addColorStop(0,'rgba(170,185,205,.16)');mg.addColorStop(1,'rgba(170,185,205,0)');x.fillStyle=mg;x.save();x.translate(mx,my);x.scale(1,.18);x.translate(-mx,-my);x.beginPath();x.arc(mx,my,w/2,0,7);x.fill();x.restore()}}}});return L};


/* ---------- v75 additions: hzpack (living art), hzbenford hzbirthday (clever thinking), hzsilence hzsfm (illusions), hztren (calm night) ---------- */
/* circle packing: circles appear where there is room and grow until they touch a neighbour */
W.hzpack=function(L,it){grad(L,'#12202a','#03060a');var c=wCv(L),x=c.getContext('2d'),CX=960,CY=610,R=330,C,G,fails,st,hold,T0,SP,box=T(L,'','bottom:12px',1),last=-1;
 T(L,'<div class="hzbox">'+hd('Yaşayan Sanat · Living Art — geometri · geometry','Daire doldurma: boş yer bulan her daire, bir komşusuna değene kadar büyüyor','Circle packing — every circle that finds room grows until it touches a neighbour')+'</div>','top:12px',.4);
 function reset(){C=[];G=[];fails=0;st=0;hold=0;T0=-1;SP=0;x.clearRect(0,0,1920,1080);x.strokeStyle='rgba(200,225,230,.25)';x.lineWidth=2;x.beginPath();x.arc(CX,CY,R+3,0,7);x.stroke()}
 function free(px,py){for(var i=0;i<C.length;i++){var d=Math.sqrt((px-C[i][0])*(px-C[i][0])+(py-C[i][1])*(py-C[i][1]));if(d<C[i][2]+2)return false}return true}
 function col(r,h){var l=Math.max(34,Math.min(72,78-r*.55));return 'hsl('+h+','+(55+Math.min(25,r*.3)).toFixed(0)+'%,'+l.toFixed(0)+'%)'}
 reset();
 wLoop(L,function(t){if(hold){if(t-hold>9){x.fillStyle='rgba(3,6,10,.08)';x.fillRect(0,0,1920,1080);if(t-hold>13)reset()}}
  else{if(T0<0)T0=t;SP+=Math.min(4,.1+(t-T0)*.07);while(SP>=1){SP--;for(var a=0;a<40;a++){var an=Math.random()*6.2832,rr=Math.sqrt(Math.random())*R,px=CX+Math.cos(an)*rr,py=CY+Math.sin(an)*rr;if(free(px,py)){var hu=[188,200,168,12,340,262,210][Math.floor(Math.random()*7)];var cc=[px,py,1,1,hu];C.push(cc);G.push(cc);fails=0;break}else fails++}}
   for(var i=G.length-1;i>=0;i--){var g=G[i],stop=Math.sqrt((g[0]-CX)*(g[0]-CX)+(g[1]-CY)*(g[1]-CY))+g[2]+1.2>=R;
    if(!stop)for(var j=0;j<C.length;j++){var o=C[j];if(o===g)continue;var d=Math.sqrt((g[0]-o[0])*(g[0]-o[0])+(g[1]-o[1])*(g[1]-o[1]));if(d<g[2]+o[2]+2.4){stop=true;break}}
    if(stop||g[2]>150){g[3]=0;G.splice(i,1)}else g[2]+=1.3;
    x.fillStyle=col(g[2],g[4]);x.beginPath();x.arc(g[0],g[1],g[2],0,7);x.fill()}
   if(fails>1600||C.length>1800){hold=t}}
  var n=C.length;if(n!==last&&(Math.floor(t*3)!==st||hold)){st=Math.floor(t*3);last=n;box.innerHTML='<div class="hzbox" style="padding:.6vw 1.8vw;max-width:86vw"><div class="a" style="font-size:1.6vw">Daire · Circles: '+nTR(n)+(hold?' — yer kalmadı · no room left':'')+'</div><div class="e" style="font-size:1.08vw">Kimse büyük resmi planlamıyor; her daire yalnızca çevresine bakıyor. Doğada köpük, hücreler, zürafa benekleri ve kurumuş çamur çatlakları da benzer bir “yer kapma” oyunuyla oluşur · Nobody plans the big picture — each circle only looks at its neighbours. Foam, cells, giraffe patches and dried-mud cracks form through a similar race for space</div></div>'}});return L};

/* Benford's law: leading digits of 2^n, Fibonacci numbers and n! pile up on 1 (about 30%) */
W.hzbenford=function(L,it){grad(L,'#1a2230','#04060a');var c=wCv(L),x=c.getContext('2d'),SRC=[['2ⁿ','2’nin kuvvetleri · powers of 2'],['Fib','Fibonacci sayıları · Fibonacci numbers'],['n!','faktöriyeller · factorials']],box=T(L,'','bottom:12px',1),last=0,si=-1,n,cnt,acc,recent,lf;
 var L2=Math.log(2)/Math.LN10,PHI=Math.log((1+Math.sqrt(5))/2)/Math.LN10,S5=Math.log(Math.sqrt(5))/Math.LN10;
 T(L,'<div class="hzbox">'+hd('Zekice Düşünce · Clever Thinking — Benford yasası · Benford’s law','Dev sayıların ilk rakamı nedir? 1’den 9’a hepsi eşit şansla mı gelir?','What is the first digit of huge numbers? Does every digit from 1 to 9 come up equally often?')+'</div>','top:12px',.4);
 function lg(k){if(si==0)return k*L2;if(si==1)return k*PHI-S5;lf+=Math.log(k)/Math.LN10;return lf}
 function start(i){si=i;n=0;cnt=[0,0,0,0,0,0,0,0,0,0];acc=0;recent=[];lf=0}
 function step(){n++;var v=lg(n),e=Math.floor(v),m=Math.pow(10,v-e);if(m>=9.9995){m=1;e++}var d=Math.floor(m);if(si==1&&n<3){d=1;m=1;e=0}cnt[d]++;recent.unshift([n,m,e,d]);if(recent.length>7)recent.pop()}
 wLoop(L,function(t){var ph=Math.floor(t/38)%3,u=t%38;if(ph!==si)start(ph);acc+=u<8?.06:u<16?.35:2.5;while(acc>=1){acc--;step()}
  x.clearRect(0,0,1920,1080);var X0=760,BW=110,BASE=860,H=520,tot=0,d;for(d=1;d<10;d++)tot+=cnt[d];
  x.textAlign='center';for(d=1;d<10;d++){var bx=X0+(d-1)*BW,p=tot?cnt[d]/tot:0,ex=Math.log(1+1/d)/Math.LN10;x.fillStyle=d==1?'#ff9e7a':'#8fd3c1';x.fillRect(bx+14,BASE-p*H/.35,BW-28,p*H/.35);
   x.strokeStyle='#f3f1ec';x.lineWidth=3;x.setLineDash([10,7]);x.beginPath();x.moveTo(bx+6,BASE-ex*H/.35);x.lineTo(bx+BW-6,BASE-ex*H/.35);x.stroke();x.setLineDash([]);
   x.fillStyle='#f3f1ec';x.font='bold 38px Georgia';x.fillText(String(d),bx+BW/2,BASE+46);x.font='24px Helvetica,Arial';x.fillStyle='#c3cdd2';x.fillText('%'+(p*100).toFixed(1),bx+BW/2,BASE-p*H/.35-14)}
  x.strokeStyle='rgba(255,255,255,.35)';x.lineWidth=2;x.beginPath();x.moveTo(X0,BASE);x.lineTo(X0+9*BW,BASE);x.stroke();
  x.textAlign='left';x.font='26px Helvetica,Arial';x.fillStyle='#8fd3c1';x.fillText(SRC[si][1],110,330);x.font='22px Helvetica,Arial';x.fillStyle='#c3cdd2';x.fillText('kesikli çizgi = Benford’un tahmini · dashed line = Benford’s prediction',X0,BASE+96);
  for(var r=0;r<recent.length;r++){var q=recent[r],lab=si==0?'2^'+q[0]:si==1?'F('+q[0]+')':q[0]+'!',ms=q[1].toFixed(3).replace('.',','),y=390+r*58;x.globalAlpha=1-r*.12;x.font='30px Georgia';x.fillStyle='#f3f1ec';x.fillText(lab+' ≈ ',110,y);var w0=x.measureText(lab+' ≈ ').width;x.fillStyle='#ff9e7a';x.font='bold 30px Georgia';x.fillText(ms.charAt(0),110+w0,y);var w1=x.measureText(ms.charAt(0)).width;x.font='30px Georgia';x.fillStyle='#f3f1ec';x.fillText(ms.slice(1)+' × 10^'+q[2],110+w0+w1,y)}x.globalAlpha=1;
  if(t-last>.5){last=t;box.innerHTML='<div class="hzbox" style="padding:.6vw 1.8vw;max-width:88vw"><div class="a" style="font-size:1.55vw">Sayı · Numbers: '+nTR(tot)+' — “1” ile başlayan · starting with 1: %'+(tot?cnt[1]/tot*100:0).toFixed(1)+' (Benford: %30,1)</div><div class="e" style="font-size:1.05vw">Büyüyerek çoğalan her şeyde 1’den 2’ye çıkmak, 9’dan 10’a çıkmaktan çok daha uzun sürer; bu yüzden ilk rakam en çok 1 olur. Nehir uzunlukları, nüfuslar ve faturalar da böyle; vergi müfettişleri sahte rakamları bu yasayla yakalar · Anything that grows by multiplying spends far longer going from 1 to 2 than from 9 to 10, so 1 leads most often. River lengths, populations and invoices follow it too — auditors use it to catch invented figures</div></div>'}});return L};

/* birthday paradox: people enter a room until two share a birthday; repeat and count */
W.hzbirthday=function(L,it){grad(L,'#1d2330','#05070b');var c=wCv(L),x=c.getContext('2d'),CX=700,CY=600,R=330,MO=['Oca','Şub','Mar','Nis','May','Haz','Tem','Ağu','Eyl','Eki','Kas','Ara'],MD=[31,28,31,30,31,30,31,31,30,31,30,31],tr=null,TR=0,LE23=0,HIST=[],acc=0,box=T(L,'','bottom:12px',1),last=0,pause=0;
 for(var i=0;i<=80;i++)HIST.push(0);
 T(L,'<div class="hzbox">'+hd('Zekice Düşünce · Clever Thinking — doğum günü paradoksu · the birthday paradox','Bir odada kaç kişi olmalı ki iki kişinin doğum günü aynı gün olsun? (tahmin et!)','How many people must be in a room before two share a birthday? (make a guess!)')+'</div>','top:12px',.4);
 function ang(d){return d/365*6.2832-1.5708}
 function newT(){tr={days:{},list:[],hit:-1}}
 function add(){var d=Math.floor(Math.random()*365);if(tr.days[d]!=null){tr.hit=d;tr.list.push(d);TR++;var k=tr.list.length;HIST[Math.min(80,k)]++;if(k<=23)LE23++;return true}tr.days[d]=tr.list.length;tr.list.push(d);return false}
 newT();
 wLoop(L,function(t){var slow=TR<3,dt=1/60;
  if(pause){if(t>pause){pause=0;newT()}}else{acc+=slow?.05:TR<12?.3:6;while(acc>=1&&!pause){acc--;if(add()){pause=t+(slow?3.2:TR<12?1:.05);break}}}
  x.clearRect(0,0,1920,1080);x.lineWidth=2;var day=0;for(var m=0;m<12;m++){var a0=ang(day),a1=ang(day+MD[m]);x.strokeStyle=m%2?'rgba(143,211,193,.35)':'rgba(195,205,210,.25)';x.lineWidth=16;x.beginPath();x.arc(CX,CY,R,a0+.004,a1-.004);x.stroke();
   var am=(a0+a1)/2;x.fillStyle='#c3cdd2';x.font='22px Helvetica,Arial';x.textAlign='center';x.fillText(MO[m],CX+Math.cos(am)*(R+44),CY+Math.sin(am)*(R+44)+8);day+=MD[m]}
  for(var k=0;k<tr.list.length;k++){var d=tr.list[k],a=ang(d+.5),hit=d==tr.hit,rr=R-30-(hit&&k==tr.list.length-1?24:0);x.fillStyle=hit?'#ff9e7a':'#e8f1f2';x.beginPath();x.arc(CX+Math.cos(a)*rr,CY+Math.sin(a)*rr,hit?11:7,0,7);x.fill();if(hit){x.strokeStyle='#ff9e7a';x.lineWidth=3;x.beginPath();x.moveTo(CX,CY);x.lineTo(CX+Math.cos(a)*(R-20),CY+Math.sin(a)*(R-20));x.stroke()}}
  x.fillStyle='#f3f1ec';x.font='bold 96px Georgia';x.textAlign='center';x.fillText(String(tr.list.length),CX,CY+20);x.font='26px Helvetica,Arial';x.fillStyle='#c3cdd2';x.fillText(tr.hit>=0?'kişide eşleşme! · people — a match!':'kişi odada · people in the room',CX,CY+64);
  var HX=1170,HB=880,HW=660,mx=1;for(var j=0;j<=80;j++)if(HIST[j]>mx)mx=HIST[j];for(j=1;j<=80;j++){var h=HIST[j]/mx*380;x.fillStyle=j<=23?'#ff9e7a':'#8fd3c1';x.fillRect(HX+(j-1)*HW/80,HB-h,HW/80-1.5,h)}
  x.strokeStyle='#f3f1ec';x.setLineDash([8,6]);x.beginPath();x.moveTo(HX+22.5*HW/80,HB-400);x.lineTo(HX+22.5*HW/80,HB+6);x.stroke();x.setLineDash([]);x.font='22px Helvetica,Arial';x.textAlign='left';x.fillStyle='#c3cdd2';x.fillText('23',HX+21*HW/80,HB+32);x.fillText('eşleşmenin olduğu kişi sayısı · group size at the first match',HX,HB+64);
  if(t-last>.4){last=t;box.innerHTML='<div class="hzbox" style="padding:.6vw 1.8vw;max-width:88vw"><div class="a" style="font-size:1.55vw">Deneme · Trials: '+nTR(TR)+(TR?' — 23 kişi veya daha azında eşleşme · match with 23 people or fewer: %'+(LE23/TR*100).toFixed(1):'')+'</div>'+(TR>20?'<div class="e" style="font-size:1.05vw">Sadece 23 kişi yeter: yaklaşık %50 ihtimal! 70 kişide %99,9. Sır şu: önemli olan senin doğum günün değil, her ikili — 23 kişide 253 farklı ikili var · Just 23 people give about a 50% chance, and 70 give 99.9%. The secret: it is not about your birthday but about every pair — 23 people make 253 different pairs</div>':'')+'</div>'}});return L};

/* silencing illusion (Suchow & Alvarez 2011): dots keep changing colour, but the changes seem to stop when the ring spins */
W.hzsilence=function(L,it){L.style.background='#0b0d12';var c=wCv(L),x=c.getContext('2d'),CX=960,CY=600,D=[],i,rot=0,lt=0,box=T(L,'','bottom:12px',1),lastK='',STILL=9,SPIN=11;
 for(i=0;i<110;i++){var a=Math.random()*6.2832,r=200+Math.random()*190;D.push([a,r,Math.random()*360,.6+Math.random()*.5])}
 T(L,'<div class="hzbox">'+hd('Göz Oyunu · Optical Illusion — susturma yanılsaması · silencing','Ortadaki beyaz noktaya bak. Halkadaki noktaların rengi hiç durmadan değişiyor…','Look at the white dot in the middle. The dots in the ring never stop changing colour…')+'</div>','top:12px',.4);
 wLoop(L,function(t){var dt=Math.min(.1,t-lt);lt=t;var u=t%(STILL+SPIN),spin=u>=STILL;if(spin)rot+=dt*2.6*Math.min(1,(u-STILL)/1.2);x.clearRect(0,0,1920,1080);
  for(var k=0;k<D.length;k++){var d=D[k];d[2]=(d[2]+dt*95*d[3])%360;var a=d[0]+rot;x.fillStyle='hsl('+d[2].toFixed(0)+',80%,58%)';x.beginPath();x.arc(CX+Math.cos(a)*d[1],CY+Math.sin(a)*d[1],15,0,7);x.fill()}
  x.fillStyle='#fff';x.beginPath();x.arc(CX,CY,7,0,7);x.fill();
  var K=spin?'s':'w';if(K!==lastK){lastK=K;box.innerHTML='<div class="hzbox" style="padding:.6vw 1.8vw;max-width:86vw">'+(spin?'<div class="a" style="font-size:1.6vw">Halka dönüyor: renkler sanki donup kaldı!</div><div class="e" style="font-size:1.08vw">The ring is spinning — and the colours seem to freeze. They are changing exactly as fast as before. When things move quickly, the brain stops noticing their other changes (Suchow &amp; Alvarez, 2011)</div>':'<div class="a" style="font-size:1.6vw">Halka duruyor: renk değişimini açıkça görüyorsun</div><div class="e" style="font-size:1.08vw">The ring is still — you can clearly see the colours changing. Gözünü noktadan ayırma; birazdan halka dönecek · Keep your eyes on the dot; the ring will start spinning soon</div>')+'</div>'}});return L};

/* kinetic depth effect: flat dots that become a spinning 3D sphere — which way is it turning? */
W.hzsfm=function(L,it){L.style.background='#07090d';var c=wCv(L),x=c.getContext('2d'),CX=960,CY=600,R=320,P=[],i,box=T(L,'','bottom:12px',1),lastK='',AMB=22,REV=12;
 for(i=0;i<700;i++){var z=Math.random()*2-1,a=Math.random()*6.2832,s=Math.sqrt(1-z*z);P.push([s*Math.cos(a),z,s*Math.sin(a)])}
 T(L,'<div class="hzbox">'+hd('Göz Oyunu · Optical Illusion — hareketten derinlik · kinetic depth','Düz bir ekranda düz noktalar. Peki neden bir küre görüyorsun ve hangi yöne dönüyor?','Flat dots on a flat screen — so why do you see a sphere, and which way is it turning?')+'</div>','top:12px',.4);
 wLoop(L,function(t){var th=t*.55,co=Math.cos(th),sn=Math.sin(th),u=t%(AMB+REV),rev=u>=AMB;x.clearRect(0,0,1920,1080);
  for(var k=0;k<P.length;k++){var p=P[k],X=p[0]*co+p[2]*sn,Z=-p[0]*sn+p[2]*co;x.fillStyle=rev?(Z>0?'#ff9e7a':'rgba(143,211,193,.55)'):'#e9eef0';x.fillRect(CX+X*R-3,CY+p[1]*R-3,6,6)}
  var K=rev?'r':'a';if(K!==lastK){lastK=K;box.innerHTML='<div class="hzbox" style="padding:.6vw 1.8vw;max-width:86vw">'+(rev?'<div class="a" style="font-size:1.6vw">Şimdi öndeki noktalar turuncu: küre sağa doğru dönüyor</div><div class="e" style="font-size:1.08vw">Now the front dots are coral — the sphere turns to the right. Without that colour there was no clue at all: your brain built the 3D shape from motion alone, and either direction was a valid answer, so it can flip on its own</div>':'<div class="a" style="font-size:1.6vw">Birkaç saniye bak: dönüş yönü kendiliğinden tersine dönebilir</div><div class="e" style="font-size:1.08vw">Watch for a few seconds — the direction may flip on its own. Every dot is the same size and colour, with no shading or perspective. The 3D sphere exists only in your brain (kinetic depth effect, 1953)</div>')+'</div>'}});return L};

/* calm night: a lit night train glides along a lakeside under the mountains (illustration) */
W.hztren=function(L,it){var c=wCv(L),x=c.getContext('2d'),S=stars(190),M=[],i,j,HY=700,TY=652,NC=8,CW=150,TOT=it.tot||70;
 function rnd(s){return function(){s=(s*9301+49297)%233280;return s/233280}}var R=rnd(11);
 for(i=0;i<3;i++){var pts=[],b=420+i*90,amp=150-i*40,p1=R()*6,p2=R()*6;for(j=0;j<=96;j++){var xx=j*20;pts.push(Math.min(TY-6,b-amp*Math.abs(Math.sin(xx/(380-i*60)+p1))-amp*.35*Math.sin(xx/97+p2)))}M.push(pts)}
 var WIN=[];for(i=0;i<NC;i++){var w=[];for(j=0;j<6;j++)w.push(R()<.82?.75+R()*.25:0);WIN.push(w)}
 T(L,hd('Gece Treni · The Night Train — çizim · illustration, hayal ürünü · imagined (sakin · calm)','Dağların eteğinde, gölün kıyısından sessizce geçen ışıklı bir tren','A lit train gliding quietly along the lake beneath the mountains'),'top:44px',2);
 T(L,'<div class="sm" style="font-size:1.25vw;color:#cdd6dc">Durgun su, ışığı neredeyse hiç kaybetmeden geri yansıtır; bu yüzden gece gölleri gökyüzünü ikinci kez gösterir<br><i>Still water reflects light back with almost no loss — which is why lakes at night show the sky a second time</i></div>','bottom:40px',9);
 wLoop(L,function(t){var g=x.createLinearGradient(0,0,0,HY);g.addColorStop(0,'#02040b');g.addColorStop(1,'#14203a');x.fillStyle=g;x.fillRect(0,0,1920,HY);drawStars(x,S.filter(function(s){return s[1]<520}),t);
  x.fillStyle='rgba(236,240,248,.94)';x.beginPath();x.arc(420,190,30,0,7);x.fill();
  for(var l=0;l<M.length;l++){var sh=8+l*6;x.fillStyle='rgb('+sh+','+(sh+5)+','+(sh+13)+')';x.beginPath();x.moveTo(0,HY);for(var k=0;k<M[l].length;k++)x.lineTo(k*20,M[l][k]);x.lineTo(1920,HY);x.closePath();x.fill()}
  x.fillStyle='#070a12';x.fillRect(0,TY,1920,HY-TY);x.fillStyle='rgba(80,90,110,.5)';x.fillRect(0,TY+12,1920,2);
  var u=(t%TOT)/TOT,X0=-NC*CW-60+u*(1920+NC*CW+200);
  for(var cI=0;cI<NC;cI++){var cx=X0+cI*CW;if(cx>1940||cx<-CW)continue;x.fillStyle='#0d1119';x.fillRect(cx,TY-34,CW-10,40);
   for(var wI=0;wI<6;wI++){var a=WIN[cI][wI];if(!a)continue;var fl=a*(.92+.08*Math.sin(t*1.7+cI*3+wI));x.fillStyle='rgba(255,220,170,'+fl.toFixed(2)+')';x.fillRect(cx+10+wI*22,TY-26,14,12)}}
  if(X0+NC*CW>0&&X0<1920){var hx=X0+NC*CW-10,hg=x.createRadialGradient(hx+30,TY-14,0,hx+30,TY-14,160);hg.addColorStop(0,'rgba(240,240,225,.35)');hg.addColorStop(1,'rgba(240,240,225,0)');x.fillStyle=hg;x.fillRect(hx-20,TY-170,360,320)}
  var wg=x.createLinearGradient(0,HY,0,1080);wg.addColorStop(0,'#0c1426');wg.addColorStop(1,'#02040a');x.fillStyle=wg;x.fillRect(0,HY,1920,380);
  x.save();x.globalAlpha=.42;x.translate(0,2*HY);x.scale(1,-1);x.drawImage(c,0,320,1920,HY-320,0,320,1920,HY-320);x.restore();
  for(var yy=HY+4;yy<1080;yy+=6){x.fillStyle='rgba(2,4,10,.32)';x.fillRect(0,yy+Math.sin(t*.8+yy*.3)*1.5,1920,2.5)}});return L};

/* ---------- v76 additions: hzclifford (living art), hzperc hzstop (clever thinking), hzneon hzocclude (illusions), hzkoy (calm night) ---------- */
/* Clifford strange attractor: one simple rule repeated millions of times; points pile up into a silk-like shape. Morphs through 4 parameter sets */
W.hzclifford=function(L,it){L.style.background='#04060b';var c=wCv(L),x=c.getContext('2d'),RW=960,RH=540,off=document.createElement('canvas'),ox,img,H,px=.1,py=.1,P=[[-1.4,1.6,1,.7],[1.7,1.7,.6,1.2],[-1.7,1.3,-.1,-1.21],[-1.8,-2,-.5,-.9]],COL=[[120,200,230],[240,150,120],[150,220,190],[190,170,240]],pi=-1,T0=0,DUR=it.dur||24,mx=1,box=T(L,'','bottom:12px',1),lr=0,cnt=0;
 off.width=RW;off.height=RH;ox=off.getContext('2d');img=ox.createImageData(RW,RH);H=new Float32Array(RW*RH);
 T(L,'<div class="hzbox">'+hd('Yaşayan Sanat · Living Art — tuhaf çekici · strange attractor','Tek bir basit kural, milyonlarca kez tekrarlanıyor: her nokta bir öncekinden hesaplanıyor','One simple rule, repeated millions of times — every point is calculated from the one before')+'</div>','top:12px',.4);
 function start(i,t){pi=i;T0=t;for(var k=0;k<H.length;k++)H[k]=0;mx=1;cnt=0;px=.1;py=.1}
 wLoop(L,function(t){var ph=Math.floor(t/DUR)%P.length;if(ph!==pi)start(ph,t);var p=P[pi],a=p[0],b=p[1],cc=p[2],d=p[3],sx=RW/(2*(1+Math.abs(cc))+.2),sy=RH/(2*(1+Math.abs(d))+.2),s=Math.min(sx,sy)*.95,u=t-T0,n=u<2?4000:u<DUR-4?26000:0;
  budget(9,function(){for(var k=0;k<2000&&n>0;k++,n--){var nx=Math.sin(a*py)+cc*Math.cos(a*px),ny=Math.sin(b*px)+d*Math.cos(b*py);px=nx;py=ny;var ix=(RW/2+px*s)|0,iy=(RH/2+py*s)|0;if(ix>=0&&iy>=0&&ix<RW&&iy<RH){var v=++H[iy*RW+ix];if(v>mx)mx=v}cnt++}return n>0});
  if(t-lr>.35){lr=t;var D=img.data,lm=Math.log(mx+1),C=COL[pi],fade=u>DUR-3?Math.max(0,(DUR-u)/3):Math.min(1,u/1.5);for(var k=0;k<H.length;k++){var v=H[k]?Math.pow(Math.log(H[k]+1)/lm,.8)*fade:0,o=k*4;D[o]=Math.min(255,C[0]*v*1.25+v*v*60);D[o+1]=Math.min(255,C[1]*v*1.2+v*v*60);D[o+2]=Math.min(255,C[2]*v*1.15+v*v*60);D[o+3]=255}ox.putImageData(img,0,0);x.fillStyle='#04060b';x.fillRect(0,0,1920,1080);x.drawImage(off,0,140,1920,1080*.86-20);
   box.innerHTML='<div class="hzbox" style="padding:.6vw 1.8vw;max-width:88vw"><div class="a" style="font-size:1.45vw">x′ = sin('+a+'·y) + '+cc+'·cos('+a+'·x) &nbsp; y′ = sin('+b+'·x) + '+d+'·cos('+b+'·y) — nokta · points: '+nTR(cnt)+'</div><div class="e" style="font-size:1.05vw">Kural rastgele değil, ama sonuç hiç tekrar etmiyor: noktalar sonsuza dek aynı şeklin üzerinde dolaşıyor ve asla aynı yere iki kez dönmüyor. Dört sayıdan birini biraz değiştir, bambaşka bir şekil doğar · Nothing here is random, yet it never repeats — the points wander over the same shape forever and never land in the same place twice. Nudge one of the four numbers and a completely different shape is born</div></div>'}});return L};

/* percolation: a forest with tree density p; a fire lit on the left edge. Below ~59.3% it dies out, above it crosses the whole forest */
W.hzperc=function(L,it){grad(L,'#18221c','#040705');var c=wCv(L),x=c.getContext('2d'),CW=12,NX=140,NY=54,X0=(1920-NX*CW)/2,Y0=250,G,FR,P=[.45,.55,.593,.62,.7],pi=-1,T0=0,DUR=it.dur||19,burn,trees,acc,done,box=T(L,'','bottom:12px',1),lk='';
 T(L,'<div class="hzbox">'+hd('Zekice Düşünce · Clever Thinking — süzülme eşiği · percolation','Ağaçların bir kısmı kesilmiş bir orman. Sol kenarda yangın çıkıyor: karşıya ulaşır mı?','A forest with some trees missing. A fire starts on the left edge — will it reach the other side?')+'</div>','top:12px',.4);
 function start(i,t){pi=i;T0=t;G=new Uint8Array(NX*NY);FR=[];burn=0;trees=0;acc=0;done=0;for(var k=0;k<NX*NY;k++)if(Math.random()<P[pi]){G[k]=1;trees++}for(var y=0;y<NY;y++)if(G[y*NX]){G[y*NX]=2;FR.push(y*NX)}x.clearRect(0,0,1920,1080);for(k=0;k<NX*NY;k++)if(G[k])draw(k)}
 function draw(k){var gx=k%NX,gy=(k/NX)|0,v=G[k];x.fillStyle=v==1?'#3f7a4a':v==2?'#ff8a3d':'#3a2a24';x.fillRect(X0+gx*CW+1,Y0+gy*CW+1,CW-2,CW-2)}
 function step(){var NF=[];for(var i=0;i<FR.length;i++){var k=FR[i],gx=k%NX;G[k]=3;draw(k);burn++;var nb=[gx>0?k-1:-1,gx<NX-1?k+1:-1,k-NX,k+NX];for(var j=0;j<4;j++){var m=nb[j];if(m>=0&&m<NX*NY&&G[m]==1){G[m]=2;draw(m);NF.push(m);if(m%NX==NX-1)done=1}}}FR=NF}
 wLoop(L,function(t){var ph=Math.floor(t/DUR)%P.length;if(ph!==pi)start(ph,t);acc+=.6;while(acc>=1&&FR.length){acc--;step()}
  var pct=trees?burn/trees*100:0,st=FR.length?'yanıyor… · burning…':done?'yangın karşıya ulaştı · the fire crossed the forest':'yangın söndü · the fire died out',K=pi+st+Math.round(pct);
  if(K!==lk){lk=K;box.innerHTML='<div class="hzbox" style="padding:.6vw 1.8vw;max-width:88vw"><div class="a" style="font-size:1.55vw">Ağaç yoğunluğu · tree density: %'+(P[pi]*100).toFixed(1).replace('.0','')+' — yanan ağaç · trees burnt: %'+pct.toFixed(0)+' — '+st+'</div><div class="e" style="font-size:1.05vw">Sihirli sınır yaklaşık %59,3: altında yangın küçük adacıklarda kalır, üstünde neredeyse bütün ormanı geçer. Aynı eşik kahvenin telveden süzülmesinde, salgınların yayılmasında ve elektriğin karışık malzemelerde akmasında da karşımıza çıkar · The magic line is about 59.3%: below it a fire stays in small islands, above it sweeps across almost everything. The same threshold shows up in coffee seeping through grounds, epidemics spreading and electricity finding a path through mixed materials</div></div>'}});return L};

/* optimal stopping (the secretary problem): look at the first 37%, then take the first one better than all of them */
W.hzstop=function(L,it){grad(L,'#1d2230','#05070b');var c=wCv(L),x=c.getContext('2d'),N=100,CUT=[10,37,70],SC,best,tr=0,win=[0,0,0],cur,pick,DS=null,t0=0,acc=0,box=T(L,'','bottom:12px',1),last=0,phase=0,hold=0;
 T(L,'<div class="hzbox">'+hd('Zekice Düşünce · Clever Thinking — ne zaman durmalı? · optimal stopping','100 aday tek tek geliyor. Her birine hemen evet ya da hayır demelisin; geri dönüş yok. En iyisini nasıl seçersin?','100 candidates arrive one by one. You must say yes or no on the spot — no going back. How do you pick the best one?')+'</div>','top:12px',.4);
 function newT(){SC=[];for(var i=0;i<N;i++)SC.push(Math.random());best=0;for(i=1;i<N;i++)if(SC[i]>SC[best])best=i;pick=[];for(var j=0;j<3;j++){var m=-1,p=N-1;for(i=0;i<CUT[j];i++)if(SC[i]>m)m=SC[i];for(i=CUT[j];i<N;i++)if(SC[i]>m){p=i;break}pick.push(p)}cur=0}
 function finish(){tr++;for(var j=0;j<3;j++)if(pick[j]==best)win[j]++;DS=[SC.slice(),pick.slice(),best]}
 newT();
 wLoop(L,function(t){var slow=tr<3;if(hold){if(t>hold){hold=0;newT()}}else{acc+=slow?.5:tr<10?3:100;while(acc>=1&&!hold){acc--;cur++;if(cur>=N){finish();if(slow||tr<10)hold=t+(slow?3.5:1);else newT();break}}}
  if(slow||tr<10||Math.floor(t*4)!==phase){phase=Math.floor(t*4);x.clearRect(0,0,1920,1080);var X0=210,BW=15,BASE=730,HH=360,v=Math.min(cur,N),SC0=SC,pk0=pick,bs0=best,cu0=cur;if(!slow&&tr>=10&&DS){SC=DS[0];pick=DS[1];best=DS[2];cur=N;v=N}
   x.fillStyle='rgba(195,205,210,.10)';x.fillRect(X0-4,BASE-HH-20,CUT[1]*BW+2,HH+24);x.font='24px Helvetica,Arial';x.fillStyle='#c3cdd2';x.textAlign='left';x.fillText('ilk %37: sadece bak · first 37%: just look',X0,BASE-HH-34);
   for(var i=0;i<v;i++){var h=SC[i]*HH,col=i<CUT[1]?'rgba(195,205,210,.55)':'#8fd3c1';if(i==pick[1]&&cur>pick[1])col='#ff9e7a';x.fillStyle=col;x.fillRect(X0+i*BW,BASE-h,BW-3,h)}
   if(cur>=N){var bx=X0+best*BW+BW/2-1.5;x.strokeStyle='#f3f1ec';x.lineWidth=3;x.beginPath();x.arc(bx,BASE-SC[best]*HH-26,12,0,7);x.stroke();x.fillStyle='#f3f1ec';x.textAlign='center';x.font='22px Helvetica,Arial';x.fillText('en iyi · best',bx,BASE-SC[best]*HH-48)}SC=SC0;pick=pk0;best=bs0;cur=cu0;
   x.textAlign='left';x.font='26px Georgia';for(var j=0;j<3;j++){var yy=800+j*38,r=tr?win[j]/tr*100:0;x.fillStyle=j==1?'#ff9e7a':'#c3cdd2';x.fillText('İlk '+CUT[j]+' adayı geç · skip the first '+CUT[j]+':',X0,yy);x.fillRect(X0+520,yy-20,r*6,22);x.fillText('%'+r.toFixed(1),X0+530+r*6,yy)}}
  if(t-last>.5){last=t;box.innerHTML='<div class="hzbox" style="padding:.6vw 1.8vw;max-width:88vw"><div class="a" style="font-size:1.5vw">Deneme · Trials: '+nTR(tr)+' — %37 kuralıyla en iyiyi bulma · finding the very best with the 37% rule: %'+(tr?win[1]/tr*100:0).toFixed(1)+'</div>'+(tr>20?'<div class="e" style="font-size:1.05vw">Rastgele seçsen başarı şansın %1. Kural: ilk %37’yi sadece incele, sonra şimdiye kadarkilerin hepsinden iyi olan ilk kişide dur — en iyiyi yaklaşık %37 ihtimalle yakalarsın. Ev ararken, park yeri ararken de işe yarar · Picking at random gives a 1% chance. The rule: only study the first 37%, then stop at the first one better than all before — you land the very best about 37% of the time. It works for house hunting and parking spots too</div>':'')+'</div>'}});return L};

/* neon colour spreading (van Tuijl 1975): red segments inside black crosses paint a pale glowing disc that is not there */
W.hzneon=function(L,it){L.style.background='#ece9e2';var c=wCv(L),x=c.getContext('2d'),CX=960,CY=610,SP=78,R=250,ON=10,OFF=7,box=T(L,'','bottom:12px',1),lk='';
 var hdr=T(L,'<div class="hzbox">'+hd('Göz Oyunu · Optical Illusion — neon renk yayılması · neon colour spreading','Kırmızı bir daire görüyor musun? Kenarlarına ve ortasına dikkatle bak','Can you see a pale red disc? Look carefully at its edges and its middle')+'</div>','top:12px',.4);
 wLoop(L,function(t){var u=t%(ON+OFF),on=u<ON,a=on?Math.min(1,u/1.2):Math.max(0,1-(u-ON)/1.2);x.clearRect(0,0,1920,1080);x.lineCap='butt';
  for(var gx=-7;gx<=7;gx++)for(var gy=-4;gy<=4;gy++){var px=CX+gx*SP,py=CY+gy*SP;if(py<300||py>1000)continue;var d=Math.sqrt((px-CX)*(px-CX)+(py-CY)*(py-CY)),inr=d<R,h=SP*.42;
   x.strokeStyle='#15171c';x.lineWidth=5;x.beginPath();x.moveTo(px-h,py);x.lineTo(px+h,py);x.moveTo(px,py-h);x.lineTo(px,py+h);x.stroke();
   if(inr&&a>0){x.strokeStyle='rgba(214,40,40,'+a.toFixed(2)+')';x.lineWidth=5;var s=SP*.2;x.beginPath();x.moveTo(px-s,py);x.lineTo(px+s,py);x.moveTo(px,py-s);x.lineTo(px,py+s);x.stroke()}}
  var K=on?'on':'off';if(K!==lk){lk=K;box.innerHTML='<div class="hzbox" style="padding:.6vw 1.8vw;max-width:86vw">'+(on?'<div class="a" style="font-size:1.6vw">Haçların arası da pembe görünüyor, değil mi?</div><div class="e" style="font-size:1.08vw">The gaps between the crosses look pink too, don’t they? They are exactly the same pale paper as the rest. Only the small centre segments are red — your brain spreads their colour and even draws a soft edge around the disc</div>':'<div class="a" style="font-size:1.6vw">Kırmızı kısımlar gitti: daire de onlarla birlikte yok oldu</div><div class="e" style="font-size:1.08vw">The red bits are gone — and the disc vanished with them. Nothing between the lines ever changed colour. Beyin kenarları tamamlamaya ve yüzeyleri boyamaya o kadar alışkın ki olmayan bir şekli “görür” · The brain is so used to completing edges and filling surfaces that it “sees” a shape that is not there</div>')+'</div>'}});return L};

/* motion binding (Lorenceau & Shiffrar 1992): a diamond circling behind four occluders looks whole; hide the occluders and it breaks into four wandering lines */
W.hzocclude=function(L,it){L.style.background='#0b0d12';var c=wCv(L),x=c.getContext('2d'),CX=960,CY=610,V=230,MR=34,OS=150,A=12,B=12,C2=8,box=T(L,'','bottom:12px',1),lk='';
 T(L,'<div class="hzbox">'+hd('Göz Oyunu · Optical Illusion — hareketi birleştirme · motion binding','Dört kısa çizgi. Sence birlikte mi hareket ediyorlar, yoksa her biri kendi yolunda mı?','Four short lines. Are they moving together, or is each one going its own way?')+'</div>','top:12px',.4);
 wLoop(L,function(t){var u=t%(A+B+C2),ph=u<A?0:u<A+B?1:2,an=t*1.7,dx=Math.cos(an)*MR,dy=Math.sin(an)*MR,cx=CX+dx,cy=CY+dy;x.clearRect(0,0,1920,1080);
  x.strokeStyle='#e8eef0';x.lineWidth=7;x.beginPath();x.moveTo(cx,cy-V);x.lineTo(cx+V,cy);x.lineTo(cx,cy+V);x.lineTo(cx-V,cy);x.closePath();x.stroke();
  var oc=ph==0?'#5a6270':'#0b0d12',P=[[CX,CY-V],[CX+V,CY],[CX,CY+V],[CX-V,CY]];x.fillStyle=oc;for(var i=0;i<4;i++)x.fillRect(P[i][0]-OS/2,P[i][1]-OS/2,OS,OS);
  if(ph==2){x.strokeStyle='rgba(255,158,122,.55)';x.lineWidth=3;x.setLineDash([10,8]);x.beginPath();x.moveTo(cx,cy-V);x.lineTo(cx+V,cy);x.lineTo(cx,cy+V);x.lineTo(cx-V,cy);x.closePath();x.stroke();x.setLineDash([])}
  var K=String(ph);if(K!==lk){lk=K;var m=[['Gri kareler görünürken: tek bir eşkenar dörtgen, daireler çizerek dönüyor','With the grey squares visible: one single diamond, gliding round in a circle. Your brain assumes the corners are hidden behind them'],['Kareler görünmez oldu: şimdi dört çizgi ayrı ayrı inip çıkıyor gibi','The squares became invisible — now four lines seem to slide up and down on their own. Nothing else changed: same lines, same motion'],['Gerçek: hep aynı şekil, hep aynı hareket','The truth: always the same shape, always the same motion. Beyin bir şeyin önünü kapatan bir neden görmezse, parçaları birleştirmez · Without a visible reason for the gaps, the brain will not join the pieces']][ph];
   box.innerHTML='<div class="hzbox" style="padding:.6vw 1.8vw;max-width:86vw"><div class="a" style="font-size:1.6vw">'+m[0]+'</div><div class="e" style="font-size:1.08vw">'+m[1]+'</div></div>'}});return L};

/* calm night: a hillside village above the sea; warm windows go out one by one as the night deepens (illustration) */
W.hzkoy=function(L,it){var c=wCv(L),x=c.getContext('2d'),S=stars(200),i,j,SY=760,HL=[],HS=[],TOT=it.tot||90;
 function rnd(s){return function(){s=(s*9301+49297)%233280;return s/233280}}var R=rnd(7);
 for(i=0;i<3;i++){var pts=[],b=430+i*95,amp=120-i*25,p1=R()*6;for(j=0;j<=96;j++){var xx=j*20;pts.push(b-amp*Math.sin(xx/(520-i*90)+p1)-amp*.3*Math.sin(xx/130+p1*2)-(i==2?(xx>900?(xx-900)*.12:0):0))}HL.push(pts)}
 for(i=0;i<46;i++){var hx=80+R()*1760,l=1+Math.floor(R()*2),k=Math.floor(hx/20),hy=HL[l][k]+18+R()*Math.max(20,(l==2?SY-30:HL[l+1][k])-HL[l][k]-40);if(hy>SY-24)continue;HS.push([hx,hy,l,R(),R()*.9])}
 HS.sort(function(a,b){return a[4]-b[4]});
 T(L,hd('Köy Uyurken · As the Village Sleeps — çizim · illustration, hayal ürünü · imagined (sakin · calm)','Denize bakan yamaçta, pencereler birer birer kararıyor','On the hillside above the sea, the windows go dark one by one'),'top:44px',2);
 T(L,'<div class="sm" style="font-size:1.25vw;color:#cdd6dc">Karadeniz köylerinde evler yamaca dağınık kurulur: her biri kendi bahçesinin, kendi çay ya da fındık bahçesinin ortasında<br><i>In Black Sea villages the houses are scattered over the slopes — each one in the middle of its own garden, its own tea or hazelnut plot</i></div>','bottom:40px',9);
 wLoop(L,function(t){var g=x.createLinearGradient(0,0,0,SY);g.addColorStop(0,'#02040b');g.addColorStop(1,'#16223a');x.fillStyle=g;x.fillRect(0,0,1920,SY);drawStars(x,S.filter(function(s){return s[1]<480}),t);
  var mxp=1700,myp=300;x.fillStyle='rgba(238,240,246,.95)';x.beginPath();x.arc(mxp,myp,36,0,7);x.fill();var mg=x.createRadialGradient(mxp,myp,30,mxp,myp,170);mg.addColorStop(0,'rgba(200,215,240,.22)');mg.addColorStop(1,'rgba(200,215,240,0)');x.fillStyle=mg;x.fillRect(mxp-180,myp-180,360,360);
  var u=(t%TOT)/TOT,offN=u<.85?Math.floor(u/.85*HS.length*.8):Math.floor(HS.length*.8*(1-(u-.85)/.15));
  for(var l=0;l<HL.length;l++){var sh=9+l*6;x.fillStyle='rgb('+sh+','+(sh+6)+','+(sh+12)+')';x.beginPath();x.moveTo(0,SY);for(var k=0;k<HL[l].length;k++)x.lineTo(k*20,Math.min(SY,HL[l][k]));x.lineTo(1920,SY);x.closePath();x.fill();
   for(var h=0;h<HS.length;h++){var H=HS[h];if(H[2]!=l)continue;x.fillStyle='rgb('+(sh+10)+','+(sh+12)+','+(sh+16)+')';x.fillRect(H[0]-14,H[1]-12,28,18);x.beginPath();x.moveTo(H[0]-17,H[1]-12);x.lineTo(H[0],H[1]-24);x.lineTo(H[0]+17,H[1]-12);x.fill();
    if(h>=offN){var gl=x.createRadialGradient(H[0],H[1]-3,0,H[0],H[1]-3,26);gl.addColorStop(0,'rgba(255,212,150,.40)');gl.addColorStop(1,'rgba(255,212,150,0)');x.fillStyle=gl;x.fillRect(H[0]-26,H[1]-29,52,52);x.fillStyle='rgba(255,222,170,.92)';x.fillRect(H[0]-8,H[1]-7,6,7);if(H[3]>.5)x.fillRect(H[0]+2,H[1]-7,6,7)}}}
  var wg=x.createLinearGradient(0,SY,0,1080);wg.addColorStop(0,'#101a2e');wg.addColorStop(1,'#02040a');x.fillStyle=wg;x.fillRect(0,SY,1920,320);
  for(var r=0;r<26;r++){var yy=SY+8+r*11,w=12+r*5,sx=mxp+Math.sin(t*.9+r*1.7)*(6+r*.8);x.fillStyle='rgba(225,232,246,'+(.38-r*.012).toFixed(3)+')';x.fillRect(sx-w/2,yy,w,2.5)}
  for(var yy2=SY+4;yy2<1080;yy2+=7){x.fillStyle='rgba(2,4,10,.25)';x.fillRect(0,yy2+Math.sin(t*.7+yy2*.25)*1.4,1920,2)}});return L};

/* ---------- v77 additions: hzphysarum (living art), hzaxelrod hzcrowd (clever thinking), hzdelboeuf hzwagon (illusions), hzstartrail (calm night) ---------- */
/* slime mould (Physarum) agent model: thousands of agents sniff a shared trail, turn toward the strongest scent and leave their own; food spots emit scent. A network connecting the food grows by itself */
W.hzphysarum=function(L,it){L.style.background='#03070a';var c=wCv(L),x=c.getContext('2d'),RW=320,RH=170,off=document.createElement('canvas'),ox,img,TR=new Float32Array(RW*RH),TB=new Float32Array(RW*RH),N=it.n||6000,AX=new Float32Array(N),AY=new Float32Array(N),AH=new Float32Array(N),F=[],T0=-1,DUR=it.dur||40,box=T(L,'','bottom:12px',1),lk='',SD=9,SA=.4,RA=.6,rd=0,Y0=150,SC=1920/RW;
 off.width=RW;off.height=RH;ox=off.getContext('2d');img=ox.createImageData(RW,RH);
 T(L,'<div class="hzbox">'+hd('Yaşayan Sanat · Living Art — balçık mantarı simülasyonu · slime mould simulation','Beyni yok, gözü yok, planı yok. Yine de besinleri birbirine bağlayan bir yol ağı kuruyor','No brain, no eyes, no plan — and yet it builds a network of paths linking the food')+'</div>','top:12px',.4);
 function start(t){T0=t;rd++;for(var k=0;k<TR.length;k++)TR[k]=0;F=[];var nf=9+Math.floor(Math.random()*4),tries=0;while(F.length<nf&&tries<500){tries++;var fx=18+Math.random()*(RW-36),fy=34+Math.random()*(RH-48),ok=1;for(var j=0;j<F.length;j++){var dx=F[j][0]-fx,dy=F[j][1]-fy;if(dx*dx+dy*dy<900)ok=0}if(ok)F.push([fx,fy])}
  for(k=0;k<N;k++){AX[k]=2+Math.random()*(RW-4);AY[k]=2+Math.random()*(RH-4);AH[k]=Math.random()*6.283}}
 function sn(px,py,a){var sx=(px+Math.cos(a)*SD)|0,sy=(py+Math.sin(a)*SD)|0;if(sx<0||sy<0||sx>=RW||sy>=RH)return -1;return TR[sy*RW+sx]}
 function step(){var k,i;for(i=0;i<F.length;i++){var fx=F[i][0]|0,fy=F[i][1]|0;for(var dy=-2;dy<=2;dy++)for(var dx=-2;dx<=2;dx++){var q=(fy+dy)*RW+fx+dx;if(q>=0&&q<TR.length)TR[q]+=4}}
  for(k=0;k<N;k++){var h=AH[k],f=sn(AX[k],AY[k],h),l=sn(AX[k],AY[k],h-SA),r=sn(AX[k],AY[k],h+SA);if(f>=l&&f>=r){}else if(l>r)h-=RA;else if(r>l)h+=RA;else h+=(Math.random()-.5)*RA*2;h+=(Math.random()-.5)*.12;
   var nx=AX[k]+Math.cos(h),ny=AY[k]+Math.sin(h);if(nx<1||ny<1||nx>=RW-1||ny>=RH-1){h=Math.random()*6.283;nx=AX[k];ny=AY[k]}AX[k]=nx;AY[k]=ny;AH[k]=h;TR[(ny|0)*RW+(nx|0)]+=1}
  for(var y=1;y<RH-1;y++)for(var xx=1;xx<RW-1;xx++){var p=y*RW+xx;TB[p]=(TR[p]*2+TR[p-1]+TR[p+1]+TR[p-RW]+TR[p+RW])/6*.86}var tmp=TR;TR=TB;TB=tmp}
 wLoop(L,function(t){if(T0<0||t-T0>DUR)start(t);var u=t-T0;if(u<DUR-3){step();if(u>1)step()}
  var D=img.data,fade=u>DUR-3?Math.max(0,(DUR-u)/3):Math.min(1,u/1);for(var k=0;k<TR.length;k++){var v=Math.min(1,TR[k]/9);v=Math.pow(v,.55)*fade;var o=k*4;D[o]=40*v+v*v*150;D[o+1]=150*v+v*v*90;D[o+2]=170*v+v*v*70;D[o+3]=255}ox.putImageData(img,0,0);
  x.fillStyle='#03070a';x.fillRect(0,0,1920,1080);x.imageSmoothingEnabled=true;x.drawImage(off,0,Y0,1920,RH*SC*.82);
  x.fillStyle='rgba(240,236,226,'+(.9*fade).toFixed(2)+')';for(var i=0;i<F.length;i++){x.beginPath();x.arc(F[i][0]*SC,Y0+F[i][1]*SC*.82,7,0,7);x.fill()}
  var K=rd+'|'+(u<12?0:1);if(K!==lk){lk=K;box.innerHTML='<div class="hzbox" style="padding:.6vw 1.8vw;max-width:88vw"><div class="a" style="font-size:1.45vw">Minik gezgin · tiny walkers: '+nTR(N)+' — besin noktası · food spots (beyaz · white): '+F.length+'</div><div class="e" style="font-size:1.05vw">Her gezgin tek bir kural izliyor: önündeki üç yönü kokla, kokunun en güçlü olduğu yöne dön, giderken arkanda iz bırak. Kimse ağın tamamını bilmiyor; ama sık kullanılan yollar güçleniyor, boş kalanlar siliniyor. Gerçek balçık mantarı Physarum polycephalum da aşağı yukarı böyle çalışır · Each walker follows one rule: sniff three directions ahead, turn toward the strongest scent, leave a trail behind. No one knows the whole network — but busy paths grow stronger and unused ones fade. The real slime mould Physarum polycephalum works much the same way</div></div>'}});return L};

/* Delboeuf illusion: the same portion looks bigger on a small plate (two identical discs on different plates, then the plates fade and the discs meet) */
W.hzdelboeuf=function(L,it){grad(L,'#3a2c24','#120c09');var c=wCv(L),x=c.getContext('2d'),A=14,B=10,CY=620,R=78,PL=[[560,CY,300],[1360,CY,108]],box=T(L,'','bottom:12px',1),lk='';
 T(L,'<div class="hzbox">'+hd('Göz Oyunu · Optical Illusion — Delboeuf yanılsaması · Delboeuf illusion','Hangi tabaktaki porsiyon daha büyük: soldaki mi, sağdaki mi?','Which plate holds the bigger portion — left or right?')+'</div>','top:12px',.4);
 function plate(px,py,r,a){if(a<=0)return;x.globalAlpha=a;var g=x.createRadialGradient(px-r*.2,py-r*.25,r*.1,px,py,r);g.addColorStop(0,'#fbfaf6');g.addColorStop(.8,'#e6e3dc');g.addColorStop(1,'#bdb8ae');x.fillStyle='rgba(0,0,0,.35)';x.beginPath();x.arc(px+8,py+12,r,0,7);x.fill();x.fillStyle=g;x.beginPath();x.arc(px,py,r,0,7);x.fill();x.strokeStyle='rgba(150,145,135,.55)';x.lineWidth=3;x.beginPath();x.arc(px,py,r*.78,0,7);x.stroke();x.globalAlpha=1}
 function food(px,py){var g=x.createRadialGradient(px-R*.3,py-R*.35,R*.1,px,py,R);g.addColorStop(0,'#c0583a');g.addColorStop(1,'#7a2a1c');x.fillStyle=g;x.beginPath();x.arc(px,py,R,0,7);x.fill();x.fillStyle='rgba(120,170,90,.9)';for(var i=0;i<5;i++){var a=i*1.26+.4;x.beginPath();x.ellipse(px+Math.cos(a)*R*.45,py+Math.sin(a)*R*.45,9,4,a,0,7);x.fill()}}
 wLoop(L,function(t){var u=t%(A+B),ph=u<A?0:1,k=ph?Math.min(1,(u-A)/2.5):0,e=k*k*(3-2*k);x.clearRect(0,0,1920,1080);
  plate(PL[0][0],PL[0][1],PL[0][2],1-e);plate(PL[1][0],PL[1][1],PL[1][2],1-e);
  var x1=PL[0][0]+(960-R-10-PL[0][0])*e,x2=PL[1][0]+(960+R+10-PL[1][0])*e;food(x1,CY);food(x2,CY);
  if(ph&&k>=1){x.strokeStyle='rgba(243,241,236,.8)';x.lineWidth=2;x.setLineDash([12,10]);x.beginPath();x.moveTo(700,CY-R);x.lineTo(1220,CY-R);x.moveTo(700,CY+R);x.lineTo(1220,CY+R);x.stroke();x.setLineDash([])}
  var K=String(ph);if(K!==lk){lk=K;box.innerHTML='<div class="hzbox" style="padding:.6vw 1.8vw;max-width:86vw">'+(ph?'<div class="a" style="font-size:1.6vw">İkisi tıpatıp aynı boyutta!</div><div class="e" style="font-size:1.08vw">They are exactly the same size! Beyin bir şeyin büyüklüğünü çevresine göre ölçer: dar bir kenar onu büyütür, geniş boşluk küçültür · The brain judges size by what surrounds it — a thin rim makes it look bigger, a wide empty border makes it look smaller. Restoranlar ve oteller bunu bilir: küçük tabak, cömert görünen porsiyon · Restaurants and hotels know it: a small plate makes a portion look generous</div>':'<div class="a" style="font-size:1.6vw">Çoğu kişi sağdakini daha büyük görür</div><div class="e" style="font-size:1.08vw">Most people see the portion on the right as bigger. Ölçmeden önce bir karar ver · Make up your mind before we measure</div>')+'</div>'}});return L};

/* wagon-wheel effect: a wheel filmed at 12 frames per second; as it speeds up it seems to stop, then spin backwards */
W.hzwagon=function(L,it){grad(L,'#1c2430','#05070b');var c=wCv(L),x=c.getContext('2d'),FS=12,NS=8,CX=760,CY=620,RR=250,th=0,lt=0,shown=0,lastF=-1,box=T(L,'','bottom:12px',1),lk='',CYC=48;
 T(L,'<div class="hzbox">'+hd('Göz Oyunu · Optical Illusion — araba tekerleği etkisi · wagon-wheel effect','Bu tekerlek saniyede 12 kare çeken bir kamerayla görüntüleniyor. Hız arttıkça ne oluyor?','This wheel is shown through a camera taking 12 frames a second. Watch what happens as it speeds up')+'</div>','top:12px',.4);
 function rpm(u){if(u<36){var k=u<18?u/18:(36-u)/18;return k*200}return 86}
 wLoop(L,function(t){var dt=Math.min(.1,t-lt);lt=t;var u=t%CYC,R=rpm(u);th+=R/60*6.2832*dt;var fr=Math.floor(t*FS);if(fr!==lastF){lastF=fr;shown=th}
  x.clearRect(0,0,1920,1080);x.save();x.translate(CX,CY);x.rotate(shown);x.strokeStyle='#cfd6dc';x.lineWidth=22;x.beginPath();x.arc(0,0,RR,0,7);x.stroke();x.strokeStyle='#5e6874';x.lineWidth=6;x.beginPath();x.arc(0,0,RR-16,0,7);x.stroke();
  for(var i=0;i<NS;i++){var a=i*6.2832/NS;x.strokeStyle=(u>=36&&i==0)?'#ff7a5a':'#aeb8c2';x.lineWidth=14;x.beginPath();x.moveTo(Math.cos(a)*40,Math.sin(a)*40);x.lineTo(Math.cos(a)*(RR-14),Math.sin(a)*(RR-14));x.stroke()}
  x.fillStyle='#3a4450';x.beginPath();x.arc(0,0,48,0,7);x.fill();x.fillStyle='#cfd6dc';x.beginPath();x.arc(0,0,16,0,7);x.fill();x.restore();
  var per=R/60*360/FS,sp=360/NS,ap=((per%sp)+sp)%sp;if(ap>sp/2)ap-=sp;var st=Math.abs(ap)<1.2?'duruyor gibi · seems to stand still':ap>0?'ileri dönüyor gibi · seems to turn forwards':'GERİ dönüyor gibi · seems to turn BACKWARDS';
  x.fillStyle='#f3f1ec';x.textAlign='left';x.font='40px Georgia';x.fillText('Gerçek hız · real speed:',1180,520);x.font='bold 76px Georgia';x.fillText(Math.round(R)+' dev/dk · rpm',1180,610);x.font='30px Georgia';x.fillStyle='#c3cdd2';x.fillText('Her karede dönüş · turn per frame: '+per.toFixed(1)+'°',1180,680);x.fillText('Teller arası · between spokes: '+sp+'°',1180,725);x.fillStyle=ap<-1.2?'#ff9e7a':'#8fd3c1';x.font='34px Georgia';x.fillText(st,1180,790);
  var K=(u>=36?'m':'')+st;if(K!==lk){lk=K;box.innerHTML='<div class="hzbox" style="padding:.6vw 1.8vw;max-width:88vw">'+(u>=36?'<div class="a" style="font-size:1.5vw">Bir teli kırmızıya boyadık: şimdi gerçeği görüyorsun</div><div class="e" style="font-size:1.05vw">We painted one spoke red — now you can see the truth: the wheel really turns forwards all the time. Diğer teller birbirinin aynısı olduğu için beyin her karede en yakın teli “aynı tel” sanır · Because all the other spokes look identical, the brain matches each one to the nearest spoke in the next frame</div>':'<div class="a" style="font-size:1.5vw">Tekerlek hep ileri dönüyor ve gittikçe hızlanıyor</div><div class="e" style="font-size:1.05vw">The wheel always turns forwards and keeps speeding up. Bir karede teller arası açıdan (45°) biraz azını dönerse ileri, tam 45° dönerse duruyor, biraz fazlasını dönerse geri dönüyor gibi görünür. Eski kovboy filmlerindeki geri dönen at arabası tekerlekleri buydu · Turning a little under 45° per frame looks forwards, exactly 45° looks frozen, a little over looks backwards — the backward-spinning wagon wheels of old western films</div>')+'</div>'}});return L};

/* iterated prisoner's dilemma: Axelrod-style round robin of 7 strategies (200 rounds each), then an ecological contest where winners grow */
W.hzaxelrod=function(L,it){grad(L,'#1b2430','#05070b');var c=wCv(L),x=c.getContext('2d'),NR=200,box=T(L,'','bottom:12px',1),lk='',
 NM=['Kısasa Kısas · Tit for Tat','Hep İyi · Always Nice','Hep Kötü · Always Mean','Kinci · Grudger','Yazı-Tura · Random','Affedici · Forgiving (2 tit for tat)','Sinsi · Sneaky (10%)'],CL=['#8fd3c1','#a9c8ff','#ff7a5a','#d6b3ff','#9aa4ae','#b8e08f','#ffb08a'],S=NM.length,
 PL=[function(m,o){return o.length?o[o.length-1]:1},function(){return 1},function(){return 0},function(m,o){return o.indexOf(0)<0?1:0},function(){return Math.random()<.5?1:0},function(m,o){var n=o.length;return n>1&&!o[n-1]&&!o[n-2]?0:1},function(m,o){if(Math.random()<.1)return 0;return o.length?o[o.length-1]:1}],
 PAY=[[1,5],[0,3]],M,TOT,PR,pi,mv,hold,T0=-1,phase,GEN,POP,lg=0;
 T(L,'<div class="hzbox">'+hd('Zekice Düşünce · Clever Thinking — mahkûm ikilemi turnuvası · prisoner’s dilemma tournament','Her turda iki oyuncu ya iş birliği yapar ya da karşısındakini kazıklar. 200 tur sonunda kim kazanır: iyiler mi, kurnazlar mı?','Each round two players either cooperate or cheat. After 200 rounds, who comes out ahead — the nice or the cunning?')+'</div>','top:12px',.4);
 function play(i,j){var a=[],b=[],sa=0,sb=0;for(var r=0;r<NR;r++){var p=PL[i](a,b),q=PL[j](b,a);a.push(p);b.push(q);sa+=PAY[p][q];sb+=PAY[q][p]}return [a,b,sa,sb]}
 function start(t){T0=t;M=[];TOT=[];for(var i=0;i<S;i++){M.push([]);TOT.push(0)}PR=[];for(i=0;i<S;i++)for(var j=i;j<S;j++)PR.push([i,j]);pi=0;mv=null;phase=0;GEN=[];POP=[];for(i=0;i<S;i++)POP.push(1/S);GEN.push(POP.slice())}
 function evo(){var f=[],s=0,i,j;for(i=0;i<S;i++){f[i]=0;for(j=0;j<S;j++)f[i]+=POP[j]*M[i][j]/NR;}for(i=0;i<S;i++){POP[i]*=f[i];s+=POP[i]}for(i=0;i<S;i++)POP[i]/=s;GEN.push(POP.slice())}
 wLoop(L,function(t){if(T0<0||t-T0>70)start(t);var u=t-T0;x.clearRect(0,0,1920,1080);x.textAlign='left';
  if(phase==0){var want=Math.min(PR.length,Math.floor(u/1.05)+1);while(pi<want){var p=PR[pi],r=play(p[0],p[1]);M[p[0]][p[1]]=r[2];M[p[1]][p[0]]=r[3];TOT[p[0]]+=r[2];if(p[0]!=p[1])TOT[p[1]]+=r[3];mv=[p,r];pi++}if(pi>=PR.length&&u>PR.length*1.05+3)phase=1}
  if(phase==0&&mv){var p=mv[0],r=mv[1];x.font='30px Georgia';for(var s2=0;s2<2;s2++){var ix=p[s2],hh=r[s2],yy=450+s2*120;x.fillStyle=CL[ix];x.fillText(NM[ix]+' — '+r[2+s2]+' puan · points',120,yy-14);for(var k=0;k<50;k++){x.fillStyle=hh[k]?'#8fd3c1':'#ff7a5a';x.fillRect(120+k*20,yy,16,40)}}
   x.font='24px Helvetica,Arial';x.fillStyle='#c3cdd2';x.fillText('İlk 50 hamle · first 50 moves — yeşil · green: iş birliği · cooperate, kırmızı · red: kazık · cheat',120,720);x.fillText('İkisi iyi: 3+3 · both nice: 3+3   ·   biri kazıklarsa: 5+0 · one cheats: 5+0',120,760);x.fillText('İkisi kötü: 1+1 · both cheat: 1+1',120,800);
   var ord=[];for(var i=0;i<S;i++)ord.push(i);ord.sort(function(a,b){return TOT[b]-TOT[a]});var mx=Math.max.apply(null,TOT)||1;x.font='26px Georgia';x.fillStyle='#f3f1ec';x.fillText('Toplam puan · total score ('+pi+'/'+PR.length+' maç · matches)',1250,370);
   for(i=0;i<S;i++){var q=ord[i],y2=420+i*68;x.fillStyle=CL[q];x.fillRect(1250,y2,TOT[q]/mx*420,32);x.fillStyle='#f3f1ec';x.font='22px Georgia';x.fillText(NM[q],1250,y2-6);x.fillText(nTR(TOT[q]),1680,y2+25)}}
  if(phase==1){var tg=Math.min(60,Math.floor((u-(PR.length*1.05+3))/.4));while(GEN.length<=tg)evo();var X0=160,W2=1160,Y1=390,H2=500;x.strokeStyle='rgba(243,241,236,.35)';x.lineWidth=2;x.strokeRect(X0,Y1,W2,H2);x.font='24px Georgia';x.fillStyle='#c3cdd2';x.fillText('Nesil · generation: '+(GEN.length-1)+' — kazananlar çoğalıyor, kaybedenler azalıyor · winners multiply, losers shrink',X0,Y1-20);
   for(i=0;i<S;i++){x.strokeStyle=CL[i];x.lineWidth=5;x.beginPath();for(var g=0;g<GEN.length;g++){var px=X0+g/60*W2,py=Y1+H2-GEN[g][i]*H2/.6;if(py<Y1)py=Y1;g?x.lineTo(px,py):x.moveTo(px,py)}x.stroke()}
   var o2=[];for(i=0;i<S;i++)o2.push(i);o2.sort(function(a,b){return POP[b]-POP[a]});for(i=0;i<S;i++){var q2=o2[i];x.fillStyle=CL[q2];x.fillRect(1380,400+i*66,30,30);x.fillStyle='#f3f1ec';x.font='24px Georgia';x.fillText(NM[q2].split(' · ')[0]+' %'+(POP[q2]*100).toFixed(0),1425,425+i*66)}}
  var K=phase+'';if(K!==lk){lk=K;box.innerHTML='<div class="hzbox" style="padding:.6vw 1.8vw;max-width:88vw">'+(phase==0?'<div class="a" style="font-size:1.45vw">Herkes herkesle 200 tur oynuyor</div><div class="e" style="font-size:1.05vw">Everyone plays everyone for 200 rounds. 1980’de Robert Axelrod bu turnuvayı bilgisayar programlarıyla yaptı; kazanan en kısa program oldu: “Kısasa Kısas” — önce iyi davran, sonra karşındakinin son hamlesini tekrarla · In 1980 Robert Axelrod ran this tournament with computer programs — the winner was the shortest one: “Tit for Tat”: be nice first, then copy your opponent’s last move</div>':'<div class="a" style="font-size:1.45vw">Şimdi puan = çocuk sayısı: iyi oynayan çoğalıyor</div><div class="e" style="font-size:1.05vw">Now points become offspring — good players multiply. “Hep Kötü” başta saf oyuncuları sömürerek büyür, ama kurbanları bitince kendisi de söner. Ayakta kalanlar iyi niyetli, kazığa karşılık veren ve affedebilen stratejiler · “Always Mean” grows at first by exploiting the naive, then fades once its victims are gone. The survivors are nice, hit back when cheated, and can forgive</div>')+'</div>'}});return L};

/* wisdom of crowds: 300 independent guesses of the beans in a jar — the crowd's median lands close; then a herding round where people hear the loud first guess */
W.hzcrowd=function(L,it){grad(L,'#1f2a30','#05080a');var c=wCv(L),x=c.getContext('2d'),N=300,TRUE,G,T0=-1,rd=0,mode=0,box=T(L,'','bottom:12px',1),lk='',BE=[],MAXV=3000,X0=820,XW=1000,BASE=820;
 T(L,'<div class="hzbox">'+hd('Zekice Düşünce · Clever Thinking — kalabalığın bilgeliği · the wisdom of crowds','Kavanozda kaç şeker var? 300 kişi birbirinden habersiz tahmin ediyor','How many sweets are in the jar? 300 people guess without seeing each other’s answers')+'</div>','top:12px',.4);
 function gauss(){return Math.sqrt(-2*Math.log(Math.random()+1e-9))*Math.cos(6.2832*Math.random())}
 function start(t){T0=t;rd++;mode=(rd+1)%2;TRUE=700+Math.floor(Math.random()*700);G=[];BE=[];var cols=['#ff7a5a','#8fd3c1','#a9c8ff','#d6b3ff','#b8e08f','#f3f1ec','#ff9ec4'];for(var i=0;i<420;i++){var yy=Math.random(),w=260+yy*0;BE.push([480+(Math.random()-.5)*300,420+Math.random()*400,cols[i%cols.length],Math.random()*3])}}
 function med(a){var b=a.slice().sort(function(p,q){return p-q});return b.length?b[b.length>>1]:0}
 wLoop(L,function(t){if(T0<0||t-T0>34)start(t);var u=t-T0,want=Math.min(N,Math.floor(u/22*N));while(G.length<want){var own=TRUE*Math.exp(gauss()*.45),g=own;if(mode==1){if(!G.length)g=TRUE*1.9;else{var an=0,na=Math.min(5,G.length);for(var z=0;z<na;z++)an+=Math.log(G[z]);g=Math.exp(.7*an/na+.3*Math.log(own))}}G.push(Math.min(MAXV-1,Math.round(g)))}
  x.clearRect(0,0,1920,1080);
  x.strokeStyle='rgba(230,240,245,.55)';x.lineWidth=5;x.beginPath();x.moveTo(320,380);x.lineTo(320,840);x.quadraticCurveTo(320,870,350,870);x.lineTo(610,870);x.quadraticCurveTo(640,870,640,840);x.lineTo(640,380);x.stroke();x.fillStyle='rgba(200,215,225,.25)';x.fillRect(310,350,340,30);
  for(var i=0;i<BE.length;i++){var b=BE[i];x.fillStyle=b[2];x.beginPath();x.ellipse(Math.max(340,Math.min(620,b[0])),b[1]+30,13,8,b[3],0,7);x.fill()}
  var H=[],NB=50,bw=MAXV/NB,mh=1;for(i=0;i<NB;i++)H.push(0);for(i=0;i<G.length;i++){var k=Math.floor(G[i]/bw);H[k]++;if(H[k]>mh)mh=H[k]}
  for(i=0;i<NB;i++){x.fillStyle='rgba(169,200,255,.75)';var hh=H[i]*Math.min(10,320/Math.max(mh,1));x.fillRect(X0+i*XW/NB,BASE-hh,XW/NB-2,hh)}
  x.strokeStyle='#c3cdd2';x.lineWidth=2;x.beginPath();x.moveTo(X0,BASE);x.lineTo(X0+XW,BASE);x.stroke();x.fillStyle='#c3cdd2';x.font='22px Helvetica,Arial';x.textAlign='center';for(var v=0;v<=MAXV;v+=500)x.fillText(nTR(v),X0+v/MAXV*XW,BASE+30);
  var m2=med(G),err=G.length?Math.abs(m2-TRUE)/TRUE*100:0,better=0;for(i=0;i<G.length;i++)if(Math.abs(G[i]-TRUE)<Math.abs(m2-TRUE))better++;var done=G.length>=N&&u>23;
  if(G.length){var mxp=X0+m2/MAXV*XW;x.strokeStyle='#ff9e7a';x.lineWidth=4;x.beginPath();x.moveTo(mxp,BASE);x.lineTo(mxp,BASE-420);x.stroke();x.fillStyle='#ff9e7a';x.font='26px Georgia';x.fillText('kalabalık · crowd: '+nTR(m2),mxp,BASE-430)}
  if(done){var tp=X0+TRUE/MAXV*XW;x.strokeStyle='#8fd3c1';x.lineWidth=4;x.setLineDash([10,8]);x.beginPath();x.moveTo(tp,BASE);x.lineTo(tp,BASE-360);x.stroke();x.setLineDash([]);x.fillStyle='#8fd3c1';x.fillText('gerçek · true: '+nTR(TRUE),tp,BASE-372)}
  x.textAlign='left';x.font='22px Georgia';x.fillStyle='#f3f1ec';x.fillText((mode?'2. tur: herkes önceki tahminleri duyuyor · Round 2: everyone hears the earlier guesses':'1. tur: herkes kendi başına · Round 1: everyone on their own')+' — tahmin · guesses: '+G.length,X0-40,345);
  var K=rd+'|'+done;if(K!==lk){lk=K;box.innerHTML='<div class="hzbox" style="padding:.6vw 1.8vw;max-width:88vw">'+(done?'<div class="a" style="font-size:1.5vw">Kalabalığın tahmini %'+err.toFixed(0)+' şaşıyor; 300 kişiden '+(mode?'':'yalnızca ')+better+' tanesi kalabalıktan daha iyi tahmin etti</div>':'<div class="a" style="font-size:1.5vw">Tek tek tahminler çok dağınık…</div>')+'<div class="e" style="font-size:1.05vw">'+(mode?'Herding: the first loud guess was far too high, and everyone leaned towards what they had heard. Kalabalık ancak herkes kendi kafasıyla düşündüğünde akıllıdır; birbirini taklit edince hata büyür · A crowd is only wise when each person thinks for themselves — once they copy each other, the error grows':'Single guesses are all over the place — but their middle value lands surprisingly close. Hatalar birbirini götürür: kimi çok fazla, kimi çok az der · The errors cancel out: some guess far too many, some far too few')+'</div></div>'}});return L};

/* calm night: star trails building up around the Pole Star above Black Sea hills and a lone wooden house (illustration, time-lapse) */
W.hzstartrail=function(L,it){var c=wCv(L),x=c.getContext('2d'),tc=document.createElement('canvas'),tx,PX=1240,PY=250,ST=[],i,TOT=it.tot||80,lt=-1,cyc=-1,HL=[],SY=820;tc.width=1920;tc.height=1080;tx=tc.getContext('2d');
 function rnd(s){return function(){s=(s*9301+49297)%233280;return s/233280}}var R=rnd(11);
 for(i=0;i<420;i++){var r=20+Math.pow(R(),.8)*1500,a=R()*6.283,b=R(),col=b<.15?'255,214,180':b<.35?'190,210,255':'240,244,255';ST.push([r,a,.25+R()*.75,col])}
 for(i=0;i<2;i++){var pts=[],p1=R()*6;for(var j=0;j<=96;j++){var xx=j*20;pts.push(640+i*80-90*Math.sin(xx/(600-i*150)+p1)-40*Math.sin(xx/170+p1*2))}HL.push(pts)}
 T(L,hd('Kutup Yıldızı Etrafında · Around the Pole Star — çizim · illustration, hayal ürünü · imagined, hızlandırılmış · time-lapse (sakin · calm)','Gece boyunca yıldızlar Kutup Yıldızı’nın çevresinde yavaşça yay çiziyor','All night long the stars slowly draw arcs around the Pole Star'),'top:44px',2);
 T(L,'<div class="sm" style="font-size:1.25vw;color:#cdd6dc">Aslında dönen gökyüzü değil, biziz: Dünya her saatte 15 derece döner. Kutup Yıldızı, Dünya’nın ekseninin tam ucunda durduğu için neredeyse hiç kımıldamaz<br><i>It is not the sky that turns — it is us: the Earth turns 15 degrees every hour. The Pole Star sits almost exactly above the Earth’s axis, so it barely moves</i></div>','bottom:40px',9);
 wLoop(L,function(t){var u=t%TOT,cy=Math.floor(t/TOT);if(cy!==cyc){cyc=cy;tx.clearRect(0,0,1920,1080);lt=-1}var w=.0105,ang=u*w,fade=u>TOT-6?(TOT-u)/6:1;
  if(lt>=0&&u<TOT-6){var a0=lt*w;tx.lineWidth=1.6;for(var k=0;k<ST.length;k++){var s=ST[k];tx.strokeStyle='rgba('+s[3]+','+(s[2]*.8).toFixed(2)+')';tx.beginPath();tx.arc(PX,PY,s[0],s[1]-a0,s[1]-ang,true);tx.stroke()}}lt=u;
  var g=x.createLinearGradient(0,0,0,SY);g.addColorStop(0,'#01030a');g.addColorStop(1,'#0f1a2e');x.fillStyle=g;x.fillRect(0,0,1920,1080);x.globalAlpha=fade;x.drawImage(tc,0,0);x.globalAlpha=1;
  for(k=0;k<ST.length;k++){var s2=ST[k],aa=s2[1]-ang;x.fillStyle='rgba('+s2[3]+','+s2[2].toFixed(2)+')';x.fillRect(PX+Math.cos(aa)*s2[0]-1,PY+Math.sin(aa)*s2[0]-1,2.4,2.4)}
  x.fillStyle='#fff';x.beginPath();x.arc(PX,PY,4,0,7);x.fill();var pg=x.createRadialGradient(PX,PY,0,PX,PY,30);pg.addColorStop(0,'rgba(220,230,255,.5)');pg.addColorStop(1,'rgba(220,230,255,0)');x.fillStyle=pg;x.fillRect(PX-30,PY-30,60,60);
  for(var l=0;l<HL.length;l++){var sh=8+l*7;x.fillStyle='rgb('+sh+','+(sh+5)+','+(sh+10)+')';x.beginPath();x.moveTo(0,SY);for(var q=0;q<HL[l].length;q++)x.lineTo(q*20,HL[l][q]);x.lineTo(1920,SY);x.closePath();x.fill()}
  var hq=15;for(var q3=15;q3<60;q3++)if(HL[1][q3]<HL[1][hq])hq=q3;var hx=hq*20,hy=HL[1][hq]+14;x.fillStyle='#1c2230';x.fillRect(hx-40,hy-34,80,40);x.beginPath();x.moveTo(hx-50,hy-34);x.lineTo(hx,hy-66);x.lineTo(hx+50,hy-34);x.fill();var wl=.75+.08*Math.sin(t*.9);x.fillStyle='rgba(255,214,160,'+wl.toFixed(2)+')';x.fillRect(hx-22,hy-22,13,14);var gl=x.createRadialGradient(hx-15,hy-15,0,hx-15,hy-15,40);gl.addColorStop(0,'rgba(255,210,150,.25)');gl.addColorStop(1,'rgba(255,210,150,0)');x.fillStyle=gl;x.fillRect(hx-55,hy-55,80,80);
  var wg=x.createLinearGradient(0,SY,0,1080);wg.addColorStop(0,'#0c1526');wg.addColorStop(1,'#02040a');x.fillStyle=wg;x.fillRect(0,SY,1920,260);
  for(var yy=SY+5;yy<1080;yy+=7){x.fillStyle='rgba(150,170,210,'+(.05+.04*Math.sin(t*.6+yy*.21)).toFixed(3)+')';x.fillRect(0,yy+Math.sin(t*.7+yy*.3)*1.5,1920,1.5)}});return L};


/* ---------- v78 addition: hzglowworm (calm night, imagined glowworm cave) ---------- */
W.hzglowworm=function(L,it){var c=wCv(L),x=c.getContext('2d'),N=it.n||320,G=[],i,HY=660,TH=[],RIV=720;
 T(L,hd('Hayal ürünü · Imagined — çizim · illustration (sakin · calm)','Tavanda, minik larvaların mavi-yeşil ışıkları bir yıldız gökyüzü gibi asılı duruyor','On the ceiling, the blue-green lights of tiny larvae hang like a sky of stars'),'top:40px',2);
 T(L,'<div class="sm" style="font-size:1.25vw;color:#cdd6dc">Işık, avını çekmek için yanar. Yapışkan ipek iplikler tavandan suya doğru sarkar; bunlar ateşböceği değil, mağarada yaşayan larvalardır<br><i>The light is a lure. Sticky silk threads hang from the ceiling toward the water — these are cave-dwelling larvae, not fireflies</i></div>','bottom:36px',8);
 for(i=0;i<N;i++){var yy=40+Math.pow(Math.random(),.7)* (HY-80);G.push({x:80+Math.random()*1760,y:yy,p:Math.random()*6.283,w:.35+Math.random()*1.1,r:.8+Math.random()*1.8,a:.35+Math.random()*.65,th:Math.random()<.16?1:0})}
 for(i=0;i<14;i++)TH.push({x:200+Math.random()*1520,y:80+Math.random()*280,l:80+Math.random()*220});
 wLoop(L,function(t){var g,k,a,xx,yy,gl;
  g=x.createLinearGradient(0,0,0,HY);g.addColorStop(0,'#050308');g.addColorStop(.55,'#0a0810');g.addColorStop(1,'#07060c');x.fillStyle=g;x.fillRect(0,0,1920,1080);
  x.fillStyle='#08060a';x.beginPath();x.moveTo(0,HY+20);x.quadraticCurveTo(300,HY-90,640,HY-20);x.quadraticCurveTo(980,HY+50,1280,HY-40);x.quadraticCurveTo(1580,HY-100,1920,HY+10);x.lineTo(1920,0);x.lineTo(0,0);x.closePath();x.fill();
  x.fillStyle='rgba(18,16,22,.55)';x.beginPath();x.moveTo(0,0);x.lineTo(0,220);x.quadraticCurveTo(400,40,900,160);x.quadraticCurveTo(1400,30,1920,200);x.lineTo(1920,0);x.closePath();x.fill();
  var wg=x.createLinearGradient(0,RIV,0,1080);wg.addColorStop(0,'#070810');wg.addColorStop(1,'#03040a');x.fillStyle=wg;x.fillRect(0,RIV,1920,1080-RIV);
  x.strokeStyle='rgba(40,70,80,.18)';x.lineWidth=1;
  for(k=0;k<TH.length;k++){xx=TH[k].x;yy=TH[k].y;x.beginPath();x.moveTo(xx,yy);x.lineTo(xx+Math.sin(t*.15+k)*2,yy+TH[k].l);x.stroke()}
  x.save();x.globalCompositeOperation='lighter';
  for(i=0;i<N;i++){var s=G[i];a=s.a*(.25+.75*(.5+.5*Math.sin(t*s.w+s.p)));a=Math.max(0,Math.min(1,a));
   gl=x.createRadialGradient(s.x,s.y,0,s.x,s.y,s.r*10);gl.addColorStop(0,'rgba(140,245,230,'+(a*.9).toFixed(3)+')');gl.addColorStop(.35,'rgba(70,200,210,'+(a*.35).toFixed(3)+')');gl.addColorStop(1,'rgba(40,160,180,0)');
   x.fillStyle=gl;x.beginPath();x.arc(s.x,s.y,s.r*10,0,7);x.fill();
   x.fillStyle='rgba(210,255,245,'+(a*.95).toFixed(3)+')';x.beginPath();x.arc(s.x,s.y,s.r,0,7);x.fill();
   if(s.th){var ry=RIV+30+(s.y*.08)+Math.sin(t*.2+s.p)*1.5,ra=a*.22;x.fillStyle='rgba(90,210,210,'+ra.toFixed(3)+')';x.beginPath();x.ellipse(s.x,ry,s.r*3.2,s.r*1.1,0,0,7);x.fill()}}
  x.restore();
  x.strokeStyle='rgba(80,120,140,'+(0.07+.03*Math.sin(t*.4)).toFixed(3)+')';x.lineWidth=1.2;x.beginPath();
  for(xx=0;xx<=1920;xx+=30){yy=RIV+4+Math.sin(xx*.004+t*.15)*1.6;xx?x.lineTo(xx,yy):x.moveTo(xx,yy)}x.stroke()
 });return L};



/* ---------- v79 additions: hzdoublepend (living art), hzhanoi hzwalk (clever thinking), hzbenham hzenigma (illusions), hzwhale (calm night) ---------- */
/* double pendulum chaos: three double pendulums released from almost the same angle (differences of 0.001 rad) drift apart within seconds */
W.hzdoublepend=function(L,it){L.style.background='#05080c';var c=wCv(L),x=c.getContext('2d'),tr=document.createElement('canvas'),tx,CX=960,CY=330,L1=210,L2=210,G=9.81,P=[],T0=-1,DUR=it.dur||45,box=T(L,'','bottom:12px',1),lk='',COL=['120,200,230','230,120,100','160,220,140'];tr.width=1920;tr.height=1080;tx=tr.getContext('2d');
 T(L,'<div class="hzbox">'+hd('Yaşayan Sanat · Living Art — çift sarkaç simülasyonu · double pendulum simulation','Üç çift sarkaç, neredeyse aynı açıdan bırakıldı. Ne kadar süre birlikte sallanacaklar?','Three double pendulums released from almost the same angle — how long will they swing together?')+'</div>','top:12px',.4);
 function start(t){T0=t;tx.clearRect(0,0,1920,1080);var a=2.2+Math.random()*.6;P=[];for(var i=0;i<3;i++)P.push({a1:a+i*.001,a2:a+.3+i*.001,w1:0,w2:0,px:null,py:null})}
 function der(s){var d=s[0]-s[1],den=2-Math.cos(2*d),w1=s[2],w2=s[3];
  var dw1=(-G*3*Math.sin(s[0])-G*Math.sin(s[0]-2*s[1])-2*Math.sin(d)*(w2*w2*1+w1*w1*Math.cos(d)))/(1*den),
      dw2=(2*Math.sin(d)*(w1*w1*2+G*2*Math.cos(s[0])+w2*w2*Math.cos(d)))/(1*den);return [w1,w2,dw1,dw2]}
 function rk(p,h){var s=[p.a1,p.a2,p.w1,p.w2],k1=der(s),k2=der(s.map(function(v,i){return v+k1[i]*h/2})),k3=der(s.map(function(v,i){return v+k2[i]*h/2})),k4=der(s.map(function(v,i){return v+k3[i]*h}));
  s=s.map(function(v,i){return v+h/6*(k1[i]+2*k2[i]+2*k3[i]+k4[i])});p.a1=s[0];p.a2=s[1];p.w1=s[2];p.w2=s[3]}
 wLoop(L,function(t){if(T0<0||t-T0>DUR)start(t);var u=t-T0,i,k,p;tx.fillStyle='rgba(5,8,12,.018)';tx.fillRect(0,0,1920,1080);
  for(i=0;i<3;i++){p=P[i];for(k=0;k<8;k++)rk(p,.004);var x1=CX+L1*Math.sin(p.a1),y1=CY+L1*Math.cos(p.a1),x2=x1+L2*Math.sin(p.a2),y2=y1+L2*Math.cos(p.a2);
   if(p.px!==null){tx.strokeStyle='rgba('+COL[i]+',.75)';tx.lineWidth=2;tx.beginPath();tx.moveTo(p.px,p.py);tx.lineTo(x2,y2);tx.stroke()}p.px=x2;p.py=y2;p.x1=x1;p.y1=y1}
  x.fillStyle='#05080c';x.fillRect(0,0,1920,1080);x.drawImage(tr,0,0);
  for(i=0;i<3;i++){p=P[i];x.strokeStyle='rgba('+COL[i]+',.95)';x.lineWidth=4;x.beginPath();x.moveTo(CX,CY);x.lineTo(p.x1,p.y1);x.lineTo(p.px,p.py);x.stroke();x.fillStyle='rgb('+COL[i]+')';x.beginPath();x.arc(p.x1,p.y1,10,0,7);x.fill();x.beginPath();x.arc(p.px,p.py,14,0,7);x.fill()}
  x.fillStyle='#dfe6ea';x.beginPath();x.arc(CX,CY,7,0,7);x.fill();
  var K=Math.floor(u/6);if(K!==lk){lk=K;box.innerHTML='<div class="hzbox" style="padding:.6vw 1.8vw;max-width:88vw"><div class="a" style="font-size:1.45vw">Başlangıç farkı: 0,001 radyan (yaklaşık 0,06°) · Starting difference: 0.001 rad (about 0.06°) — geçen süre · elapsed: '+Math.floor(u)+' sn · s</div><div class="e" style="font-size:1.05vw">Kurallar tamamen belirli, içinde hiç rastlantı yok. Yine de başlangıçtaki minicik fark her salınımda büyüyor ve birkaç saniye sonra üç sarkaç bambaşka yollara sapıyor. Buna kaos denir: hava durumunu iki haftadan uzun tahmin etmenin zor olmasının nedeni de bu · The rules are fully fixed, with no chance in them. Yet the tiny starting difference grows with every swing, and within seconds the three go their own ways. This is chaos — and the reason weather is hard to forecast beyond about two weeks</div></div>'}});return L};

/* Tower of Hanoi: discs moved one at a time, never a bigger disc on a smaller one; minimum 2^n - 1 moves */
W.hzhanoi=function(L,it){grad(L,'#1c2a30','#060a0c');var c=wCv(L),x=c.getContext('2d'),N=it.n||6,MV=[],PG,T0=-1,SP=it.sp||.45,box=T(L,'','bottom:12px',1),lk='',PX=[460,960,1460],BY=820,DH=46,COL=['#5fa8c8','#6fbfa0','#c87a5a','#8a90d0','#d0a0b8','#7aa0b0','#a8c870','#c8c8c8'];
 T(L,'<div class="hzbox">'+hd('Zekice Düşünce · Clever Thinking — Hanoi Kulesi · Tower of Hanoi','Bütün diskleri sağdaki çubuğa taşı: her seferinde tek disk, büyük disk asla küçüğün üstüne konmaz','Move every disc to the right-hand peg — one disc at a time, never a bigger disc on a smaller one')+'</div>','top:12px',.4);
 function hn(n,a,b,cc){if(!n)return;hn(n-1,a,cc,b);MV.push([a,b]);hn(n-1,cc,b,a)}
 function start(t){T0=t;MV=[];hn(N,0,2,1);PG=[[],[],[]];for(var i=N;i>=1;i--)PG[0].push(i)}
 function disc(sz,cx,y){var w=60+sz*(300/N);x.fillStyle=COL[(sz-1)%COL.length];x.beginPath();x.roundRect?x.roundRect(cx-w/2,y-DH+4,w,DH-6,14):x.rect(cx-w/2,y-DH+4,w,DH-6);x.fill();x.fillStyle='rgba(255,255,255,.18)';x.fillRect(cx-w/2+10,y-DH+8,w-20,6)}
 wLoop(L,function(t){if(T0<0)start(t);var u=t-T0,tot=MV.length,m=Math.floor(u/SP),f=(u/SP)-m,i,j;
  if(m>tot+10/SP){N=N>=7?5:N+1;start(t);u=0;m=0;f=0;tot=MV.length}
  var pg=[[],[],[]];for(i=N;i>=1;i--)pg[0].push(i);var mm=Math.min(m,tot);for(i=0;i<mm;i++){var mv=MV[i];pg[mv[1]].push(pg[mv[0]].pop())}
  var fly=null;if(m<tot){var mv2=MV[m],sz=pg[mv2[0]][pg[mv2[0]].length-1];pg[mv2[0]].pop();var y0=BY-pg[mv2[0]].length*DH,y1=BY-pg[mv2[1]].length*DH,e=f*f*(3-2*f),top=BY-(N+2)*DH;
   var cx,cy;if(e<.33){cx=PX[mv2[0]];cy=y0+(top-y0)*(e/.33)}else if(e<.66){cx=PX[mv2[0]]+(PX[mv2[1]]-PX[mv2[0]])*((e-.33)/.33);cy=top}else{cx=PX[mv2[1]];cy=top+(y1-top)*((e-.66)/.34)}fly=[sz,cx,cy]}
  x.clearRect(0,0,1920,1080);x.fillStyle='#3a4a50';x.fillRect(260,BY,1400,18);for(i=0;i<3;i++){x.fillStyle='#55666c';x.fillRect(PX[i]-8,BY-(N+1)*DH-10,16,(N+1)*DH+10)}
  for(i=0;i<3;i++)for(j=0;j<pg[i].length;j++)disc(pg[i][j],PX[i],BY-j*DH);if(fly)disc(fly[0],fly[1],fly[2]);
  var K=N+'|'+mm;if(K!==lk){lk=K;box.innerHTML='<div class="hzbox" style="padding:.6vw 1.8vw;max-width:88vw"><div class="a" style="font-size:1.5vw">'+N+' disk · discs — hamle · move '+mm+' / '+tot+' (en az · minimum 2<sup>'+N+'</sup> − 1 = '+tot+')</div><div class="e" style="font-size:1.05vw">Sır: en büyük diski taşımak için önce üstündeki '+(N-1)+' diski ortadaki çubuğa park et, büyüğü taşı, sonra o '+(N-1)+' diski üstüne geri getir. Her yeni disk hamle sayısını iki katına çıkarır (+1) · The secret: to move the biggest disc, first park the '+(N-1)+' above it on the middle peg, move the big one, then bring the '+(N-1)+' back on top. Each extra disc doubles the number of moves (+1)</div></div>'}});return L};

/* random walks: coin-flip steps; after N steps a walker is typically about sqrt(N) steps from the start */
W.hzwalk=function(L,it){L.style.background='#070a0e';var c=wCv(L),x=c.getContext('2d'),tr=document.createElement('canvas'),tx,CX=960,CY=600,S=it.s||5,NW=6,NH=400,W6=[],HX,HY,n=0,T0=-1,DUR=it.dur||50,box=T(L,'','bottom:12px',1),lk='',COL=['120,200,230','230,130,110','160,220,140','210,170,230','240,220,150','120,220,210'];tr.width=1920;tr.height=1080;tx=tr.getContext('2d');
 T(L,'<div class="hzbox">'+hd('Zekice Düşünce · Clever Thinking — rastgele yürüyüş · random walk','Her adımda yazı-tura: kuzey, güney, doğu ya da batı. Bir yürüyüşçü ne kadar uzağa gider?','A coin toss at every step — north, south, east or west. How far does a walker get?')+'</div>','top:12px',.4);
 function start(t){T0=t;n=0;tx.clearRect(0,0,1920,1080);W6=[];for(var i=0;i<NW;i++)W6.push([0,0]);HX=new Int32Array(NH);HY=new Int32Array(NH)}
 var D=[[1,0],[-1,0],[0,1],[0,-1]];
 wLoop(L,function(t){if(T0<0||t-T0>DUR)start(t);var u=t-T0,i,k,st=u<DUR-6?6:0;
  for(k=0;k<st;k++){n++;for(i=0;i<NW;i++){var d=D[Math.random()*4|0],ox=W6[i][0],oy=W6[i][1];W6[i][0]+=d[0];W6[i][1]+=d[1];tx.strokeStyle='rgba('+COL[i]+',.55)';tx.lineWidth=2;tx.beginPath();tx.moveTo(CX+ox*S,CY+oy*S);tx.lineTo(CX+W6[i][0]*S,CY+W6[i][1]*S);tx.stroke()}
   for(i=0;i<NH;i++){var dd=D[Math.random()*4|0];HX[i]+=dd[0];HY[i]+=dd[1]}}
  var s2=0;for(i=0;i<NH;i++)s2+=HX[i]*HX[i]+HY[i]*HY[i];var rms=Math.sqrt(s2/NH);
  x.fillStyle='#070a0e';x.fillRect(0,0,1920,1080);x.strokeStyle='rgba(220,230,235,.35)';x.setLineDash([10,10]);x.lineWidth=2;x.beginPath();x.arc(CX,CY,Math.sqrt(n)*S,0,7);x.stroke();x.setLineDash([]);x.drawImage(tr,0,0);
  for(i=0;i<NW;i++){x.fillStyle='rgb('+COL[i]+')';x.beginPath();x.arc(CX+W6[i][0]*S,CY+W6[i][1]*S,8,0,7);x.fill()}x.fillStyle='#fff';x.beginPath();x.arc(CX,CY,6,0,7);x.fill();
  var K=Math.floor(u/3);if(K!==lk){lk=K;box.innerHTML='<div class="hzbox" style="padding:.6vw 1.8vw;max-width:88vw"><div class="a" style="font-size:1.45vw">Adım · steps: '+nTR(n)+' — √adım · √steps: '+Math.sqrt(n).toFixed(1)+' — 400 yürüyüşçünün ortalama uzaklığı · typical distance of 400 walkers: '+rms.toFixed(1)+'</div><div class="e" style="font-size:1.05vw">Kesikli çember √N adım yarıçaplı. 100 adım atan biri çoğu zaman başlangıçtan yalnızca 10 adım kadar uzaklaşır; 10.000 adımda 100 adım. Rastlantı ilerler ama çok yavaş · The dashed circle has a radius of √N steps. Someone who takes 100 random steps usually ends up only about 10 steps from the start; after 10,000 steps, about 100. Chance does get somewhere — just very slowly</div></div>'}});return L};

/* Benham's top: a black-and-white disc that shows faint colours when it spins */
W.hzbenham=function(L,it){grad(L,'#2a2c30','#0a0b0c');var c=wCv(L),x=c.getContext('2d'),CX=960,CY=590,R=330,A=10,B=26,ang=0,lt=-1,box=T(L,'','bottom:12px',1),lk='';
 T(L,'<div class="hzbox">'+hd('Göz Oyunu · Optical Illusion — Benham topacı · Benham’s top','Bu diskte yalnızca siyah ve beyaz var. Dönmeye başlayınca halkalara bak','There is only black and white on this disc — watch the rings once it starts to spin')+'</div>','top:12px',.4);
 function draw(){x.save();x.translate(CX,CY);x.rotate(ang);x.fillStyle='#f4f4f2';x.beginPath();x.arc(0,0,R,0,7);x.fill();x.fillStyle='#000';x.beginPath();x.moveTo(0,0);x.arc(0,0,R,Math.PI,2*Math.PI);x.closePath();x.fill();
  x.strokeStyle='#000';x.lineWidth=9;for(var g=0;g<4;g++)for(var r=0;r<3;r++){var rr=R*(.32+g*.17+r*.045),a0=g*Math.PI/4;x.beginPath();x.arc(0,0,rr,a0,a0+Math.PI/4);x.stroke()}
  x.restore();x.strokeStyle='rgba(255,255,255,.25)';x.lineWidth=2;x.beginPath();x.arc(CX,CY,R+2,0,7);x.stroke()}
 wLoop(L,function(t){var u=t%(A+B),spin=u>=A,dt=lt<0?0:Math.min(.1,t-lt);lt=t;if(spin){var sp=Math.min(1,(u-A)/3)*2*Math.PI*6;ang+=sp*dt}
  x.clearRect(0,0,1920,1080);draw();
  var K=String(spin);if(K!==lk){lk=K;box.innerHTML='<div class="hzbox" style="padding:.6vw 1.8vw;max-width:86vw">'+(spin?'<div class="a" style="font-size:1.55vw">Halkalarda soluk renkler görüyor musun? Mavimsi, kırmızımsı, kahverengimsi…</div><div class="e" style="font-size:1.05vw">Do you see faint colours in the rings — bluish, reddish, brownish? Herkes görmez, görenlerin renkleri de birbirinden farklı olabilir. Açıklama hâlâ tartışılıyor; en yaygın görüş, gözdeki renk algılayıcılarının ışığa farklı hızlarda tepki vermesi. İngiliz oyuncakçı Charles Benham bu topacı 1894’te sattı · Not everyone sees them, and people may see different colours. The cause is still debated — the leading idea is that the eye’s colour receptors respond to flashes at different speeds. English toymaker Charles Benham sold this top in 1894</div>':'<div class="a" style="font-size:1.55vw">Yarısı siyah, yarısı beyaz üzerinde ince siyah yaylar: başka hiçbir renk yok</div><div class="e" style="font-size:1.05vw">Half black, half white with thin black arcs — no other colour at all. Az sonra dönmeye başlayacak · It will start spinning in a moment</div>')+'</div>'}});return L};

/* Leviant's Enigma: a still image of radiating lines and plain rings in which many people see streaming motion */
W.hzenigma=function(L,it){grad(L,'#24262c','#08090b');var c=wCv(L),x=c.getContext('2d'),CX=960,CY=600,R=400,NL=it.nl||120,i,done=0;
 T(L,'<div class="hzbox">'+hd('Göz Oyunu · Optical Illusion — Leviant’ın “Enigma”sı · Leviant’s “Enigma”','Ortadaki noktaya birkaç saniye bak: halkaların içinde bir şey akıyor mu?','Look at the centre dot for a few seconds — does anything flow inside the rings?')+'</div>','top:12px',.4);
 T(L,'<div class="hzbox" style="padding:.6vw 1.8vw;max-width:86vw"><div class="a" style="font-size:1.45vw">Resim tamamen durgun: hiçbir piksel hareket etmiyor</div><div class="e" style="font-size:1.05vw">The picture is completely still — not one pixel moves. Yine de birçok kişi halkalarda dönen, parıldayan akıntılar görür. Fransız sanatçı Isia Leviant 1981’de yaptı. Bir araştırma bunu, gözün farkına varmadan yaptığı minik sıçramalara (mikrosakkadlar) bağladı; konu hâlâ tartışılıyor · Still, many people see shimmering streams circling in the rings. French artist Isia Leviant made it in 1981. One study linked it to the tiny jumps the eye makes without our noticing (microsaccades) — the question is still debated</div></div>','bottom:12px',1.2);
 wLoop(L,function(t){if(done)return;done=1;x.clearRect(0,0,1920,1080);x.fillStyle='#f6f6f4';x.beginPath();x.arc(CX,CY,R,0,7);x.fill();x.fillStyle='#000';
  for(i=0;i<NL;i++){var a0=i*2*Math.PI/NL,a1=a0+Math.PI/NL;x.beginPath();x.moveTo(CX,CY);x.arc(CX,CY,R,a0,a1);x.closePath();x.fill()}
  [[.34,.42],[.6,.68],[.86,.94]].forEach(function(b){x.fillStyle='#3a5fb0';x.beginPath();x.arc(CX,CY,R*b[1],0,7);x.arc(CX,CY,R*b[0],0,7,true);x.fill()});
  x.fillStyle='#f6f6f4';x.beginPath();x.arc(CX,CY,R*.12,0,7);x.fill();x.fillStyle='#c03030';x.beginPath();x.arc(CX,CY,7,0,7);x.fill()});return L};

/* calm night: imagined humpback mother and calf gliding through moonlit blue water */
W.hzwhale=function(L,it){var c=wCv(L),x=c.getContext('2d'),P=[],i,DUR=it.dur||110;
 T(L,hd('Hayal ürünü · Imagined — çizim · illustration (sakin · calm)','Ay ışığında bir kambur balina annesi ve yavrusu, derin mavide ağır ağır süzülüyor','In the moonlight a humpback mother and her calf glide slowly through the deep blue'),'top:40px',2);
 T(L,'<div class="sm" style="font-size:1.25vw;color:#cdd6dc">Yavru, annesine çok yakın yüzer; ikisi zaman zaman fısıltıya benzeyen kısık seslerle haberleşir<br><i>The calf swims very close to its mother — the two keep in touch with soft, quiet calls</i></div>','bottom:36px',8);
 for(i=0;i<160;i++)P.push({x:Math.random()*1920,y:Math.random()*1080,r:.6+Math.random()*1.8,v:3+Math.random()*8,p:Math.random()*6.28});
 function whale(cx,cy,s,t,a){x.save();x.translate(cx,cy);x.scale(s,s);x.rotate(Math.sin(t*.25)*.03);x.globalAlpha=a;var fl=Math.sin(t*.9)*12;
  var g=x.createLinearGradient(0,-60,0,70);g.addColorStop(0,'#3a5c72');g.addColorStop(1,'#1a3344');x.fillStyle=g;
  x.beginPath();x.moveTo(-240,0);x.bezierCurveTo(-200,-62,40,-70,170,-30);x.bezierCurveTo(230,-12,260,-4,300,fl*.6);x.bezierCurveTo(255,10,210,30,160,40);x.bezierCurveTo(30,72,-180,60,-240,0);x.closePath();x.fill();
  x.beginPath();x.moveTo(295,fl*.6);x.quadraticCurveTo(330,-40+fl,360,-58+fl);x.quadraticCurveTo(340,fl*.6,365,48+fl);x.quadraticCurveTo(330,30+fl,295,fl*.6);x.fill();
  x.fillStyle='#284556';x.beginPath();x.moveTo(-120,32);x.quadraticCurveTo(-60,120+Math.sin(t*.5)*10,10,170+Math.sin(t*.5)*14);x.quadraticCurveTo(-30,110,-70,40);x.closePath();x.fill();
  x.fillStyle='rgba(180,215,230,.22)';x.beginPath();x.ellipse(-60,-34,150,10,-.05,0,7);x.fill();x.restore()}
 wLoop(L,function(t){var g=x.createLinearGradient(0,0,0,1080);g.addColorStop(0,'#123a52');g.addColorStop(.45,'#082436');g.addColorStop(1,'#020a12');x.fillStyle=g;x.fillRect(0,0,1920,1080);
  x.save();x.globalCompositeOperation='lighter';for(i=0;i<6;i++){var bx=500+i*190+Math.sin(t*.07+i)*40,a=.05+.03*Math.sin(t*.2+i*1.7);var rg=x.createLinearGradient(0,0,0,900);rg.addColorStop(0,'rgba(160,210,230,'+a.toFixed(3)+')');rg.addColorStop(1,'rgba(160,210,230,0)');x.fillStyle=rg;x.beginPath();x.moveTo(bx-30,0);x.lineTo(bx+30,0);x.lineTo(bx+170,900);x.lineTo(bx+40,900);x.closePath();x.fill()}x.restore();
  var u=(t%DUR)/DUR,fade=Math.min(1,Math.min(u,1-u)*8),wx=2400-u*2900;whale(wx,560+Math.sin(t*.12)*20,1.25,t,fade);whale(wx+120,660+Math.sin(t*.12+.8)*18,.55,t+1.3,fade);
  for(i=0;i<P.length;i++){var q=P[i];q.y-=q.v*.016;if(q.y<-5){q.y=1085;q.x=Math.random()*1920}x.fillStyle='rgba(190,220,235,'+(.25+.2*Math.sin(t+q.p)).toFixed(3)+')';x.beginPath();x.arc(q.x+Math.sin(t*.3+q.p)*6,q.y,q.r,0,7);x.fill()}
 });return L};


/* ---------- v80 additions: hzpenrose (living art) ---------- */
/* Penrose P3 tiling by Robinson-triangle subdivision: each round splits every piece into smaller copies; the pattern never repeats, and thick:thin tiles approach the golden ratio */
W.hzpenrose=function(L,it){L.style.background='#0a0d12';var c=wCv(L),x=c.getContext('2d'),G=(1+Math.sqrt(5))/2,CX=960,CY=560,R=1250,GEN=[],MAXG=it.g||7,STEP=it.step||5.2,box=T(L,'','bottom:12px',1),lk=-1,gi=-1,painted=0,order=null;
 T(L,'<div class="hzbox">'+hd('Yaşayan Sanat · Living Art — Penrose döşemesi · Penrose tiling','Sadece iki şekil: kalın ve ince bir eşkenar dörtgen. Sonsuza kadar döşenir ama desen asla kendini tekrar etmez','Just two shapes, a thick and a thin rhombus. They tile forever, yet the pattern never repeats itself')+'</div>','top:12px',.4);
 var T0=[];for(var i=0;i<10;i++){var a1=(2*i-1)*Math.PI/10,a2=(2*i+1)*Math.PI/10,B=[Math.cos(a1),Math.sin(a1)],C=[Math.cos(a2),Math.sin(a2)];if(i%2==0){var tmp=B;B=C;C=tmp}T0.push([0,[0,0],B,C])}
 function lerp(p,q,f){return [p[0]+(q[0]-p[0])*f,p[1]+(q[1]-p[1])*f]}
 function sub(T){var o=[];for(var i=0;i<T.length;i++){var t=T[i],A=t[1],B=t[2],C=t[3];if(t[0]==0){var P=lerp(A,B,1/G);o.push([0,C,P,B]);o.push([1,P,C,A])}else{var Q=lerp(B,A,1/G),Rr=lerp(B,C,1/G);o.push([1,Rr,C,A]);o.push([1,Q,Rr,B]);o.push([0,Rr,Q,A])}}return o}
 GEN.push(T0);for(var g=1;g<=MAXG;g++)GEN.push(sub(GEN[g-1]));
 function rnd(s){return function(){s=(s*9301+49297)%233280;return s/233280}}
 var PALS=[['#e9dfcb','#2b7a80'],['#f0e6d6','#b4573c'],['#dfe8ea','#3c5f8f']];
 function prep(g){var T=GEN[g],r=rnd(g*7+3),o=[];for(var i=0;i<T.length;i++){var t=T[i],mx=(t[1][0]+t[2][0]+t[3][0])/3,my=(t[1][1]+t[2][1]+t[3][1])/3;o.push([Math.sqrt(mx*mx+my*my)+r()*.04,t,r()])}o.sort(function(a,b){return a[0]-b[0]});return o}
 function tile(e,g,pal){var t=e[1],A=t[1],B=t[2],C=t[3],v=e[2];x.beginPath();x.moveTo(CX+A[0]*R,CY+A[1]*R);x.lineTo(CX+B[0]*R,CY+B[1]*R);x.lineTo(CX+C[0]*R,CY+C[1]*R);x.closePath();
  x.globalAlpha=t[0]==0?.86+v*.14:.8+v*.2;x.fillStyle=t[0]==0?pal[0]:pal[1];x.fill();x.globalAlpha=1;
  x.strokeStyle='rgba(10,13,18,.85)';x.lineWidth=Math.max(.8,3.4-g*.38);x.beginPath();x.moveTo(CX+C[0]*R,CY+C[1]*R);x.lineTo(CX+A[0]*R,CY+A[1]*R);x.lineTo(CX+B[0]*R,CY+B[1]*R);x.stroke()}
 var cyc=0,pal=PALS[0];
 wLoop(L,function(t){var tot=STEP*MAXG+10,u=t%tot,k=Math.floor(t/tot),g=Math.min(MAXG,1+Math.floor(u/STEP));if(k!==cyc){cyc=k;pal=PALS[k%PALS.length]}
  if(g!==gi||k*100+g!==lk){gi=g;lk=k*100+g;order=prep(g);painted=0;
   var thick=0,thin=0;for(var i=0;i<GEN[g].length;i++){if(GEN[g][i][0]==1)thick++;else thin++}
   box.innerHTML='<div class="hzbox" style="padding:.6vw 1.8vw;max-width:88vw"><div class="a" style="font-size:1.45vw">Bölme · Subdivision '+g+' — parça · pieces: '+nTR(GEN[g].length)+' — kalın ÷ ince · thick ÷ thin: '+(thick/Math.max(1,thin)).toFixed(3)+' → φ ≈ 1.618</div><div class="e" style="font-size:1.05vw">Her turda her parça, altın oranla küçülmüş kopyalarına bölünüyor. Roger Penrose bu deseni 1974’te buldu; 1982’de Dan Shechtman doğada aynı “tekrarsız düzene” sahip kristalleri keşfetti ve 2011’de Nobel aldı · Each round splits every piece into copies shrunk by the golden ratio. Roger Penrose found this pattern in 1974; in 1982 Dan Shechtman discovered real crystals with the same never-repeating order, and won the 2011 Nobel Prize</div></div>'}
  var want=Math.min(order.length,Math.ceil(order.length*Math.min(1,(u-(g-1)*STEP)/(STEP*.6))));
  if(u>=STEP*MAXG)want=order.length;
  var lim=Math.min(want,painted+1400);for(;painted<lim;painted++)tile(order[painted],g,pal)});return L};


/* muted looping YouTube footage. it: yt, start, f (poster still if the TV cannot play the embed), tr, en, cr */
W.hzvideo=function(L,it){
 L.style.background='#000';
 if(it.f){var m=wEl('img','');m.src=it.f;
  m.style.cssText='position:absolute;top:0;left:0;width:100%;height:100%;object-fit:'+(it.fit||'cover')+';object-position:'+(it.pos||'50% 50%')+';filter:brightness('+(it.dim==null?0.85:it.dim)+')';
  L.appendChild(m)}
 var wrap=wEl('div','');
 wrap.style.cssText='position:absolute;top:50%;left:50%;width:177.78vh;height:100vh;min-width:100vw;min-height:56.25vw;transform:translate(-50%,-50%);overflow:hidden;pointer-events:none';
 var id=it.yt,st=it.start||0;
 var src='https://www.youtube-nocookie.com/embed/'+id+'?autoplay=1&mute=1&controls=0&disablekb=1&fs=0&iv_load_policy=3&modestbranding=1&playsinline=1&rel=0&loop=1&playlist='+id+'&start='+st;
 var fr=document.createElement('iframe');
 fr.setAttribute('src',src);fr.setAttribute('allow','autoplay; encrypted-media');fr.setAttribute('frameborder','0');fr.setAttribute('title','');
 fr.style.cssText='position:absolute;top:50%;left:50%;width:120%;height:120%;border:0;transform:translate(-50%,-50%);pointer-events:none';
 wrap.appendChild(fr);L.appendChild(wrap);
 if(it.tr||it.cr){
  var op=it.capop==null?0.34:it.capop;
  var html='<div style="opacity:'+op+';font-family:Helvetica,Arial,sans-serif;text-align:left;text-shadow:0 1px 10px rgba(0,0,0,.8)">';
  if(it.tr) html+='<div style="font-size:1.05vw;letter-spacing:.08em;color:#e8eef2;font-weight:400">'+it.tr+(it.en?' <span style="font-style:italic;opacity:.8">· '+it.en+'</span>':'')+'</div>';
  if(it.cr) html+='<div style="font-size:.68vw;color:#c5ced4;margin-top:.35vh;letter-spacing:.04em">'+it.cr+'</div>';
  html+='</div>';
  L.appendChild(wEl('div','',html,'position:absolute;left:3vw;right:3vw;bottom:2.6vh;top:auto;text-align:left;z-index:2;pointer-events:none'))}
 L.tri='fade';L.dur=it.d;L.corner=false;return L};

})();
