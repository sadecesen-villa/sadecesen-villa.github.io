/* wow.js v51 — live/generative scenes + still frame-wall gallery. ES5 only. */
var WOWV=42,LAT=40.94,LON=39.95,RAD=Math.PI/180;
function wEl(t,c,h,s){var e=document.createElement(t);if(c)e.className=c;if(h!=null)e.innerHTML=h;if(s)e.style.cssText=s;return e}
function wCv(L){var c=document.createElement('canvas');c.width=1920;c.height=1080;c.style.cssText='position:absolute;left:0;top:0;width:100%;height:100%';L.appendChild(c);return c}
function wLoop(L,f){var t0=Date.now();function s(){if(!L.parentNode&&Date.now()-t0>3000)return;f((Date.now()-t0)/1000);requestAnimationFrame(s)}requestAnimationFrame(s)}
function wTxt(L,html,css){var d=wEl('div','wt',html,css);L.appendChild(d);return d}
function p2(x){return(x<10?'0':'')+x}
function hm(d){if(!d)return '—';var t=new Date(d.getTime()+(d.getTimezoneOffset()+180)*60000);return p2(t.getHours())+':'+p2(t.getMinutes())}
/* ---------- astronomy (low precision) ---------- */
function jd(d){return d.getTime()/864e5+2440587.5}
function sunPos(d){var n=jd(d)-2451545,L=(280.46+.9856474*n)%360,g=(357.528+.9856003*n)*RAD,l=(L+1.915*Math.sin(g)+.02*Math.sin(2*g))*RAD,e=23.439*RAD,ra=Math.atan2(Math.cos(e)*Math.sin(l),Math.cos(l)),dec=Math.asin(Math.sin(e)*Math.sin(l));return{ra:ra,dec:dec}}
function moonPos(d){var n=jd(d)-2451545,L=(218.316+13.176396*n)*RAD,M=(134.963+13.064993*n)*RAD,F=(93.272+13.229350*n)*RAD,l=L+6.289*RAD*Math.sin(M),b=5.128*RAD*Math.sin(F),e=23.4397*RAD;
 return{ra:Math.atan2(Math.sin(l)*Math.cos(e)-Math.tan(b)*Math.sin(e),Math.cos(l)),dec:Math.asin(Math.sin(b)*Math.cos(e)+Math.cos(b)*Math.sin(e)*Math.sin(l))}}
function gmst(d){return(280.16+360.9856235*(jd(d)-2451545))*RAD}
function alt(p,d){var H=gmst(d)+LON*RAD-p.ra;return Math.asin(Math.sin(LAT*RAD)*Math.sin(p.dec)+Math.cos(LAT*RAD)*Math.cos(p.dec)*Math.cos(H))/RAD}
function crossings(fn,h0,from){var r={rise:null,set:null},st=600000,prev=alt(fn(from),from)-h0;for(var t=from.getTime()+st;t<from.getTime()+864e5*1.05;t+=st){var d=new Date(t),a=alt(fn(d),d)-h0;if(prev<0&&a>=0&&!r.rise)r.rise=new Date(t-st*a/(a-prev));if(prev>=0&&a<0&&!r.set)r.set=new Date(t-st*a/(a-prev));prev=a}return r}
function mphase(){var syn=29.530588853,ref=Date.UTC(2000,0,6,18,14)/864e5,age=((Date.now()/864e5-ref)%syn+syn)%syn;return{age:age,f:age/syn,ill:(1-Math.cos(2*Math.PI*age/syn))/2}}
function drawMoon(x,cx,cy,r,ph){x.save();x.fillStyle='#1b2433';x.beginPath();x.arc(cx,cy,r,0,7);x.fill();
 var g=x.createRadialGradient(cx-r*.3,cy-r*.3,r*.1,cx,cy,r);g.addColorStop(0,'#f4f6f8');g.addColorStop(1,'#b9c2cc');x.fillStyle=g;
 var f=ph.f,k=Math.cos(2*Math.PI*f),wax=f<.5;x.beginPath();x.arc(cx,cy,r,-Math.PI/2,Math.PI/2,!wax);x.ellipse?x.ellipse(cx,cy,Math.abs(k)*r,r,0,Math.PI/2,-Math.PI/2,(wax?k>0:k<0)):0;x.closePath();x.fill();
 x.shadowColor='rgba(220,230,255,.6)';x.shadowBlur=60;x.strokeStyle='rgba(220,230,255,.15)';x.beginPath();x.arc(cx,cy,r,0,7);x.stroke();x.restore()}
