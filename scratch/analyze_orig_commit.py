import os
from PIL import Image
import numpy as np

orig = Image.open('scratch/orig_commit_cards.png').convert('RGB')
user_orig = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789473470465.png').convert('RGB')

print("orig size:", orig.size)
print("user_orig size:", user_orig.size)

# Let's crop the left card area in orig (792, 500):
orig_left = orig.crop((0, 0, 400, 500))
orig_left.save('scratch/orig_left_full.png')

# Let's find the exact region of the left card in orig:
# Where does the original left card lie in orig?
# Let's find the exact 4 corners of the photo in orig:
orig_arr = np.array(orig)
# Background is #5a000f:
bg = np.array([90, 0, 15], dtype=float)

# In orig, what is the card?
# Let's inspect the white border / photo area of Card 1 in orig:
# Let's find the 4 corners of Card 1 in orig:
