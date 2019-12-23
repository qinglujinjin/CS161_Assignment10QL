# project 7a
# Name: Tristan Bragg
# Date: 11/13/19
# Description: defines a function that squares the numbers that are ran through the list


"""defining the function square_list"""
def square_list(a_list):
    a_list[0:0] = []
    for num in range(len(a_list)):
        a_list[num]**2


# testing
a_list =[7, -3, 12, 9]

square_list(a_list)

