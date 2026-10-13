from weasyprint import HTML,CSS
from pathlib import Path
import fitz,zipfile
P=Path('/mnt/data/Nexus_Digital')
html=HTML(filename=str(P/'index.html'),base_url=str(P))
# Browser alternative: static print rendering from HTML + CSS. Use explicit tall canvas.
doc=html.render(stylesheets=[CSS(string='@page {size: 1440px 4800px; margin:0} .container{max-width:1280px} .hero-image{background-image:linear-gradient(90deg,#041126 0%,#0411265e 55%,#04112614),url("assets/hero-technologijos.png")}')])
pdf=P/'Nexus_Digital_dizainas.pdf';doc.write_pdf(pdf)
print('pages',len(doc.pages))
with fitz.open(pdf) as f:
 for i,page in enumerate(f):
  pix=page.get_pixmap(matrix=fitz.Matrix(96/72,96/72),alpha=False)
  out=P/('Nexus_Digital_1440px.png' if i==0 else f'Nexus_Digital_puslapis_{i+1}.png')
  pix.save(out)
  print(out,pix.width,pix.height)
# leave user-facing presentation files in root; extras source scripts within source
for name in []:
 f=P/name
 if f.exists(): f.rename(P/'source'/name)
with zipfile.ZipFile('/mnt/data/Nexus_Digital_visas_projektas.zip','w',zipfile.ZIP_DEFLATED,compresslevel=7) as z:
 for f in P.rglob('*'):
  if f.is_file(): z.write(f,arcname='Nexus_Digital/'+str(f.relative_to(P)))
print('ZIP READY')
