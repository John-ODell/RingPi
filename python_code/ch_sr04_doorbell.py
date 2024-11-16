import RPi.GPIO as GPIO
import time
import pygame

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
TRIG = 23
ECHO = 24
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# Initialize Pygame mixer
pygame.mixer.init()
pygame.mixer.music.load("/home/user/filetosound.wav")

def get_distance():
    GPIO.output(TRIG, False)
    time.sleep(2)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    return distance

try:
    while True:
        dist = get_distance()
        print("Distance:", dist, "cm")
        if dist < 60:
            pygame.mixer.music.play()
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