function stars(n){var a=[];for(var i=0;i<n;i++)a.push([Math.random()*1920,Math.random()*1080,Math.random()*1.6+.3,Math.random()*6.28]);return a}
var CSS='.wt{position:absolute;color:#eef3f6;font-family:Georgia,serif;text-shadow:0 2px 18px rgba(0,0,0,.7)}.wt .s{font-family:Helvetica,Arial,sans-serif;letter-spacing:.4em;font-size:22px;color:#9fc9d0;text-transform:uppercase}.wt .tr{font-size:52px}.wt .en{font-size:34px;color:#b8c6cf;font-style:italic}.wfade{animation:wf 2.5s ease both}@keyframes wf{from{opacity:0;transform:translateY(30px)}to{opacity:1;transform:none}}.cur:after{content:"|";animation:bl 1s steps(1) infinite}@keyframes bl{50%{opacity:0}}';
(function(){var s=document.createElement('style');s.innerHTML=CSS;document.head.appendChild(s)})();
var WOW={};
/* 1. live sky */
WOW.sky=function(L){var c=wCv(L),x=c.getContext('2d'),S=stars(420),now=new Date(),ph=mphase(),
 d0=new Date(now.getTime()-3*36e5),su=crossings(sunPos,-.833,d0),mo=crossings(moonPos,.125,d0),ma=alt(moonPos(now),now),sa=alt(sunPos(now),now);
 var N=[['Yeni Ay','New Moon'],['Büyüyen Hilal','Waxing Crescent'],['İlk Dördün','First Quarter'],['Şişkin Ay (büyüyen)','Waxing Gibbous'],['Dolunay','Full Moon'],['Şişkin Ay (küçülen)','Waning Gibbous'],['Son Dördün','Last Quarter'],['Küçülen Hilal','Waning Crescent']][Math.floor(ph.f*8+.5)%8];
 wLoop(L,function(t){var g=x.createLinearGradient(0,0,0,1080);g.addColorStop(0,'#02040c');g.addColorStop(1,'#0b2236');x.fillStyle=g;x.fillRect(0,0,1920,1080);
  x.save();x.translate(960,1500);x.rotate(t*.004);for(var i=0;i<S.length;i++){var s=S[i];x.globalAlpha=.4+.6*Math.abs(Math.sin(t*1.3+s[3]));x.fillStyle='#fff';x.fillRect(s[0]-960,s[1]-1500,s[2],s[2])}x.restore();x.globalAlpha=1;
  if(t%9<1.2){var q=(t%9)/1.2;x.strokeStyle='rgba(255,255,255,'+(1-q)+')';x.lineWidth=2;x.beginPath();x.moveTo(300+q*500,120+q*200);x.lineTo(240+q*500,90+q*200);x.stroke()}
  drawMoon(x,1420,330,150,ph);x.fillStyle='#050a10';x.beginPath();x.moveTo(0,1080);for(var i=0;i<=1920;i+=40)x.lineTo(i,960-80*Math.sin(i/300)-40*Math.sin(i/97));x.lineTo(1920,1080);x.fill()});
 wTxt(L,'<div class="s">Arsin · 40.94°K 39.95°D · Canlı gökyüzü · Live sky</div><div class="tr" style="margin-top:20px">'+N[0]+' · %'+Math.round(ph.ill*100)+' aydınlık</div><div class="en">'+N[1]+' · '+Math.round(ph.ill*100)+'% illuminated · '+ph.age.toFixed(1)+' days old</div>'+
 '<div style="font-family:Helvetica,Arial;font-size:30px;line-height:1.8;margin-top:36px;color:#dfe8ee">☾ Ay doğuşu · Moonrise <b>'+hm(mo.rise)+'</b> &nbsp; Ay batışı · Moonset <b>'+hm(mo.set)+'</b><br>☀ Gün doğumu · Sunrise <b>'+hm(su.rise)+'</b> &nbsp; Gün batımı · Sunset <b>'+hm(su.set)+'</b><br><span style="color:#9fc9d0">Ay şu an ufkun '+Math.abs(Math.round(ma))+'° '+(ma>=0?'üstünde':'altında')+' · The moon is '+Math.abs(Math.round(ma))+'° '+(ma>=0?'above':'below')+' the horizon now</span></div><div class="s" style="margin-top:30px;font-size:16px">Gerçek zamanlı hesap · Calculated live from the current time</div>','left:120px;top:150px;width:1100px').className+=' wfade';
 L.corner=false;return L};
