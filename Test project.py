import time

seconds = 0
minutes = 0
hours = 0
while True:
    time.sleep(1)
    seconds += 1
    if seconds == 60:
        seconds = 0
        minutes += 1
    if minutes == 60:
        minutes = 0
        hours += 1
    if hours == 24:
        hours = 0
    print(f"{hours:02d}:{minutes:02d}:{seconds:02d}", end="\r", flush=True)