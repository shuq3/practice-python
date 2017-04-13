# input if types int equality comparison numbers mod
# odd or even
num = (int(input("Inuput a number:")))
check = (int(input("Inuput another number:")))
if num % 2 == 1:
    print("It is a odd num")
else:
    print("It is a even num")

if num % 4 == 0:
    print("It is a mup of 4")

if check == 0:
    print ("The second number is zero")
else:
    print ("first num % second num is", num % check)
