string = input("Input a str: ")
num = len(string) - 1
half = num / 2

for c in string:
    if num <= half:
        print ("right")
        break
    if c == string[num]:
        num -= 1;
    else:
        print("not a palindrome")
        break

#7 filter
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [value for value in a if value%2 == 0]
