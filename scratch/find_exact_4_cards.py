import os
from PIL import Image, ImageDraw
import numpy as np

orig_2x = Image.open('scratch/true_orig_cards.png').convert('RGB').resize((792, 500), Image.Resampling.LANCZOS)
arr = np.array(orig_2x)
bg = np.array([90, 0, 15], dtype=float)

# Let's inspect the 4 cards and verify their corner coordinates:
# We can draw the 4 card quads on top of orig_2x to visually inspect them:

# Let's test the 4 quadrilaterals:
# Card 1:
quad_c1 = [(15, 23), (250, 10), (268, 324), (33, 337)]
# Card 2:
quad_c2 = [(246, 26), (510, 6), (528, 316), (264, 336)]
# Card 3:
quad_c3 = [(152, 314), (414, 292), (430, 494), (168, 499)]
# Card 4:
quad_c4 = [(456, 178), (648, 192), (628, 488), (436, 474)]

vis = orig_2x.copy()
draw = ImageDraw.Draw(vis)
draw.polygon(quad_c1, outline=(0, 255, 0), width=2)
draw.polygon(quad_c2, outline=(0, 255, 255), width=2)
draw.polygon(quad_c3, outline=(255, 255, 0), width=2)
draw.polygon(quad_c4, outline=(255, 0, 255), width=2)

vis.save('scratch/vis_4_quads.png')
print("Saved scratch/vis_4_quads.png")
