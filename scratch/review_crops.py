import os
from PIL import Image
import numpy as np

for name in ['full', 'balanced', 'close']:
    img = Image.open(f'scratch/final_candidate_{name}.png')
    
    # Save a crop of the left half for easy review
    crop_left = img.crop((0, 0, 420, 500))
    crop_left.save(f'scratch/review_left_{name}.png')
    
    # Check dimensions
    print(f"{name}: size={img.size}, mode={img.mode}")

print("Saved review crops.")
