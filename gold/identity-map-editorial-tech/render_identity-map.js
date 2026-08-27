const {Canvas, FontLibrary, Path2D} = require('skia-canvas');
const {spawn} = require('child_process');

const W=1920,H=1080,RW=960,RH=540,FPS=30,DUR=31.633,FRAMES=Math.ceil(FPS*DUR);
// Optional mono font override; falls back to Noto Sans when unavailable.
const fs=require('fs');
const monoPath=process.env.MONO_FONT || '/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf';
if(fs.existsSync(monoPath)) FontLibrary.use('JetBrains Mono', monoPath);
const C={bg:'#06080d',panel:'#0d1320',paper:'#F2F5F5',ink:'#E3EAF3',muted:'#95A3B4',faint:'#4D5A6E',line:'#233047',cyan:'#00B8FF',cyan2:'#5FD9FF'};
const serif='"Noto Serif CJK SC"', mono='"JetBrains Mono"';
const clamp=(v,a=0,b=1)=>Math.max(a,Math.min(b,v));
const lerp=(a,b,t)=>a+(b-a)*t;
const easeOut=t=>1-Math.pow(1-clamp(t),3);
const smooth=t=>{t=clamp(t);return t*t*(3-2*t)};
const p=(f,s,d=18)=>easeOut((f-s)/d);
const fadeOut=(f,s,d=18)=>1-clamp((f-s)/d);
function font(ctx,px,fam=mono,w=500){ctx.font=`${w} ${px}px ${fam}`;}
function txt(ctx,t,x,y,px,color=C.ink,fam=mono,w=500,a=1,align='left'){
  ctx.save();ctx.globalAlpha*=a;ctx.fillStyle=color;ctx.textAlign=align;ctx.textBaseline='alphabetic';font(ctx,px,fam,w);ctx.fillText(t,x,y);ctx.restore();
}
function chamfer(x,y,w,h,c=14){const q=new Path2D();q.moveTo(x+c,y);q.lineTo(x+w-c,y);q.lineTo(x+w,y+c);q.lineTo(x+w,y+h-c);q.lineTo(x+w-c,y+h);q.lineTo(x+c,y+h);q.lineTo(x,y+h-c);q.lineTo(x,y+c);q.closePath();return q;}
function panel(ctx,x,y,w,h,{a=1,active=false,fill=C.panel,ch=14}={}){
  ctx.save();ctx.globalAlpha*=a;const q=chamfer(x,y,w,h,ch);ctx.fillStyle=fill;ctx.fill(q);ctx.strokeStyle=active?C.cyan:C.line;ctx.lineWidth=active?3:2;ctx.stroke(q);
  if(active){ctx.fillStyle=C.cyan;ctx.fillRect(x+24,y+22,54,4);}ctx.restore();
}
function node(ctx,x,y,w,h,zh,en,{a=1,active=false,large=false}={}){
  panel(ctx,x,y,w,h,{a,active,fill:active?'#08131D':C.panel});
  txt(ctx,zh,x+30,y+(large?96:82),large?50:38,C.paper,serif,800,a);
  txt(ctx,en,x+31,y+h-30,large?18:16,active?C.cyan2:C.muted,mono,650,a);
}
function line(ctx,pts,prog,{color=C.line,width=2,a=1}={}){
  if(prog<=0)return;prog=clamp(prog);let seg=[],total=0;for(let i=1;i<pts.length;i++){const l=Math.hypot(pts[i][0]-pts[i-1][0],pts[i][1]-pts[i-1][1]);seg.push(l);total+=l;}
  let r=total*prog;ctx.save();ctx.globalAlpha*=a;ctx.strokeStyle=color;ctx.lineWidth=width;ctx.beginPath();ctx.moveTo(...pts[0]);
  for(let i=1;i<pts.length;i++){const l=seg[i-1];if(r>=l){ctx.lineTo(...pts[i]);r-=l;}else{const t=l?r/l:0;ctx.lineTo(lerp(pts[i-1][0],pts[i][0],t),lerp(pts[i-1][1],pts[i][1],t));break;}}ctx.stroke();ctx.restore();
}
function dot(ctx,x,y,r,c=C.cyan,a=1){ctx.save();ctx.globalAlpha*=a;ctx.fillStyle=c;ctx.beginPath();ctx.arc(x,y,r,0,Math.PI*2);ctx.fill();ctx.restore();}
function cameraX(f){
  if(f<260)return 0;
  if(f<360)return lerp(0,-1420,smooth((f-260)/100));
  if(f<582)return -1420;
  if(f<654)return lerp(-1420,-3000,smooth((f-582)/72));
  if(f<748)return -3000;
  if(f<820)return lerp(-3000,-4200,smooth((f-748)/72));
  return -4200;
}
function identity(ctx,f){
  const aName=p(f,11,18)*fadeOut(f,300,26);
  txt(ctx,'示例创作者',190,368,126,C.paper,serif,900,aName);
  txt(ctx,'CREATOR NAME',198,432,28,C.muted,mono,700,aName);
  ctx.save();ctx.globalAlpha*=aName;ctx.fillStyle=C.cyan;ctx.fillRect(190,474,96,4);ctx.restore();

  const retire=fadeOut(f,330,40);
  const aa=p(f,47,18)*retire,ad=p(f,131,16)*retire;
  node(ctx,720,238,480,220,'技术实践者','TECH PRACTITIONER',{a:aa,active:f>=47&&f<181});
  node(ctx,720,590,480,220,'视觉创作者','VISUAL CREATOR',{a:ad,active:f>=131&&f<230});
  ctx.save();ctx.globalAlpha*=aa*.75;for(let r=0;r<3;r++)for(let c=0;c<7;c++)dot(ctx,1010+c*20,304+r*20,2.4,C.cyan);ctx.restore();
  ctx.save();ctx.globalAlpha*=ad*.78;ctx.strokeStyle=C.muted;ctx.lineWidth=2.2;ctx.beginPath();ctx.moveTo(997,674);ctx.bezierCurveTo(1046,618,1082,748,1165,676);ctx.stroke();ctx.restore();

  const lm=p(f,181,48)*retire;
  line(ctx,[[1200,348],[1345,348],[1345,518],[1480,518]],lm,{color:C.cyan,width:2.5});
  line(ctx,[[1200,700],[1345,700],[1345,518],[1480,518]],lm,{color:C.line,width:2});
  const am=p(f,194,22)*fadeOut(f,330,34);
  panel(ctx,1480,408,520,220,{a:am,active:true,fill:'#08131D',ch:18});
  txt(ctx,'跨学科身份',1740,500,54,C.paper,serif,850,am,'center');
  txt(ctx,'CROSS-DISCIPLINARY PRACTICE',1740,560,16,C.cyan2,mono,700,am,'center');
  dot(ctx,1480,518,6,C.cyan,am);
}
function experiment(ctx,f){
  const retire=fadeOut(f,632,42);
  const base=p(f,312,18)*retire;const x=2220,y=300;
  txt(ctx,'发起人',2220,242,24,C.cyan2,serif,650,base);
  node(ctx,x,y,660,300,'创作社群','CREATIVE COMMUNITY',{a:base,active:true,large:true});
  txt(ctx,'示例创作者 · FOUNDER',x+32,y+232,18,C.muted,mono,650,base);

  const stem=p(f,411,34)*retire;
  line(ctx,[[x+330,y+300],[x+330,690]],stem,{color:C.cyan,width:2.5});
  line(ctx,[[x+330,690],[2040,690]],stem,{color:C.line,width:2});
  line(ctx,[[x+330,690],[2550,690]],stem,{color:C.line,width:2});
  line(ctx,[[x+330,690],[3060,690]],stem,{color:C.line,width:2});

  const aArt=p(f,477,16)*retire,aTech=p(f,498,16)*retire,aComm=p(f,525,18)*retire;
  node(ctx,1845,730,390,170,'艺术','ART',{a:aArt,active:f>=477&&f<525});
  node(ctx,2360,730,390,170,'科技','TECHNOLOGY',{a:aTech,active:f>=498&&f<548});
  node(ctx,2875,730,430,170,'社群组织','COMMUNITY',{a:aComm,active:f>=525});

  const aSum=p(f,548,18)*retire;
  txt(ctx,'艺术 × 科技',3210,420,42,C.paper,serif,800,aSum,'center');
  txt(ctx,'构成创作者社群',3210,486,28,C.muted,serif,500,aSum,'center');
  line(ctx,[[2880,450],[2990,450]],p(f,546,20)*retire,{color:C.cyan,width:3});

  // One internal narrative line carries the community node into teaching.
  line(ctx,[[3305,815],[3440,815],[3440,505],[3740,505]],p(f,574,42),{color:C.cyan,width:2.5,a:fadeOut(f,730,32)});
}
function teaching(ctx,f){
  const x=3740,y=260;
  const base=p(f,582,18);
  node(ctx,x,y,720,300,'教学工作','TEACHING PRACTICE',{a:base,active:f>=582&&f<761,large:true});
  txt(ctx,'当前主要实践',x+32,y+235,18,C.muted,serif,520,base);

  // Teaching branches remain internal to the content, not decorative edge furniture.
  const stem=p(f,620,34);
  line(ctx,[[x+360,y+300],[x+360,700]],stem,{color:C.cyan,width:2.5});
  line(ctx,[[x+360,700],[3690,700]],stem,{color:C.line,width:2});
  line(ctx,[[x+360,700],[4330,700]],stem,{color:C.line,width:2});
  line(ctx,[[x+360,700],[4860,700]],p(f,742,34),{color:C.line,width:2});

  const aDm=p(f,700,16),aGen=p(f,724,16);
  node(ctx,3490,738,430,170,'数媒','DIGITAL MEDIA',{a:aDm,active:f>=700&&f<724});
  node(ctx,4140,738,460,170,'生成艺术','GENERATIVE ART',{a:aGen,active:f>=724&&f<761});

  // AI is the current focus and takes over the visual center as its subtitle begins.
  const aAI=p(f,761,18);
  node(ctx,5250,330,700,300,'人工智能','ARTIFICIAL INTELLIGENCE',{a:aAI,active:true,large:true});
  txt(ctx,'近几年教学重心',5282,570,18,C.muted,serif,520,aAI);
  line(ctx,[[4860,700],[5000,700],[5000,480],[5250,480]],p(f,752,28),{color:C.cyan,width:2.5});
  for(let i=0;i<9;i++)dot(ctx,5700+(i%3)*32,420+Math.floor(i/3)*32,3,C.cyan,aAI*.72);

  // Complete the self-introduction instead of cutting off after teaching.
  const aPersonal=p(f,890,18);
  node(ctx,4720,744,460,170,'个人创作','PERSONAL WORK',{a:aPersonal,active:false});
  line(ctx,[[5250,650],[5100,650],[5100,829],[5180,829]],p(f,884,22),{color:C.line,width:2});
}
function drawFrame(f){
  const c=new Canvas(RW,RH),ctx=c.getContext('2d');ctx.scale(RW/W,RH/H);ctx.fillStyle=C.bg;ctx.fillRect(0,0,W,H);
  const cam=cameraX(f);ctx.save();ctx.translate(cam,0);identity(ctx,f);experiment(ctx,f);teaching(ctx,f);ctx.restore();
  const g=ctx.createRadialGradient(W/2,H/2,260,W/2,H/2,1050);g.addColorStop(0,'rgba(0,0,0,0)');g.addColorStop(1,'rgba(0,0,0,.16)');ctx.fillStyle=g;ctx.fillRect(0,0,W,H);
  return c;
}

