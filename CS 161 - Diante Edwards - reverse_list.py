
# Author: Diante Edwards
# Date: 11/13/2019
# Description: Function takes a list as a parameter and reverses the list.

def reverse_list(list):
    """
    Function reverse the list in the list argument. Does not return anything.
    """
    i = 0
    j = len(list)-1
    while i < j:
        # Loop pops each element in the list argument and replaces each element with the square of itself.
        temp_element = list[i]
        list[i] = list[j]
        list[j] = temp_element
        i+=1
