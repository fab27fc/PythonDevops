#Data Type Tuples
my_tuple = (1, 2, 3, 4, 5)
print("The tuple is:", my_tuple)
#Accessing elements in a tuple
print("The first element of the tuple is:", my_tuple[0])
print("The last element of the tuple is:", my_tuple[-1])
#Tuples are immutable, so we cannot change their elements
#my_tuple[0] = 10 # This will raise an error
#However, we can concatenate tuples to create a new tuple
new_tuple = my_tuple + (6, 7, 8)
print("The new tuple is:", new_tuple)
