import os
from PIL import Image
import numpy as np

img = Image.open('scratch/no_red_outline_white.png')
arr = np.array(img)

# Background color is [255, 255, 255]
# Let's check for any red hue around the perimeter of the cards:
# Red background had color [90, 0, 15] or (r >> g and r >> b with r in 60..120)
# Outside the cards (where r,g,b > 240 or in shadow r=g=b ~ 200..250):
shadow_and_bg = (arr[:, :, 0] > 180) & (arr[:, :, 1] > 180) & (arr[:, :, 2] > 180)
print("Background & shadow pixels are neutral white/gray:", np.mean(shadow_and_bg))

print("Image size:", img.size)
