picam
=====

A simple python script to capture images from Raspberry Pi + Camera Board

Scehdule the script to run at a specified interval (here, once a minute) if desired:

  sudo crontab -e
  * * * * * /home/pi/camera.py 2>&1
