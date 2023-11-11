from pynput import keyboard
import os


class Key_Handler:
    
    @staticmethod
    def F1_btn(key):
        if key == keyboard.Key.f1:
            os.system('cls' if os.name == 'nt' else 'clear')
            return "F1"
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
    def F4_btn(key):
        if key == keyboard.Key.f4:
            os.system('cls' if os.name == 'nt' else 'clear')
            return "F4"
    
    @staticmethod
    def F5_btn(key):
        if key == keyboard.Key.f5:
            os.system('cls' if os.name == 'nt' else 'clear')
            return "F5"
    
    @staticmethod
    def F6_btn(key):
        if key == keyboard.Key.f6:
            os.system('cls' if os.name == 'nt' else 'clear')
            return "F6"
    
    @staticmethod
    def F7_btn(key):
        if key == keyboard.Key.f7:
            os.system('cls' if os.name == 'nt' else 'clear')
            return "F7"
    
    @staticmethod
    def F8_btn(key):
        if key == keyboard.Key.f8:
            os.system('cls' if os.name == 'nt' else 'clear')
            return "F8"
    
    @staticmethod
    def F9_btn(key):
        if key == keyboard.Key.f9:
            os.system('cls' if os.name == 'nt' else 'clear')
            return "F9"
        
    @staticmethod
    def F8_btn(key):
        if key == keyboard.Key.f8:
            os.system('cls' if os.name == 'nt' else 'clear')
            return "F8"
    
    @staticmethod
    def F9_btn(key):
        if key == keyboard.Key.f9:
            os.system('cls' if os.name == 'nt' else 'clear')
            return "F9"
    
    @staticmethod
    def F10_btn(key):
        if key == keyboard.Key.f10:
            os.system('cls' if os.name == 'nt' else 'clear')
            return "F10"
        
    @staticmethod
    def F11_btn(key):
        if key == keyboard.Key.f11:
            os.system('cls' if os.name == 'nt' else 'clear')
            return "F11"
    
    @staticmethod
    def F12_btn(key):
        if key == keyboard.Key.f12:
            os.system('cls' if os.name == 'nt' else 'clear')
            return "F12"
    
        


    def on_release(self, key):
        pass


# Create an instance of the Key_Handler class
handler = Key_Handler()

# Create a listener and assign the handler's methods as callbacks
with keyboard.Listener(on_press=handler.on_press, on_release=handler.on_release) as listener:
    listener.join()