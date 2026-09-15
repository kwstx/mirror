import os
from PIL import Image, ImageOps, ImageFilter
import numpy as np

cards_img = Image.open('public/images/party_of_four_cards.png').convert('RGBA')
ref_img = Image.open('public/images/party_of_four_reference.png').convert('RGBA')
user_old = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789473470465.png').convert('RGBA')
user_new = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789473482059.jpg').convert('RGBA')

print("cards_img size:", cards_img.size)
print("user_old size:", user_old.size)
print("user_new size:", user_new.size)

# Let's inspect the cards in cards_img
# We want to find the corners of the left card in cards_img
arr = np.array(cards_img)
bg_color = np.array([90, 0, 15, 255])

# Left card is approximately in x: [0, 350], y: [0, 500]
# Let's inspect the white border or corners of the left photo card
# In a polaroid / photo card, there's usually a white border or photo frame tilted at some angle.
# Let's find pixels with high brightness in the left half (white border)
r, g, b, a = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2], arr[:, :, 3]
is_white_border = (r > 200) & (g > 200) & (b > 200)

y_white, x_white = np.where(is_white_border[:, :350])
print(f"White border in left region: x=[{x_white.min()}, {x_white.max()}], y=[{y_white.min()}, {y_white.max()}]")

# Let's save a visualization of the left card edges
Image.fromarray((is_white_border[:, :350] * 255).astype(np.uint8)).save('scratch/white_border_left.png')
print("Saved scratch/white_border_left.png")
