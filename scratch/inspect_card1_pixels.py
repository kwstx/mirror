import os
from PIL import Image
import numpy as np

orig = Image.open('scratch/orig_cards_binary.png').convert('RGB')
arr = np.array(orig)

# Let's inspect rows y=30, 60, 90, 120, 150, 180, 210
# For each row, print the first 10 pixels starting from x=0
for y in [30, 60, 90, 120, 150, 180, 210]:
    print(f"\nRow y={y}:")
    for x in range(0, 30, 2):
        print(f"x={x:2d}: {arr[y, x]}")
