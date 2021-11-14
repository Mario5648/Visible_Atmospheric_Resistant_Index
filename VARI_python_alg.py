'''
What is VARI?

The Visible Atmospherically Resistant Index (VARI) was designed and tested to work with RGB sensors.
VARI is a measure of “how green” an image is. VARI is not intended as a substitute for an NIR camera,
but it is meaningful when working with non-NDVI imagery. RGB images with the VARI algorithm applied
make it possible to detect areas of crop stress in a field.

VARI = (Green - Red) / (Green + Red - Blue)
'''

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mimg

#Image
picture = Image.open("./test_images/test1.png")

width, height = picture.size
count = 0
for x in range(width):
    for y in range(height):
        current_color = picture.getpixel((x,y))
        r,g,b,a = current_color

        if (g + r - b) == 0:
            count +=1
            continue
        nc = (g - r) / (g + r - b)

        picture.putpixel((x,y) , (int( abs(r * nc)),int( abs(g * nc)),int( abs(b * nc)),a))

print(count)
#Save image
picture.save("./output_images/output_analysis.png")

#Load image in matplotlib
img = mimg.imread('./output_images/output_analysis.png')
lum_img = img[:, :, 0]

color_map = plt.cm.get_cmap('RdYlGn')
reversed_color_map = color_map.reversed()


plt.imshow(lum_img,cmap=reversed_color_map)

plt.colorbar()
plt.set_cmap(reversed_color_map)
plt.show()
#picture.save("/Users/mariodejesus/Desktop/test_field3.png")
