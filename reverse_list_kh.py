#Author: Khai Hoang
#Date: 11/13/2019
#Description: Takes a parameter list and reverses the order of the elements in that list.
# It should not return anything - it should mutate the original list.

def reverse_list(list_input):
    list_input[::] = list_input[::-1]
    print(list_input)

example_list = [7, -3, 12, 9]
print(example_list)
reverse_list(example_list)
print(example_list)