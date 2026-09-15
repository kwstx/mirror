import os
from PIL import Image
import numpy as np

orig_user = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789473470465.png').convert('RGB')
new_cards = Image.open('scratch/exact_placed_cards_2x.png').convert('RGB')

# Let's inspect orig_user (287, 272)
print("orig_user size:", orig_user.size)

# In orig_user:
# It shows the left card with the blond guy:
# Top white border, left white border, right side where next card starts, bottom where t-shirt is.
# Let's crop from new_cards the equivalent region:
# In new_cards (792, 500):
# Let's crop x: [0, 350], y: [0, 450]
crop_new = new_cards.crop((0, 0, 350, 450))
crop_new.save('scratch/compare_new_crop.png')

print("Saved compare_new_crop.png")
