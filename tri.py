num = int(input("Input a num: "))

def triangles(n):
    L = [1]
    for i in range(n):
        yield L
        L = [1] + [L[i]+L[i+1] for i in range(len(L)-1)] + [1]

for t in triangles(num):
    print(t)
