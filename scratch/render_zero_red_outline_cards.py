import os
from PIL import Image, ImageFilter, ImageDraw
import numpy as np
from scipy.ndimage import binary_fill_holes, binary_erosion, binary_dilation

# Load the original 2x cards (792 x 500)
orig_2x = Image.open('scratch/true_orig_cards.png').convert('RGBA').resize((792, 500), Image.Resampling.LANCZOS)
arr = np.array(orig_2x)
bg = np.array([90, 0, 15], dtype=float)

# 1. Detect all card content (excluding only the dark wine background)
diff = np.linalg.norm(arr[:, :, :3].astype(float) - bg, axis=2)
raw_card_mask = diff > 25

# 2. Fill any holes inside the cards (so orange/red shirts or dark areas inside cards are 100% preserved)
filled_mask = binary_fill_holes(raw_card_mask)

# 3. Erode by 2 pixels to completely eliminate ANY outer red fringe from the background
inner_mask = binary_erosion(filled_mask, iterations=2)

# 4. Dilate by 1 pixel from inner_mask to create a clean crisp 3px white border around all card edges
border_mask = binary_dilation(inner_mask, iterations=3)

# 5. Build clean image:
# Outer canvas: transparent
clean_rgba = Image.new('RGBA', (792, 500), (0, 0, 0, 0))

# Paste white border
white_border_img = Image.new('RGBA', (792, 500), (252, 252, 252, 255))
clean_rgba.paste(white_border_img, (0, 0), Image.fromarray((border_mask * 255).astype(np.uint8)))

# Paste original cards content using inner_mask (strictly within inner_mask, so 0% red background bleed)
clean_rgba.paste(orig_2x, (0, 0), Image.fromarray((inner_mask * 255).astype(np.uint8)))

# 6. Create natural soft drop shadow for white background:
shadow_base = Image.new('RGBA', (792, 500), (0, 0, 0, 0))
shadow_tint = Image.new('RGBA', (792, 500), (0, 0, 0, 55))
shadow_base.paste(shadow_tint, (0, 3), Image.fromarray((border_mask * 255).astype(np.uint8)))
shadow_blur = shadow_base.filter(ImageFilter.GaussianBlur(radius=4.5))

# Combine shadow and clean cards on transparent canvas
final_trans = Image.new('RGBA', (792, 500), (0, 0, 0, 0))
final_trans.paste(shadow_blur, (0, 0), shadow_blur)
final_trans.paste(clean_rgba, (0, 0), clean_rgba)

# Test on pure white background
test_white = Image.new('RGB', (792, 500), (255, 255, 255))
test_white.paste(final_trans, (0, 0), final_trans)

# Save test outputs
test_white.save('scratch/no_red_outline_white.png')
final_trans.save('scratch/no_red_outline_trans.png')

# Save directly to public/images and dist/images
final_trans.save('public/images/party_of_four_cards.png', 'PNG', optimize=True)

if os.path.exists('dist/images'):
    final_trans.save('dist/images/party_of_four_cards.png', 'PNG', optimize=True)

# Copy to artifact dir for presentation
artifact_dir = r"C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a"
test_white.save(os.path.join(artifact_dir, "party_of_four_white_bg.png"), 'PNG', optimize=True)
final_trans.save(os.path.join(artifact_dir, "party_of_four_cards.png"), 'PNG', optimize=True)

print("Successfully created zero-red-outline cards asset!")
