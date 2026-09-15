import os
from PIL import Image
import numpy as np

img = Image.open('scratch/perfect_clean_white_test.png')
arr = np.array(img)

# Check background
# Corners must be pure white [255, 255, 255]
print("Top-left (0,0):", arr[0, 0])
print("Top-right (0,-1):", arr[0, -1])
print("Bottom-left (-1,0):", arr[-1, 0])
print("Bottom-right (-1,-1):", arr[-1, -1])

# Save as public/images/party_of_four_cards.png
trans_img = Image.open('scratch/perfect_clean_trans.png')
trans_img.save('public/images/party_of_four_cards.png', 'PNG', optimize=True)

if os.path.exists('dist/images'):
    trans_img.save('dist/images/party_of_four_cards.png', 'PNG', optimize=True)

# Copy to artifact dir for presentation
artifact_dir = r"C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a"
img.save(os.path.join(artifact_dir, "party_of_four_white_bg.png"), 'PNG', optimize=True)
trans_img.save(os.path.join(artifact_dir, "party_of_four_cards.png"), 'PNG', optimize=True)

print("Saved clean cards to public/images and artifact directory!")
