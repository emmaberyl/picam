import os
#name of directory where pictures files will be written
location = "sanfrancisco"

#this was my first attempt at pulling the system time, adapted from other code
#out of desperation when I had no internet access (the horror!)
#picstr = "/home/pi/" + location + "/" + os.popen("date +%F_%H%M").read().rstrip() + ".jpg"

#slightly more straightforward:
from datetime import datetime
now = datetime.now()
picstr = "/home/pi/" + location + now.strftime("/%Y-%m-%d_%H%M.jpg")

#capture the picture and write to the desired file name
os.system("raspistill -o " + picstr)
