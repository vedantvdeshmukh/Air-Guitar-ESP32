import serial
import pygame

port = "COM5"
baud_rate = 115200

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()

sounds = {
    "C": pygame.mixer.Sound("sounds/c_major.wav"),
    "G": pygame.mixer.Sound("sounds/g_major.wav"),
    "Am": pygame.mixer.Sound("sounds/a_minor.wav"),
    "F": pygame.mixer.Sound("sounds/f_major.wav"),
    "D": pygame.mixer.Sound("sounds/d_major.wav"),
    "Em": pygame.mixer.Sound("sounds/e_minor.wav"),
    "A": pygame.mixer.Sound("sounds/a_major.wav"),
    "E": pygame.mixer.Sound("sounds/e_major.wav"),
}

try:
    esp = serial.Serial(port, baud_rate, timeout=0.01)
    esp.flushInput()
    print("Connected to ESP32!")

    while True:
        if esp.in_waiting > 0:
            data = esp.readline().decode(errors='ignore').strip()
            print("Received:", data)

            if data in sounds:
                sounds[data].play()

except Exception as e:
    print("Error:", e)