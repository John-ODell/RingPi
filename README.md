Ring Pi, Raspberry Pi Zero W Bluetooth and Camera Doorbell by John O'Dell (johncodell@outlook.com)

Items Needed
- Raspberry Pi Zero WH (With Headers Soldered)
- HC-SR04 Ultrasonic Sensor
- Raspberrry RPi Compatable Camera
- Bluetooth Speaker
- Micro SD Card

Download the Raspberry Pi Imager https://www.raspberrypi.com/software/
MobaXterm (SSH/VNC/Headless) https://mobaxterm.mobatek.net/download.html

SET UP INSTRUCTIONS
 - if you know how to setup a Raspberry Pi, Connect it to Wi-Fi and BlueTooth,
  Skip to the ----RING PI----- Section.

Open the Raspberry Pi Imager
- Choose Device
  - Raspberry Pi Zero
- Operating System 
  - Rasberry Pi OS (32-Bit) With Raspberry Pi Desktop
  - if you know how to set up a headless Pi and connect it to a bluetooth speaker the Desktop Environment is not required but makes it much easier for beginners.
- Desktop Environment is preffered for the full Ring Pi experience
   - Storage
      - MAKE SURE YOU CHOOSE YOUR MICRO SD CARD! DO NOT CHOOSE 
        DRIVE C OR D! CHECK THE MEMORY SIZE OF THE CARD BEFORE FORMATING!!!
        - Next
        - Edit Settings
            - Leave the hostname
            - You can change the user name, if you do change your directories
            to /home/"username"/ otherwise it is home/pi.
            - If you are using a screen you can configure lan later, if you are
            using headless go head and enter it now
        -Services
            - Enable SSH
            - Use password authentication
    -Save
Let it Write, Then Verify. (this will take sometime)

Put the SD card into the Raspberry Pi Zero W and wait for about 5 minutes for it
to initial boot.

IF YOU DO NOT HAVE A SCREEN/HEADLESS SET UP

Make sure you entered your Wi-Fi credentials before flashing. If you did not, put
the sd card back into the Pi Imager.
- Rasppberry Pi Device
 - (ignore)
- Operating System
 - Erase
- Storage
 - SD Card
- Re-Flash the SD card with the Approriate Raspberry Pi Os and enter your Wi-Fi Under the Edit Settings after pressing Next

Open MobaXterm after the inital boot and the Pi Zero W is connected to the Wi-Fi. Navigate to the top bar and press
- Tools 
 - Network scanner
  - Ip address range 1 -> 400
   - Your Pi Will be closer to 400
        - take picture/mark down the adresses
    - Click Session in the Top left
        - Click SSH
        - Enter the addresses until a warning screen asking for permission, you have found your pi
        - MobaXterm may want you to make a password, Choose once for this computer (this is not your pi password)

LOGGING INTO A RASPBERRY PI
- If its your first time with a raspberry pi, you will be prompted with your log in, this is either the username
that you set yourself, or the default is pi.
- When the password is prompted it will not show you typing anything, just press enter when you have typed it. 
- If it is incorrect you will be prompted to re-try.
  - The default password is raspberry
  - login = pi (username)
  - password = raspberry (password)

CONNECTING TO WIFI
-If you are using a screen, at this point at the top right connect to the Wi-Fi

If you are having Problems, use the command 
sudo raspi-config
    - then arrow down to networking, press enter
     and enter it in manually from there
    - use the command sudo reboot and check your connection

CONNECTING BLUETOOTH
- Next to the wifi is a blue tooth icon, press it and connect it to your blue tooth speaker

HEADLESS BLUETOOTH CONNECTION WITH DESKTOP
-Exit out of the current MobaXterm session
-Click on Session
  - VNC
    - Type the same adress
    - Wait until you see the desktop come up
    - in the top right Connect to blue tooth

HEADLESS BLUETOOTH CONNECTION WITH NO DESKTOP
- First start blue tooth service with these two commands
   - sudo systemctl start bluetooth
   - sudo systemctl enable bluetooth

We start the connection Process with this command
- sudo bluetoothctl

We start to scan for Bluetooth with these commands
- agent on
- defualt-agent
- scan on

A list of MAC adresses should start to appear as it is scanning. Take
note of the MAC adress of the device you are trying to connect to
XX:XX:XX:XX:XX:XX

Once found we pair with the speaker with these commands
- pair XX:XX:XX:XX:XX:XX
- trust XX:XX:XX:XX:XX:XX
- connect XX:XX:XX:XX:XX:XX

Then we exit out of bluetoothctl with the command
- sudo quit

