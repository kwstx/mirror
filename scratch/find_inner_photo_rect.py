import os
from PIL import Image
import numpy as np

orig_card = Image.open('scratch/exact_orig_upright_card.png').convert('RGB')
arr = np.array(orig_card)

# In exact_orig_upright_card.png (144, 240):
# Let's find the inner photo rectangle:
# The white border pixels have high brightness (R>150, G>150, B>150, low saturation)
# Inside the white border is the photo.
# Let's find the exact bounding box of the photo inside the white border:
print("Upright card size:", orig_card.size)

# Let's save a crop of the card and mark the inner photo rectangle
# Let's inspect along rows from top to bottom
for y in range(0, 40):
    # check row y average color
    row = arr[y, 20:120]
    is_w = np.mean((row[:, 0] > 160) & (row[:, 1] > 160) & (row[:, 2] > 160))
    print(f"y={y:2d}: white fraction = {is_w:.2f}, avg color = {np.mean(row, axis=0).astype(int)}")
