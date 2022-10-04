# Initialize the list
my_list = [1, 3, 6, 10]

# same thing can be done using a generator expression
# generator expressions are surrounded by parenthesis ()
generator = (x**2 for x in my_list)
print(generator)
my_list = [1, 3, 6, 10]

a = (x**2 for x in my_list)
print(next(a))
print(next(a))
