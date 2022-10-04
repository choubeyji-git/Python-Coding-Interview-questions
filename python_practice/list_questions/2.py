# Exercise 2: Concatenate two lists index-wise

lst_1 = ['M', 'N', 'I','A']

lst_2 = ['y','ame','s','khil']

lst_3 = [(i+j) for i,j in zip(lst_1,lst_2)]

# for i,j in zip(lst_1,lst_2):
#         lst_3.append(i + j)


print(lst_3)