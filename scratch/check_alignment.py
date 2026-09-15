import os
from PIL import Image
import numpy as np

orig_2x = Image.open('scratch/orig_cards_binary.png').convert('RGB').resize((792, 500), Image.Resampling.LANCZOS)
new_2x = Image.open('scratch/perfect_party_2x.png').convert('RGB')

arr_orig = np.array(orig_2x)
arr_new = np.array(new_2x)

bg = np.array([90, 0, 15], dtype=float)

# Compare masks of Card 1:
mask_orig = np.linalg.norm(arr_orig[:, :300].astype(float) - bg, axis=2) > 25
mask_new = np.linalg.norm(arr_new[:, :300].astype(float) - bg, axis=2) > 25

# Card 1 bounds in orig_2x:
y_o, x_o = np.where(mask_orig)
y_n, x_n = np.where(mask_new)

print(f"Orig Card 1 bounds: x in [{x_o.min()}, {x_o.max()}], y in [{y_o.min()}, {y_o.max()}]")
print(f"New Card 1 bounds:  x in [{x_n.min()}, {x_n.max()}], y in [{y_n.min()}, {y_n.max()}]")

# Overlap difference:
iou = np.sum(mask_orig & mask_new) / np.sum(mask_orig | mask_new)
print(f"Mask IoU: {iou * 100:.2f}%")

# Save a comparison overlay showing orig vs new
diff_vis = Image.new('RGB', (300, 500), (0, 0, 0))
diff_arr = np.array(diff_vis)
diff_arr[mask_orig, 0] = 255 # red for orig
diff_arr[mask_new, 1] = 255  # green for new (yellow where both overlap)
Image.fromarray(diff_arr).save('scratch/mask_alignment_check.png')
print("Saved mask_alignment_check.png")
