# The following script moves all the clips from the default folder to the desired folder.
# You can assing your shortcut button on for saving buffer replays in different direcotry other than the original one
# You can create an .exe file if your stream deck software or its alternative doesn't support 
# running the script, using the follwoing line in cmd: pyinstaller --onefile clippingScrpt.py

import os
import shutil

def save_config(src_dir, dst_dir):
    with open('config.txt', 'w') as config_file:
        config_file.write(src_dir + '\n')
        config_file.write(dst_dir)

def load_config():
    with open('config.txt', 'r') as config_file:
        src_dir = config_file.readline().strip()
        dst_dir = config_file.readline().strip()
    return src_dir, dst_dir

if os.path.exists('config.txt'):
    src_dir, dst_dir = load_config()
else:
    src_dir = input('Enter the path to directory A: ')
    dst_dir = input('Enter the path to directory B: ')
    save_config(src_dir, dst_dir)

files = os.listdir(src_dir)

for file in files:
    src_file = os.path.join(src_dir, file)
    dst_file = os.path.join(dst_dir, file)

    if os.path.isdir(src_file):

        if os.path.exists(dst_file):

            for f in os.listdir(src_file):
                s = os.path.join(src_file, f)
                d = os.path.join(dst_file, f)
                shutil.move(s, d)
        else:
            shutil.move(src_file, dst_file)
    else:
        shutil.move(src_file, dst_file)
