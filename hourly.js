/* hourly.js v63 — reusable scene library for the hourly day schedules (days/YYYY-MM-DD.json). ES5 only. Requires wow.js helpers (wEl, wCv, wLoop, WOW).
   Data-driven templates: hzphoto hzquote hzriddle hzsteps hzfact.  Living art: hzpend hzgalton hzharmono hzphyllo hzboids hzfourier hzripple hzmonte hzulam hzfirefly hzsleep.
   Illusions: hzcafe hzebb hzkaniz hzlilac hzstep hzhermann hzafter.  v56: hzpwave hzlangton hzchaos hzmaze hzkoch hzaurora + illusions hzcheck hzdrift.  v58: hzchladni hzsort hzspiro hzrose hzmoire hzkoi + illusion hzzoll.  v59: hzturing hzvoronoi hzcollatz hzsnow + illusions hzpogg hzwhite.  v60: hzdla hzsandpile hzgalaxy hzmoonsea + illusions hzhering hzponzo.  v62: hzlorenz hzlife hztree hzdragon hzrainwin + illusions hzmuller hzjastrow.  v63: group templates hzwelcome hzchoose hzguess + party game hzstroop.  See README.md "Hourly day schedule". */
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
function fitEl(el,maxVh){if(!el)return;var max=maxVh/100*(el.ownerDocument.documentElement.clientHeight||1080),g=0;while(el.scrollHeight>max+2&&g<8){g++;var ns=el.querySelectorAll('.q,.e,.a,.sm,div,span');for(var i=0;i<ns.length;i++){var fs=parseFloat(getComputedStyle(ns[i]).fontSize);if(fs>10)ns[i].style.fontSize=(fs*0.88)+'px'}}}

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
 if(it.fit=='contain'){var b=wEl('img','');b.src=it.f;b.style.cssText='position:absolute;top:-4vw;left:-4vw;width:108vw;height:108vh;object-fit:cover;filter:blur(30px) brightness(.35)';L.appendChild(b)}
 var m=wEl('img','');m.src=it.f;m.style.cssText='position:absolute;top:0;left:0;width:100%;height:100%;object-fit:'+(it.fit||'cover')+';object-position:'+(it.pos||'50% 50%');L.appendChild(m);
 var top=it.cp=='top';
 L.appendChild(wEl('div','',null,'position:absolute;left:0;right:0;'+(top?'top:0':'bottom:0')+';height:58%;background:linear-gradient('+(top?'rgba(0,0,0,.86),rgba(0,0,0,.5) 50%,transparent':'transparent,rgba(0,0,0,.5) 50%,rgba(0,0,0,.88)')+')'));
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
 var h='<div class="lb" style="color:'+p[4]+';text-shadow:none;margin-bottom:1.6vh">Mevlânâ’dan · From Rumi</div>';
 for(i=0;i<ln.length;i++)h+='<div class="qln" style="font-size:'+fs+';color:'+p[2]+'"><span class="hzw" style="animation-delay:'+(1.2+i*4)+'s">'+ln[i]+'</span></div>';
 var qz=T(L,h,'',0.2);qz.className+=' hz-qzone';qz.style.textShadow='none';
 var attr=T(L,'<div style="width:6vw;height:2px;background:'+p[4]+';margin:0 auto 1.4vh"></div><div class="e" style="color:'+p[3]+';text-shadow:none;font-size:1.55vw">'+it.en+'</div><div class="sm" style="color:'+p[3]+';text-shadow:none">Mevlânâ’ya atfedilir · attributed to Rumi — yazı çizimi · lettering illustration</div>','',1.6);
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
 var m=wEl('img','');m.src=it.f;m.style.cssText='position:absolute;top:0;left:0;width:100%;height:100%;object-fit:cover;object-position:'+(it.pos||'50% 50%');L.appendChild(m);
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

})();
