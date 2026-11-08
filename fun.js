/* fun.js v53 — Fun & Mind Spark reel (8 Nov). ES5 only. Requires wow.js helpers. */
(function(){
var s=document.createElement('style');s.innerHTML='.fn{position:absolute;color:#f2f4f5;font-family:Georgia,serif;text-align:center;left:0;right:0}.fn .lb{font-family:Helvetica,Arial,sans-serif;letter-spacing:.38em;font-size:24px;color:#7fc4d4;text-transform:uppercase}.fn .q{font-size:66px;line-height:1.2;margin-top:14px}.fn .e{font-size:36px;color:#b8c6cd;font-style:italic;margin-top:12px}.fn .a{font-size:58px;color:#ffb35c;line-height:1.2}.fn .sm{font-family:Helvetica,Arial,sans-serif;font-size:24px;color:#8fa2ab;margin-top:14px}.fnin{animation:fnin 1.6s cubic-bezier(.33,1,.68,1) both}@keyframes fnin{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:none}}';document.head.appendChild(s);
function T(L,h,css,dl){var d=wEl('div','fn fnin',h,css);if(dl)d.style.animationDelay=dl+'s';L.appendChild(d);return d}
function hd(lb,q,e){return '<div class="lb">'+lb+'</div><div class="q">'+q+'</div><div class="e">'+e+'</div>'}
function ease(t){t=Math.max(0,Math.min(1,t));return t<.5?4*t*t*t:1-Math.pow(-2*t+2,3)/2}
var W=WOW;
/* 1 Müller-Lyer puzzle with timed reveal */
W.funlines=function(L,it){L.style.background='#0b1418';var c=wCv(L),x=c.getContext('2d');T(L,hd('Göz Oyunu · Visual Puzzle','Hangi çizgi daha uzun?','Which line is longer?'),'top:80px');
 var A=T(L,'<div class="a">İkisi de aynı uzunlukta!</div><div class="e">They are exactly the same length.</div><div class="sm">Müller-Lyer illüzyonu, 1889</div>','bottom:70px',13);
 wLoop(L,function(t){x.clearRect(0,0,1920,1080);x.lineCap='round';x.lineWidth=12;var y=[470,700],X0=660,X1=1260;
  for(var i=0;i<2;i++){x.strokeStyle='#eef3f5';x.beginPath();x.moveTo(X0,y[i]);x.lineTo(X1,y[i]);var d=i?-1:1;
   x.moveTo(X0,y[i]);x.lineTo(X0+d*70,y[i]-60);x.moveTo(X0,y[i]);x.lineTo(X0+d*70,y[i]+60);x.moveTo(X1,y[i]);x.lineTo(X1-d*70,y[i]-60);x.moveTo(X1,y[i]);x.lineTo(X1-d*70,y[i]+60);x.stroke()}
  var r=ease((t-12)/2);if(r>0){x.globalAlpha=r;x.strokeStyle='#ffb35c';x.lineWidth=4;x.setLineDash([14,12]);x.beginPath();x.moveTo(X0,380);x.lineTo(X0,800);x.moveTo(X1,380);x.lineTo(X1,800);x.stroke();x.setLineDash([]);x.globalAlpha=1}});return L};
/* 2 hidden circle — dots only move in straight lines */
W.funcircle=function(L,it){L.style.background='radial-gradient(ellipse at 50% 50%,#1b2a4a,#05070d 75%)';var c=wCv(L),x=c.getContext('2d'),N=8,R=300,cx=960,cy=560;
 T(L,hd('Kinetik Sır · Kinetic Secret','Bir daire dönüyor… değil mi?','A circle is rolling… or is it?'),'top:50px');
 T(L,'<div class="a">Her nokta yalnızca düz bir çizgide gidip geliyor!</div><div class="e">Each dot only moves back and forth on a straight line.</div>','bottom:40px',14);
 wLoop(L,function(t){x.clearRect(0,0,1920,1080);var r=ease((t-13)/2);
  for(var i=0;i<N;i++){var a=Math.PI*i/N,p=Math.cos(t*1.6-a)*R,px=cx+Math.cos(a)*p,py=cy+Math.sin(a)*p;
   if(r>0){x.globalAlpha=r*.55;x.strokeStyle='#7fc4d4';x.lineWidth=3;x.beginPath();x.moveTo(cx-Math.cos(a)*R,cy-Math.sin(a)*R);x.lineTo(cx+Math.cos(a)*R,cy+Math.sin(a)*R);x.stroke();x.globalAlpha=1}
   x.fillStyle='hsl('+(i*45)+',85%,65%)';x.beginPath();x.arc(px,py,22,0,7);x.fill()}});return L};
/* 3 paper folding thought experiment */
W.funfold=function(L,it){L.style.background='#070b12';var c=wCv(L),x=c.getContext('2d');T(L,hd('Düşünce Deneyi · Thought Experiment','Bir kâğıdı 42 kez katlasan ne kadar kalın olur?','Fold a 0.1 mm sheet 42 times — how thick?'),'top:60px');
 var C=T(L,'','top:400px'),M=[[0,'Kâğıt · Paper'],[10,'Kibrit kutusu · Matchbox'],[17,'5 katlı bina · Building'],[27,'Everest’i geçer · Beats Everest'],[33,'Uzay İstasyonu · Space Station'],[42,'Ay’a ulaşır! · Reaches the Moon!']];
 function f(mm){if(mm<1000)return mm.toFixed(1)+' mm';if(mm<1e6)return (mm/1000).toFixed(1)+' m';return Math.round(mm/1e6).toLocaleString('tr-TR')+' km'}
 wLoop(L,function(t){var k=Math.min(42,Math.floor(Math.max(0,t-3)/0.55)),mm=0.1*Math.pow(2,k),lab='';for(var i=0;i<M.length;i++)if(k>=M[i][0])lab=M[i][1];
  C.innerHTML='<div class="lb">Katlama · Fold '+k+'</div><div class="a" style="font-size:120px;margin:20px 0">'+f(mm)+'</div><div class="q">'+lab+'</div>'+(k==42?'<div class="sm">2⁴² × 0,1 mm ≈ 440.000 km · Ay ≈ 384.400 km · Sadece teorik!</div>':'');
  x.clearRect(0,0,1920,1080);var h=Math.min(1,Math.log(mm*10)/Math.log(4398046511104*10))*900;x.fillStyle='#ffb35c';x.fillRect(1700,1040-h,40,h);x.fillStyle='#d9dde0';x.beginPath();x.arc(1720,120,34,0,7);x.fill()});return L};
/* 4 scale journey: walking to the Moon and Sun */
W.funwalk=function(L,it){L.style.background='#04060b';var c=wCv(L),x=c.getContext('2d'),S=[];for(var i=0;i<220;i++)S.push([Math.random()*1920,Math.random()*1080,Math.random()*1.6+.3]);
 T(L,hd('Ölçek Yolculuğu · Scale Journey','Saatte 5 km yürüseydin…','If you could walk at 5 km/h, nonstop…'),'top:60px');
 var R=[['Trabzon → İstanbul','~1.070 km','9 gün · 9 days',3],['Dünya’nın çevresi · Around Earth','40.075 km','11 ay · 11 months',8],['Ay’a · To the Moon','384.400 km','8,8 yıl · 8.8 years',13],['Güneş’e · To the Sun','150 milyon km','3.400 yıl · 3,400 years',18]];
 for(var i=0;i<R.length;i++)T(L,'<span style="font-family:Helvetica,Arial;font-size:34px;color:#b8c6cd">'+R[i][0]+' · '+R[i][1]+'</span>&nbsp;&nbsp;<span class="a" style="font-size:52px">'+R[i][2]+'</span>','top:'+(360+i*130)+'px',R[i][3]);
 T(L,'<div class="sm">Işık aynı yolu Güneş’ten 8 dakika 20 saniyede alır · Light does it in 8 min 20 s</div>','bottom:60px',23);
 wLoop(L,function(t){x.clearRect(0,0,1920,1080);for(var i=0;i<S.length;i++){x.globalAlpha=.4+.3*Math.sin(t+i);x.fillStyle='#fff';x.fillRect(S[i][0],S[i][1],S[i][2],S[i][2])}x.globalAlpha=1});return L};
/* 5 geometry discovery: Seljuk 8-point star tiling */
W.funstar=function(L,it){L.style.background='#0a1622';var c=wCv(L),x=c.getContext('2d');
 T(L,'<div style="display:inline-block;background:rgba(5,10,16,.82);padding:26px 50px;border-radius:14px">'+hd('Sanat Keşfi · Art Discovery','İki kare → bir yıldız → sonsuz desen','Two squares → one star → an endless pattern')+'<div class="sm">Selçuklu ve Osmanlı çinilerinin gizli kuralı · The hidden rule of Seljuk & Ottoman tiles</div></div>','top:60px');
 function star(cx,cy,r,col,a){x.save();x.translate(cx,cy);x.strokeStyle=col;x.lineWidth=4;x.globalAlpha=a;for(var k=0;k<2;k++){x.rotate(Math.PI/4*k);x.strokeRect(-r,-r,2*r,2*r)}x.restore()}
 wLoop(L,function(t){x.clearRect(0,0,1920,1080);var g=160,shown=Math.max(0,(t-4)*9);var n=0;
  if(t<4){var p=ease(t/2.5);x.save();x.translate(960,620);x.strokeStyle='#7fc4d4';x.lineWidth=6;x.strokeRect(-150,-150,300,300);x.rotate(Math.PI/4*p);x.strokeStyle='#ffb35c';x.strokeRect(-150,-150,300,300);x.restore();return}
  for(var j=-1;j<8;j++)for(var i=-1;i<13;i++){var cx=i*g+((j%2)?g/2:0)+40,cy=j*g+40,d=Math.abs(cx-960)+Math.abs(cy-560);if(d/40<shown){var a=Math.min(1,(shown-d/40)/6);star(cx,cy,g*.36,(i+j)%2?'#7fc4d4':'#ffb35c',a*(0.8+.2*Math.sin(t+i*.5+j)))}}});return L};
/* 6 bat & ball riddle with timed reveal */
W.funriddle=function(L,it){L.style.background='radial-gradient(ellipse at 50% 40%,#2a1d12,#080604 75%)';
 T(L,hd('Bilmece · Riddle','Bir raket ve top toplam 110 TL.<br>Raket, toptan 100 TL pahalı.<br>Top kaç lira?','A bat and ball cost 110 TL. The bat costs 100 TL more than the ball. How much is the ball?'),'top:120px');
 T(L,'<div class="sm">Çoğu kişi hemen “10 TL” der… · Most people instantly say “10 TL”…</div>','top:620px',6);
 var cd=T(L,'','top:700px');
 T(L,'<div class="a">Top 5 TL! (Raket 105 TL)</div><div class="e">The ball is 5 TL — the bat 105 TL.</div>','top:760px',16);
 wLoop(L,function(t){var r=Math.ceil(15-t);cd.innerHTML=r>0&&t>6?'<div class="lb">Cevap · Answer: '+r+'</div>':''});return L};
/* 7 villa idea illustration — wall planters lighting up at dusk */
W.funvilla=function(L,it){var c=wCv(L),x=c.getContext('2d');
 T(L,'<div class="lb">Villa Fikri · Villa Idea — çizim · illustration</div><div class="q">Taşların yerine: ahşap saksı ve sıcak ışık</div><div class="e">Instead of stones: wooden planters and warm light</div>','top:50px');
 wLoop(L,function(t){var k=ease((t-3)/10);var sky=x.createLinearGradient(0,0,0,1080);sky.addColorStop(0,'rgb('+Math.round(120-100*k)+','+Math.round(170-140*k)+','+Math.round(210-150*k)+')');sky.addColorStop(1,'rgb('+Math.round(60-45*k)+','+Math.round(70-50*k)+','+Math.round(80-55*k)+')');x.fillStyle=sky;x.fillRect(0,0,1920,1080);
  x.fillStyle='#3a3f44';x.fillRect(0,880,1920,200);
  for(var i=0;i<4;i++){var px=210+i*450;
   if(i<3){x.fillStyle='#22272b';for(var b=0;b<6;b++)x.fillRect(px+130,560+b*48,320,26)}
   x.fillStyle='#8c8577';x.fillRect(px,520,130,360);x.strokeStyle='#6d675b';x.lineWidth=3;for(var r=0;r<6;r++){x.beginPath();x.moveTo(px,520+r*60);x.lineTo(px+130,520+r*60);x.stroke()}
   x.fillStyle='#8a5a34';x.beginPath();x.moveTo(px-10,520);x.lineTo(px+140,520);x.lineTo(px+130,440);x.lineTo(px,440);x.closePath();x.fill();x.strokeStyle='#6b4325';x.lineWidth=3;for(var w=1;w<6;w++){x.beginPath();x.moveTo(px+w*23,440);x.lineTo(px+w*23,520);x.stroke()}
   x.fillStyle='#3f7a3a';for(var l=0;l<9;l++){var a=l/8*Math.PI,sw=Math.sin(t*1.2+l+i)*4;x.beginPath();x.ellipse(px+65-Math.cos(a)*60+sw,440-Math.sin(a)*55,22,12,a,0,7);x.fill()}
   if(k>0){var g=x.createRadialGradient(px+65,470,5,px+65,560,260);g.addColorStop(0,'rgba(255,200,120,'+(.75*k)+')');g.addColorStop(1,'rgba(255,200,120,0)');x.fillStyle=g;x.fillRect(px-200,300,530,600)}}
  x.fillStyle='rgba(255,255,255,'+(.7*(1-Math.abs(.5-(t%14)/14)*2)*0)+')'});
 T(L,'<div class="sm">Fikir çizimi, gerçek fotoğraf değil · Concept sketch, not a real photo</div>','bottom:40px',4);return L};
})();
