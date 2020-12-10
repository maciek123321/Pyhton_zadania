import os
from PIL import Image, ImageDraw

img1 = Image.new('RGB', (60, 30), color='red')
d = ImageDraw.Draw(img1)
d.text((10, 10), "Red", fill=(255,255,255))
img1.save('/Users/maciejnawrocki/Desktop/pictures/img1.jpg', 'JPEG')
im = Image.open('/Users/maciejnawrocki/Desktop/pictures/img1.jpg')
im.save('/Users/maciejnawrocki/Desktop/pictures/img1.png')

img2 = Image.new('RGB', (60, 30), color='blue')
d = ImageDraw.Draw(img2)
d.text((10, 10), "Blue", fill=(255,255,255))
img2.save('/Users/maciejnawrocki/Desktop/pictures/img2.jpg', 'JPEG')
im = Image.open('/Users/maciejnawrocki/Desktop/pictures/img2.jpg')
im.save('/Users/maciejnawrocki/Desktop/pictures/img2.png')

img3 = Image.new('RGB', (60, 30), color='green')
d = ImageDraw.Draw(img3)
d.text((10, 10), "Green", fill=(255,255,255))
img3.save('/Users/maciejnawrocki/Desktop/pictures/img3.jpg', 'JPEG')
im = Image.open('/Users/maciejnawrocki/Desktop/pictures/img3.jpg')
im.save('/Users/maciejnawrocki/Desktop/pictures/img3.png')

img4 = Image.new('RGB', (60, 30), color='black')
d = ImageDraw.Draw(img4)
d.text((10, 10), "Black", fill=(255,255,255))
img4.save('/Users/maciejnawrocki/Desktop/pictures/img4.jpg', 'JPEG')
im = Image.open('/Users/maciejnawrocki/Desktop/pictures/img4.jpg')
im.save('/Users/maciejnawrocki/Desktop/pictures/img4.png')








