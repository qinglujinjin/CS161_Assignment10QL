#Author: Qing Lu
#Date: 11/06/2019
#Description: Define function to square elements in list



def square_list(lst):
 """"set up function to square elements in list"""
 for index in range(len(lst)):
  lst[index] = lst[index]**2 # generate square value to replace existing element
 return lst

print(square_list([7, -3, 12, 9]))

