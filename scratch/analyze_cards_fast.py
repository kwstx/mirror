import os
from PIL import Image
import numpy as np
import scipy.signal

cards = Image.open('public/images/party_of_four_cards.png').convert('RGB')
ref = Image.open('public/images/party_of_four_reference.png').convert('RGB')
user_old = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789473470465.png').convert('RGB')
user_new = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789473482059.jpg').convert('RGB')

# Let's save crops from cards:
# Left half:
cards.crop((0, 0, 396, 500)).save('scratch/cards_left.png')
# Right half:
cards.crop((396, 0, 792, 500)).save('scratch/cards_right.png')

# Let's find the exact bounding box of the left card in cards:
# In cards, the left card is located on the left.
# Let's inspect the cards image:
# Size: 792 x 500.
# Background color: #5a000f -> (90, 0, 15)

cards_arr = np.array(cards)
print("cards shape:", cards_arr.shape)

# Let's print out what cards are in party_of_four_cards.png:
# In party_of_four_cards, there is:
# 1. Left card: tilted counter-clockwise slightly or clockwise?
# Let's check the corners of the left card.
