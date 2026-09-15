import os
from PIL import Image
import numpy as np

user_orig = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789473470465.png').convert('RGB')
arr = np.array(user_orig)

# Let's save a view of user_orig
user_orig.save('scratch/user_orig_view.png')

# Let's inspect user_orig:
# Background is dark red #5a000f [81, 0, 14]
# Top-left of user_orig: dark red background
# Card top edge: thin white border line
# Card left edge: thin white border line
# Inside: photo of blond guy in beige shirt
# Right side: woman's arm resting on him, and Card 2 (white border + photo) overlapping!

print("user_orig shape:", arr.shape)
