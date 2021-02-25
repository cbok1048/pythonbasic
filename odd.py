from datetime import datetime

for odds in range(1,60,2):
    print(odds , end=' ')
odds

right_this_minute = datetime.today().minute

if right_this_minute in odds:
    print("this minute seem a little old.")
else:
    print("Not an old minute")