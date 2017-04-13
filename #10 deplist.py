# list comprehension
import random
x = random.sample(range(0,20), random.randint(5, 10))
y = random.sample(range(0,20), random.randint(5, 10))
mylist = [a for a in x for b in y if a== b]

print(mylist)

# random
# list
