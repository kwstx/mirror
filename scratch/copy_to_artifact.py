import shutil
import os

artifact_dir = r"C:/Users/galan/.gemini/antigravity/brain/ddc39c74-efb6-4df6-94ec-b3cf0ab7f65a"
shutil.copyfile("public/images/party_of_four_cards.png", os.path.join(artifact_dir, "party_of_four_cards.png"))
print("Copied to artifact dir.")
