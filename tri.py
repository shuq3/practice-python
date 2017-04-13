num = int(input("Input a num: "))

def loop(n):
    if n == 2:
        print ([1, 1])
        return [1, 1]
    else:
        mylist = loop(n-1)
        result = [1]
        for item in range(n-2):
            result.append(mylist[item]+mylist[item+1])
        result.append(1)
        print (result)
        return result

if num == 1:
    print ([1])
else:
    print ([1])
    loop(num)
