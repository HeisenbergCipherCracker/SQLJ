import os
from pydub import AudioSegment
import simpleaudio as sa

def play_wav(filename):
    # Get the current path and construct the file_path
    current_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_directory, "lib", "sound", filename)

    # Load the WAV file using pydub
    sound = AudioSegment.from_file(file_path, format="wav")

    # Convert to bytes and play using simpleaudio
    wave_obj = sa.WaveObject(sa.samples_to_array(sound.raw_data), sound.channels, sound.sample_width, sound.frame_rate)
    play_obj = wave_obj.play()
    play_obj.wait_done()

# Example usage
filename = "BEEP.wav"
play_wav(filename)
