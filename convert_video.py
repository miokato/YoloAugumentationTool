#!/usr/local/bin/python3

import sys
import os
import glob
import subprocess

paths = glob.glob('./data/*/*/*.mp4', recursive=True)

out_dir = './data/movies'
os.makedirs(out_dir, exist_ok=True)

prefix = 'out_'

for i, path in enumerate(paths):
    _, filename = os.path.split(path)
    out_filename = prefix + '{}_'.format(i) + filename
    out_path = os.path.join(out_dir, out_filename)

    subprocess.run(['ffmpeg', '-i', path, '-vf', 'transpose=2', '-metadata:s:v:0', 'rotate=0', out_path])

print('Completed!')