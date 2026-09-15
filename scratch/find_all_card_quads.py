import os
from PIL import Image, ImageDraw
import numpy as np

orig_2x = Image.open('scratch/true_orig_cards.png').convert('RGB').resize((792, 500), Image.Resampling.LANCZOS)
arr = np.array(orig_2x)
bg = np.array([90, 0, 15], dtype=float)

# Let's inspect each card:
# In 792x500:
# Card 1 (Left): x in [10, 260], y in [10, 340]
# Card 2 (Top-Center): x in [240, 520], y in [10, 320]
# Card 3 (Bottom-Center): x in [150, 420], y in [240, 480]
# Card 4 (Right): x in [450, 770], y in [80, 480]

# Let's find the 4 corners of Card 2 (Top-Center):
# Card 2 has 4 edges:
# - Left edge: x ~ 246 (sloping down)
# - Top edge: y ~ 20 (sloping right)
# - Right edge: x ~ 510 (sloping down)
# - Bottom edge: y ~ 310 (sloping left)

# Let's find Card 2's corners in orig_2x:
# Let's sample edges of Card 2:
# Top edge:
top_c2 = []
for x in range(260, 500, 5):
    for y in range(0, 80):
        if np.linalg.norm(arr[y, x].astype(float) - bg) > 25:
            top_c2.append((x, y))
            break
top_c2 = np.array(top_c2)
p_top_c2 = np.polyfit(top_c2[:, 0], top_c2[:, 1], 1)
print(f"Card 2 top line: y = {p_top_c2[0]:.4f} * x + {p_top_c2[1]:.4f}")

# Left edge:
left_c2 = []
for y in range(30, 260, 5):
    for x in range(230, 270):
        if np.linalg.norm(arr[y, x].astype(float) - bg) > 25:
            # Card 2 white border has R>190, G>190, B>190
            c = arr[y, x]
            if c[0] > 190 and c[1] > 190 and c[2] > 190:
                left_c2.append((x, y))
                break
left_c2 = np.array(left_c2)
p_left_c2 = np.polyfit(left_c2[:, 1], left_c2[:, 0], 1)
print(f"Card 2 left line: x = {p_left_c2[0]:.4f} * y + {p_left_c2[1]:.4f}")

# Right edge of Card 2:
right_c2 = []
for y in range(40, 200, 5):
    for x in range(530, 480, -1):
        if np.linalg.norm(arr[y, x].astype(float) - bg) > 25:
            right_c2.append((x, y))
            break
right_c2 = np.array(right_c2)
p_right_c2 = np.polyfit(right_c2[:, 1], right_c2[:, 0], 1)
print(f"Card 2 right line: x = {p_right_c2[0]:.4f} * y + {p_right_c2[1]:.4f}")

# Card 4 (Right):
# Top edge:
top_c4 = []
for x in range(470, 750, 5):
    for y in range(80, 200):
        if np.linalg.norm(arr[y, x].astype(float) - bg) > 25:
            top_c4.append((x, y))
            break
top_c4 = np.array(top_c4)
p_top_c4 = np.polyfit(top_c4[:, 0], top_c4[:, 1], 1)
print(f"Card 4 top line: y = {p_top_c4[0]:.4f} * x + {p_top_c4[1]:.4f}")

# Right edge:
right_c4 = []
for y in range(120, 450, 5):
    for x in range(780, 680, -1):
        if np.linalg.norm(arr[y, x].astype(float) - bg) > 25:
            right_c4.append((x, y))
            break
right_c4 = np.array(right_c4)
p_right_c4 = np.polyfit(right_c4[:, 1], right_c4[:, 0], 1)
print(f"Card 4 right line: x = {p_right_c4[0]:.4f} * y + {p_right_c4[1]:.4f}")

# Bottom edge of Card 4:
bot_c4 = []
for x in range(500, 750, 5):
    for y in range(499, 350, -1):
        if np.linalg.norm(arr[y, x].astype(float) - bg) > 25:
            bot_c4.append((x, y))
            break
bot_c4 = np.array(bot_c4)
p_bot_c4 = np.polyfit(bot_c4[:, 0], bot_c4[:, 1], 1)
print(f"Card 4 bottom line: y = {p_bot_c4[0]:.4f} * x + {p_bot_c4[1]:.4f}")
