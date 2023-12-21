import random
def f():
    print('''Winning rules:
        rock VS paper: paper win
        rock VS scissors: rock win
        paper VS scissor: scissor win
        ''')
    print("enter choice \n 1. Rock \n 2. Paper \n 3. Scissor")

    choice = int(input("enter choice:"))
    L=["Rock","Paper","Scissor"]
    y=random.choice(L)
    print("computer choice:",y)

    if choice==1 and y=="Rock":
        print("TIE!!")
    elif choice==1 and y=="Paper":
        print("YOU LOSE!!")
    elif choice==1 and y=="Scissor":
        print("YOU WIN!!")
    else:
        pass

    if choice==2 and y=="Rock":
        print("YOU WIN!!")
    elif choice==2 and y=="Paper":
        print("TIE!!")
    elif choice==2 and y=="Scissor":
        print("YOU LOSE!!")
    else:
        pass

    if choice==3 and y=="Rock":
        print("YOU LOSE!!")
    elif choice==3 and y=="Paper":
        print("YOU WIN!!")
    elif choice==3 and y=="Scissor":
        print("TIE!!")
    else:
        pass
    u=input("Do you want to continue(Y/N)-")
    if u=="y" or u=="Y":
        f()
    elif u=="n" or u=="N":
        pass
    else:
        print("Read the instructions!!")

f()


