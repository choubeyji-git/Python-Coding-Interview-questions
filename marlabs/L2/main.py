txt = 'A genome is the complete set of genetic information in an organism. It provides all of the information the organism requires to function. In living organisms, the genome is stored in long molecules of DNA called chromosomes'

lst = txt.split(" ")

d = {}

for i in lst:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

# print(d)

def return_dict(d):
    new_d = {}
    for i,v in d.items():
        if d[i] >= 2:
            d1 = {
                i:v
            }
            new_d.update(d1)
    return new_d

print(return_dict(d))





