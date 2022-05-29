import random

lower = "ashrafsiddikfaysal"
upper = "REHANASHRAFPANDA"
number ="1234567890"
special = "@#"
length = 16

all = lower +upper+number +special
password = "".join(random.sample(all, length))

print(password)

# Python3 program to demonstrate
# the use of sample() function .

# import random

#sample() is an inbuilt function of random module in Python.
#it returns a specific length of output , which is determined by the user or  programmar
from random import sample

# Prints list of random items of given length
list1 = [1, 2, 3, 4, 5]

print(sample(list1, 3))


