import os
import shutil

scene_name = 'ai_001_001'
camera = 'scene_cam_00_final_preview'
if(not os.path.exists(scene_name)):
    os.mkdir(scene_name)


start_path = r'Hypersim_raw_data/{}/images/'.format(scene_name)
dst_path = r'{}/images/'.format(scene_name)
if(not os.path.exists(dst_path)):
    os.mkdir(dst_path)
file_list = []

for filename in os.listdir(start_path):
    # print(filename)
    if(filename[0] != ('.')):
        file_path = start_path + filename + '/'
        print(file_path)
        if(filename == camera):  # only read a single camera
            for f in os.listdir(file_path):
                src_path = file_path + f
                file_list.append(f)
                shutil.copy(src_path, dst_path)

file_list.sort()
# generate the train and test.txt
rate = 0.8
train_file = open('{}/train.txt'.format(scene_name), "w")
test_file = open('{}/test.txt'.format(scene_name), "w")
for i in range(0, int(rate*len(file_list))):
    train_file.write(str(file_list[i]) + "\n")
train_file.close()

for i in range(int(rate*len(file_list)), len(file_list)):
    test_file.write(str(file_list[i]) + "\n")
test_file.close()
    

    