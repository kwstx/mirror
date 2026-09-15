import os
from PIL import Image
import numpy as np

img = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789473470465.png')
print("img size:", img.size, "mode:", img.mode)

# Let's save it to scratch to view or inspect
img.save('scratch/old_user_inspect.png')

# In media_1789473470465.png:
# Top-left is dark red background [81, 0, 14]
# Then there is a white border line tilted slightly
# Inside the white border is the photograph of the blond guy in beige shirt!
# Around the photograph is a thin white photo border (~2-4px white edge).
