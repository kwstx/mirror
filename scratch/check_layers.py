import os
from PIL import Image
import numpy as np

cards = Image.open('public/images/party_of_four_cards.png').convert('RGBA')
print("cards size:", cards.size)

# Let's inspect the cards collage:
# Let's check the overlap:
# Does the center card overlap on TOP of the left card?
# Let's check x=250..330, y=100..400
arr = np.array(cards)
# The center-top card or center card:
# In scratch/cards_left.png:
# In the right side of the left card (around x=250..300), the next card has a white border and photo that sits ON TOP of the left card!
# Let's verify which card is on top:
# If the next card sits on top of the left card, then the left card's right side is underneath the next card's white border!
