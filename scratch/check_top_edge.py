import os
from PIL import Image
import numpy as np

orig = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789475594670.png').convert('RGB')
sim = Image.open('scratch/corrected_full_sim.png').convert('RGB')

arr_orig = np.array(orig)
arr_sim = np.array(sim)
bg = np.array([90, 0, 15], dtype=float)

# Compare top edge along x from 320 to 430:
print("X    | Orig Y | Sim Y  | Diff")
print("----------------------------")
for x in range(325, 435, 10):
    y_o = None
    y_s = None
    for y in range(160, 200):
        if y_o is None and np.linalg.norm(arr_orig[y, x].astype(float) - bg) > 25:
            y_o = y
        if y_s is None and np.linalg.norm(arr_sim[y, x].astype(float) - bg) > 25:
            y_s = y
    d = abs(y_o - y_s) if (y_o and y_s) else None
    print(f"{x:3d}  | {str(y_o):6s} | {str(y_s):6s} | {d}")
