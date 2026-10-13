from pathlib import Path
from PIL import Image
from zipfile import ZipFile, ZIP_DEFLATED
from io import BytesIO
import subprocess, shutil
p=Path('/mnt/data/Nexus_Digital'); assets=p/'assets'; source=p/'source'
# PSD via ImageMagick raster copy (editable single layer)
for img in sorted(assets.glob('*.png')):
 subprocess.run(['magick',str(img),'-define','psd:additional-info=none',str(img.with_suffix('.psd'))],check=True,stdout=subprocess.DEVNULL)
 # OpenRaster with separately editable base-image + color treatment layer
 original=Image.open(img).convert('RGBA'); back=Image.new('RGBA',original.size,(2,13,29,255))
 def data(im):
  b=BytesIO(); im.save(b,format='PNG');return b.getvalue()
 name=img.stem
 xml=f'''<?xml version="1.0" encoding="UTF-8"?><image version="0.0.3" w="{original.width}" h="{original.height}" name="{name}"><stack><layer name="Apdorota iliustracija" src="data/layer1.png" opacity="1.0" visibility="visible" composite-op="svg:src-over" x="0" y="0"/><layer name="Tamsus pagrindas" src="data/layer0.png" opacity="1.0" visibility="visible" composite-op="svg:src-over" x="0" y="0"/></stack></image>'''
 with ZipFile(source/(name+'.ora'),'w') as z:
  z.writestr('mimetype','image/openraster',compress_type=0)
  z.writestr('stack.xml',xml); z.writestr('data/layer1.png',data(original));z.writestr('data/layer0.png',data(back));z.writestr('mergedimage.png',data(original))
 print('saved',name)
