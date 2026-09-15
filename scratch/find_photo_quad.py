import os
from PIL import Image
import numpy as np

orig_2x = Image.open('scratch/orig_cards_binary.png').convert('RGB').resize((792, 500), Image.Resampling.LANCZOS)
arr = np.array(orig_2x)

# In orig_2x, let's find the 4 corners of the photo inside Card 1:
# The photo has:
# - Top-Left inner corner (where hair/couch meets white top-left border)
# - Top-Right inner corner (where couch/wall meets white top border)
# - Bottom-Left inner corner (where shirt meets white bottom-left border)
# - Bottom-Right inner corner (where shirt/arm meets white border or Card 2)

# Let's inspect the white border lines:
# Top white border of Card 1:
# Let's inspect along columns x=50, 100, 150, 200
# From top downwards: background [90, 0, 15] -> white border [>180] -> photo [<160]
for x in [50, 100, 150, 200]:
    col = arr[:, x]
    print(f"\n--- Col x = {x} ---")
    # find transition from bg to white
    w_start = None
    w_end = None
    for y in range(0, 150):
        c = col[y]
        if w_start is None and c[0] > 170 and c[1] > 170 and c[2] > 170:
            w_start = y
        elif w_start is not None and w_end is None and not (c[0] > 170 and c[1] > 170 and c[2] > 170):
            w_end = y
            break
    print(f"Col x={x}: white outer={w_start}, photo inner={w_end}")

# Left white border of Card 1:
# Along rows y=100, 150, 200, 250
# From left rightwards: background -> white border -> photo
for y in [100, 150, 200, 250]:
    row = arr[y, :]
    print(f"\n--- Row y = {y} ---")
    w_start = None
    w_end = None
    for x in range(0, 150):
        c = row[x]
        if w_start is None and c[0] > 170 and c[1] > 170 and c[2] > 170:
            w_start = x
        elif w_start is not None and w_end is None and not (c[0] > 170 and c[1] > 170 and c[2] > 170):
            w_end = x
            break
    print(f"Row y={y}: white outer={w_start}, photo inner={w_end}")
