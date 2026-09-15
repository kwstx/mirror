import os
from PIL import Image
import numpy as np

orig = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789475594670.png').convert('RGB')
sim = Image.open('scratch/simulated_full_page.png').convert('RGB')

arr_orig = np.array(orig)
arr_sim = np.array(sim)

# Let's inspect the cards area in orig (x: 300..460, y: 155..330)
# Let's find the 4 corners of Card 1 in orig:
# We can find all pixels where Card 1 is in orig:
bg = np.array([90, 0, 15], dtype=float)

mask_orig_c1 = np.zeros((425, 1024), dtype=bool)
mask_sim_c1 = np.zeros((425, 1024), dtype=bool)

for y in range(155, 330):
    for x in range(300, 460):
        # In orig, Card 1 is left of Card 2 (x < 0.09*(y-158) + 435) and above Card 3 (y < 320)
        c_o = arr_orig[y, x].astype(float)
        c_s = arr_sim[y, x].astype(float)
        if np.linalg.norm(c_o - bg) > 25:
            if x < 435 and (y < 290 or x < 380):
                mask_orig_c1[y, x] = True
        if np.linalg.norm(c_s - bg) > 25:
            if x < 435 and (y < 290 or x < 380):
                mask_sim_c1[y, x] = True

y_o, x_o = np.where(mask_orig_c1)
y_s, x_s = np.where(mask_sim_c1)

print(f"Orig Card 1 bounds in 1024x425: x in [{x_o.min()}, {x_o.max()}], y in [{y_o.min()}, {y_o.max()}]")
print(f"Sim  Card 1 bounds in 1024x425: x in [{x_s.min()}, {x_s.max()}], y in [{y_s.min()}, {y_s.max()}]")

# Top-Left corner in orig:
tl_o = (x_o[np.argmin(x_o + y_o)], y_o[np.argmin(x_o + y_o)])
tl_s = (x_s[np.argmin(x_s + y_s)], y_s[np.argmin(x_s + y_s)])
print(f"Orig TL: {tl_o}, Sim TL: {tl_s}")

# Bottom-Left corner in orig:
bl_o = (x_o[np.argmin(x_o - y_o)], y_o[np.argmin(x_o - y_o)])
bl_s = (x_s[np.argmin(x_s - y_s)], y_s[np.argmin(x_s - y_s)])
print(f"Orig BL: {bl_o}, Sim BL: {bl_s}")
