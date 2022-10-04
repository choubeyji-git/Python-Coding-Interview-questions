n = 5
arr = [1,2,3,4,5,6]
def rotate(arr,n):
    idx = arr.index(n)

    if idx == len(arr) - 1:
        arr.insert(0,arr.pop())
        print(arr)
    else:
        arr.insert(idx+1 , arr.pop())
        print(arr)    

rotate(arr,n)

    
    