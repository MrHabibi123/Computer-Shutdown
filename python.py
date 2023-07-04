import os
import pyttsx3

userInfo = input("Would you like to shut down your computer? Y or N (USE CAPS)?")
sec = 20


if userInfo == "Y":
    os.system(f"shutdown /s /t {sec}")
    pyttsx3.speak(f"your computer will shut down in {sec}seconds")
    
else:
    pyttsx3.speak(f"your computer will not shutdown.")

    