/* 2. giant clock */
WOW.bigclock=function(L){L.style.background='radial-gradient(ellipse at center,#0e2a3a 0%,#03070c 75%)';var c=wCv(L),x=c.getContext('2d');
 var GA=['Pazar','Pazartesi','Salı','Çarşamba','Perşembe','Cuma','Cumartesi'],GE=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'],AY=['Ocak','Şubat','Mart','Nisan','Mayıs','Haziran','Temmuz','Ağustos','Eylül','Ekim','Kasım','Aralık'],MO=['January','February','March','April','May','June','July','August','September','October','November','December'];
 var T=wTxt(L,'','left:0;right:0;top:0;bottom:0;text-align:center');
 wLoop(L,function(){var d=new Date(Date.now()+(new Date().getTimezoneOffset()+180)*60000),ms=d.getSeconds()+d.getMilliseconds()/1000;x.clearRect(0,0,1920,1080);
  x.lineWidth=6;x.strokeStyle='rgba(160,200,210,.12)';x.beginPath();x.arc(960,470,330,0,7);x.stroke();x.strokeStyle='#cfe6ea';x.shadowColor='#7fd0dc';x.shadowBlur=25;x.beginPath();x.arc(960,470,330,-Math.PI/2,-Math.PI/2+ms/60*2*Math.PI);x.stroke();x.shadowBlur=0;
  var a=-Math.PI/2+ms/60*2*Math.PI;x.fillStyle='#f08c3c';x.beginPath();x.arc(960+330*Math.cos(a),470+330*Math.sin(a),9,0,7);x.fill();
  for(var i=0;i<60;i++){var b=i/60*2*Math.PI;x.fillStyle=i%5?'rgba(200,220,230,.25)':'rgba(220,235,240,.7)';x.beginPath();x.arc(960+360*Math.cos(b),470+360*Math.sin(b),i%5?2:4,0,7);x.fill()}
  var k=new Date(d.getTime());
  T.innerHTML='<div style="position:absolute;top:340px;width:100%;font-family:Helvetica,Arial;font-weight:200;font-size:210px;letter-spacing:6px">'+p2(d.getHours())+'<span style="opacity:'+(d.getMilliseconds()<500?1:.3)+'">:</span>'+p2(d.getMinutes())+'</div>'+
  '<div style="position:absolute;top:880px;width:100%"><div class="tr" style="font-size:46px">'+d.getDate()+' '+AY[d.getMonth()]+' '+d.getFullYear()+', '+GA[d.getDay()]+'</div><div class="en">'+GE[d.getDay()]+', '+d.getDate()+' '+MO[d.getMonth()]+' '+d.getFullYear()+'</div><div class="s" style="margin-top:16px">İstanbul · Trabzon '+p2(d.getHours())+':'+p2(d.getMinutes())+' &nbsp;&nbsp;|&nbsp;&nbsp; Kuveyt · Kuwait '+p2(d.getHours())+':'+p2(d.getMinutes())+' (aynı saat · same time, UTC+3)</div></div>'});
 L.corner=false;return L};
/* 3. live weather */
var WW=null;function wwGet(){var r=new XMLHttpRequest();r.open('GET','https://api.open-meteo.com/v1/forecast?latitude=40.94&longitude=39.95&current=temperature_2m,apparent_temperature,relative_humidity_2m,wind_speed_10m,weather_code,is_day&daily=temperature_2m_max,temperature_2m_min&timezone=Europe%2FIstanbul&forecast_days=2',true);
 r.onload=function(){try{var j=JSON.parse(r.responseText);if(j.current)WW=j}catch(e){}};r.send()}wwGet();setInterval(wwGet,600000);
WOW.weather=function(L){if(!WW)return null;var c=WW.current,code=c.weather_code,wc=(typeof WC!='undefined'&&WC[code])||['',''],rain=code>=51&&code<=82,cloud=code>=2,snow=code>=71&&code<=77;
 L.style.background=c.is_day?'linear-gradient(#3b6c8e,#a9c6d6)':'linear-gradient(#030912,#102a3e)';var cv=wCv(L),x=cv.getContext('2d'),S=stars(200),dr=[];for(var i=0;i<260;i++)dr.push([Math.random()*1920,Math.random()*1080,6+Math.random()*8]);
 wLoop(L,function(t){x.clearRect(0,0,1920,1080);if(!c.is_day&&!cloud)for(var i=0;i<S.length;i++){x.globalAlpha=.5+.5*Math.sin(t*2+S[i][3]);x.fillStyle='#fff';x.fillRect(S[i][0],S[i][1]*.6,S[i][2],S[i][2])}x.globalAlpha=1;
  var cx=560,cy=420;if(!cloud||code==2){if(c.is_day){x.fillStyle='rgba(255,236,200,.9)';x.shadowColor='#fff3d0';x.shadowBlur=80;x.beginPath();x.arc(cx,cy,110+5*Math.sin(t*2),0,7);x.fill();x.shadowBlur=0}else drawMoon(x,cx,cy,100,mphase())}
  if(cloud){x.save();x.beginPath();x.rect(0,0,900,1080);x.clip();for(var k=0;k<3;k++){var ox=((t*(20+k*12)+k*500)%1100)-250,oy=300+k*90;x.fillStyle='rgba(225,232,238,'+((.55+k*.12)*Math.max(0,Math.min(1,(650-ox)/250,(ox+250)/250)))+')';for(var j=0;j<5;j++){x.beginPath();x.arc(ox+j*60,oy-(j%2)*40,70+(j%3)*15,0,7);x.fill()}}x.restore()}
  if(rain||snow){x.strokeStyle='rgba(200,225,240,.6)';x.fillStyle='#fff';x.lineWidth=2;for(var i=0;i<dr.length;i++){var p=dr[i];p[1]+=snow?2:p[2]*2;p[0]+=snow?Math.sin(t+i):-1;if(p[1]>1080){p[1]=-20;p[0]=Math.random()*1920}if(snow){x.beginPath();x.arc(p[0],p[1],3,0,7);x.fill()}else{x.beginPath();x.moveTo(p[0],p[1]);x.lineTo(p[0]-3,p[1]+p[2]*2);x.stroke()}}}});
 var dl=WW.daily;wTxt(L,'<div class="s">Arsin · Şu an · Right now</div><div style="font-family:Helvetica,Arial;font-weight:200;font-size:220px;line-height:1">'+Math.round(c.temperature_2m)+'°</div><div class="tr">'+wc[0]+'</div><div class="en">'+wc[1]+'</div>'+
 '<div style="font-family:Helvetica,Arial;font-size:28px;line-height:1.8;margin-top:30px">Hissedilen · Feels like <b>'+Math.round(c.apparent_temperature)+'°</b><br>Nem · Humidity <b>%'+c.relative_humidity_2m+'</b> &nbsp; Rüzgâr · Wind <b>'+Math.round(c.wind_speed_10m)+' km/s · km/h</b><br>Yarın · Tomorrow <b>'+Math.round(dl.temperature_2m_min[1])+'° / '+Math.round(dl.temperature_2m_max[1])+'°</b></div><div class="s" style="font-size:15px;margin-top:24px">Canlı veri · Live data: Open-Meteo · '+hm(new Date())+'</div>','left:1050px;top:200px;width:800px').className+=' wfade';
 L.corner=false;return L};
