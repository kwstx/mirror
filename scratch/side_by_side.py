import os
from PIL import Image, ImageDraw
import numpy as np

orig_user = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789473470465.png').convert('RGB')
match_2x = Image.open('scratch/exact_match_2x.png').convert('RGB')

# Let's resize match_2x to 1x (396, 250)
match_1x = match_2x.resize((396, 250), Image.Resampling.LANCZOS)

# Let's find the crop from match_2x that corresponds to orig_user:
# orig_user is (287, 272)
# In match_2x (792, 500), let's crop the same area:
# In find_user_orig_corners.py:
# Left edge in orig_user was x = 0.0867 * y + 30.82
# Top edge in orig_user was y = 1.5
# In match_2x, the card starts at x ~ 0, y ~ 20.
# If orig_user had 30px left margin:
# Let's crop x in [0, 300], y in [0, 300] from match_2x:
crop_match = match_2x.crop((0, 0, 300, 300))
crop_match.save('scratch/match_crop_300.png')

# Create a side-by-side comparison image:
# Resize orig_user to height 300:
scale_orig = 300 / orig_user.height
orig_scaled = orig_user.resize((int(orig_user.width * scale_orig), 300), Image.Resampling.LANCZOS)

comp = Image.new('RGB', (orig_scaled.width + crop_match.width + 10, 300), (90, 0, 15))
comp.paste(orig_scaled, (0, 0))
comp.paste(crop_match, (orig_scaled.width + 10, 0))
comp.save('scratch/side_by_side_comparison.png')

print("Saved side_by_side_comparison.png")
