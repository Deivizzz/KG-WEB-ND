from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
from pathlib import Path
import random, math
P=Path('/mnt/data/Nexus_Digital/assets'); P.mkdir(exist_ok=True)
source=Image.open('/mnt/data/a_polished_modern_dark_themed_website_homepage_ui.png').convert('RGB')
source2=Image.open('/mnt/data/a_full_page_dark_modern_high_contrast_website_la.png').convert('RGB')

def cover(im,size):
 w,h=size; s=max(w/im.width,h/im.height); im=im.resize((int(im.width*s),int(im.height*s)),Image.Resampling.LANCZOS);return im.crop(((im.width-w)//2,(im.height-h)//2,(im.width+w)//2,(im.height+h)//2))
def treatment(im, tint=(3,19,39), strength=.47):
 im=ImageEnhance.Contrast(im).enhance(1.12); im=ImageEnhance.Color(im).enhance(.68)
 layer=Image.new('RGB', im.size,tint); return Image.blend(im,layer,strength)
def finish(im,name):
 im.save(P/(name+'.png'),optimize=True)
 im.save(P/(name+'.webp'),quality=87,method=6)
 print(name,im.size)
# use independently recomposed and regraded photo areas from custom generated mockups
hero=cover(source.crop((445,70,1010,345)),(1600,810))
hero=treatment(hero,(2,18,42),.34)
d=ImageDraw.Draw(hero,'RGBA')
for i in range(600):
 x=random.Random(i*62).randrange(1600);y=random.Random(i*31).randrange(810)
 if i%13==0: d.ellipse((x,y,x+2,y+2),fill=(0,220,255,65))
# left readability gradient
mask=Image.new('RGBA',hero.size); md=ImageDraw.Draw(mask,'RGBA')
for x in range(1100):md.line((x,0,x,810),fill=(2,12,32,int(246*(1-x/1100)**1.7)),width=1)
hero=Image.alpha_composite(hero.convert('RGBA'),mask).convert('RGB');finish(hero,'hero-technologijos')
about=cover(source2.crop((385,615,1000,914)),(1200,780));about=treatment(about,(0,24,45),.30);finish(about,'apie-komanda')
# three product mockups from custom vector UI designed with raster software
random.seed(3)
def portfolio(kind,name):
 W,H=1120,720; im=Image.new('RGB',(W,H),(5,17,34));d=ImageDraw.Draw(im,'RGBA')
 for y in range(H):
  t=y/H;d.line((0,y,W,y),fill=(int(5+7*t),int(23+12*t),int(49+15*t)))
 for j in range(17):
  x=random.randrange(0,W);y=random.randrange(0,H);r=random.randrange(65,200);d.ellipse((x-r,y-r,x+r,y+r),outline=(24,190,240,15),width=2)
 if kind=='dashboard':
  d.rounded_rectangle((90,80,1020,650),radius=25,fill=(12,29,53),outline=(37,95,130),width=3)
  d.rounded_rectangle((110,104,292,626),radius=14,fill=(7,21,41))
  for j in range(6):d.rounded_rectangle((134,185+j*57,265,199+j*57),radius=6,fill=(23,61,89) if j else (8,168,227))
  for x in (325,548,771):d.rounded_rectangle((x,128,x+197,253),radius=16,fill=(18,48,76),outline=(32,90,133),width=2)
  d.rounded_rectangle((326,278,966,589),radius=18,fill=(10,34,62))
  pts=[]
  for i in range(30):
   x=352+i*20;y=515-int((.22+.58*(i/30)+.1*math.sin(i*.8))*180);pts.append((x,y))
  d.line(pts,fill=(0,220,255),width=6,joint='curve')
  for x,y in pts[::5]:d.ellipse((x-7,y-7,x+7,y+7),fill=(0,230,255))
 elif kind=='mobile':
  for idx,(x,angle) in enumerate(((360,-10),(650,11))):
   phone=Image.new('RGBA',(294,575));p=ImageDraw.Draw(phone,'RGBA');p.rounded_rectangle((6,3,286,568),radius=44,fill=(4,13,28),outline=(67,132,169),width=7)
   p.rounded_rectangle((23,26,270,542),radius=34,fill=(9,40,71));p.rounded_rectangle((97,34,198,50),radius=11,fill=(3,11,24))
   for k in range(4):p.rounded_rectangle((43,124+86*k,247,188+86*k),radius=12,fill=(20,72+8*k,104+9*k))
   for k in range(4):p.ellipse((56,136+86*k,88,168+86*k),fill=(0,216,255))
   phone=phone.rotate(angle,expand=True,resample=Image.Resampling.BICUBIC)
   im.paste(phone,(x-phone.width//2+140,65),phone)
 elif kind=='cloud':
  cx,cy=550,360
  for r in (230,175,110):d.ellipse((cx-r,cy-r,cx+r,cy+r),outline=(4,176,239,130),width=4)
  d.rounded_rectangle((392,299,721,460),radius=45,fill=(10,64,106),outline=(0,218,255),width=8)
  d.ellipse((442,236,587,381),fill=(10,64,106));d.ellipse((550,217,680,363),fill=(10,64,106))
  d.arc((410,300,700,450),0,180,fill=(0,229,255),width=7)
  for j in range(36):
   a=j*math.tau/36; x=cx+265*math.cos(a);y=cy+265*math.sin(a)
   d.ellipse((x-4,y-4,x+4,y+4),fill=(0,220,255,190))
 finish(im,name)
portfolio('dashboard','projektas-valdymo-sistema');portfolio('mobile','projektas-mobilioji-programa');portfolio('cloud','projektas-debesija')