/* 4. day/night world */
WOW.globe=function(L){L.style.background='#02060b';var c=wCv(L),x=c.getContext('2d'),dI=new Image(),nI=new Image();dI.src='m/w-day.jpg';nI.src='m/w-night.jpg';
 var W=1600,H=800,ox=160,oy=110;function px(lo,la){return[ox+(lo+180)/360*W,oy+(90-la)/180*H]}
 wLoop(L,function(t){var now=new Date(),s=sunPos(now),sl=((s.ra-gmst(now))/RAD+540)%360-180,dec=s.dec;x.fillStyle='#02060b';x.fillRect(0,0,1920,1080);
  if(nI.complete)x.drawImage(nI,ox,oy,W,H);x.save();x.beginPath();var pts=[];for(var lo=-180;lo<=180;lo+=2){var la=Math.atan(-Math.cos((lo-sl)*RAD)/Math.tan(dec))/RAD;pts.push(px(lo,la))}
  x.moveTo(pts[0][0],pts[0][1]);for(var i=1;i<pts.length;i++)x.lineTo(pts[i][0],pts[i][1]);var py=dec>0?oy:oy+H;x.lineTo(ox+W,py);x.lineTo(ox,py);x.closePath();x.clip();if(dI.complete)x.drawImage(dI,ox,oy,W,H);x.restore();
  x.strokeStyle='rgba(200,230,240,.5)';x.lineWidth=2;x.beginPath();x.moveTo(pts[0][0],pts[0][1]);for(var i=1;i<pts.length;i++)x.lineTo(pts[i][0],pts[i][1]);x.stroke();
  var ss=px(sl,dec/RAD);x.fillStyle='rgba(255,240,210,.9)';x.beginPath();x.arc(ss[0],ss[1],10,0,7);x.fill();
  var P=[['Trabzon',39.72,41.0,'#7fe0ea'],['Kuveyt · Kuwait',47.98,29.37,'#f08c3c']];for(var i=0;i<2;i++){var q=px(P[i][1],P[i][2]),r=8+6*Math.abs(Math.sin(t*2+i));x.strokeStyle=P[i][3];x.lineWidth=3;x.beginPath();x.arc(q[0],q[1],r+10,0,7);x.stroke();x.fillStyle=P[i][3];x.beginPath();x.arc(q[0],q[1],7,0,7);x.fill();x.font='26px Helvetica,Arial';x.fillText(P[i][0],q[0]+22,q[1]+(i?28:-10))}});
 wTxt(L,'<div class="s" style="text-align:center">Şu an dünyada gece ve gündüz · Day and night on Earth right now</div>','left:0;right:0;top:40px');
 wTxt(L,'<div class="tr" style="font-size:36px;text-align:center">Aydınlık taraf güneşi, karanlık taraf şehir ışıklarını gösteriyor</div><div class="en" style="font-size:26px;text-align:center">The lit side shows sunlight, the dark side shows city lights · Görüntü · Imagery: NASA</div>','left:0;right:0;top:940px');
 L.corner=false;return L};
