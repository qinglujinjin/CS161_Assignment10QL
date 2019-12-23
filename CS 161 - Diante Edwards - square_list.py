# Author: Diante Edwards
# Date: 11/13/2019
# Description: Function takes a list as a parameter and replaces each value in the list with the square of that value

def square_list(num_list):
    """
    Function computes the square of numbers in the list argument. Does not return anything.
    """
    counter = 0
    list_length = len(num_list)
    while counter < list_length:
        # Loop pops each element in the list argument and replaces each element with the square of itself.
        popped_num = num_list.pop(0)
        counter += 1
        squared_num = popped_num ** 2
        num_list.append(squared_num)
