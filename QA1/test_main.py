from PIL import Image, ImageDraw
import noises
import filters
import qualitymethods
import matplotlib.pyplot as plt


image = Image.open("lenna.png")
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
pix = image.load()
density = 25
# qualitymethods.uik(image, image, 1)
noises.salt_noise(image, density)

image = Image.open("salt_noise.png")
image1 = Image.open("lenna.png")
# print(qualitymethods.uik(image, image1, 1))
print(qualitymethods.posh(image, image1))
filters.adapt_med_filter(image, 8, 5, 5)
# filters.med_filter(image, 3, 3)
# filters.average_filter(image, 3, 3)
image = Image.open("med_ad_filter.png")
# image_med = Image.open("med_filter.png")
# image_aver = Image.open("average_filter.png")
image1111 = Image.open("lenna.png")
# l = qualitymethods.uik(image1111, image, 1)
l = qualitymethods.posh(image, image1111)
print(l)
# l = qualitymethods.posh(image_med, image1111)
del draw
