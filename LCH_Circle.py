from colormath.color_objects import LCHabColor, sRGBColor
from colormath.color_conversions import convert_color
from PIL import Image
import math

# PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]


def create_img(radius, lum, output):
    img = Image.new('RGBA', (radius*2, radius*2), "black")  # create a new black image
    pixels = img.load()  # create the pixel map

    for i in range(img.size[0]):    # for every col:
        for j in range(img.size[1]):    # For every row:
            i_0 = i-radius  # set x origin
            j_0 = j-radius  # set y origin
            r = pow(i_0*i_0 + j_0*j_0, 0.5)  # distance from origin

            if r <= radius:  # within defined radius
                if i_0 > 0:  # draws left hemisphere
                    t_color = convert_color(
                        LCHabColor(lum, r/radius*125, math.atan(j_0 / i_0) * 180 / math.pi),
                        sRGBColor)
                elif i_0 < 0:  # draws right hemisphere
                    t_color = convert_color(
                        LCHabColor(lum, r/radius*125, math.atan(j_0 / i_0) * 180 / math.pi + 180),
                        sRGBColor)
                else:  # Handles x/0
                    t_color = convert_color(
                        LCHabColor(lum, r/radius*125, 90 if j_0 >= 0 else 270),
                        sRGBColor)

                if t_color.clamped_rgb_r != t_color.rgb_r \
                        or t_color.clamped_rgb_g != t_color.rgb_g \
                        or t_color.clamped_rgb_b != t_color.rgb_b:
                    r = t_color.clamped_rgb_r * 255 if (i+j) % 3 != 0 else 255
                    g = t_color.clamped_rgb_g * 255 if (i+j) % 3 != 0 else 255
                    b = t_color.clamped_rgb_b * 255 if (i+j) % 3 != 0 else 255
                else:
                    r = t_color.clamped_rgb_r * 255
                    g = t_color.clamped_rgb_g * 255
                    b = t_color.clamped_rgb_b * 255

                pixels[i, j] = (int(r),
                                int(g),
                                int(b),
                                255)
            else:  # Outside of radius make image transparent
                pixels[i, j] = (0,0,0,0)

    img.save(output + ".png")


if __name__ == '__main__':
    in_rad = int(input("Circle radius (>0): "))
    in_lum = int(input("Luminosity level (0-100): "))
    in_out = str(input("Output: "))
    create_img(in_rad, in_lum, in_out)
