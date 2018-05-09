import random
from PIL import ImageDraw


def gauss_noise(image, noise_k):

    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    pix = image.load()

    for i in range(width):
        for j in range(height):
            draw.point((i, j), (int(pix[i, j][0] + random.gauss(0, noise_k)),
                                int(pix[i, j][1] + random.gauss(0, noise_k)),
                                int(pix[i, j][2] + random.gauss(0, noise_k))))
    image.save("gauss_noise.png", "PNG")


def pepper_noise(image, density):

    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]

    for i in range(width):
        for j in range(height):
            k = random.randint(1, 100)
            if k <= density:
                draw.point((i, j), (0, 0, 0))
    image.save("pepper_noise.png", "PNG")


def salt_noise(image, density):

    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    for i in range(width):
        for j in range(height):
            k = random.randint(1, 100)
            if k <= density:
                draw.point((i, j), (255, 255, 255))
    image.save("salt_noise.png", "PNG")


def impulse_noise(image, density):
    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    for i in range(width):
        for j in range(height):
            numb = random.randint(1, 100)
            bl_wh = random.randint(1, 2)
            if numb <= density:
                if bl_wh == 1:
                    draw.point((i, j), (255, 255, 255))
                else:
                    draw.point((i, j), (0, 0, 0))
    image.save("impulse_noise.png", "PNG")
