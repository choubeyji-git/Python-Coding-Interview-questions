import json

def lambda_function():
    lst1 = ['Akhil','Gaurav']
    lst2 = [1,2]

    my_op = dict(zip(lst2,lst1))
    final_op = json.dumps(my_op)
    print(type(final_op))
    f_op = json.loads(final_op)
    print(type(f_op))
    return f_op
print(lambda_function())    


# AWS Api gateway


# endpoint - GET  /getstudentdata/id=1