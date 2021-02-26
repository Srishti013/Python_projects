import random
def game(comp,you):
    if comp==you:
        return None
    if comp=='stone':
        if you=='paper':
            return True
        else:
            return False
    elif comp=='paper':
        if you=='scissor':
            return True
        else:
            return False
    elif comp=='scissor':
        if you=='stone':
            return True
        else:
            return False
yes=True
while(yes):
    you=input("Your Turn:\n's'-->'stone\n'p'-->'paper\n'sc'-->scissor\n")
    if(you=='s'):
        you='stone'
    elif(you=='p'):
        you='paper'
    else:
        you='scissor'
    print(f"You entered :\n            {you}")
    comp=random.randint(1,3)
    if(comp==1):
        comp='stone'
    elif(comp==2):
        comp='paper'
    else:
        comp='scissor'
    print(f"Computer entered:\n            {comp}")
    result=game(comp,you)
    if(result==None):
        print("-------It was a tie :)-------")
    elif(result==True):
        print("----------You Won!!!!----------")
    else:
        print("---------Sorry! you lost---------")
    ch=input("If you want to play again press 'y' else 'n'\n")
    if(ch=='n'):
        print("Thanks for playing")
        yes=False
