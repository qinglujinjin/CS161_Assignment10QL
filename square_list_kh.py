#Author: Khai Hoang
#Date: 11/13/2019
#Description: Takes a parameter list and replaces each value with the square of that value.
# It should not return anything - it should mutate the original list.

def square_list(list_input):
    list_input[::] = [x**2 for x in list_input]
    print(list_input)

ex_list = [7, -3, 12, 9]
print(ex_list)
square_list(ex_list)