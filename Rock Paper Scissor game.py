import random

print("\t\tROCK, PAPER AND SCISSOR GAME\t\t\n")
while 1:
    q = int(input("Press '1' to Start the Game\nPress '0' to Exit the Game\n"))
    if q==0:
        print("You Have Exited the Game")
        break

    if q==1:
        x = 10                                                                              #No of chances
        y = 0                                                                               #points of player
        z = 0                                                                               #points of computer
        while(x!=0):
            x = x-1
            inp = int(input("Enter '1' for Rock, '2' for Paper, '3' for Scissors\n"))       #Your choice (inp)
            lst = ["Rock", "Paper", "Scissor"]
            a = random.choice(lst)                                                          #computer's choice (a)
                                                                                            # you(inp, y) vs computer(a, z)
            if inp == 1 and a == "Rock":                                                    # Rock vs Rock
                print(f"You: Rock\t\t\tComputer: {a}")
            elif inp == 1 and a =="Paper":                                                  #Rock vs Paper
                z = z+1
                print(f"You: Rock\t\t\tComputer: {a}")
            elif inp == 1 and a == "Scissor":                                               #Rock vs Scissor
                y = y+1
                print(f"You: Rock\t\t\tComputer: {a}")
            elif inp == 2 and a == "Rock":                                                  #Paper vs Rock
                y = y+1
                print(f"You: Paper\t\t\tComputer: {a}")
            elif inp == 2 and a == "Paper":                                                 #Paper vs Paper
                print(f"You: Paper\t\t\tComputer: {a}")
            elif inp == 2 and a == "Scissor":                                               #Paper vs Scissor
                z = z+1
                print(f"You: Paper\t\t\tComputer: {a}")
            elif inp == 3 and a == "Rock":                                                  #Scissor vs Rock
                z = z+1
                print(f"You: Scissor\t\t\tComputer: {a}")
            elif inp == 3 and a == "Paper":                                                 #Scissor vs Paper
                y = y+1
                print(f"You: Scissor\t\t\tComputer: {a}")
            elif inp == 3 and a == "Scissor":                                               #Scissor vs Scissor
                print(f"You: Scissor\t\t\tComputer: {a}")
            else:
                print("Invalid Input")
            print(f"Your Score: {y}\t\t\tComputer's Score: {z}")
            print(f"You have {x} chances left\n")
        if y>z:
            print("\t\t\tYOU WIN!!\n\n")
        elif z>y:
            print("\t\t\tYOU LOSE!!\n\n")
        else :
            print("TIE BREAKER ROUND\n")
            y=0
            z=0
            while 1:
                inp = int(input("Enter '1' for Rock, '2' for Paper, '3' for Scissors\n"))
                lst = ["Rock", "Paper", "Scissor"]
                a = random.choice(lst)
                if (inp == 1 and a == "Scissor") or (inp == 2 and a == "Rock") or (inp == 3 and a == "Paper"):
                    print(f"Computer: {a}")
                    print("\t\t\tYOU WIN!!\n\n")
                    break
                elif (inp == 1 and a =="Paper") or (inp == 2 and a == "Scissor") or (inp == 3 and a == "Rock"):
                    print(f"Computer: {a}")
                    print("\t\t\tYOU LOSE!!\n\n")
                    break
                else:
                    print("Invalid Input")
                    continue
