


#List comprehension in Python is a compact way of creating a list from a sequence. It is a short way to create a new list. List comprehension is considerably faster than processing a list using the for loop.
# syntax
#[expression for i in iterable if condition]

#For instance if you want to change a string to a list of characters. You can use a couple of methods. Let's see some of them:

## One way of doing it

language = "Python"
lst = list(language)
print(type(lst))
print(lst)

## Another way of doing it

lst = [i for i in language]
print(type(lst))
print(lst)

## For instance if you want to generate a list of numbers:


numbers = [i for i in range(11)]
print(numbers)

# It is possible to do mathematical operations during iteration

numbers = [i * i for i in range(11)]
print(numbers)

# It is also possible to make a list of tuples

numbers = [(i,i*i) for i in range(11)]
print(numbers)

even_number = [i for i in range(21) if i % 2 ==0]
print(even_number)

odd_number = [i for i in range(21) if i % 2 !=0]
print(odd_number)


# Filter numbers: let's filter out positive even numbers from the list below
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]

filter_nums = [i for i in numbers if i < 0 and i % 2 == 0]
print(filter_nums)


# Flattening a two dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flatten_lst = [num for row in list_of_lists for num in row ]
print(flatten_lst)
