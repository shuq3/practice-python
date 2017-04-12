# get random list and find the duplicated element

import random
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a = []
b = []
numa = random.randint(0, 10)
numb = random.randint(0, 20)
for item in range(0, numa):
    a.append(random.randint(0, 40))

for item in range(0, numb):
    b.append(random.randint(0, 40))


mylist = []

for item in a:
    if item in b and item not in mylist:
        mylist.append(item)

print (mylist)
