import math


def sko(image_filtered, image_original):

    width = image_filtered.size[0]
    height = image_filtered.size[1]
    pix_filtered = image_filtered.load()
    pix_original = image_original.load()
    sum_red = 0
    sum_green = 0
    sum_blue = 0

    for i in range(width):
        for j in range(height):
            sum_red = sum_red + (pix_filtered[i, j][0] - pix_original[i, j][0]) ** 2.0
            sum_green = sum_green + (pix_filtered[i, j][1] - pix_original[i, j][1]) ** 2.0
            sum_blue = sum_blue + (pix_filtered[i, j][2] - pix_original[i, j][2]) ** 2.0
    sko_red = math.sqrt(sum_red / ((width - 10) * (height - 10)))
    sko_green = math.sqrt(sum_green / ((width - 10) * (height - 10)))
    sko_blue = math.sqrt(sum_blue / ((width - 10) * (height - 10)))
    result_sko = [sko_red, sko_green, sko_blue]

    return result_sko


def mae(image_filtered, image_original):

    width = image_filtered.size[0]
    height = image_filtered.size[1]
    pix_filtered = image_filtered.load()
    pix_original = image_original.load()
    sum_red = 0
    sum_green = 0
    sum_blue = 0

    for i in range(width):
        for j in range(height):
            sum_red = sum_red + math.fabs(pix_original[i, j][0] - pix_filtered[i, j][0])
            sum_green = sum_green + math.fabs(pix_original[i, j][1] - pix_filtered[i, j][1])
            sum_blue = sum_blue + math.fabs(pix_original[i, j][2] - pix_filtered[i, j][2])
    result_mae = (sum_red + sum_green + sum_blue) / (3 * width * height)
    # print(result_mae)

    return result_mae


def posh(image_filtered, image_original):

    sko_red = sko(image_filtered, image_original)[0]
    sko_green = sko(image_filtered, image_original)[1]
    sko_blue = sko(image_filtered, image_original)[2]

    k_red = 20 * math.log10(255 / sko_red)
    k_green = 20 * math.log10(255 / sko_green)
    k_blue = 20 * math.log10(255 / sko_blue)
    res_posh = [k_red, k_green, k_blue]

    return res_posh


def uik(image_filtered, image_original, rgb):
    width = image_filtered.size[0]
    height = image_filtered.size[1]
    pix_filtered = image_filtered.load()
    pix_original = image_original.load()

    lot_uik = []

    for x_1 in range(1, width - 7, 7):
        for y_1 in range(1, height - 7, 7):
            # for xy in range(49):
            x_sum = 0
            y_sum = 0
            for i in range(x_1, x_1 + 7):
                for j in range(y_1, y_1 + 7):
                    x_sum = x_sum + (pix_filtered[i, j][rgb])
                    y_sum = y_sum + (pix_original[i, j][rgb])
            x_sum = x_sum / 49.0
            # print(x_sum)
            y_sum = y_sum / 49.0

            sigma_x = 0
            sigma_y = 0
            sigma_xy = 0
            for i in range(x_1, x_1 + 7):
                for j in range(y_1, y_1 + 7):
                    sigma_x = sigma_x + ((pix_filtered[i, j][rgb]) - x_sum) ** 2.0
                    sigma_y = sigma_y + ((pix_original[i, j][rgb]) - y_sum) ** 2.0
                    sigma_xy = sigma_xy + ((pix_filtered[i, j][rgb]) - x_sum) * ((pix_original[i, j][rgb]) - y_sum)
            sigma_x = sigma_x / 49.0
            sigma_y = sigma_y / 49.0
            sigma_xy = sigma_xy / 49.0

            if ((sigma_x + sigma_y) * (x_sum ** 2.0 + y_sum ** 2.0)) == 0:
                result_uik = 1
            else:
                result_uik = 4 * sigma_xy * x_sum * y_sum / ((sigma_x + sigma_y) * (x_sum ** 2.0 + y_sum ** 2.0))
            lot_uik.append(result_uik)

    sm_uik = 0
    for i in range(len(lot_uik)):
        sm_uik = sm_uik + lot_uik[i]
    uik_fin = sm_uik / len(lot_uik)

    return uik_fin
