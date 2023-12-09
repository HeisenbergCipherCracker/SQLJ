import os
import sys
import os
import subprocess
import platform




#!This feature is not available for windows

current_directory = os.getcwd()

sys.path.append(current_directory)






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


def soundplay():
    if platform.system().lower() == "darwin":
        Playsound.playsound_normal_macos("beep.wav")
    
    elif platform.system().lower() == "linux":
        Playsound.playsound_normal_linux("beep.wav")
    
    elif platform.system().lower() == "linux":
        Playsound.windows_pay_sound("beep.wav")
    
    else:
        # No such platform founded
        pass
    


    
    

    

Playsound.playsound_normal_macos("beep.wav")
