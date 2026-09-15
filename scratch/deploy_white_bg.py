import os
from PIL import Image
import numpy as np

img = Image.open('scratch/cards_pure_white_bg.png')
arr = np.array(img)

print("Image size:", img.size)
print("Corner (0,0):", arr[0, 0])
print("Corner (0,-1):", arr[0, -1])
print("Corner (-1,0):", arr[-1, 0])
print("Corner (-1,-1):", arr[-1, -1])

# Save as public/images/party_of_four_cards.png
# We can save both transparent and white background versions or the transparent PNG
trans_img = Image.open('scratch/cards_pure_trans.png')
trans_img.save('public/images/party_of_four_cards.png', 'PNG', optimize=True)

if os.path.exists('dist/images'):
    trans_img.save('dist/images/party_of_four_cards.png', 'PNG', optimize=True)

# Also copy to artifact dir for presentation
artifact_dir = r"C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a"
img.save(os.path.join(artifact_dir, "party_of_four_white_bg.png"), 'PNG', optimize=True)
trans_img.save(os.path.join(artifact_dir, "party_of_four_cards.png"), 'PNG', optimize=True)

print("Saved to public/images and artifact directory!")
