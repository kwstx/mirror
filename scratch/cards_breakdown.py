import os
from PIL import Image
import numpy as np

cards = Image.open('public/images/party_of_four_cards.png').convert('RGB')
ref = Image.open('public/images/party_of_four_reference.png').convert('RGB')

# Let's save a clear diagram of cards with annotations of all 4 cards
# In party_of_four_cards: (792 x 500)
# Card 1 (left): x ~ [0, 320], y ~ [20, 420]
# Card 2 (center-top): x ~ [240, 520], y ~ [20, 320]
# Card 3 (center-bottom): x ~ [300, 560], y ~ [220, 480]
# Card 4 (right): x ~ [500, 780], y ~ [80, 420]

print("Card 1 (Left guy):", "tilted at ~ -5 deg")
