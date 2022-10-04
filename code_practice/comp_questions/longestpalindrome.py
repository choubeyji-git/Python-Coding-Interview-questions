lst=['dad', 'flower', 'python', 'malayalam', 'container', 'pandas']
newList = max([x for x in lst if x == x[::-1]],key=len)
print(newList)