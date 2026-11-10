/* hourly.js v57 — reusable scene library for the hourly day schedules (days/YYYY-MM-DD.json). ES5 only. Requires wow.js helpers (wEl, wCv, wLoop, WOW).
   Data-driven templates: hzphoto hzquote hzriddle hzsteps hzfact.  Living art: hzpend hzgalton hzharmono hzphyllo hzboids hzfourier hzripple hzmonte hzulam hzfirefly hzsleep.
   Illusions: hzcafe hzebb hzkaniz hzlilac hzstep hzhermann hzafter.  v56: hzpwave hzlangton hzchaos hzmaze hzkoch hzaurora + illusions hzcheck hzdrift.  See README.md "Hourly day schedule". */
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

})();
