import time
import sys
import os
import threading    
from playsound import playsound

lyrics = [
    "",
    "",
    "Merah pipi kamu",
    "Kau pun lirik aku",
    "Tepat di bawah lampu",
    "Kau bisikkan kamu...",
    "Apa yang kau mau",
    "dia atau aku",
    "Garam atau madu",
    "",
    "Hold my hand",
    "Don’t, don’t tell your friends",
    "Cerita kemarin",
    "Ku ingat kemarin",
    "manismu kaya permen",
    "I hope this never end",
    "Oke you’ll be my gwen and i’ll be the spiderman"
]

def typewriter(text, delay=0.043, bold=False):
    if bold:
        sys.stdout.write('\033[1m')
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    if bold:
        sys.stdout.write('\033[0m')
    print()

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def play_music():
    playsound(r'C:\Users\adeli\Documents\tester\pukimai.mp3')

if __name__ == "__main__":

    music_thread = threading.Thread(target=play_music, daemon=True)
    music_thread.start()

    for line in lyrics:
        clear_screen()
        typewriter(line, bold=True)
        time.sleep(1.2)

    clear_screen()
    typewriter("Garam & Madu Versi python", bold=True)
    input("press enter to exit script")
    clear_screen()