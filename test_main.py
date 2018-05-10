#from PIL import Image, ImageDraw
import noises
import filters
import qualitymethods
import matplotlib.pyplot as plt
import cv2

# считываем изображение
'''image = Image.open("lenna.png")
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
pix = image.load()'''
# выставляем плотность шума
density = 25

image = cv2.imread("salt_noise.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image1 = cv2.imread("lenna.png")
image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)

# print(qualitymethods.uik(image, image1, 1))
# считаем УИК для зашмленного изобажения и исходного
print(qualitymethods.posh(image, image1))
# применяем фильтр
filters.adapt_med_filter(image, 8, 5, 5)
image = cv2.imread("med_ad_filter.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

image2 = cv2.imread("lenna.png")
image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)

l = qualitymethods.posh(image, image2)
print(l)
# l = qualitymethods.posh(image_med, image2)

