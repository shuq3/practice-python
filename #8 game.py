print ("\nLet us play Rock-Paper-Scissors game.\nInput 1 for rock, 2 for paper, 3 forScissors\n")
quit = input('Type "enter" to quit, other to start: ' )
while quit != "enter":
    num1 = int(input("Player #1 input:"))
    num2 = int(input("Player #2 input:"))
    if num1 == num2:
        print ("Equal")
    elif ((num1 == 1 and num2 == 2) or (num1 == 2 and num2 == 3) or (num1 == 3 and num2 == 1)):
        print ("Player #2 win")
    else:
        print ("Player #1 win")
    quit = input('Type "enter" to quit, other to start: ' )
