import os
from PIL import Image, ImageDraw
import numpy as np

cards = Image.open('public/images/party_of_four_cards.png').convert('RGB')
ref = Image.open('public/images/party_of_four_reference.png').convert('RGB')
user_old = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789473470465.png').convert('RGB')
user_new = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789473482059.jpg').convert('RGB')

# Let's inspect where user_old comes from:
# Let's check the size of user_old: (287, 272)
# Let's check ref size: (1024, 425)
# Let's search user_old in ref vs cards:
# Let's find user_old in ref:
user_old_arr = np.array(user_old)
ref_arr = np.array(ref)

# Let's find the closest match in ref:
h_old, w_old, _ = user_old_arr.shape
best_ref_diff = float('inf')
best_ref_pos = None

# Let's test with a coarse step
for y in range(0, ref_arr.shape[0] - h_old + 1, 2):
    for x in range(0, ref_arr.shape[1] - w_old + 1, 2):
        sub = ref_arr[y:y+h_old, x:x+w_old]
        diff = np.mean(np.abs(sub.astype(float) - user_old_arr.astype(float)))
        if diff < best_ref_diff:
            best_ref_diff = diff
            best_ref_pos = (x, y)

print(f"Match in party_of_four_reference.png: diff={best_ref_diff:.2f}, pos={best_ref_pos}")

# Also search in cards:
cards_arr = np.array(cards)
best_cards_diff = float('inf')
best_cards_pos = None
for y in range(0, cards_arr.shape[0] - h_old + 1, 2):
    for x in range(0, cards_arr.shape[1] - w_old + 1, 2):
        sub = cards_arr[y:y+h_old, x:x+w_old]
        diff = np.mean(np.abs(sub.astype(float) - user_old_arr.astype(float)))
        if diff < best_cards_diff:
            best_cards_diff = diff
            best_cards_pos = (x, y)

print(f"Match in party_of_four_cards.png: diff={best_cards_diff:.2f}, pos={best_cards_pos}")
