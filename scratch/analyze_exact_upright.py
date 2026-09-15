import os
from PIL import Image
import numpy as np

upright = Image.open('scratch/exact_orig_upright_card.png').convert('RGB')
arr = np.array(upright)

print("Upright size:", upright.size) # (144, 240)

# Let's inspect the white border:
# Let's find white pixels across rows and cols
# Background is #5a000f:
bg = np.array([90, 0, 15], dtype=float)

# In upright (144, 240):
# Top border of the card:
# Let's inspect col x=72 from top (y=0) to bottom (y=239)
for y in range(0, 40):
    print(f"y={y}: color={arr[y, 72]}")

print("...")
for y in range(200, 240):
    print(f"y={y}: color={arr[y, 72]}")

# Left border:
print("\nLeft border at row y=100:")
for x in range(0, 30):
    print(f"x={x}: color={arr[100, x]}")

# Right border:
print("\nRight border at row y=100:")
for x in range(114, 144):
    print(f"x={x}: color={arr[100, x]}")
