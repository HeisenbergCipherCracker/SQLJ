from pynput import keyboard
import os


class Key_Handler:
    
    @staticmethod
    def F1_btn(key):
        if key == keyboard.Key.f1:
            return "F1"
    @staticmethod
    def F2_btn(key):
        if key == keyboard.Key.f2:
            return "F2"    
    @staticmethod
    def F3_btn(key):
        if key == keyboard.Key.f3:
            return "F3"   
    
    @staticmethod
    def F4_btn(key):
        if key == keyboard.Key.f4:
            return "F4"
    
    @staticmethod
    def F5_btn(key):
        if key == keyboard.Key.f5:
            return "F5"
    
    @staticmethod
    def F6_btn(key):
        if key == keyboard.Key.f6:
            return "F6"
    
    @staticmethod
    def F7_btn(key):
        if key == keyboard.Key.f7:
            return "F7"
    
    @staticmethod
    def F8_btn(key):
        if key == keyboard.Key.f8:
            return "F8"
    
    @staticmethod
    def F9_btn(key):
        if key == keyboard.Key.f9:
            return "F9"
        
    @staticmethod
    def F8_btn(key):
        if key == keyboard.Key.f8:
            return "F8"
    
    @staticmethod
    def F9_btn(key):
        if key == keyboard.Key.f9:
            return "F9"
    
    @staticmethod
    def F10_btn(key):
        if key == keyboard.Key.f10:
            return "F10"
        
    @staticmethod
    def F11_btn(key):
        if key == keyboard.Key.f11:
            return "F11"
    
    @staticmethod
    def F12_btn(key):
        if key == keyboard.Key.f12:
            return "F12"
    
        


    def on_release(self, key):
        pass


# Create an instance of the Key_Handler class
handler = Key_Handler()

# Create a listener and assign the handler's methods as callbacks
with keyboard.Listener(on_press=handler.on_press, on_release=handler.on_release) as listener:
    listener.join()