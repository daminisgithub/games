import random
l=["Rock",'Paper',"Scissor"]

print("\n**Welcome To ROCK PAPER SCISSOR GAME**")
a=int(input('''\nHey do u want to play game with me
press
1.For Yes
2.For No \n'''))
if a==1:
    while True:
        b=int(input('''\nEnter Ur Choice
        1.For Rock
        2.For Scissor
        3.For Paper\n'''))
        

        ucount=0
        ccount=0
        mychoice=random.choice(l)
        
    
        if b==1:
            userchoice="Rock"
        elif b==2:
            userchoice="Scissor"
        elif b==3:
            userchoice="Paper"
        else:
            print("INVALID CHOICE!!")

        
        if userchoice=="Rock" and mychoice=="Scissor"or userchoice=="Scissor" and mychoice=="Paper" or userchoice=="Paper" and mychoice=="Rock":

             print("\nCONGRATS U HAVE WIN !!AS-")
             print("My choice =" ,mychoice)
             print("Ur choice =",userchoice)
             ucount=ucount+1
             print("Your Score",ucount)
             print("My Score",ccount)

        elif userchoice==mychoice:
             print("\noops!!! The Game has Tie...Try one more Time")
             print("My choice =" ,mychoice)
             print("Ur choice =",userchoice)
             ucount=ucount+1
             ccount=ccount+1
             print("Your Score",ucount)
             print("My Score",ccount)

        

        else:
             print("\nYes I have win!!")
             print("My choice =" ,mychoice)
             print("Ur choice =",userchoice)
             ccount=ccount+1
             print("Your Score",ucount)
             print("My Score",ccount)

        c=input("Write yes/no if u want to exit-\n")
        if c=="yes" and "Yes":
            break

else:
    
    print("okkk !!Do come again")