import os
from PIL import Image
import numpy as np

orig = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789475594670.png').convert('RGB')
sim = Image.open('scratch/corrected_full_sim.png').convert('RGB')

arr_orig = np.array(orig)
arr_sim = np.array(sim)

bg = np.array([90, 0, 15], dtype=float)

# Compare left edge:
# For each y in 175..320: find the first non-bg x in orig and sim:
print("Y    | Orig X | Sim X  | Diff")
print("----------------------------")
diffs = []
for y in range(175, 325, 10):
    x_o = None
    x_s = None
    for x in range(300, 360):
        if x_o is None and np.linalg.norm(arr_orig[y, x].astype(float) - bg) > 25:
            x_o = x
        if x_s is None and np.linalg.norm(arr_sim[y, x].astype(float) - bg) > 25:
            x_s = x
    d = abs(x_o - x_s) if (x_o and x_s) else None
    diffs.append(d)
    print(f"{y:3d}  | {str(x_o):6s} | {str(x_s):6s} | {d}")

# Save side by side crop of cards
crop_o = orig.crop((280, 140, 750, 425))
crop_s = sim.crop((280, 140, 750, 425))

comp = Image.new('RGB', (crop_o.width * 2 + 20, crop_o.height), (90, 0, 15))
comp.paste(crop_o, (0, 0))
comp.paste(crop_s, (crop_o.width + 20, 0))
comp.save('scratch/corrected_comparison.png')

print("Saved scratch/corrected_comparison.png")
