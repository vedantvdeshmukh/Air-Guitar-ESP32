import serial
import pygame
import os
import time

PORT = "COM5"
BAUD = 9600

pygame.mixer.init()

BASE_PATH = os.path.dirname(__file__)

def load_sound(filename):
    return pygame.mixer.Sound(os.path.join(BASE_PATH, "sounds", filename))

sounds = {
    "C": load_sound("c_major.wav"),
    "D": load_sound("d_major.wav"),
    "E": load_sound("e_major.wav"),
    "F": load_sound("f_major.wav"),
    "G": load_sound("g_major.wav"),
    "A": load_sound("a_major.wav"),
    "Am": load_sound("a_minor.wav"),
    "Em": load_sound("e_minor.wav"),
}

try:
    print("Connecting to AirGuitar Bluetooth...")
    esp = serial.Serial(PORT, BAUD, timeout=0.1)
    time.sleep(2)
    esp.reset_input_buffer()

    print("Connected Successfully 🎸")

    while True:
        if esp.in_waiting:
            chord = esp.readline().decode(errors='ignore').strip()

            if chord in sounds:
                print("Playing:", chord)
                sounds[chord].play()

except Exception as e:
    print("Connection Error:", e)