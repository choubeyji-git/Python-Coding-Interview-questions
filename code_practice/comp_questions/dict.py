dict={'abc':8,'adc':10,'dbc':4,'cde':6}
key='bc'
list1=[]
for e in dict:
    if key in e:
        list1.append(dict[e])
print(list1)