/* 5. aurora / flow */
WOW.aurora=function(L){var c=wCv(L),x=c.getContext('2d'),S=stars(300),PT=[];for(var i=0;i<900;i++)PT.push([Math.random()*1920,Math.random()*1080]);
 x.fillStyle='#01040a';x.fillRect(0,0,1920,1080);
 wLoop(L,function(t){x.fillStyle='rgba(1,4,10,.09)';x.fillRect(0,0,1920,1080);
  for(var b=0;b<3;b++){x.beginPath();for(var i=0;i<=1920;i+=20){var y=380+b*70+80*Math.sin(i/260+t*.4+b)+40*Math.sin(i/90-t*.7);i?x.lineTo(i,y):x.moveTo(i,y)}x.strokeStyle=['rgba(80,230,190,.06)','rgba(90,170,240,.05)','rgba(160,120,230,.04)'][b];x.lineWidth=120;x.stroke()}
  x.fillStyle='rgba(190,240,235,.55)';for(var i=0;i<PT.length;i++){var p=PT[i],a=Math.sin(p[1]/180+t*.3)*2+Math.cos(p[0]/240-t*.2);p[0]+=Math.cos(a)*1.4;p[1]+=Math.sin(a)*1.4;if(p[0]<0||p[0]>1920||p[1]<0||p[1]>1080){p[0]=Math.random()*1920;p[1]=Math.random()*1080}x.fillRect(p[0],p[1],1.6,1.6)}});
 wTxt(L,'<div class="tr" style="text-align:center">Akan ışık, akan zaman</div><div class="en" style="text-align:center">Flowing light, flowing time</div><div class="s" style="text-align:center;margin-top:16px">Üretken sanat · Generative art · Canlı çiziliyor · Drawn live</div>','left:0;right:0;bottom:90px').className+=' wfade';
 L.corner=false;return L};
/* 6. on this day */
WOW.otd=function(L){L.style.background='radial-gradient(ellipse at 30% 30%,#11314a,#03070d 80%)';var F=[['1512','Michelangelo’nun Sistine Şapeli tavan freskleri ilk kez halka gösterildi.','Michelangelo’s Sistine Chapel ceiling was first shown to the public.'],
 ['1922','TBMM saltanatı kaldırdı; Osmanlı saltanatı sona erdi.','The Grand National Assembly abolished the Ottoman sultanate.'],['1928','Türk Harf Devrimi: yeni Türk alfabesi kanunu kabul edildi.','Turkey adopted the law introducing the new Latin-based Turkish alphabet.'],['1993','Maastricht Antlaşması yürürlüğe girdi ve Avrupa Birliği kuruldu.','The Maastricht Treaty took effect, founding the European Union.']];
 var h='<div class="s">Tarihte bugün · On this day · 1 Kasım · 1 November</div>';for(var i=0;i<F.length;i++)h+='<div class="wfade" style="animation-delay:'+(1+i*2.5)+'s;margin-top:44px;display:flex"><div style="font-family:Helvetica,Arial;font-weight:200;font-size:76px;color:#9fe0e8;width:260px">'+F[i][0]+'</div><div><div class="tr" style="font-size:40px">'+F[i][1]+'</div><div class="en" style="font-size:28px">'+F[i][2]+'</div></div></div>';
 h+='<div class="s wfade" style="animation-delay:11s;font-size:14px;margin-top:50px;letter-spacing:.15em">Kaynak · Source: Wikipedia — Sistine Chapel ceiling; Abolition of the Ottoman sultanate; Turkish alphabet reform (Law No. 1353); Maastricht Treaty</div>';
 wTxt(L,h,'left:140px;top:110px;right:140px');L.corner=false;return L};
/* 7. typewriter word */
WOW.type=function(L){L.style.background='linear-gradient(135deg,#050b14,#0d2b3a)';var W=[['Huzur','hu-ZUR','İç rahatlığı, dinginlik; hiçbir şeyin eksik olmadığı an.','Peace of mind, serenity; the moment when nothing is missing.'],
 ['Gönül','gö-NÜL','Kalp, sevgi ve istek; “gönül vermek” birini sevmektir.','Heart, affection and desire; “to give one’s gönül” means to fall in love.'],['Keyif','key-İF','Tadını çıkarılan rahat, hoş an.','A relaxed, pleasant moment you savour.']],w=W[Math.floor(Date.now()/36e5)%W.length];
 var T=wTxt(L,'','left:200px;top:260px;right:200px');var full=[['<div class="s">Gecenin kelimesi · Word of the night</div><div style="font-size:140px;margin-top:20px">',w[0]],['</div><div style="font-family:Helvetica,Arial;font-size:34px;color:#9fe0e8">/ ',w[1]],[' /</div><div class="tr" style="margin-top:40px;font-size:46px">',w[2]],['</div><div class="en" style="margin-top:14px">',w[3]],['</div>','']];
 var t0=Date.now();wLoop(L,function(){var n=Math.floor((Date.now()-t0-800)/70),h='',done=true;for(var i=0;i<full.length;i++){h+=full[i][0];var s=full[i][1];if(n>=s.length){h+=s;n-=s.length}else{h+='<span class="cur">'+s.substr(0,Math.max(0,n))+'</span>';n=-1e9;done=false}}if(T.innerHTML.length!=h.length)T.innerHTML=h});
 L.corner=false;return L};
