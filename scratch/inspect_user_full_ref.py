import os
from PIL import Image
import numpy as np

# Load the exact original screenshot provided by the user
orig_full = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789475594670.png').convert('RGB')
user_new = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789473482059.jpg').convert('RGB')

print("orig_full size:", orig_full.size) # (1024, 425)

# Save the full cards region from orig_full
# In 1024x425, where are the cards?
# Let's crop x: [300, 750], y: [150, 425]
cards_crop = orig_full.crop((300, 150, 750, 425))
cards_crop.save('scratch/orig_user_cards_crop.png')

# Let's save a crop of the left card in orig_full
left_card_crop = orig_full.crop((300, 160, 450, 340))
left_card_crop.save('scratch/orig_user_left_card.png')

print("Saved scratch/orig_user_cards_crop.png and scratch/orig_user_left_card.png")
