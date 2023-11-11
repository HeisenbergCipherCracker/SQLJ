from pynput import keyboard
import os


class Key_Handler:
    @staticmethod
    def F2_btn(key):
        if key == keyboard.Key.f2:
            os.system('cls' if os.name == 'nt' else 'clear')
            return "F2"    
    @staticmethod
    def F3_btn(key):
        if key == keyboard.Key.f3:
            os.system('cls' if os.name == 'nt' else 'clear')
            return "F3"   
    
    @staticmethod
    def F4_btn(key) 


    def on_release(self, key):
        pass


# Create an instance of the Key_Handler class
handler = Key_Handler()

# Create a listener and assign the handler's methods as callbacks
with keyboard.Listener(on_press=handler.on_press, on_release=handler.on_release) as listener:
    listener.join()