import os
import sys
import os

#!This feature is not available for windows

cur = os.getcwd()
sys.path.append(cur)

class Playsound:
    @staticmethod
    def playsound_normal_macos(fname):
        current_directory = os.getcwd()
        path = os.path.join(current_directory, fname)
        os.system(f"afplay {fname}")

    @staticmethod
    def playsound_normal_linux(fname):
        current_directory = os.getcwd()
        path = os.path.join(current_directory, fname)
        os.system(f"aplay {fname}")
    
    @staticmethod
    def windows_pay_sound(fname):
        current_directory = os.getcwd()
        path = os.path.join(current_directory, fname)
        os.system(f"start {fname}")



# Playsound.playsound_normal_macos("beep.wav")
