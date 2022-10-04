def find_missing(lst):
    return [x for x in range(lst[0], lst[-1]+1)
                               if x not in lst]
 
# Driver code
lst = [1, 2, 4, 6, 7, 9, 10]
print(find_missing(lst))

lst=[1,2,3,5,7,8,9,10]
for n in range(1,11):
    if n not in lst:
      print(n,end=" ")
   