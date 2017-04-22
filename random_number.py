s, g = Counter('1234'), Counter('4567')
a = sum(i == j for i, j in zip(secret, guess))
print (a, sum((s & g).values()) - a)
