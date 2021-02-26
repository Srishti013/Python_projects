import random
yes=True
right=True
comp_score=0
pl_score=0
while yes:
    print("Welcome!!\nHere are some rules:\nYou have to enter a number between 1 to 5 and if the choice of computer matches your choice you win")
    print("1-->Red\n2-->Blue\n3-->Green\n4-->Yellow\n5-->Black")
    right=True
    while(right):
        col=int(input("Enter a number from 1 to 5:\n"))
        if(col>=1 and col<=5):
            right=False
        else:
            print("Wrong input")
            right=True
    if(col==1):
        cl='red'
    elif(col==2):
        cl='blue'
    elif(col==3):
        cl='green'
    elif(col==4):
        cl='yellow'
    else:
        cl='black'
    print(f"Your color is:\n{cl}")
    comp_col=random.randint(1,5)
    if(comp_col==1):
        ccl='red'
    elif(comp_col==2):
        ccl='blue'
    elif(comp_col==3):
        ccl='green'
    elif(comp_col==4):
        ccl='yellow'
    else:
        ccl='black'
    print(f"The computer's color is:\n{ccl}")
    if(ccl==cl):
        pl_score+=1
        print(f"-----You won!!!-----\nYour score={pl_score}\nComputer's score={comp_score}")
    else:
        comp_score+=1
        print(f"-----Sorrry! you lost ;)-----\nYour score={pl_score}\nComputer's score={comp_score}")
    print("If you want to play again press 'y' else press 'n'")
    right=True
    while(right):
        choice=input()
        if(choice=='y'):
            yes=True
            right=False
        elif(choice=='n'):
            yes=False
            if comp_score>pl_score:
                print("You lost! Better luck next time.....")
            elif pl_score>comp_score:
                print("Congratulations!!! You won :)")
            else:
                print("It was a tie....")
            print("-----------Thanks for playing--------")
            right=False
        else:
            print("Press 'y' or 'n'\n") 
            
