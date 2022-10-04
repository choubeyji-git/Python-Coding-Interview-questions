class test:
    def __init__(self,a):
        self.a = a

    def operation(self,a,b):
        return a

str1 = 'aeiou'
str2 = 'AEIOU'

a = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']
obj = test(a)
b = 'HackerEarth Tests'
c = obj.operation(a,b)

print(c)