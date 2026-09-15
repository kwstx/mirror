import os
from PIL import Image
import numpy as np

cards = Image.open('public/images/party_of_four_cards.png').convert('RGB')
old_user = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789473470465.png').convert('RGB')

# Let's find where old_user matches in cards:
cards_crop = cards.crop((0, 0, 287, 400))
cards_crop.save('scratch/cards_left_crop.png')
print("Saved cards_left_crop.png")

print("old_user size:", old_user.size)
# Let's check the pixels of old_user:
old_arr = np.array(old_user)
print("old_user top left pixel:", old_arr[0, 0])
print("old_user top right pixel:", old_arr[0, -1])
print("old_user bottom left pixel:", old_arr[-1, 0])
print("old_user bottom right pixel:", old_arr[-1, -1])
