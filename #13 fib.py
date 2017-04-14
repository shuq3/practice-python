num = int(input("Input a num: "))

def fib(n):
    if n == 1:
        return [1];
    if n == 2:
        return [1, 1];
    else:
        arr = fib(n-1);
        arr.append(arr[n-2]+arr[n-3])
        return arr;

resultarr = fib(num);
print (resultarr)
