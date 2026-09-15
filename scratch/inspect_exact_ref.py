import os
from PIL import Image
import numpy as np

# Load original reference
ref = Image.open('public/images/party_of_four_reference.png').convert('RGB')
user_crop = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789473470465.png').convert('RGB')

# Let's inspect ref in the area around cards (x=300..750, y=150..410)
# In ref, let's crop the left card area:
left_card_ref = ref.crop((300, 150, 480, 380))
left_card_ref.save('scratch/left_card_ref.png')

print("Saved scratch/left_card_ref.png")
print("user_crop size:", user_crop.size)

# Let's check how user_crop compares with left_card_ref
# In user_crop:
# Notice user_crop is (287, 272).
# Let's check the size in ref: left_card_ref is around (180, 230) in 1x, or 287x272 at ~1.3x/2x scale.
