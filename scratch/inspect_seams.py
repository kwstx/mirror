import os
from PIL import Image, ImageDraw
import numpy as np

# Let's inspect the seam in candidate_party_B.png
for label in ['A', 'B', 'C', 'D']:
    cand = Image.open(f'scratch/candidate_party_{label}.png')
    
    # Zoom in on the left card (0, 0, 450, 500)
    crop_left = cand.crop((0, 0, 450, 500))
    crop_left.save(f'scratch/zoom_left_{label}.png')
    
    # Zoom in on the seam between Card 1 and Card 2 (200, 0, 350, 400)
    crop_seam = cand.crop((200, 0, 350, 400))
    crop_seam.save(f'scratch/zoom_seam_{label}.png')

print("Saved zoomed crops for inspection.")
