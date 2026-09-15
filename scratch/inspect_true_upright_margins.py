import os
from PIL import Image
import numpy as np

img = Image.open('scratch/true_card1_upright.png').convert('RGB')
arr = np.array(img)

print("Size:", img.size)

# Let's inspect the white border / photo area:
# Top border:
print("Top border (col x=68):")
for y in range(0, 20):
    print(f"y={y:2d}: {arr[y, 68]}")

# Left border:
print("\nLeft border (row y=83):")
for x in range(0, 20):
    print(f"x={x:2d}: {arr[83, x]}")

# Bottom border:
print("\nBottom border (col x=68):")
for y in range(146, 166):
    print(f"y={y:2d}: {arr[y, 68]}")
