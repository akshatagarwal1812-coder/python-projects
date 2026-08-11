
import random
import time
def waiting_game():
    print("Welcome to the Waiting Game!")
    target_time = random.randint(2, 5)
    print(input("enter to start the game"))
    start_time= int(time.time())
    print(input(f"your target time is: {target_time} seconds ENTER just after the target time without pressing any key"))
    last_time = int(time.time())
    print(f"Your reaction time was: {last_time - start_time} seconds")
    if last_time - start_time < target_time:
        print("You pressed too early! Try again.")
    elif last_time - start_time > target_time:
        print("You pressed too late! Try again.")
    else:
        print("Congratulations! You pressed at the right time!")
print(waiting_game())