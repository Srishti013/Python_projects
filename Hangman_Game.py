lives = ['''
  ________
   |     \|
   O      |
  /|\     |
  / \     |
          |
  =========
 ''' , '''
  ________
   |     \|
   O      |
  /|\     |
    \     |
          |
  =========
  ''' , '''
  ________
   |     \|
   O      |
  /|\     |
          |
          |
  =========
  ''','''
  ________
   |     \|
   O      |
   |\     |
          |
          |
  =========
  ''','''
  ________
   |     \|
   O      |
   |      |
          |
          |
  =========
   ''','''
  ________
   |     \|
   O      |
          |
          |
  =========
  ''',''' 
  ________
   |     \|
          |
          |
          |
          |
  =========
   ''']

game_name = '''
 _                                             
| |                                            
| |___    __ _      __ __    __ _     _____      __       ___  
|  _  |  / _  |    |  _  \  / _  |  /_   _ \   /  _\    |  _ \ 
| | | | | (_| |_   | | | | | (_| |  | | | | | | (_| |_  | | | |
|_| |_|  \______|  |_| |_|  \___ |  |_| | |_|  \______| |_| |_|
                             __/ |                      
                            |___/

'''
guess_list = ['Almond', 'Banana', 'Blewits', 'Brazil', 'Carrot', 'Casaba', 'Cashew', 'Celery', 'Cherry', 'Chives', 'Chocho', 'Citron', 'Citrus', 'Cob nut', 'Cooker', 'Daikon', 'Damson', 'Endive', 'Fennel', 'Garlic', 'Girkin', 'Greens', 'Kiwano', 'Lentil', 'Lichee', 'Lychee', 'Marrow', 'Medlar', 'Nettle', 'Orange', 'Oyster', 'Papaya', 'Pawpaw', 'Peanut', 'Pepper', 'Pignut', 'Pippin', 'Potato', 'Quince', 'Radish', 'Raisin', 'Rocket', 'Russet', 'Squash', 'Tomato', 'Turnip', 'Wakame', 'Walnut']
import random
print("Welcome!!\nIn this game you have to guess the word given by guessing letters that you think might be present in the word\nAll the best")
yes=True
while yes:
    print(game_name)
    word_indx=random.randint(0,len(guess_list)-1)
    word=guess_list[word_indx]
    word=word.lower()
    p_l1=random.randint(0,len(word)-1)
    p_l2=random.randint(0,len(word)-1)
    p_l3=random.randint(0,len(word)-1)
    x=list('_'*len(word))
    x[p_l1]=word[p_l1]
    x[p_l2]=word[p_l2]
    x[p_l3]=word[p_l3]
    for i in x:
        print(i,end=" ")
    hngmn=len(lives)-1
    print(lives[hngmn])
    game=True
    while(game):
        c=input("Guess a letter\n")
        i=0
        if c in word:
            for j in range(len(x)):
                if x[j]=='_':
                    if(word[j]==c):
                        x[j]=c
                        y=True
            if(y):
                print("Great!")
        else:
            hngmn-=1
            print(f"Wrong choice!\n")
        for i in x:
            print(i,end=" ")
        print(lives[hngmn])
        if(word.lower()=="".join(x)):
            print("----------Congratulations!! You won----------")
            game=False
        elif(hngmn<=0):
            print(f"The correct word was {word}")
            print("-------Sorry ;) you lost, better luck next time------")
            game=False
    print("Do you want to play more?\nIf yes press 'y' else 'n'")
    right=True
    while(right):
        choice=input()
        if choice=='n':
            yes=False
            right=False
            print("Thanks for playing!!")
        elif choice=='y':
            right=False
        else:
            print("Enter 'y' or 'n'")
    
