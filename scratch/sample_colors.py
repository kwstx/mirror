import os
from PIL import Image
import numpy as np

cards = Image.open('public/images/party_of_four_cards.png').convert('RGB')
arr = np.array(cards)

# Let's inspect row y=100 from x=0 to x=350:
# Let's print the colors every 20 pixels or so to see the structure
print("Row y=100:")
for x in range(0, 350, 25):
    print(f"x={x}: {arr[100, x]}")

print("\nRow y=200:")
for x in range(0, 350, 25):
    print(f"x={x}: {arr[200, x]}")

print("\nRow y=300:")
for x in range(0, 350, 25):
    print(f"x={x}: {arr[300, x]}")

print("\nColumn x=100:")
for y in range(0, 500, 25):
    print(f"y={y}: {arr[y, 100]}")