Now to set the speaker as our default audio device, first we find the sinks list command
- pactl list short sinks

To set it to default, find the sink_name of the device and set it with the command
- pactl set-default-sink sink_name


-------------- RING PI----------------

Update and Install needed Packages
- sudo apt-get update
- sudo apt-get install python3-pip
- sudo apt-get install RPi.GPIO
- sudo apt-get install pygame
- sudo apt-get Picamera2 

TESTING THE BLUETOOTH SPEAKER

     Download a WAV file to the Pi Zero W with the wget Command or
     Use the dbell.wav
    - the command to play a sound is 
    aplay yoursound.wav
     - I found it easiest to connect to MobaExterm and move a file
        onto the Pi Zero W 
            - If done this way, it can be put in the home directory
            drag the your soundfile onto the side with the folders
            check to make sure it transfered
            cd /home/(user)/
            ls
             to play use the command
            aplay /home/(user)/soundfilename.format
             or navigate to the file
            cd /home/(user)/
             list the files in the folder with the command 
            ls
             and use the aplay command directly with the files in that folder
            aplay soundfilename.format
    
    Trouble Shooting
        - Other types of sound files will play, Though i had the best luck with WAV
        - wget and curl are picky, and file transfer is recommended
        - make sure the volume on the Pi and Bluetooth Speaker are Up
        - You do not have to store it in the Music folder

TESTING THE HC-SR04 ULTRASONIC SENSOR 

Open the file "ch_sr04_test.py" inside Thonny. 

Pin Connections
- Trig -> GPIO 23 (pin 16)
- Echo -> GPIO 24 (pin 18)
- VCC -> 5v (pin 2)
- GND -> GND (pin 6)

Create a new python file with the command
- sudo nano /home/user/ch_sr04_test.py

Either Copy and paste from Thonny into MobaXterm or type in the code provided
- Press CTRL+O, Enter, CTRL+X to save and exit

Next make the Python Script executable with this command
- chmod +x /home/user/ch_sr04_test.py

Finally, run the script and see the output from the command line
- python3 /home/user/ch_sr04_test.py

    Trouble Shooting
        - Make sure your pinouts are correct, Pi boards vary from each other
        - Make sure your libraries are up to date
            sudo apt-get update
            sudo apt-get upgrade
        - check your spelling and file paths
    

!!!!!!!!GET YOUR BLUETOOTH/HC_SR04 SENSOR WORKING HERE BEFORE MOVING FORWARD!!!!!!!


TESTING ULTRASONIC BLUETOOTH DOORBELL

Open the file "ch_sr04_doorbell" in Thonny IDE

Create a new python file with the command
- sudo nano /home/user/ch_sr04_doorbell.py

Copy and Paste Code, MobaXterm recommended
- Press CTRL+O, enter, CTRL+X to save and exit

Make the Python script executable with the command
- chmod +x /home/user/ch_sr04_doorbell.py

Run the code with the command
- python3 /home/user/ch_sr04_doorbell.py

When the ultrasonic sensor senses something that is 60cm or about 
2 feet away, it will play a sound on the bluetooth speaker. 

TESTING THE RASPBERRY PI CAMERA

Connect the camera to the CSI port by pulling down on the sides
of the black plastic, with the ribbon cables facing down.

use the command
- sudo raspi-config
  - Interfacing Options
    - Camera
      - Enable
- sudo reboot

To take a test image use the command
- raspistill -o image.jpg

to find it navigate back to the root of the Pi with
- cd
Then list what is on the root
- ls
and there should be a file named image.jpg

The Ring Pi Doorbell

Make sure the previous tests have worked. We will not be calling on the past
examples, but may be needed for debugging. 

Open the file "doorbell_ch_sr04_cam_sd" in Thonny Ide

Create a new python file with the command
- sudo nano /home/user/doorbell_ch_sr04_cam_sd.py

Copy and Paste Code, MobaXterm recommended
- Press CTRL+O, enter, CTRL+X to save and exit

Make the Python script executable with the command
- chmod +x /home/user/doorbell_ch_sr04_cam_sd.py

Run the code with the command
- python3 /home/user/doorbell_ch_sr04_cam_sd.py

When the ultrasonic sensor senses something that is 60cm or about 
2 feet away, it will play a sound on the bluetooth speaker and capture
an image that is saved to the sd card with a time stamp. The Pi Connected
to a Local Network or a direct HDMI output will show a preview of image as well 
when captured.

This is an alpha build as a ch_sr04 by itself is not good enough of detection
for accuracy, but it is good for motion. 

Please contact me for any questions or comments. Look for updates.

