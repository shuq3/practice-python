# find divitor of a certain num
num = int(input("Input a num:"))
mylist = []
for x in range(2, num):
    if num % x == 0:
        mylist.append(x)
print (mylist)
