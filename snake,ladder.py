import random
ladder ={1:38,4:14,9:31,21:42,28:84,51:67,72:91,80:99}
snake  ={17:7,54:34,62:19,64:60,87:36,93:73,95:75,98:79}
pos1=0
pos2=0
def func(pos1):
    b=random.randint(1,6)
    pos1=pos1+b
    print(f"\nUr Dice Value is:{b}")
    if pos1 in ladder:
        print("\nYES!!climbed by Ladder")
        pos1=ladder[pos1]
        print(f"position is {pos1}\n")
    elif pos1 in snake:
        print("\nOops!!Bitten By snake")
        pos1=snake[pos1]
        print(f"position is {pos1}\n")
    else:
        print(f"Position is {pos1} ")
    return pos1
    
print("\n**Welcome tO Snake Ladder Game**\n")
while True:
    a=input("Enter \"A\" for throwing a dice\n")
    pos1=func(pos1)
    if pos1>=100:
        print("CONGRATS!!winner is 1st player")
        break
    b=input("Enter \"B\" for throwing a dice\n")
    pos2=func(pos2)
    if pos2>=100:
        print("CONGRATS!!winner is 2nd player")
        break