import os
from PIL import Image
import numpy as np
import scipy.signal

ref = Image.open('public/images/party_of_four_reference.png').convert('RGB')
crop = Image.open(r'C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a/.user_uploaded/media_1789473470465.png').convert('RGB')

ref_arr = np.array(ref)
crop_arr = np.array(crop)

print("Ref shape:", ref_arr.shape)
print("Crop shape:", crop_arr.shape)

# Let's inspect the crop image:
# Size: 287 wide, 272 high.
# Let's check where in ref or in another image it appears:
# Let's compute fast cross correlation for each scale
for scale in [0.5, 0.75, 1.0, 1.25, 1.5, 2.0]:
    sw = int(round(crop.width * scale))
    sh = int(round(crop.height * scale))
    if sw <= ref.width and sh <= ref.height:
        resized_crop = crop.resize((sw, sh), Image.Resampling.BILINEAR)
        arr_c = np.array(resized_crop).astype(float)
        
        # Mean squared error on gray
        ref_gray = np.mean(ref_arr, axis=2)
        crop_gray = np.mean(arr_c, axis=2)
        
        # Convolve
        crop_gray_norm = crop_gray - np.mean(crop_gray)
        res = scipy.signal.correlate2d(ref_gray - np.mean(ref_gray), crop_gray_norm, mode='valid')
        y, x = np.unravel_index(np.argmax(res), res.shape)
        max_corr = res[y, x] / (np.std(crop_gray_norm) * np.std(ref_gray[y:y+sh, x:x+sw]) * sw * sh + 1e-6)
        print(f"Scale {scale:.2f} (size {sw}x{sh}): max correlation={max_corr:.4f} at (x={x}, y={y})")
