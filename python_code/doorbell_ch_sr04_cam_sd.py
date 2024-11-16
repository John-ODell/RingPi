from picamera2 import Picamera2, Preview
import time
from datetime import datetime
import RPi.GPIO as GPIO
import pygame

# Set up GPIO pins
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
TRIG = 23
ECHO = 24
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

# Initialize Pygame mixer
pygame.mixer.init()
pygame.mixer.music.load("/home/user/filepathtosound.wav")

# Initialize the camera
picam2 = Picamera2()
camera_config = picam2.create_still_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores")
picam2.configure(camera_config)

def get_distance():
    GPIO.output(TRIG, False)
    time.sleep(0.5)  
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    
    pulse_start = time.time()
    pulse_end = time.time()
    
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()
    
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    return distance

def capture():
    picam2.start_preview(Preview.QTGL)
    timestamp = datetime.now().isoformat()
    picam2.start()
    time.sleep(2)
    picam2.capture_file('/home/user/Pictures/%s.jpg' % timestamp)
    picam2.stop_preview()
    picam2.stop()
    print(f"Image saved: /home/user/Pictures/{timestamp}.jpg")

try:
    while True:
        dist = get_distance()
        print("Distance:", dist, "cm")
        if dist < 16:
            print("Distance is less than half a foot, capturing image and playing sound...")
            pygame.mixer.music.play()
            capture()
            print("Image captured and sound played.")
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
