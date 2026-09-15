import os
from PIL import Image
import numpy as np

orig_full = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789475594670.png').convert('RGB')
arr = np.array(orig_full)
bg = np.array([90, 0, 15], dtype=float)

diff = np.linalg.norm(arr.astype(float) - bg, axis=2)
is_cards = (diff > 25) & (np.arange(425)[:, None] > 150)

y_c, x_c = np.where(is_cards)
print(f"Cards area: x in [{x_c.min()}, {x_c.max()}] (w={x_c.max()-x_c.min()+1}), y in [{y_c.min()}, {y_c.max()}] (h={y_c.max()-y_c.min()+1})")

cards_exact = orig_full.crop((x_c.min(), y_c.min(), x_c.max() + 1, y_c.max() + 1))
print("Cards exact size:", cards_exact.size) # (396, 250)
cards_exact.save('scratch/true_orig_cards.png')

# Let's inspect the Left Card (Card 1) in true_orig_cards:
# Size is (396, 250)!
# In true_orig_cards (396, 250):
# Card 1 (Left Card with blond guy) is located at x in [0, 140], y in [10, 175]!
# Let's find the EXACT 4 corners of Card 1 in true_orig_cards:
