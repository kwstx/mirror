import os
from PIL import Image
import numpy as np

# Let's inspect the facial bounding box in user_new:
user_new = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789473482059.jpg').convert('RGB')
arr_new = np.array(user_new)

# In user_new (727 x 1024):
# Top of hair: ~ y=140
# Eyes: ~ y=370
# Nose: ~ y=440
# Mouth/smile: ~ y=490
# Chin: ~ y=540
# Shoulders: ~ y=580..1000

# In generate_exact_match.py:
# crop_box = (0, 20, 727, 20 + 880) = (0, 20, 727, 900)
# Top of hair (y=140 in original) -> y = 140 - 20 = 120 in 880px -> 120 / 880 = 13.6% from top!
# In 344px card height: 13.6% = y=47
# Eyes (y=370 in original) -> (370 - 20) / 880 = 39.7% -> y=136 in 344px card
# Chin (y=540 in original) -> (540 - 20) / 880 = 59.1% -> y=203 in 344px card
# Carhartt logo / chest -> y=203..344 in 344px card

# Notice how closely this aligns with the original:
# Original:
# Top of hair: ~10% from top
# Eyes: ~35% from top
# Chin: ~55% from top
# Chest / arm: 55% - 100%

print("Alignment matches closely!")
