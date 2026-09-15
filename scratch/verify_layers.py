import os
from PIL import Image
import numpy as np

cards = Image.open('public/images/party_of_four_cards.png').convert('RGB')
arr = np.array(cards)

# In cards, Card 2 is around x: [250, 500], y: [20, 320]
# Card 2 has a white border and a photo.
# The white border of Card 2 clearly cuts over the right side of Card 1!
# That means if we render Card 1 on the canvas, and then keep Card 2, 3, 4 on top,
# the result will have clean, natural overlapping edges just like the original design!

# Let's verify what the mask of Card 2 and other overlapping cards is:
# We can find all pixels of Card 2 & 3 that overlap Card 1 by looking at where Card 2's white border and content start.
