lst = [5,-2,4,-2,1]

def max_sum(lst):
    m_sum = lst[0]
    curr_max_sum = lst[0]
    l = len(lst)

    for i in range(1,l):
        curr_max_sum = max(lst[i],curr_max_sum + lst[i])
        m_sum = max(m_sum,curr_max_sum)

    return m_sum


print(max_sum(lst))