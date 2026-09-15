import os
from PIL import Image
import numpy as np

img = Image.open('scratch/test_cards_on_white.png').convert('RGB')
arr = np.array(img)

# Check corner colors (should be [255, 255, 255])
print("Corner (0, 0):", arr[0, 0])
print("Corner (0, -1):", arr[0, -1])
print("Corner (-1, 0):", arr[-1, 0])
print("Corner (-1, -1):", arr[-1, -1])

# Save transparent cards as public/images/party_of_four_cards.png
# Save both PNG with alpha channel so it works seamlessly on any white background
cards_trans = Image.open('scratch/cards_transparent.png')
cards_trans.save('public/images/party_of_four_cards.png', 'PNG', optimize=True)

if os.path.exists('dist/images'):
    cards_trans.save('dist/images/party_of_four_cards.png', 'PNG', optimize=True)

print("Saved transparent party_of_four_cards.png!")
