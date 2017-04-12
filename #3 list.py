a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
num = int(input("Input a num:"))

# for item in reversed(a):
#     if item >= 5:
#         a.pop()
def lessthan5(n):
    return n < num

a = list(filter(lessthan5, a))

print (a)
