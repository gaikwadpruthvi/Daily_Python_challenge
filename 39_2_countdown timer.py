#	Create a countdown timer using the time module.
'''
import time

def countdown_timer():
    seconds = int(input("Enter the countdown time in seconds: "))
    
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02}:{secs:02}"
        print(timer, end="\r")  # Overwrites the previous line
        time.sleep(1)
        seconds -= 1

    print("Time's up!")

# Run the countdown timer
countdown_timer()
'''
import time
import sys

# For sound notification
try:
    import winsound  # Windows
except ImportError:
    import os  # macOS & Linux

def play_sound():
    """Plays a beep sound when the timer ends."""
    try:
        winsound.Beep(1000, 500)  # Beep at 1000 Hz for 500 ms (Windows)
    except NameError:
        os.system("printf '\a'")  # Beep sound for macOS/Linux

def countdown_timer():
    seconds = int(input("Enter the countdown time in seconds: "))
    
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02}:{secs:02}"
        print(timer, end="\r")  # Overwrites the previous line
        time.sleep(1)
        seconds -= 1

    print("Time's up!")
    play_sound()  # Play sound when countdown ends

# Run the countdown timer
countdown_timer()
