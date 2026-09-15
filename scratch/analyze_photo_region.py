import os
from PIL import Image
import numpy as np

cards = Image.open('public/images/party_of_four_cards.png').convert('RGB')
old_crop = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789473470465.png').convert('RGB')

cards_arr = np.array(cards)
old_arr = np.array(old_crop)

# Let's find where old_crop appears inside cards using template matching / convolution
# Or cross-correlation:
from scipy import signal

# Since old_crop might be rotated or scaled or exact sub-region:
# Let's check old_crop size: (287, 272)
print("old_crop size (w, h):", old_crop.size)

# Let's check if old_crop is already rotated in cards or if it's axis-aligned in old_crop:
# In media1: is the image tilted or upright?
# In media1: we see the red background (#5a000f) on the left/top/right edges, which means media1 was a screenshot or crop from the page / reference!
# Notice media1 has the #5a000f background around the tilted photo!

# Let's find the exact correlation between old_crop and cards_arr
# We can search for the best match position of old_crop in cards_arr
best_val = float('inf')
best_pos = None

crop_h, crop_w, _ = old_arr.shape
cards_h, cards_w, _ = cards_arr.shape

# Let's do a search over reasonable scale factors if needed, or exact match
for y in range(0, max(1, cards_h - crop_h + 1)):
    for x in range(0, max(1, cards_w - crop_w + 1)):
        sub = cards_arr[y:y+crop_h, x:x+crop_w]
        diff = np.mean(np.abs(sub.astype(float) - old_arr.astype(float)))
        if diff < best_val:
            best_val = diff
            best_pos = (x, y)

print(f"Direct match search (1:1 scale): best diff={best_val:.2f} at pos={best_pos}")

# If scale differs (e.g. 0.5x, 2x, etc.):
for scale in [0.5, 0.75, 1.0, 1.25, 1.5, 2.0]:
    scaled_w = int(round(old_crop.width * scale))
    scaled_h = int(round(old_crop.height * scale))
    if scaled_w <= cards_w and scaled_h <= cards_h:
        scaled_old = old_crop.resize((scaled_w, scaled_h), Image.Resampling.BILINEAR)
        scaled_arr = np.array(scaled_old)
        
        # Test a few positions
        sub_best = float('inf')
        sub_pos = None
        for y in range(0, cards_h - scaled_h + 1, 2):
            for x in range(0, cards_w - scaled_w + 1, 2):
                sub = cards_arr[y:y+scaled_h, x:x+scaled_w]
                d = np.mean(np.abs(sub.astype(float) - scaled_arr.astype(float)))
                if d < sub_best:
                    sub_best = d
                    sub_pos = (x, y)
        print(f"Scale {scale:.2f} ({scaled_w}x{scaled_h}): best diff={sub_best:.2f} at pos={sub_pos}")
