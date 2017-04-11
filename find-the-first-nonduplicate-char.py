str = 'abbacd'
mylist = []
for index in range(0, 25):
    mylist.append([0, 0, index])

for index, item in enumerate(str):
  num = ord(item) - ord('a')
  mylist[num][0] += 1
  mylist[num][1] = index

def once(n):
    return n[0] == 1

mylist = filter(once, mylist)
mylist = sorted(mylist, key=lambda x : x[1])
print mylist[0]
