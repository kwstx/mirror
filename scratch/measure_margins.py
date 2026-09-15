import os
from PIL import Image
import numpy as np

upright = Image.open('scratch/card_upright.png').convert('RGB')
arr = np.array(upright)

# Let's inspect the card in upright:
# Size: 290 x 410
# Card center: (145, 205)
# In upright:
# Top border of card: where does non-bg start?
# Left border of card: where does non-bg start?
# Right border: where does card end or meet next card?
# Bottom border: where does card end?

# Let's find for each row and col:
bg = np.array([90, 0, 15], dtype=float)
diff = np.linalg.norm(arr.astype(float) - bg, axis=2)
is_card = diff > 30

y_idx, x_idx = np.where(is_card)
print(f"Upright card bounds: x in [{x_idx.min()}, {x_idx.max()}] (w={x_idx.max()-x_idx.min()+1}), y in [{y_idx.min()}, {y_idx.max()}] (h={y_idx.max()-y_idx.min()+1})")

# Let's find the white border thickness:
# In the card, the white border is around the edges.
# Let's check the top white border:
top_y = y_idx.min()
# How many pixels down is white until the photo begins?
for y in range(top_y, top_y + 40):
    c = arr[y, 145]
    print(f"y={y}: color={c}")

# Let's check the left white border:
left_x = x_idx.min()
for x in range(left_x, left_x + 40):
    c = arr[205, x]
    print(f"x={x}: color={c}")
