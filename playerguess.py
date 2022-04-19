import random
randnumber=random.randrange(1,10)
playerguess=int(input("***Enter any number***:-"))
guesss=1

while(playerguess!=randnumber):
    print("**OOPS wrong guessing***")
    if(playerguess<randnumber):
        print("Enter a higher value")
    else:
        print("Enter a smaller value")

    playerguess=int(input("Hence Enter another number:"))
    guesss=guesss+1

print(f"CONGRATULATION U HAVE GUESSED CORRECT at gussed no. {guesss}")
print("\n")

with open ("guinessrecord.txt","w") as f:
    f.write("The lower guess no. is 5")
with open("guinessrecord.txt","r") as f:
    highrecord = f.read()
    highrecord = int(highrecord)

if(guesss<highrecord):
    print("U have break the record hence printed in guinessrecord text visit to see that!!!!")
    guesss=str(guesss)
    with open("guinessrecord.txt","w") as f:
        f.write(f"Now The guess record is :-{guesss}")