/* 8. countdown */
WOW.countdown=function(L){var c=wCv(L),x=c.getContext('2d'),S=stars(300),tgt=Date.UTC(2026,11,31,21,0,0);var T=wTxt(L,'','left:0;right:0;top:300px;text-align:center');
 wLoop(L,function(t){x.fillStyle='#02050b';x.fillRect(0,0,1920,1080);x.save();x.translate(960,540);for(var i=0;i<S.length;i++){var s=S[i],z=((s[3]*100+t*60)%600)/600,k=.2+z*2.5;x.globalAlpha=z;x.fillStyle='#e8f6ff';x.fillRect((s[0]-960)*k,(s[1]-540)*k,s[2]*k,s[2]*k)}x.restore();x.globalAlpha=1;
  var r=Math.max(0,tgt-Date.now()),d=Math.floor(r/864e5),h=Math.floor(r/36e5)%24,m=Math.floor(r/6e4)%60,s=Math.floor(r/1e3)%60;function b(v,a,e){return '<div style="display:inline-block;width:300px"><div style="font-family:Helvetica,Arial;font-weight:200;font-size:150px">'+p2(v)+'</div><div class="s">'+a+' · '+e+'</div></div>'}
  T.innerHTML='<div class="tr">2027’ye geri sayım</div><div class="en" style="margin-bottom:40px">Countdown to New Year 2027 · İstanbul saati · Istanbul time</div>'+b(d,'Gün','Days')+b(h,'Saat','Hours')+b(m,'Dakika','Minutes')+b(s,'Saniye','Seconds')});
 L.corner=false;return L};
/* 9. Black Sea waves + moon */
WOW.waves=function(L){var c=wCv(L),x=c.getContext('2d'),S=stars(250),ph=mphase();
 wLoop(L,function(t){var g=x.createLinearGradient(0,0,0,600);g.addColorStop(0,'#020611');g.addColorStop(1,'#0c2438');x.fillStyle=g;x.fillRect(0,0,1920,600);
  for(var i=0;i<S.length;i++){x.globalAlpha=.3+.7*Math.abs(Math.sin(t+S[i][3]));x.fillStyle='#fff';x.fillRect(S[i][0],S[i][1]*.5,S[i][2],S[i][2])}x.globalAlpha=1;drawMoon(x,960,250,80,ph);
  for(var l=0;l<14;l++){var y0=600+l*l*2.6,a=4+l*2.2,sp=.6+l*.08;x.fillStyle='rgb('+(6+l)+','+(22+l*3)+','+(38+l*4)+')';x.beginPath();x.moveTo(0,1080);for(var i=0;i<=1920;i+=24)x.lineTo(i,y0+a*Math.sin(i/(90+l*14)+t*sp+l)+a*.5*Math.sin(i/37-t*sp*1.7));x.lineTo(1920,1080);x.fill();
   for(var k=0;k<10;k++){var w=(1-l/14)*0+30+l*14,xx=960+(Math.sin(k*12.9+l*3.1)*w)+Math.sin(t*2+k+l)*8;x.fillStyle='rgba(225,235,245,'+(.5*Math.abs(Math.sin(t*3+k*1.7+l))*ph.ill+.05)+')';x.fillRect(xx,y0+a*Math.sin(xx/(90+l*14)+t*sp+l)+2,10+l*3,2)}}});
 wTxt(L,'<div class="tr" style="text-align:center">Karadeniz’de ay ışığı · yakamoz</div><div class="en" style="text-align:center">Moonlight on the Black Sea · the moon shown in tonight’s real phase</div><div class="s" style="text-align:center;margin-top:12px">Canlı animasyon · Live animation</div>','left:0;right:0;bottom:60px');
 L.corner=false;return L};
/* 10. 4-7-8 breathing */
WOW.breathe=function(L){L.style.background='radial-gradient(circle,#0f3442,#02070c 75%)';var c=wCv(L),x=c.getContext('2d'),T=wTxt(L,'','left:0;right:0;top:860px;text-align:center');
 var H=wTxt(L,'<div class="s" style="text-align:center">4-7-8 nefes · 4-7-8 breathing · Benimle nefes al · Breathe with me</div>','left:0;right:0;top:70px');
 wLoop(L,function(t){var q=t%19,r,a,b,n;if(q<4){r=150+200*q/4;a='Nefes al';b='Breathe in';n=4-Math.floor(q)}else if(q<11){r=350;a='Tut';b='Hold';n=11-Math.floor(q)}else{r=350-200*(q-11)/8;a='Yavaşça ver';b='Breathe out slowly';n=19-Math.floor(q)}
  x.clearRect(0,0,1920,1080);for(var i=4;i>0;i--){x.fillStyle='rgba(120,210,215,'+(.05*i)+')';x.beginPath();x.arc(960,480,r+i*22,0,7);x.fill()}x.fillStyle='rgba(225,245,248,.9)';x.beginPath();x.arc(960,480,r,0,7);x.fill();
  x.fillStyle='#0b2a36';x.font='200 120px Helvetica,Arial';x.textAlign='center';x.fillText(n,960,520);T.innerHTML='<div class="tr">'+a+'</div><div class="en">'+b+'</div>'});
 L.corner=false;return L};

