import os


class Playsound:
    @staticmethod
    def playsound_normal(fname):
        current_directory = os.getcwd()
        path = os.path.join(current_directory, fname)
        os.system(f"afplay {fname}")


# Playsound.playsound_normal("beep.wav")
