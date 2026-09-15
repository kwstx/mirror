import os
from PIL import Image
import numpy as np

orig = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789475594670.png').convert('RGB')
sim = Image.open('scratch/simulated_full_page.png').convert('RGB')

# Crop the cards area (x: 280..750, y: 140..425) from both:
crop_orig = orig.crop((280, 140, 750, 425))
crop_sim = sim.crop((280, 140, 750, 425))

# Save side-by-side
comp = Image.new('RGB', (crop_orig.width * 2 + 20, crop_orig.height), (90, 0, 15))
comp.paste(crop_orig, (0, 0))
comp.paste(crop_sim, (crop_orig.width + 20, 0))
comp.save('scratch/full_page_comparison.png')

print("Saved full_page_comparison.png")
