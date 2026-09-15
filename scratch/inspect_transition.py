import os
from PIL import Image
import numpy as np

cards_orig = Image.open('public/images/party_of_four_cards.png').convert('RGBA')
cand_b = Image.open('scratch/candidate_party_B.png').convert('RGBA')

orig_arr = np.array(cards_orig)
cand_arr = np.array(cand_b)

# Compare x in [300, 792] - should be identical to cards_orig!
diff_right = np.max(np.abs(orig_arr[:, 320:, :3].astype(int) - cand_arr[:, 320:, :3].astype(int)))
print("Max diff on right side (x > 320):", diff_right)

# Let's check Card 2's left edge in cards_orig:
# Let's inspect the transition between Card 1 and Card 2 in cards_orig:
# In cards_orig, around y=100, x=240..260:
print("\nTransition at y=100 in cards_orig:")
for x in range(235, 260):
    print(f"x={x}: orig={orig_arr[100, x, :3]}, cand={cand_arr[100, x, :3]}")

print("\nTransition at y=200 in cards_orig:")
for x in range(245, 270):
    print(f"x={x}: orig={orig_arr[200, x, :3]}, cand={cand_arr[200, x, :3]}")
