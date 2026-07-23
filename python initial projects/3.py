import time
t=time.strftime('%H:%M:%S')
hour=int(time.strftime('%H'))
print(hour)
if(hour<12):
    print("good morning")
elif(hour>12 and hour<4):
    print("good affternoon")
elif(hour>4 and hour<8):
    print("good evening")
else:
    print("good bye")
 