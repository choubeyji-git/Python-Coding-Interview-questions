# 
lst_1 = ['M', 'N', 'I','A']

lst_2 = ['y','ame','s','bhishek']

#ouput = My Name Is Abhishek
#string= list(zip(list.__add__, lst_1, lst_2))

lst_3 = []

for i,j in zip(lst_1, lst_2):
    lst_3.append(i+j)
print(lst_3)
output=" ".join(lst_3)
print(output)