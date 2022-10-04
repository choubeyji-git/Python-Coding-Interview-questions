test_list = [12, 67, 98, 34]
res = []
for i in test_list:
    sum = 0
    for digit in str(i):
        sum += int(digit)
    res.append(sum)

print(res)