import subprocess

import os,sys

cur = os.getcwd()
sys.path.append(cur)

def safe_play_sound():
    subprocess.run(["python", "sound.py"],cwd="lib/sound")

safe_play_sound()