import pickle
import os
import subprocess

valid_idx_path = 'scene_stairs/valid_image_idx.pkl'
img_path = 'scene_stairs/images/scene_cam_00_final_preview/'

with open(valid_idx_path, 'rb') as f:
    valid_imgs = pickle.load(f)
    print(valid_imgs)
    
img_names = os.listdir(img_path)
img_names.sort()
img_id = 1

to_remove = []
for img_name in img_names:
    splitted = img_name.split('.')
    if splitted[-1].lower() == 'jpg' or splitted[-1].lower == 'jpeg' or splitted[-1].lower() == 'png':
        if img_id not in valid_imgs:
            full_img_path = os.path.join(img_path, img_name)
            to_remove.append(full_img_path)
        img_id += 1

for full_img_path in to_remove:
    subprocess.run(['rm', full_img_path])
    print('removed', full_img_path)
