from PIL import ImageDraw
import math, numpy


def average_filter(image_noised, m, n):

    draw = ImageDraw.Draw(image_noised)
    width = image_noised.size[0]
    height = image_noised.size[1]
    pix_noised = image_noised.load()

    for i in range(int(m // 2), width - int(m // 2)):
        for j in range(int(n // 2), height - int(n // 2)):
            a = 0
            b = 0
            c = 0

            for x in range(i - int(m // 2), i + int(m // 2) + 1):
                for y in range(j - int(n // 2), j + int(n // 2) + 1):
                    a = a + pix_noised[x, y][0]
                    b = b + pix_noised[x, y][1]
                    c = c + pix_noised[x, y][2]
            draw.point((i, j), (int(a // (n * m)), int(b // (n * m)), int(c // (n * m))))
    # print(n)
    image_noised.save("average_filter.png", "PNG")
    del draw

    return


def med_filter(image, m, n):
    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    pix = image.load()
    for i in range(int(m // 2), width - int(m // 2)):
        for j in range(int(n // 2), height - int(n // 2)):
            i_j_r = []
            i_j_g = []
            i_j_b = []
            for x in range(i - int(m // 2), i + int(m // 2) + 1):
                for y in range(j - int(n // 2), j + int(n // 2) + 1):
                    i_j_r.append(pix[x, y][0])
                    i_j_g.append(pix[x, y][1])
                    i_j_b.append(pix[x, y][2])
            draw.point((i, j), (int(numpy.median(i_j_r)), int(numpy.median(i_j_g)), int(numpy.median(i_j_b))))
    image.save("med_filter.png", "PNG")

    return


def med_myself_filter(image, m, n):
    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    pix = image.load()
    for i in range(int(m // 2), width - int(m // 2)):
        for j in range(int(n // 2), height - int(n // 2)):
            i_j_r = []
            i_j_g = []
            i_j_b = []
            for x in range(i - int(m // 2), i + int(m // 2) + 1):
                for y in range(j - int(n // 2), j + int(n // 2) + 1):
                    i_j_r.append(pix[x, y][0])
                    i_j_g.append(pix[x, y][1])
                    i_j_b.append(pix[x, y][2])

            cncn = 0
            for x in range(i - 1, i + 2):
                for y in range (j - 1, j + 2):
                    if math.fabs((pix[x, y][0] + pix[x, y][1] + pix[x, y][2]) - (pix[i, j][0] + pix[i, j][1] + pix[i, j][2])) > 100:
                        cncn = cncn + 1
            if cncn > 4:
                draw.point((i, j), (int(numpy.median(i_j_r)), int(numpy.median(i_j_g)), int(numpy.median(i_j_b))))
    image.save("med1.png", "PNG")

    return


def adapt_med_filter(image, s_m, m, n):
    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    pix = image.load()

    for i in range(int(s_m // 2), width - int(s_m // 2)):
        for j in range(int(s_m // 2), height - int(s_m // 2)):
            i_j_r = []
            i_j_g = []
            i_j_b = []
            check = 1
            m1 = m
            n1 = n
            while check == 1:
                for x in range(i - int(m1 // 2), i + int(m1 // 2) + 1):
                    for y in range(j - int(n1 // 2), j + int(n1 // 2) + 1):
                        i_j_r.append(pix[x, y][0])
                        i_j_g.append(pix[x, y][1])
                        i_j_b.append(pix[x, y][2])
                z_xy0 = pix[i, j][0]
                z_xy1 = pix[i, j][1]
                z_xy2 = pix[i, j][2]

                z_min0 = int(numpy.amin(i_j_r))
                z_min1 = int(numpy.amin(i_j_g))
                z_min2 = int(numpy.amin(i_j_b))

                z_max0 = int(numpy.amax(i_j_r))
                z_max1 = int(numpy.amax(i_j_g))
                z_max2 = int(numpy.amax(i_j_b))

                z_med0 = int(numpy.median(i_j_r))
                z_med1 = int(numpy.median(i_j_g))
                z_med2 = int(numpy.median(i_j_b))

                a1_0 = z_med0 - z_min0
                a1_1 = z_med1 - z_min1
                a1_2 = z_med2 - z_min2

                a2_0 = z_med0 - z_max0
                a2_1 = z_med1 - z_max1
                a2_2 = z_med2 - z_max2

                if(a1_0 > 0) and (a2_0 < 0) and (a1_1 > 0) and (a2_1 < 0) and (a1_2 > 0) and (a2_2 < 0):
                    b1_0 = z_xy0 - z_min0
                    b1_1 = z_xy1 - z_min1
                    b1_2 = z_xy2 - z_min2

                    b2_0 = z_xy0 - z_max0
                    b2_1 = z_xy1 - z_max1
                    b2_2 = z_xy2 - z_max2

                    if (b1_0 > 0) and (b2_0 < 0) and (b1_1 > 0) and (b2_1 < 0) and (b1_2 > 0) and (b2_2 < 0):
                        check = 0
                    else:
                        check = 0
                        draw.point((i, j), (z_med0, z_med1, z_med2))
                else:
                    if m1*n1 <= s_m * s_m:
                        m1 = m1 + 1
                        n1 = n1 + 1
                        check = 1
                    else:
                        check = 0

    image.save("med_ad_filter.png", "PNG")
    return
