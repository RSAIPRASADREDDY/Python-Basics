import random
##Module is something we can creste some code and it can re-used in other file by importing it
a=1
b=100

# Heads or tails
random_int=random.randint(0,1)
print(random_int)

#Random int generator
random_int=random.randint(a,b)
print(random_int)

#Random range by stepping generator
random_range=random.randrange(a,b,2)
print(random_range)

#Random float generator
random_float=random.random()
random_float =random_float*5
print(random_float)