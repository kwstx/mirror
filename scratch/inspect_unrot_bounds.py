import os
from PIL import Image
import numpy as np

unrot = Image.open('scratch/user_orig_unrotated.png').convert('RGB')
arr = np.array(unrot)

# In unrot:
# Top-left of photo is around (31, 1).
# Let's check the white border:
print("Row y=10 across x=20..50:")
for x in range(20, 50):
    print(f"x={x}: {arr[10, x]}")

print("\nCol x=50 across y=0..30:")
for y in range(0, 30):
    print(f"y={y}: {arr[y, 50]}")
