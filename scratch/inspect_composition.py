import os
from PIL import Image
import numpy as np

cards = Image.open('public/images/party_of_four_cards.png').convert('RGB')
ref = Image.open('public/images/party_of_four_reference.png').convert('RGB')
user_old = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789473470465.png').convert('RGB')
user_new = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789473482059.jpg').convert('RGB')

# Let's inspect the cards image
print("cards.size:", cards.size)
print("ref.size:", ref.size)
print("user_old.size:", user_old.size)
print("user_new.size:", user_new.size)

# Let's check how the left card looks.
# In party_of_four_cards:
# Is it a single image of 4 tilted cards?
# Let's check the cards in party_of_four_cards:
# 1) Left card: a guy with blond-ish highlights, beige shirt, resting chin on hand.
# 2) Center-top card: girl/guy smiling?
# 3) Center-bottom card?
# 4) Right card?

# Let's find the exact boundaries of the inner photo of the left card in cards.
# Where is the photo inside the white border?
# The photo has distinct colors, bounded by a white polaroid border.
# Let's find the inner photo rectangle/quadrilateral of the left card.
