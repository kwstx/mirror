import os
from PIL import Image, ImageFilter
import numpy as np

# Load party_of_four_cards.png
cards = Image.open('public/images/party_of_four_cards.png').convert('RGBA')
arr = np.array(cards)

# Background is #5a000f -> [90, 0, 15]
bg = np.array([90, 0, 15], dtype=float)

# Calculate color distance to background
diff = np.linalg.norm(arr[:, :, :3].astype(float) - bg, axis=2)

# Create alpha mask:
# For pixels very close to bg (diff < 15): alpha = 0
# For pixels in transition / shadow (15 <= diff < 40): partial alpha
# For pixels in cards (diff >= 40): alpha = 255
alpha = np.zeros(diff.shape, dtype=np.uint8)
alpha[diff >= 35] = 255
trans_mask = (diff >= 10) & (diff < 35)
alpha[trans_mask] = ((diff[trans_mask] - 10) / 25.0 * 255).astype(np.uint8)

# Let's create an RGBA image with transparent background
# For card pixels with shadow on white:
# On white background, shadow is dark with alpha
# Let's create a clean transparent version with shadow for white background
cards_rgba = Image.new('RGBA', cards.size, (0, 0, 0, 0))

# Put alpha onto cards
cards_with_alpha = cards.copy()
cards_with_alpha.putalpha(Image.fromarray(alpha))

# Let's create an elegant drop shadow for the cards on white background:
# Extract card silhouette (alpha > 128)
card_silhouette = Image.fromarray((alpha > 128).astype(np.uint8) * 255)
shadow = Image.new('RGBA', cards.size, (0, 0, 0, 0))
shadow_stamp = Image.new('RGBA', cards.size, (0, 0, 0, 60))
shadow.paste(shadow_stamp, (0, 4), card_silhouette)
shadow = shadow.filter(ImageFilter.GaussianBlur(radius=5))

# Combine shadow and cards on transparent canvas
transparent_cards = Image.new('RGBA', cards.size, (0, 0, 0, 0))
transparent_cards.paste(shadow, (0, 0), shadow)
transparent_cards.paste(cards_with_alpha, (0, 0), cards_with_alpha)

# Test on white background
test_white = Image.new('RGBA', cards.size, (255, 255, 255, 255))
test_white.paste(transparent_cards, (0, 0), transparent_cards)
test_white.save('scratch/test_cards_on_white.png')
transparent_cards.save('scratch/cards_transparent.png')

print("Saved test_cards_on_white.png and cards_transparent.png")
