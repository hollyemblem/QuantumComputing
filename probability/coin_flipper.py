import random
from collections import Counter

'''
Simple program to recreate flipping a coin 100 items, for probability exercises.
We are looking to use the program to justify that our coin is unbiased.
We note that the larger the number of trials in an experiment, the closer the experimental probability becomes to its theoretical counterpart.
'''

coin_flip_amount = 100
variable_set = ['h','t']
coin_flip = list()

def coin_flipper(amount,list_flip, choices):
    i = 0
    while i < amount:
        list_flip.append(random.choice(choices))
        i = i +1
    return list_flip

outcome = coin_flipper(coin_flip_amount, coin_flip, variable_set)

print(len(outcome))
print(Counter(outcome))

