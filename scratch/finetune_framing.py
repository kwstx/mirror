import os
from PIL import Image, ImageDraw
import numpy as np

# Let's inspect the framings:
# In user_new (727 x 1024):
# The guy has his head at y: [150, 450], chest and Carhartt jacket at y: [450, 950].
# He has a nice smile, dimples, brown hair.

# Let's test a few fine-tuned crops to make sure the face and jacket are framed harmoniously:
user_new = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789473482059.jpg').convert('RGBA')

# Target aspect ratio: 280 / 398 = 0.7035175879396985
# If w = 727, h = 727 / 0.7035 = 1033.4 -> Full image (0, 0, 727, 1024) is already almost exact!
# Let's test:
# 1. Full image: (0, 0, 727, 1024) -> aspect ratio 0.710. Resized to 280 x 398.
#    This shows his hair, face, shoulders, and full Carhartt jacket with the logo patch on the left chest!
# 2. Centered crop with slightly more headroom: (15, 0, 727-15, int((727-30)/280*398))
# 3. Slightly closer portrait framing: (30, 40, 727-30, 40 + int((727-60)/280*398))

print("User new size:", user_new.size)
