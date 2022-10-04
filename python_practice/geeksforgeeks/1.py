# Python | Ways to find length of list
import time

lst = [5,7,4,3,2]


start_time_len = time.time()
len_of_lst = 0
for i in lst:
    len_of_lst +=1

end_time_len = (time.time() - start_time_len)
print(len_of_lst,end_time_len)