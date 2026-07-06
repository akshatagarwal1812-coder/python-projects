# 0 stands for snake
# 1 stands for water
# 2 stands for gun
dict = {
    0:"snake",
    1:"water",
    2:"gun"
}
scoreP= 0
scoreC=0
for i in range(3):
    player= int(input("0 for snake 1 for water 2 for gun: "))
    import random
    computer = random.choice([0, 1, 2])
    print(f"player chose {dict[player]} and computer chose {dict[computer]}")
    if(player==computer):
        print("tie")
    elif(player==0 and computer==1):
        print("player wins")
        scoreP+=1
    elif(player==1 and computer==0):
        print("computer wins")
        scoreC+=1
    elif(player==2 and computer==1):
        print("computer wins")
        scoreC+=1
    elif(player==1 and computer==2):
        print("player wins")
        scoreP+=1   
    elif(player==0 and computer==2):
        print("computer wins")
        scoreC+=1
    elif(player==2 and computer==0):
        print("player wins")
        scoreP+=1

print(f"Player's score: {scoreP}")
print(f"Computer's score: {scoreC}")
if(scoreP>scoreC):
    print("Congratulations! You won the game")
else:
    print("Unfortunately! you lost the game")    