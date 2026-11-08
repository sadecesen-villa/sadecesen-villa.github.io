/* night.js v54 — bedtime reel (8 Nov). ES5 only. Requires wow.js helpers. */
(function(){
var s=document.createElement('style');s.innerHTML='.nt{position:absolute;left:0;right:0;text-align:center;color:#eef2f6;font-family:Georgia,serif;text-shadow:0 2px 18px rgba(0,0,0,.8)}.nt .lb{font-family:Helvetica,Arial,sans-serif;letter-spacing:.38em;font-size:22px;color:#9fbfd8;text-transform:uppercase}.nt .q{font-size:60px;margin-top:12px}.nt .e{font-size:34px;color:#c0ccd6;font-style:italic;margin-top:10px}.nt .sm{font-family:Helvetica,Arial,sans-serif;font-size:20px;color:#8796a3;margin-top:12px}.ntin{opacity:0;animation:ntin 4s ease forwards}@keyframes ntin{to{opacity:1}}';document.head.appendChild(s);
function T(L,h,css,dl){var d=wEl('div','nt ntin',h,css);d.style.animationDelay=(dl||1)+'s';L.appendChild(d);return d}
var W=WOW;
/* still real photo with caption */
W.ntphoto=function(L,it){var m=wEl('img','');m.src=it.f;m.style.cssText='position:absolute;inset:0;width:100%;height:100%;object-fit:cover';L.appendChild(m);
 L.appendChild(wEl('div','',null,'position:absolute;left:0;right:0;bottom:0;height:45%;background:linear-gradient(transparent,rgba(0,0,0,.75))'));
 T(L,'<div class="lb">'+it.lb+'</div><div class="q">'+it.tr+'</div><div class="e">'+it.en+'</div><div class="sm">'+it.cr+'</div>','bottom:60px',2);return L};
/* stars circling Polaris, Big Dipper highlighted */
W.ntsky=function(L,it){var c=wCv(L),x=c.getContext('2d'),S=[],px=960,py=300;for(var i=0;i<900;i++)S.push([Math.random()*1500,Math.random()*6.283,Math.random()*1.5+.3,Math.random()*6]);
 var BD=[[-140,330],[-60,300],[20,320],[90,330],[150,290],[160,400],[260,410]];
 T(L,'<div class="lb">Gece Gökyüzü · Night Sky — çizim · illustration</div><div class="q">Gece boyunca yıldızlar Kutup Yıldızı’nın etrafında döner</div><div class="e">All night, the stars turn around the North Star</div>','bottom:60px',3);
 wLoop(L,function(t){var a=t*.012;var g=x.createLinearGradient(0,0,0,1080);g.addColorStop(0,'#02040c');g.addColorStop(.75,'#0a1630');g.addColorStop(1,'#1a2440');x.fillStyle=g;x.fillRect(0,0,1920,1080);
  for(var i=0;i<S.length;i++){var r=S[i][0],b=S[i][1]+a,sx=px+Math.cos(b)*r,sy=py+Math.sin(b)*r;if(sy>860)continue;x.globalAlpha=.45+.35*Math.sin(t*.8+S[i][3]);x.fillStyle='#fff';x.fillRect(sx,sy,S[i][2],S[i][2])}
  x.globalAlpha=1;x.fillStyle='#fff';x.beginPath();x.arc(px,py,4,0,7);x.fill();
  var P=[];for(var j=0;j<BD.length;j++){var r=Math.sqrt(BD[j][0]*BD[j][0]+BD[j][1]*BD[j][1]),b=Math.atan2(BD[j][1],BD[j][0])+a;P.push([px+Math.cos(b)*r,py+Math.sin(b)*r])}
  x.strokeStyle='rgba(160,200,235,.35)';x.lineWidth=2;x.beginPath();x.moveTo(P[0][0],P[0][1]);for(j=1;j<5;j++)x.lineTo(P[j][0],P[j][1]);x.lineTo(P[6][0],P[6][1]);x.lineTo(P[5][0],P[5][1]);x.lineTo(P[4][0],P[4][1]);x.stroke();
  for(j=0;j<P.length;j++){x.fillStyle='#e8f0ff';x.beginPath();x.arc(P[j][0],P[j][1],4.5,0,7);x.fill()}
  x.fillStyle='#04060a';x.beginPath();x.moveTo(0,1080);for(var k=0;k<=1920;k+=40)x.lineTo(k,860+Math.sin(k*.004)*40+Math.sin(k*.013)*18);x.lineTo(1920,1080);x.fill();
  x.font='22px Helvetica';x.fillStyle='rgba(180,205,230,.7)';x.fillText('Kutup Yıldızı · Polaris',px+16,py-12);x.fillText('Büyükayı · Big Dipper',P[2][0]+16,P[2][1]+30)});return L};
/* good night: moonlit sea with quiet window glow */
W.ntbye=function(L,it){var c=wCv(L),x=c.getContext('2d');
 T(L,'<div class="q" style="font-size:84px">İyi geceler</div><div class="e" style="font-size:44px">Good night</div><div class="sm">Villa Sadece Sen — çizim · illustration</div>','top:170px',2);
 wLoop(L,function(t){var g=x.createLinearGradient(0,0,0,1080);g.addColorStop(0,'#050914');g.addColorStop(.6,'#111d36');g.addColorStop(1,'#060a14');x.fillStyle=g;x.fillRect(0,0,1920,1080);
  var mg=x.createRadialGradient(1450,260,10,1450,260,220);mg.addColorStop(0,'rgba(235,240,255,.35)');mg.addColorStop(1,'rgba(235,240,255,0)');x.fillStyle=mg;x.fillRect(1150,0,600,600);x.fillStyle='#eef1fa';x.beginPath();x.arc(1450,260,60,0,7);x.fill();
  x.fillStyle='#0b1428';x.fillRect(0,700,1920,380);
  for(var i=0;i<26;i++){var y=715+i*13,w=30+i*9+Math.sin(t*.6+i)*14;x.globalAlpha=.5-i*.016;x.fillStyle='#dfe6f5';x.fillRect(1450-w/2+Math.sin(t*.4+i*1.7)*10,y,w,2)}x.globalAlpha=1;
  x.fillStyle='#03050a';x.beginPath();x.moveTo(0,760);x.lineTo(180,640);x.lineTo(420,620);x.lineTo(640,720);x.lineTo(700,1080);x.lineTo(0,1080);x.fill();
  x.fillRect(220,520,240,140);x.beginPath();x.moveTo(200,525);x.lineTo(340,440);x.lineTo(480,525);x.fill();
  var f=.85+.08*Math.sin(t*.7);x.fillStyle='rgba(255,196,120,'+f+')';x.fillRect(260,560,50,55);x.fillRect(370,560,50,55);
  var wg=x.createRadialGradient(340,590,10,340,590,220);wg.addColorStop(0,'rgba(255,190,110,.25)');wg.addColorStop(1,'rgba(255,190,110,0)');x.fillStyle=wg;x.fillRect(100,380,480,420)});return L};
})();
