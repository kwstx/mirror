import os
from PIL import Image
import numpy as np

orig = Image.open('scratch/orig_cards_binary.png').convert('RGB')
arr = np.array(orig)
bg = np.array([90, 0, 15], dtype=float)

# Let's find every pixel of Card 1:
# Card 1 is the card on the left.
# Card 2 is the card in the center-top.
# Card 2 has a white border on its left edge.
# Where is Card 2's white border?
# Let's find Card 2's white border line:
card2_border_x = []
for y in range(0, 150):
    # Scan from x=100 to x=150
    for x in range(100, 150):
        c = arr[y, x]
        if c[0] > 190 and c[1] > 190 and c[2] > 190:
            card2_border_x.append((x, y))
            break

card2_border_x = np.array(card2_border_x)
p_c2 = np.polyfit(card2_border_x[:, 1], card2_border_x[:, 0], 1)
print(f"Card 2 left border: x = {p_c2[0]:.4f} * y + {p_c2[1]:.4f}")

# Card 3 is at the bottom (y > 140, x > 60):
# Card 3 also has a white border.
card3_border_x = []
for y in range(140, 250):
    for x in range(50, 150):
        c = arr[y, x]
        if c[0] > 190 and c[1] > 190 and c[2] > 190:
            card3_border_x.append((x, y))
            break

card3_border_x = np.array(card3_border_x)
if len(card3_border_x) > 0:
    p_c3 = np.polyfit(card3_border_x[:, 1], card3_border_x[:, 0], 1)
    print(f"Card 3 border: x = {p_c3[0]:.4f} * y + {p_c3[1]:.4f}")

# Now, Card 1's exact pixel mask in orig (396x250) is:
# - All pixels not background [90, 0, 15]
# - Left of Card 2's border (x < p_c2[0]*y + p_c2[1]) for y in Card 2
# - Above / Left of Card 3's border for y in Card 3
# - That's EXACTLY Card 1!
