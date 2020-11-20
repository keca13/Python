#https://datatofish.com/images-to-pdf-python/
# pip install Pillow
from PIL import Image
import sys
sys

# file_in = sys.argv[1]
image1 = Image.open(r'D:\\UP\\CERTYFIKATY\\workandtravel.jpg')
# image1 = Image.open(file_in)
im1 = image1.convert('RGB')
im1.save(r'D:\\UP\\CERTYFIKATY\\workandtravel.pdf')
