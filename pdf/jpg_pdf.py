#https://datatofish.com/images-to-pdf-python/
from PIL import Image
import sys

# file_in = sys.argv[1]
image1 = Image.open('E:\\UP\\CERTYFIKATY\\asterisk.jpg')
# image1 = Image.open(file_in)
im1 = image1.convert('RGB')
im1.save(r'E:\\UP\\CERTYFIKATY')