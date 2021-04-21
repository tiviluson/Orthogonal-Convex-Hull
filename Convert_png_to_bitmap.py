from PIL import Image
import pandas as pd

full_image_name = "0_fill.png"
image_name = full_image_name[: len(full_image_name) - 4]
img = Image.open(full_image_name)
r, g, b, a = img.split()
img = Image.merge("RGB", (r, g, b))
img.save(image_name + ".bmp")
image = Image.open(image_name + '.bmp')
data = []
for x in range(image.width):
    for y in range(image.height):
        data.append(image.getpixel((x, y)))

data_bit = []
column_bit = []
for pixel in range(len(data)):
    if data[pixel] < (20, 20, 20):
        column_bit.append(1)
    else:
        column_bit.append(0)
    if (pixel + 1) % image.height == 0 and pixel != 0:
        column_bit.reverse()
        data_bit.append(column_bit)
        column_bit = []

# Write the list into a csv file
df = pd.DataFrame(data)
df.to_csv(image_name + '_rgb.csv', index=False, header=False)
df = pd.DataFrame(data_bit)
df.to_csv(image_name + '.csv', index=False, header=False)
