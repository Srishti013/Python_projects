board=[" "]*9
def display_board():
    print(f"{board[0]}  |{board[1]}  |{board[2]}")
    print(" ---------")
    print(f"{board[3]}  |{board[4]}  |{board[5]}")
    print(" ---------")
    print(f"{board[6]}  |{board[7]}  |{board[8]}")
    print(" ---------")
    
P_1=input("Player_1: Choose X or O\n")
if(P_1=="O"):
    P_2="X"
else:
    P_2="O"    
print(f"Player_2:Your character is {P_2}")
c=0
flag=False
display_board()
while(c<=8):
    c+=2
    print("Player_1's Turn")
    num1=int(input("Enter the place where you want to place your character(from 1-9):\n"))
    while(board[num1-1]!=" " or num1<1 or num1>9):
        print("This choice cannot be made")
        num1=int(input("Enter New Choice"))
    if(board[num1-1]==" "):
        board[num1-1]=P_1
    display_board()
    
    
    if(c>=6):
        if((board[0]==P_1 and board[1]==P_1 and board[2]==P_1) or (board[3]==P_1 and board[4]==P_1 and board[5]==P_1) or (board[6]==P_1 and board[7]==P_1 and board[8]==P_1)):
            print("---------Congratulations!! Player_1 You have won :)---------")
            flag=True
            break
        elif((board[0]==P_1 and board[3]==P_1 and board[6]==P_1) or (board[1]==P_1 and board[4]==P_1 and board[7]==P_1) or (board[2]==P_1 and board[5]==P_1 and board[8]==P_1)):
            print("---------Congratulations!! Player_1 You have won :)---------")
            flag=True
            break
        elif((board[0]==P_1 and board[4]==P_1 and board[8]==P_1) or (board[2]==P_1 and board[4]==P_1 and board[6]==P_1) ):
            print("---------Congratulations!! Player_1 You have won :)---------")
            flag=True
            break 
           
    print("Player_2's Turn")
    num2=int(input("Enter the place where you want to place your character:\n"))
    while(board[num2-1]!=" " or num1<1 or num1>9):
        print("This choice cannot be made")
        num2=int(input("Enter New Choice\n"))
    if(board[num2-1]==" "):
        board[num2-1]=P_2
    display_board()
    if(c>=6):
                if((board[0]==P_2 and board[1]==P_2 and board[2]==P_2) or (board[3]==P_2 and board[4]==P_2 and board[5]==P_2) or (board[6]==P_2 and board[7]==P_2 and board[8]==P_2)):
                        display_board()
                        print("---------Congratulations!! Player_2 You have won :)---------")
                        flag=True
                        break
                elif((board[0]==P_2 and board[3]==P_2 and board[6]==P_2) or (board[1]==P_2 and board[4]==P_2 and board[7]==P_2) or (board[2]==P_2 and board[5]==P_2 and board[8]==P_2)):
                    display_board()
                    print("---------Congratulations!! Player_2 You have won :)---------")
                    flag=True   
                    break
                elif((board[0]==P_2 and board[4]==P_2 and board[8]==P_2) or (board[2]==P_2 and board[4]==P_2 and board[6]==P_2) ):
                    display_board()
                    print("---------Congratulations!! Player_2 You have won :)---------")
                    flag=True
                    break
if(not flag):
    print("It's a tie")
