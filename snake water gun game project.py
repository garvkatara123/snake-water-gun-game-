#snake water gun game#

def snake_water_gun():
    name=input("please enter your name:- ")
    print(f"\nHello {name} Welcome.")
    print("Are you ready for the game")
    print("press (y) for yes and (n) for no.")
    ch=input("enter your decision:- ")
    cmpoint=0
    uspoint=0
    while True:    
        if(ch=="y" or ch=="Y"):    
            print("if you want snake press(0)\nif you want water press(1) and\nif you want gun press(2)")
            com=int(input("enter your choice:- "))
            if com==0:
                c1="snake"
            elif com==1:
                c1="water"
            elif com==2:
                c1="gun"
            else:
                print("\nInvalid choice")
                print("you score:- ",uspoint)
                if(uspoint>cmpoint):
                    print(f"you won this whole game,\nyour score is {uspoint} and computer score is {cmpoint}.")
                    break
                elif(uspoint<cmpoint):
                    print(f"you lost this whole game,\nyour score is {uspoint} and computer score is {cmpoint}.")
                    break
                elif(uspoint==cmpoint):
                    print(f"game draw,\nyour score is {uspoint} and computer score is {cmpoint}.")
                    break
                else:
                    pass
            import random
            l=["snake","water","gun"]
            print("you entered- ",c1)
            m=random.choice(l)
            print("computer entered- ",m)
            if(c1==m):
                print("game draw")
            elif(c1=="water" and m=="snake"):
                print("you lost the game")
                cmpoint+=1
            elif(c1=="gun"and m=="snake"):
                print("you won the game")
                uspoint+=1
            elif(c1=="snake"and m=="water"):
                print("you won the game")
                uspoint+=1
            elif(c1=="gun" and m=="water"):
                print("you lost the game")
                cmpoint+=1
            elif(c1=="snake" and m=="gun"):
                print("you lost the game")
                cmpoint+=1
            elif(c1=="water" and m=="gun"):
                print("you won the game")
                uspoint+=1
            else:
                print("in")
            print("if you want to play again.")
            ch=input("press (y) otherwise (n):- ")
        elif(ch=="n" or ch=="N"):
            print(f"now {name}\nyou are exit from the game")
            if(uspoint>cmpoint):
                print(f"\nyou won this whole game,\nyour score is {uspoint} and computer score is {cmpoint}.")
                break
            elif(uspoint<cmpoint):
                print(f"you lost this whole game,\nyour score is {uspoint} and computer score is {cmpoint}.")
                break
            elif(uspoint==cmpoint):
                print(f"game draw,\nyour score is {uspoint} and computer score is {cmpoint}.")
                break
            else:
                pass
        else:
            print(f"sorry {name}\nyou entered invalid decision")
            print("you score:- ",uspoint)
            break
snake_water_gun()       





        
