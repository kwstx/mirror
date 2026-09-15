import os
from PIL import Image
import numpy as np

img = Image.open('scratch/card_2x_upright.png').convert('RGB')
arr = np.array(img)

# Let's inspect the card in 2x:
# Top white border:
# Let's scan along col x=144 from y=0 to y=100
print("Column x=144:")
for y in range(0, 100, 5):
    print(f"y={y:2d}: {arr[y, 144]}")

# Bottom white border / photo end:
print("\nBottom of photo around y=300..400:")
for y in range(300, 420, 5):
    print(f"y={y:2d}: {arr[y, 144]}")

# Left white border:
print("\nRow y=200:")
for x in range(0, 80, 5):
    print(f"x={x:2d}: {arr[200, x]}")

# Right border / photo end:
print("\nRow y=200 right side:")
for x in range(200, 288, 5):
    print(f"x={x:2d}: {arr[200, x]}")
