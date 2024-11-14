import array

# Demonstrating lists
my_list = [1, 2, 3, 4, 5]
print("List:", my_list)
print("Type of my_list:", type(my_list))

# Accessing elements in a list
print("First element in the list:", my_list[0])
print("Last element in the list:", my_list[-1])

# Demonstrating types
integer_var = 10
float_var = 10.5
string_var = "Hello, World!"
boolean_var = True

print("Type of integer_var:", type(integer_var))
print("Type of float_var:", type(float_var))
print("Type of string_var:", type(string_var))
print("Type of boolean_var:", type(boolean_var))

# Demonstrating arrays
my_array = array.array('i', [1, 2, 3, 4, 5])
print("Array:", my_array)
print("Type of my_array:", type(my_array))

# Accessing elements in an array
print("First element in the array:", my_array[0])
print("Last element in the array:", my_array[-1])

""" 
# Output:

List: [1, 2, 3, 4, 5]
Type of my_list: <class 'list'>
First element in the list: 1
Last element in the list: 5
Type of integer_var: <class 'int'>
Type of float_var: <class 'float'>
Type of string_var: <class 'str'>
Type of boolean_var: <class 'bool'>
Array: array('i', [1, 2, 3, 4, 5])
Type of my_array: <class 'array.array'>
First element in the array: 1
Last element in the array: 5
"""