async function exportStill(frame, out){
  const c=drawFrame(frame);
  const ext=(out.split('.').pop()||'png').toLowerCase();
  const fmt=ext==='svg'?'svg':'png';
  const b=await c.toBuffer(fmt);
  require('fs').writeFileSync(out,b);
}

async function main(){
  if(process.argv[2]==='--still'){const frame=Number(process.argv[3]);const out=process.argv[4]||`still-${frame}.svg`;await exportStill(frame,out);console.log(out);return;}
  const out=process.argv[2]||'render_identity-map-editorial-tech.mp4';
  const ff=spawn('ffmpeg',['-y','-loglevel','error','-f','image2pipe','-framerate',String(FPS),'-i','-','-vf','scale=1920:1080:flags=lanczos','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p','-movflags','+faststart','-r',String(FPS),out],{stdio:['pipe','inherit','inherit']});
  for(let f=0;f<FRAMES;f++){const b=await drawFrame(f).toBuffer('png');if(!ff.stdin.write(b))await new Promise(r=>ff.stdin.once('drain',r));if(f%90===0)process.stderr.write(`frame ${f}/${FRAMES}\n`);}ff.stdin.end();await new Promise((res,rej)=>ff.on('exit',c=>c===0?res():rej(new Error('ffmpeg '+c))));console.log(out);
}
main().catch(e=>{console.error(e);process.exit(1)});
