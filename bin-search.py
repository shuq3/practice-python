a = [1, 3, 4, 5, 6, 7]
num = int(input("Input a number: "))
start = 0
end = len(a) - 1
exist = 0

while True:
    if (end >= start):
        middle = a[start + int((end-start)/2)]
        if (middle < num):
            start = int(start + (end-start)/2 + 1)
        elif (middle > num):
            end = int(start + (end-start)/2 - 1)
        else:
            exist = 1
            break
    else:
        break

print (exist)
