# Python program to interchange first and last elements in a lists
lst = [12,35,9,56,24]
def swapList(newlist):
    newlist[0] , newlist[-1]  = newlist[-1] , newlist[0]

    return newlist

print(swapList(lst))  