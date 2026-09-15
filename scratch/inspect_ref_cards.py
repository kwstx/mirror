import os
from PIL import Image
import numpy as np

ref = Image.open('public/images/party_of_four_reference.png').convert('RGB')
cards = Image.open('public/images/party_of_four_cards.png').convert('RGB')

# Let's save a side-by-side or detailed inspection of both ref and cards
print("ref size:", ref.size)
print("cards size:", cards.size)

# In ref, where is the cards collage?
# In scratch/single_test.py:
# .cards-container { position: absolute; top: 158px; left: 317px; width: 396px; height: 250px; }
# Ref was 1024x425, cards in ref is located around (317, 158) with size 396x250.
# cards.png is 792x500 (exactly 2x of 396x250).

ref_cards_crop = ref.crop((317, 158, 317 + 396, 158 + 250))
ref_cards_crop.save('scratch/ref_cards_crop.png')
print("Saved scratch/ref_cards_crop.png")
