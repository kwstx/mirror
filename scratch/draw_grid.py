import os
from PIL import Image, ImageDraw
import numpy as np

cards = Image.open('public/images/party_of_four_cards.png').convert('RGB')
arr = np.array(cards)

# Let's inspect the left card and its neighbor
# Let's save a crop of x from 0 to 450, y from 0 to 500 with a grid
img_grid = cards.crop((0, 0, 450, 500))
draw = ImageDraw.Draw(img_grid)
for x in range(0, 450, 50):
    draw.line([(x, 0), (x, 500)], fill=(0, 255, 0, 128))
    draw.text((x+2, 5), str(x), fill=(0, 255, 0))

for y in range(0, 500, 50):
    draw.line([(0, y), (450, y)], fill=(0, 255, 0, 128))
    draw.text((5, y+2), str(y), fill=(0, 255, 0))

img_grid.save('scratch/left_grid.png')
print("Saved scratch/left_grid.png")