/* 11. dining frame wall demo — projection-mapped gunmetal frames */
(function(){
var FCSS=''
+'.fw{position:absolute;inset:0;overflow:hidden;background:#1a1612}'
+'.fw-wall{position:absolute;left:0;right:0;top:0;bottom:0;background-size:cover;background-position:center;transition:filter 1.2s ease,opacity 1.2s}'
+'.fw-dim{position:absolute;inset:0;background:rgba(8,6,4,.0);transition:background 1.2s}'
+'.fw.on .fw-dim{background:rgba(8,6,4,.18)}'
+'.fw-group{position:absolute;left:50%;top:40%;width:68vw;max-width:1280px;height:auto;transform:translate(-50%,-50%);display:grid;'
+'grid-template-columns:28fr 7fr 110fr 7fr 26fr;grid-template-rows:37fr 7fr 37fr;gap:0}'
+'.fw-f{position:relative;box-sizing:border-box;border:0.45vw solid #5c5a58;border-radius:0.1vw;'
+'box-shadow:0 0.4vw 1.2vw rgba(0,0,0,.45), inset 0 0 0 0.18vw #1a1a1a;overflow:hidden;background:#f5f2ea}'
+'.fw-f:before{content:"";position:absolute;inset:0;box-shadow:inset 0 0 0 0.18vw #0a0a0a;z-index:3;pointer-events:none}'
+'.fw-L{grid-column:1;grid-row:1/4}'
+'.fw-C{grid-column:3;grid-row:1/4}'
+'.fw-RT{grid-column:5;grid-row:1}'
+'.fw-RB{grid-column:5;grid-row:3}'
+'.fw-cv{position:absolute;inset:0.22vw;overflow:hidden;background:#f7f4ec}'
+'.fw-cv img,.fw-cv .fw-fill{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block}'
+'.fw-cv .fw-fill{background-size:cover;background-position:center}'
+'.fw.on .fw-f{box-shadow:0 0 1.8vw rgba(255,236,200,.28),0 0.5vw 1.4vw rgba(0,0,0,.55), inset 0 0 0 0.18vw #111}'
+'.fw.on .fw-cv{box-shadow:inset 0 0 2vw rgba(255,250,230,.12)}'
+'.fw-glow{position:absolute;inset:-1.2vw;border-radius:0.3vw;background:radial-gradient(ellipse at center,rgba(255,230,180,.22),rgba(255,230,180,0) 70%);opacity:0;pointer-events:none;z-index:0;transition:opacity 1s}'
+'.fw.on .fw-glow{opacity:1}'
+'.fw-f>*{z-index:1}'
+'.fw-cap{position:absolute;left:0;right:0;bottom:2.2vh;text-align:center;z-index:5;pointer-events:none;'
+'font-family:Helvetica,Arial,sans-serif;padding:0 6vw}'
+'.fw-cap .tag{font-size:0.72vw;letter-spacing:.28em;text-transform:uppercase;color:#9a8b72;margin-bottom:0.2vh;opacity:.85}'
+'.fw-cap .tr{font-family:Georgia,serif;font-size:0.85vw;color:#c8bda8;line-height:1.25;text-shadow:0 1px 8px rgba(0,0,0,.75)}'
+'.fw-cap .en{font-family:Georgia,serif;font-size:0.7vw;color:#a89880;font-style:italic;margin-top:0.15vh;text-shadow:0 1px 8px rgba(0,0,0,.7)}'
+'.fw-txt{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;text-align:center;padding:6%;'
+'font-family:Georgia,serif;color:#f4efe4;background:linear-gradient(160deg,#2a2420,#1a1612)}'
+'.fw-txt .q{font-size:clamp(14px,2.1vw,42px);line-height:1.35;font-style:italic}'
+'.fw-txt .a{font-family:Helvetica,Arial,sans-serif;font-size:clamp(10px,1vw,18px);letter-spacing:.25em;text-transform:uppercase;color:#b9a88a;margin-top:1.2em}'
+'.fw-txt .big{font-size:clamp(18px,3.2vw,64px);font-style:normal;letter-spacing:.04em}'
;

var st=document.createElement('style');st.id='fw-css';st.innerHTML=FCSS;
if(!document.getElementById('fw-css'))document.head.appendChild(st);

function fwEl(t,c,h){var e=document.createElement(t);if(c)e.className=c;if(h!=null)e.innerHTML=h;return e}
function fwSet(el,src,cls){
  el.innerHTML='';
  if(!src){el.style.background='#f7f4ec';return}
  if(src.indexOf('text:')===0){
    var parts=src.slice(5).split('|');
    var d=fwEl('div','fw-txt');
    var q=fwEl('div',parts[2]||'q',parts[0]||'');
    d.appendChild(q);
    if(parts[1]){var a=fwEl('div','a',parts[1]);d.appendChild(a)}
    el.appendChild(d);return;
  }
  if(src.indexOf('fill:')===0){
    var d=fwEl('div','fw-fill'+(cls?' '+cls:''));
    d.style.backgroundImage='url('+src.slice(5)+')';
    el.appendChild(d);return;
  }
  var im=document.createElement('img');
  im.src=src;im.alt='';
  if(cls)im.className=cls;
  el.appendChild(im);
}

WOW.frames=function(L,it){
  var mode=((it&&it.mode)||'off');
  var root=fwEl('div','fw'+(mode==='off'?'':' on'));
  L.appendChild(root);
  var wallSrc=(mode==='evening'||mode==='quote')?'m/fw/stone-dusk.jpg':'m/fw/stone.jpg';
  var wall=fwEl('div','fw-wall');
  wall.style.backgroundImage='url('+wallSrc+')';
  if(mode==='off'){wall.style.filter='brightness(1.12) saturate(1.02)'}
  else{wall.style.filter='brightness(1.0) saturate(.95)'}
  root.appendChild(wall);
  root.appendChild(fwEl('div','fw-dim'));

  var g=fwEl('div','fw-group');
  var slots=['L','C','RT','RB'];
  var cvs={};
  for(var i=0;i<slots.length;i++){
    var id=slots[i];
    var f=fwEl('div','fw-f fw-'+id);
    var glow=fwEl('div','fw-glow');f.appendChild(glow);
    var cv=fwEl('div','fw-cv');f.appendChild(cv);
    g.appendChild(f);cvs[id]=cv;
  }
  root.appendChild(g);
  // size group to 178:81 without relying on aspect-ratio (older TV WebViews)
  (function(){function sz(){var w=g.clientWidth||Math.min(window.innerWidth*0.78,1500);g.style.height=Math.round(w*81/178)+'px'}sz();setTimeout(sz,50);setTimeout(sz,400)})();

  // content per mode — STILL possibility reel v52 (no afternoon loop, no motion)
  var A={
    off:['','','',''],
    jp:['m/fw/jp-L.jpg','m/fw/jp-C.jpg','m/fw/jp-RT.jpg','m/fw/jp-RB.jpg'],
    noc:['m/fw/noc-L.jpg','m/fw/noc-C.jpg','m/fw/noc-RT.jpg','m/fw/noc-RB.jpg'],
    abs:['m/fw/abs-L.jpg','m/fw/abs-C.jpg','m/fw/abs-RT.jpg','m/fw/abs-RB.jpg'],
    arch:['m/fw/arch-L.jpg','m/fw/arch-C.jpg','m/fw/arch-RT.jpg','m/fw/arch-RB.jpg'],
    bot:['m/fw/bot-L.jpg','m/fw/bot-C.jpg','m/fw/bot-RT.jpg','m/fw/bot-RB.jpg'],
    map:['m/fw/map-L.jpg','m/fw/map-C.jpg','m/fw/map-RT.jpg','m/fw/map-RB.jpg'],
    mast:['m/fw/mast-L.jpg','m/fw/mast-C.jpg','m/fw/mast-RT.jpg','m/fw/mast-RB.jpg'],
    guest:['m/fw/guest-L.jpg','m/fw/guest-C.jpg','m/fw/guest-RT.jpg','m/fw/guest-RB.jpg'],
    photo:['m/fw/photo-L.jpg','m/fw/photo-C.jpg','m/fw/photo-RT.jpg','m/fw/photo-RB.jpg'],
    season:['m/fw/season-L.jpg','m/fw/season-C.jpg','m/fw/season-RT.jpg','m/fw/season-RB.jpg'],
    mat:['m/fw/mat-L.jpg','m/fw/mat-C.jpg','m/fw/mat-RT.jpg','m/fw/mat-RB.jpg'],
    // kept for future reels / fallbacks (not in active tonight set)
    quote:['m/fw/art-reed.jpg','m/fw/art-mevlana.jpg','m/fw/art-moon.jpg','m/fw/art-whirl.jpg'],
    welcome:['m/fw/mood-tea.jpg','m/fw/art-welcome.jpg','m/fw/paint-morning.jpg','m/fw/mood-cay.jpg']
  };
  var srcs=A[mode]||A.off;
  for(var j=0;j<4;j++){
    fwSet(cvs[slots[j]], srcs[j], '');
  }

    var cap=fwEl('div','fw-cap');
  cap.innerHTML='<div class="tag">'+((it&&it.tag)||'Çerçeve Duvarı · Frame Wall')+'</div>'
    +'<div class="tr">'+((it&&it.tr)||'')+'</div>'
    +'<div class="en">'+((it&&it.en)||'')+'</div>';
  root.appendChild(cap);

  L.corner=false;
  L.dur=(it&&it.d)||40;
  return L;
};
})();
