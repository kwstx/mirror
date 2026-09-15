import os
from PIL import Image, ImageFilter, ImageDraw
import numpy as np

# Load original pristine cards collage (395 x 250 or 792 x 500)
# We have scratch/true_orig_cards.png extracted directly from the user's reference screenshot
cards_1x = Image.open('scratch/true_orig_cards.png').convert('RGBA') # (395, 250)
cards_2x = cards_1x.resize((792, 500), Image.Resampling.LANCZOS) # (792, 500)

arr_2x = np.array(cards_2x)
bg = np.array([90, 0, 15], dtype=float)

# Color difference to #5a000f
diff = np.linalg.norm(arr_2x[:, :, :3].astype(float) - bg, axis=2)

# Precise alpha mask of the cards:
# Inside cards: diff is large (diff > 40)
# Background: diff is near 0
# Edge transition: smooth alpha
alpha = np.zeros(diff.shape, dtype=np.float32)
# Inside card
alpha[diff >= 30] = 1.0
# Transition zone
trans = (diff > 8) & (diff < 30)
alpha[trans] = (diff[trans] - 8) / 22.0

# Convert cards RGB to un-tinted where alpha is applied:
# If a pixel was blended with red background:
# C_obs = alpha * C_card + (1 - alpha) * C_bg
# => C_card = (C_obs - (1 - alpha) * C_bg) / max(alpha, 0.01)
cards_rgb = arr_2x[:, :, :3].astype(np.float32)
cards_unblended = np.zeros_like(cards_rgb)
for c in range(3):
    cards_unblended[:, :, c] = np.clip((cards_rgb[:, :, c] - (1.0 - alpha) * bg[c]) / np.maximum(alpha, 0.05), 0, 255)

card_rgba = np.dstack([cards_unblended, (alpha * 255).astype(np.uint8)]).astype(np.uint8)
cards_clean_img = Image.fromarray(card_rgba, 'RGBA')

# Create clean drop shadow on white background:
# Shadow silhouette from alpha
silh = Image.fromarray((alpha > 0.3).astype(np.uint8) * 255, 'L')
# Smooth shadow
shadow_img = Image.new('RGBA', (792, 500), (0, 0, 0, 0))
shadow_tint = Image.new('RGBA', (792, 500), (0, 0, 0, 50))
shadow_img.paste(shadow_tint, (0, 3), silh)
shadow_blur = shadow_img.filter(ImageFilter.GaussianBlur(radius=4))

# Combine on pure white background
white_canvas = Image.new('RGBA', (792, 500), (255, 255, 255, 255))
white_canvas.paste(shadow_blur, (0, 0), shadow_blur)
white_canvas.paste(cards_clean_img, (0, 0), cards_clean_img)

# Save result
final_white_bg = white_canvas.convert('RGB')
final_white_bg.save('scratch/cards_pure_white_bg.png')

# Also create transparent version
trans_canvas = Image.new('RGBA', (792, 500), (0, 0, 0, 0))
trans_canvas.paste(shadow_blur, (0, 0), shadow_blur)
trans_canvas.paste(cards_clean_img, (0, 0), cards_clean_img)
trans_canvas.save('scratch/cards_pure_trans.png')

print("Saved scratch/cards_pure_white_bg.png and scratch/cards_pure_trans.png")
