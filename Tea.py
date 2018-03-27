import datetime
import time
import winsound
from datetime import timedelta

minutes = int(input("Bitte Minuten eingeben: "))
seconds = int(input("Bitte Sekunden eingeben: "))

n = minutes*60+seconds
i = 0

while n > 0: 
    print(timedelta(minutes=minutes, seconds=seconds) - timedelta(seconds=i),end="\r")
    n -= 1
    i += 1
    time.sleep(1)

print("Tee ist fertig!")
winsound.PlaySound("SystemExit",winsound.SND_FILENAME)
