import os
from PIL import Image
import numpy as np

ref_crop = Image.open('scratch/ref_cards_crop.png').convert('RGB')
cards = Image.open('public/images/party_of_four_cards.png').convert('RGB')

# Let's save a side-by-side comparison of ref_cards_crop and party_of_four_cards
# Note: ref_cards_crop is (396, 250), cards is (792, 500) (2x)
ref_2x = ref_crop.resize(cards.size, Image.Resampling.LANCZOS)
ref_2x.save('scratch/ref_2x.png')

print("Ref 2x saved.")
