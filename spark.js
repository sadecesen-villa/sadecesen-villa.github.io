/* spark.js v43 — Mind Spark scenes. ES5 only. Requires wow.js helpers. */
(function(){
var CSS='.sp{position:absolute;color:#eef1f3;font-family:Georgia,serif}.sp .lb{font-family:Helvetica,Arial,sans-serif;letter-spacing:.42em;font-size:22px;color:#8fb8c4;text-transform:uppercase}.sp .tr{font-size:60px;line-height:1.25}.sp .en{font-size:36px;color:#b4c2ca;font-style:italic;margin-top:18px;line-height:1.35}.sp .st{font-family:Helvetica,Arial,sans-serif;font-size:26px;color:#c9d3d8;line-height:1.6;margin-top:26px}.sp .ln{width:90px;height:2px;background:#6fa7b5;margin:26px 0}.sp .or{color:#f0a050}.spf{animation:spf 2.4s cubic-bezier(.33,1,.68,1) both}@keyframes spf{from{opacity:0;transform:translateY(28px)}to{opacity:1;transform:none}}.spl{display:inline-block;opacity:0;filter:blur(8px);animation:spl 1.6s ease forwards}@keyframes spl{to{opacity:1;filter:none}}';
var s=document.createElement('style');s.innerHTML=CSS;document.head.appendChild(s);
function D(L,html,css,cls){var d=document.createElement('div');d.className='sp '+(cls||'spf');d.innerHTML=html;d.style.cssText=css;L.appendChild(d);return d}
function bg(L,a,b){L.style.background='radial-gradient(ellipse at 30% 30%,'+a+','+b+' 80%)'}
function dl(n){return 'style="animation-delay:'+n+'s"'}
function cv(L){return wCv(L)}
var W=WOW;
/* 1 idea card */
W.idea=function(L,it){bg(L,'#14303a','#03080c');var c=cv(L),x=c.getContext('2d'),P=[];for(var i=0;i<60;i++)P.push([Math.random()*1920,Math.random()*1080,Math.random()*2+1,Math.random()*6]);
 wLoop(L,function(t){x.clearRect(0,0,1920,1080);for(var i=0;i<P.length;i++){var p=P[i];x.fillStyle='rgba(160,210,220,'+(.15+.15*Math.sin(t*.7+p[3]))+')';x.beginPath();x.arc(p[0]+Math.sin(t*.1+p[3])*40,(p[1]-t*8*p[2]+1080*4)%1080,p[2],0,7);x.fill()}});
 D(L,'<div class="lb">'+(it.lb||'Büyük Fikir · Big Idea')+'</div><div class="ln"></div><div class="tr">'+it.tr+'</div><div class="en spf" '+dl(1.5)+'>'+it.en+'</div>'+(it.st?'<div class="st spf" '+dl(3)+'>'+it.st+'</div>':''),'left:180px;right:220px;top:50%;transform:translateY(-50%)','');
 L.corner=false;return L};
/* 2 compounding */
W.compound=function(L){bg(L,'#0e2430','#020509');var c=cv(L),x=c.getContext('2d');
 D(L,'<div class="lb">Zihinsel Model · Mental Model</div><div class="tr" style="font-size:54px">Bileşik Etki</div><div class="en">Compounding — tiny daily changes, huge yearly results</div>','left:160px;top:80px');
 wLoop(L,function(t){var k=Math.min(1,t/14),N=Math.floor(365*k);x.clearRect(0,0,1920,1080);var X0=200,Y0=940,WW=1300,HH=560,mx=Math.log(40);
  x.strokeStyle='rgba(255,255,255,.2)';x.lineWidth=2;x.beginPath();x.moveTo(X0,Y0-HH);x.lineTo(X0,Y0);x.lineTo(X0+WW,Y0);x.stroke();
  function curve(r,col){x.strokeStyle=col;x.lineWidth=5;x.beginPath();for(var d=0;d<=N;d++){var v=Math.pow(r,d),y=Y0-HH*(v/40);x[d?'lineTo':'moveTo'](X0+WW*d/365,y)}x.stroke()}
  curve(1.01,'#7fd3c8');curve(.99,'#e8873a');var a=Math.pow(1.01,N),b=Math.pow(.99,N);
  x.font='26px Helvetica,Arial';x.fillStyle='#c9d3d8';x.textAlign='left';x.fillText('Gün · Day '+N,X0+WW-200,Y0+50);
  x.fillStyle='#7fd3c8';x.font='300 64px Helvetica,Arial';x.fillText(a.toFixed(2)+'×',1560,420);x.font='24px Helvetica,Arial';x.fillText('Her gün %1 daha iyi · 1% better daily',1560,460);
  x.fillStyle='#e8873a';x.font='300 64px Helvetica,Arial';x.fillText(b.toFixed(2)+'×',1560,640);x.font='24px Helvetica,Arial';x.fillText('Her gün %1 daha kötü · 1% worse daily',1560,680);
  if(k>=1){x.fillStyle='rgba(238,241,243,'+Math.min(1,(t-14)/2)+')';x.font='italic 34px Georgia';x.fillText('1.01³⁶⁵ ≈ 37.8   ·   0.99³⁶⁵ ≈ 0.03',1560,820)}});
 L.corner=false;return L};
/* 3 Conway's Game of Life */
W.life=function(L){L.style.background='#03070a';var c=cv(L),x=c.getContext('2d'),S=16,C=120,R=68,g=[],i,j,last=0;for(i=0;i<C*R;i++)g.push(Math.random()<.22?1:0);
 D(L,'<div class="lb">Canlı Algoritma · Living Algorithm</div><div class="tr" style="font-size:46px">Conway’in Hayat Oyunu</div><div class="en" style="font-size:28px">Conway’s Game of Life — four simple rules, endless complexity</div>','left:80px;bottom:60px;background:rgba(3,7,10,.75);padding:24px 34px;border-radius:8px');
 wLoop(L,function(t){if(t-last<.12)return;last=t;var n=[];for(j=0;j<R;j++)for(i=0;i<C;i++){var s=0;for(var dy=-1;dy<2;dy++)for(var dx=-1;dx<2;dx++)if(dx||dy)s+=g[((j+dy+R)%R)*C+(i+dx+C)%C]?1:0;var v=g[j*C+i];n.push(v?(s==2||s==3?Math.min(v+1,9):0):(s==3?1:0))}g=n;
  if(Math.random()<.08){var cx=Math.floor(Math.random()*(C-20)),cy=Math.floor(Math.random()*(R-14));for(i=0;i<120;i++)if(Math.random()<.45)g[(cy+Math.floor(i/12))*C+cx+i%12]=1}
  x.fillStyle='rgba(3,7,10,.55)';x.fillRect(0,0,1920,1080);for(j=0;j<R;j++)for(i=0;i<C;i++){var v=g[j*C+i];if(v){x.fillStyle='hsl('+(185-v*6)+',55%,'+(70-v*4)+'%)';x.fillRect(i*S+1,j*S+1,S-2,S-2)}}});
 L.corner=false;return L};
/* 4 flow field */
W.flow=function(L){L.style.background='#04080c';var c=cv(L),x=c.getContext('2d'),P=[],i,seed=Math.random()*100;x.fillStyle='#04080c';x.fillRect(0,0,1920,1080);for(i=0;i<1400;i++)P.push([Math.random()*1920,Math.random()*1080]);
 D(L,'<div class="lb">Üretken Sanat · Generative Art</div><div class="tr" style="font-size:44px">Rüzgârın görünmez haritası</div><div class="en" style="font-size:28px">An invisible map of wind — each line follows a mathematical field</div>','right:90px;bottom:70px;text-align:right');
 wLoop(L,function(t){x.fillStyle='rgba(4,8,12,.035)';x.fillRect(0,0,1920,1080);x.lineWidth=1.8;for(i=0;i<P.length;i++){var p=P[i],a=Math.sin(p[0]*.0023+seed)*2+Math.cos(p[1]*.0031+t*.05)*2,nx=p[0]+Math.cos(a)*2.2,ny=p[1]+Math.sin(a)*2.2;
  x.strokeStyle='hsla('+(170+p[1]/1080*60)+',55%,70%,.6)';x.beginPath();x.moveTo(p[0],p[1]);x.lineTo(nx,ny);x.stroke();p[0]=nx;p[1]=ny;if(nx<0||nx>1920||ny<0||ny>1080||Math.random()<.004){p[0]=Math.random()*1920;p[1]=Math.random()*1080}}});
 L.corner=false;return L};
/* 5 fractal tree */
W.tree=function(L){bg(L,'#10242c','#020507');var c=cv(L),x=c.getContext('2d'),sw=Math.random()*10;
 D(L,'<div class="lb">Doğanın Matematiği · Nature’s Math</div><div class="tr" style="font-size:46px">Tek bir kural, koca bir ağaç</div><div class="en" style="font-size:28px">One rule — split and shrink — grows a whole tree. Ferns, rivers and lungs branch the same way.</div>','left:120px;top:90px;max-width:760px');
 function br(x0,y0,len,ang,d,g){if(d>11||g<=0)return;var f=Math.min(1,g),x1=x0+Math.cos(ang)*len*f,y1=y0+Math.sin(ang)*len*f;x.strokeStyle=d>8?'rgba(140,215,180,.8)':'rgba(220,225,215,'+(.9-d*.05)+')';x.lineWidth=Math.max(1,14-d*1.3);x.beginPath();x.moveTo(x0,y0);x.lineTo(x1,y1);x.stroke();if(g>1){br(x1,y1,len*.74,ang-.42+Math.sin(sw+d)*.05,d+1,g-1);br(x1,y1,len*.7,ang+.36+Math.cos(sw+d)*.05,d+1,g-1)}}
 wLoop(L,function(t){x.clearRect(0,0,1920,1080);sw=t*.4;x.lineCap='round';br(1240,1040,230,-Math.PI/2,0,t/1.4)});
 L.corner=false;return L};
/* 6 powers of ten */
var SC=[[-10,'Atom','An atom','0,1 nanometre · 0.1 nm'],[-7,'Virüs','A virus','100 nanometre · 100 nm'],[-5,'Hücre','A cell','10 mikrometre · 10 µm'],[-3,'Kum tanesi','A grain of sand','1 milimetre · 1 mm'],[0,'İnsan','A human','~1,7 metre · ~1.7 m'],[4,'Trabzon','A city','~10 kilometre · ~10 km'],[7,'Dünya','Planet Earth','12.742 km çap · 12,742 km wide'],[9,'Güneş','The Sun','1,39 milyon km · 1.39 million km'],[13,'Güneş Sistemi','The Solar System','~9 milyar km · ~9 billion km (to Neptune)'],[21,'Samanyolu','The Milky Way','~100.000 ışık yılı · ~100,000 light-years']];
W.scale=function(L){L.style.background='#000';var c=cv(L),x=c.getContext('2d'),T=D(L,'','left:0;right:0;bottom:90px;text-align:center','');
 D(L,'<div class="lb">Ölçek · Scale — atomdan galaksiye · from atom to galaxy</div>','left:0;right:0;top:60px;text-align:center');
 var per=5.5,li=-1;wLoop(L,function(t){var f=t/per,i=Math.min(SC.length-1,Math.floor(f)),u=f-i;x.fillStyle='rgba(0,0,0,.25)';x.fillRect(0,0,1920,1080);x.save();x.translate(960,480);
  for(var k=0;k<SC.length;k++){var r=60*Math.pow(6,k-f+1);if(r<2||r>3000)continue;x.strokeStyle='hsla('+(190+k*14)+',60%,70%,'+Math.max(0,Math.min(.8,1-Math.abs(k-f)/3))+')';x.lineWidth=2;x.beginPath();x.arc(0,0,r,0,7);x.stroke()}
  for(var n=0;n<80;n++){var a=n*2.4+t*.05,rr=(n*37%400)*Math.pow(1.3,u*3);x.fillStyle='rgba(200,230,255,.5)';x.fillRect(Math.cos(a)*rr,Math.sin(a)*rr,2,2)}x.restore();
  x.fillStyle='#eef1f3';x.font='200 150px Helvetica,Arial';x.textAlign='center';x.fillText('10',920,520);x.font='200 70px Helvetica,Arial';x.fillText((SC[i][0]<0?'−':'')+Math.abs(SC[i][0]),1040,440);x.font='26px Helvetica,Arial';x.fillStyle='#8fb8c4';x.fillText('metre · metres',960,580);
  if(i!=li){li=i;T.innerHTML='<div class="spf"><div class="tr">'+SC[i][1]+'</div><div class="en">'+SC[i][2]+'</div><div class="st">'+SC[i][3]+'</div></div>'}});
 L.corner=false;return L};
/* 7 typed story */
W.story=function(L,it){bg(L,'#1a2226','#050607');D(L,'<div class="lb">'+(it.lb||'Bir Buluşun Hikâyesi · Invention Story')+'</div><div class="tr" style="font-size:56px;margin-top:20px">'+it.h+'</div>','left:180px;top:120px;right:180px');
 var A=D(L,'','left:180px;right:220px;top:360px','');var full=[it.tr,it.en],k=0;
 wLoop(L,function(t){var n=Math.floor(t*28),a=full[0].slice(0,n),b=n>full[0].length+20?full[1].slice(0,n-full[0].length-20):'';var h='<div class="st" style="font-size:34px;font-family:Georgia;color:#eef1f3">'+a+(b?'':'<span class="cur"></span>')+'</div>'+(b?'<div class="st" style="font-size:30px;font-style:italic;font-family:Georgia;color:#b4c2ca">'+b+'<span class="cur"></span></div>':'');if(h!=A.innerHTML)A.innerHTML=h});
 L.corner=false;return L};
/* 8 word of the day */
W.word=function(L,it){bg(L,'#1c2a2e','#040708');D(L,'<div class="lb">Günün Kelimesi · Word of the Day</div><div class="ln" style="margin:26px auto"></div><div class="tr" style="font-size:150px;letter-spacing:.04em">'+it.w+'</div><div class="st" style="font-size:28px;color:#8fb8c4">'+it.p+'</div><div class="en spf" '+dl(1.5)+' style="font-size:44px">'+it.en+'</div><div class="st spf" '+dl(3)+' style="max-width:1300px;margin:30px auto 0">'+it.st+'</div>','left:0;right:0;top:50%;transform:translateY(-50%);text-align:center','');L.corner=false;return L};
/* 9 animated number */
W.number=function(L,it){bg(L,'#0f2a33','#020608');var N=D(L,'','left:0;right:0;top:250px;text-align:center','');
 D(L,'<div class="lb">Biliyor muydunuz? · Did you know?</div>','left:0;right:0;top:120px;text-align:center');
 D(L,'<div class="tr" style="font-size:50px">'+it.tr+'</div><div class="en">'+it.en+'</div>','left:200px;right:200px;top:560px;text-align:center').style.animationDelay='3s';
 wLoop(L,function(t){var k=1-Math.pow(1-Math.min(1,t/4),3),v=it.n*k,s=it.dec?v.toFixed(it.dec):Math.round(v).toLocaleString('en-US');N.innerHTML='<div style="font-family:Helvetica,Arial;font-weight:200;font-size:220px;color:#eef1f3">'+(it.pre||'')+s+'<span style="font-size:80px;color:#8fb8c4"> '+(it.u||'')+'</span></div>'});
 L.corner=false;return L};
/* 10 calligraphic quote */
W.callig=function(L,it){bg(L,'#1d1f24','#050506');var c=cv(L),x=c.getContext('2d');
 wLoop(L,function(t){x.clearRect(0,0,1920,1080);x.strokeStyle='rgba(143,184,196,.25)';x.lineWidth=1.5;for(var r=0;r<6;r++){x.beginPath();for(var a=0;a<Math.min(t*.6,6.3);a+=.02){var R=380+r*28+Math.sin(a*6+t*.3+r)*12;x.lineTo(960+Math.cos(a-1.57)*R,540+Math.sin(a-1.57)*R*.62)}x.stroke()}});
 var tr=it.tr.split(' ').map(function(w,i){return '<span class="spl" style="animation-delay:'+(.5+i*.35)+'s">'+w+'</span>'}).join(' ');
 var dl2=.5+it.tr.split(' ').length*.35+.8;
 D(L,'<div class="lb">'+(it.lb||'Bilgelik · Wisdom')+'</div><div class="tr" style="font-size:64px;font-style:italic;margin-top:40px">'+tr+'</div><div class="en spf" style="animation-delay:'+dl2+'s">'+it.en+'</div><div class="st spf" style="animation-delay:'+(dl2+1)+'s;color:#8fb8c4">— '+it.a+'</div>','left:300px;right:300px;top:50%;transform:translateY(-50%);text-align:center','');L.corner=false;return L};
/* 11 small challenge with timer */
W.challenge=function(L,it){bg(L,'#132a2a','#030707');var c=cv(L),x=c.getContext('2d'),T=it.sec||120;
 D(L,'<div class="lb or">Küçük Meydan Okuma · One Small Challenge</div><div class="ln"></div><div class="tr">'+it.tr+'</div><div class="en">'+it.en+'</div>','left:160px;top:50%;transform:translateY(-50%);width:950px','');
 wLoop(L,function(t){var r=Math.max(0,T-t),f=r/T;x.clearRect(0,0,1920,1080);x.lineWidth=10;x.strokeStyle='rgba(255,255,255,.08)';x.beginPath();x.arc(1480,540,220,0,7);x.stroke();x.strokeStyle='#e8873a';x.lineCap='round';x.beginPath();x.arc(1480,540,220,-Math.PI/2,-Math.PI/2+f*Math.PI*2);x.stroke();
  x.fillStyle='#eef1f3';x.font='200 110px Helvetica,Arial';x.textAlign='center';x.fillText(Math.floor(r/60)+':'+p2(Math.floor(r%60)),1480,575);x.font='24px Helvetica,Arial';x.fillStyle='#8fb8c4';x.fillText(r>0?'Başla · Go':'Bitti · Done',1480,640)});
 L.corner=false;return L};
/* 12 mental model steps */
W.model=function(L,it){bg(L,'#152530','#03060a');var c=cv(L),x=c.getContext('2d'),n=it.s.length;
 D(L,'<div class="lb">Zihinsel Model · Mental Model</div><div class="tr" style="font-size:58px">'+it.h+'</div><div class="en">'+it.he+'</div>','left:160px;top:90px;right:160px');
 for(var i=0;i<n;i++){D(L,'<div style="font-family:Helvetica,Arial;font-size:22px;color:#8fb8c4;letter-spacing:.3em">0'+(i+1)+'</div><div class="tr" style="font-size:36px;margin-top:10px">'+it.s[i][0]+'</div><div class="en" style="font-size:26px;margin-top:8px">'+it.s[i][1]+'</div>','left:'+(160+i*(1600/n))+'px;width:'+(1600/n-80)+'px;top:640px').style.animationDelay=(2+i*3)+'s'}
 wLoop(L,function(t){x.clearRect(0,0,1920,1080);var k=Math.min(n,(t-1.5)/3);x.strokeStyle='#6fa7b5';x.lineWidth=3;x.beginPath();x.moveTo(170,590);x.lineTo(170+Math.max(0,k)*(1600/n),590);x.stroke();for(var i=0;i<n;i++)if(k>i){x.fillStyle='#eef1f3';x.beginPath();x.arc(170+i*(1600/n),590,9,0,7);x.fill()}});
 L.corner=false;return L};
})();
