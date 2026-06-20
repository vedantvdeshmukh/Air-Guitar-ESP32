import serial
import pygame
import sys

# -------- SERIAL --------
port = "COM11"   # change if needed
baud_rate = 115200

esp = serial.Serial(port, baud_rate, timeout=0.01)
esp.flushInput()

print("Connected to ESP32!")

# -------- PYGAME INIT --------
pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🎸 Air Guitar Live")

font_big = pygame.font.SysFont("Arial", 120)
font_small = pygame.font.SysFont("Arial", 40)

# -------- LOAD SOUNDS --------
sounds = {
    "C": pygame.mixer.Sound("sounds/c_major.wav"),
    "D": pygame.mixer.Sound("sounds/d_major.wav"),
    "E": pygame.mixer.Sound("sounds/e_major.wav"),
    "F": pygame.mixer.Sound("sounds/f_major.wav"),
    "G": pygame.mixer.Sound("sounds/g_major.wav"),
    "A": pygame.mixer.Sound("sounds/a_major.wav"),
    "B": pygame.mixer.Sound("sounds/b_major.wav"),
    "Am": pygame.mixer.Sound("sounds/a_minor.wav"),
}

current_chord = ""
flash_timer = 0

clock = pygame.time.Clock()

# -------- MAIN LOOP --------
while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # ---- SERIAL READ ----
    if esp.in_waiting > 0:
        data = esp.readline().decode().strip()

        if data in sounds:
            current_chord = data
            sounds[data].play()
            flash_timer = 10   # flash frames

    # ---- DRAW ----
    if flash_timer > 0:
        screen.fill((30, 30, 60))  # flash color
        flash_timer -= 1
    else:
        screen.fill((15, 15, 15))  # normal background

    # Draw chord
    text = font_big.render(current_chord, True, (0, 255, 200))
    rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, rect)

    # Footer text
    footer = font_small.render("Air Guitar - Live Mode", True, (200, 200, 200))
    screen.blit(footer, (20, HEIGHT - 50))

    pygame.display.flip()