import os
import glob
import random
import shutil

# --- Configuration ---
SOURCE_ROOT = "./data"
DEST_ROOT = "./data_small"
NUM_FILES_TO_KEEP = 500
# ---------------------

SOURCE_IMG_DIR = os.path.join(SOURCE_ROOT, "leftImg8bit", "train")
SOURCE_LBL_DIR = os.path.join(SOURCE_ROOT, "gtFine", "train")

DEST_IMG_DIR = os.path.join(DEST_ROOT, "leftImg8bit", "train")
DEST_LBL_DIR = os.path.join(DEST_ROOT, "gtFine", "train")

print(f"Finding all images in {SOURCE_IMG_DIR}...")
all_image_files = glob.glob(os.path.join(SOURCE_IMG_DIR, "**", "*.png"), recursive=True)

if not all_image_files:
    print(f"Error: No image files found in {SOURCE_IMG_DIR}. Did you set the SOURCE_ROOT correctly?")
    exit()

print(f"Found {len(all_image_files)} total images. Sampling {NUM_FILES_TO_KEEP}...")
sampled_image_files = random.sample(all_image_files, NUM_FILES_TO_KEEP)
copied_count = 0

for src_img_path in sampled_image_files:
    relative_path = os.path.relpath(src_img_path, SOURCE_IMG_DIR)
    base_filename = os.path.basename(relative_path).replace("_leftImg8bit.png", "")
    
    # --- Define all file paths ---
    
    # 1. Source files
    src_lbl_path = os.path.join(SOURCE_LBL_DIR, os.path.dirname(relative_path), 
                                f"{base_filename}_gtFine_labelIds.png")
    src_inst_path = os.path.join(SOURCE_LBL_DIR, os.path.dirname(relative_path), 
                                 f"{base_filename}_gtFine_instanceIds.png")
    
    # Check if all required files exist before copying
    if not os.path.exists(src_lbl_path) or not os.path.exists(src_inst_path):
        print(f"Skipping {base_filename}, missing label or instance file.")
        continue

    # 2. Destination files
    dest_img_path = os.path.join(DEST_IMG_DIR, relative_path)
    dest_lbl_path = os.path.join(DEST_LBL_DIR, os.path.dirname(relative_path), 
                                 f"{base_filename}_gtFine_labelIds.png")
    dest_inst_path = os.path.join(DEST_LBL_DIR, os.path.dirname(relative_path), 
                                  f"{base_filename}_gtFine_instanceIds.png")

    # --- Create directories and copy ---
    os.makedirs(os.path.dirname(dest_img_path), exist_ok=True)
    os.makedirs(os.path.dirname(dest_lbl_path), exist_ok=True)
    
    shutil.copy(src_img_path, dest_img_path)
    shutil.copy(src_lbl_path, dest_lbl_path)
    shutil.copy(src_inst_path, dest_inst_path)
    copied_count += 1

print(f"Done. Copied {copied_count} images (with labels and instances) to {DEST_ROOT}")