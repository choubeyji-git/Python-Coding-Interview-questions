my_str = '''Immo sit sane nihil melius, inquam-nondum enim id quaero-, num propterea idem voluptas est, quod, ut ita dicam, indolentia?'''

my_lst = my_str.replace(",","").replace("-",",").replace("'","")
my_lst = my_lst.split(" ")

my_str_2 = 'akhiltripathi'
lst = [i for i in my_str_2]

d = {}

for i in lst:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1

print(d)

