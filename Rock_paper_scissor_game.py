import random

'''

Rock=1
Paper=-1
Scissor=0

'''

computer=random.choice([-1,0,1])
yourchoice=input("Enter Your Choice: ")
yourdict={"Rock":1, "Paper":-1, "Scissor":0}
reversedict={1:"Rock", -1:"Paper", 0:"Scissor"}

you=yourdict[yourchoice]

print(f"You choose {reversedict[you]}\nComputer choose {reversedict[computer]} ")

if computer==you:
    print("It's a draw...a worthy opponent")

else:
    if(computer==1 and you==0):
        print("You Lose!,Better luck next time loser i'm computer after all")
    
    elif(computer==1 and you==-1):
        print("Hurray!,i won...You are nothing just a piece of my intelligence you filthy machine ")

    elif(computer==0 and you==1):
        print("Hurray!,i won...You are nothing just a piece of my intelligence you filthy machine ")
    
    elif(computer==0 and you==-1):
        print("You Lose!,Better luck next time loser i'm computer after all")
    
    elif(computer==-1 and you==1):
        print("Hurray!,i won...You are nothing just a piece of my intelligence you filthy machine ")
    
    elif(computer==-1 and you==0):
        print("You Lose!,Better luck next time loser i'm computer after all")
    
    else:
        print("Something Went Wrong")