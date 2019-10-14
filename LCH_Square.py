from colormath.color_objects import LCHabColor, sRGBColor
from colormath.color_conversions import convert_color
from PIL import Image
import math

# PIL accesses images in Cartesian co-ordinates, so it is Image[columns, rows]


def create_img(variable, value, width, height, output):
    img = Image.new('RGB', (width, height), "black")  # create a new black image
    pixels = img.load()  # create the pixel map

    for i in range(img.size[0]):    # for every col:
        for j in range(img.size[1]):    # for every row:
            if variable == 76 or variable == 108:

                t_color = convert_color(
                    LCHabColor(value,
                               -(j * height / 125) + height,
                               i * 360 / width),
                    sRGBColor)

            elif variable == 67 or variable == 99:

                t_color = convert_color(
                    LCHabColor(-(j * height / 100) + height,
                               value,
                               i * 360 / width),
                    sRGBColor)

            elif variable == 72 or variable == 104:

                t_color = convert_color(
                    LCHabColor(-(j * height / 100) + height,
                               i * width / 125,
                               value),
                    sRGBColor)

            else:
                print("Invalid variable, please input one of: L, l, C, c, H, h")
                quit(0)

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
                            int(b))

    img.save(output + ".png")


if __name__ == '__main__':
    in_var = ord(input("Variable (L, C, H): "))
    in_val = int(input("Value of variable? "))
    in_width = int(input("Image width: "))
    in_height = int(input("Image height: "))
    in_out = str(input("Output: "))
    create_img(in_var, in_val, in_width, in_height, in_out)
