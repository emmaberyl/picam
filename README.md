picam
=====

A simple python script to capture images from Raspberry Pi + Camera Board

Scehdule the script to run at a specified interval (here, once a minute) if desired:

pi$ sudo crontab -e

then add: * * * * * /home/pi/camera.py 2>&1

save and exit.
