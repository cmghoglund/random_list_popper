# Toy program that pops all numbers from a list one by one in random order and displays the results

import random

def pop_random(target_list=None):
    if target_list is None: # If no list provided as argument, use default list created by program
        target_list = list(range(1, 11)) # Create default list with integers 1-10

    print(target_list) # Print original list

    for _ in range(len(target_list)): # Loop through all numbers in list
        pop_index = random.randint(0, len(target_list) - 1) # Choose random number from list
        target_list.pop(pop_index) # Pop the number
        print(target_list) # Print the resulting list

if __name__ == '__main__':
    pop_random()
