 import copy

result_akhil = [[45,75,85],[99,200,300]]

result_ashish = copy.deepcopy(result_akhil)

result_mayur = copy.copy(result_akhil)


#change first year 1st marks 

result_ashish[0][0] = 80
result_mayur[0][0] = 95

print("Original list : ",result_akhil)
print('Copied list :',result_ashish)
print('same copies : ',result_mayur)