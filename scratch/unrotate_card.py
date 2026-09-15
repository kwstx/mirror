import os
from PIL import Image
import numpy as np

cards = Image.open('public/images/party_of_four_cards.png').convert('RGBA')

# Let's unrotate the cards image by +5.0 degrees around the card center
# Card center:
cx = (-0.7 + 318.9) / 2
cy = (40.7 + 417.3) / 2
print(f"Card center: ({cx}, {cy})")

# Let's rotate cards by +5.0 degrees (counter-clockwise by -5 degrees to make upright)
# In PIL, rotate(angle, resample=BICUBIC, center=(cx, cy))
# Notice PIL rotate positive angle is counter-clockwise.
# Since the card was rotated by -5.0 degrees (clockwise by 5 deg), rotating by +5.0 degrees will make it upright!
unrotated = cards.rotate(5.0, resample=Image.Resampling.BICUBIC, center=(cx, cy))

# Let's crop the upright card region:
# In the upright image, the card should be centered at (cx, cy) with width ~285, height ~403
crop_box = (int(cx - 145), int(cy - 205), int(cx + 145), int(cy + 205))
card_upright = unrotated.crop(crop_box)
card_upright.save('scratch/card_upright.png')
print("Saved scratch/card_upright.png, size:", card_upright.size)
