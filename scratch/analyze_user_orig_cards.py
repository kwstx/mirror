import os
from PIL import Image
import numpy as np

orig_full = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789475594670.png').convert('RGB')
arr = np.array(orig_full)

# Background color: #5a000f -> [90, 0, 15]
bg = np.array([90, 0, 15], dtype=float)

# Let's inspect the cards area in orig_full:
# In orig_full (1024, 425):
# Find all non-background pixels:
diff = np.linalg.norm(arr.astype(float) - bg, axis=2)
is_cards = diff > 25

y_c, x_c = np.where(is_cards)
print(f"Cards bounds in orig_full (1024x425): x in [{x_c.min()}, {x_c.max()}] (w={x_c.max()-x_c.min()+1}), y in [{y_c.min()}, {y_c.max()}] (h={y_c.max()-y_c.min()+1})")

# Let's crop the cards area exactly:
# Cards area: x in [317, 712], y in [158, 407] (w=396, h=250)
cards_exact = orig_full.crop((x_c.min(), y_c.min(), x_c.max() + 1, y_c.max() + 1))
print("Cards exact size:", cards_exact.size)
cards_exact.save('scratch/user_orig_cards_exact.png')

# Let's inspect the Left Card (Card 1) in orig_full:
# In cards_exact (or orig_full):
# Let's find the 4 corners of the Left Card:
# In cards_crop: Left card is around x: [315, 450], y: [165, 330] in orig_full.
# Let's print out the exact corners of the Left Card!
