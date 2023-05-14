# Toy program that pops all numbers from a list one by one in random order and displays the results

import random

t = list(range(1, 11)) # Create list with integers 1-10

print(t) # Print original list

for _ in range(len(t)):
    pop_index = random.randint(0, len(t) - 1) # Choose random number from list
    t.pop(pop_index) # Pop the number
    print(t) # Print the resulting list
