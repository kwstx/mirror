import os
from PIL import Image
import numpy as np

user_orig = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789473470465.png').convert('RGB')

# Unrotate user_orig by +4.95 degrees around TL corner (30.93, 1.26)
unrotated = user_orig.rotate(4.95, resample=Image.Resampling.BICUBIC, center=(30.93, 1.26))
unrotated.save('scratch/user_orig_unrotated.png')

# In unrotated:
# Top edge is horizontal at y ~ 1
# Left edge is vertical at x ~ 31
# Let's inspect the bounding box of the photo in unrotated:
# Width and height:
print("Saved user_orig_unrotated.png")
