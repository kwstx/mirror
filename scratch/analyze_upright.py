import os
from PIL import Image
import numpy as np

upright = Image.open('scratch/card_upright.png').convert('RGB')
arr = np.array(upright)

# Let's inspect the card_upright image
# Background is #5a000f -> [90, 0, 15]
# Let's find the white border bounds inside card_upright
# Let's check across the middle row (y=205) and middle col (x=145)
print("Middle row y=205:")
for x in range(0, 290, 10):
    print(f"x={x:3d}: {arr[205, x]}")

print("\nMiddle col x=145:")
for y in range(0, 410, 15):
    print(f"y={y:3d}: {arr[y, 145]}")
