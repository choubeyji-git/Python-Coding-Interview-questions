def divide(x,y):
    try:
        result = x//y
    except ZeroDivisionError as e:
        print(e)
    else:
        print('your answer is : ',result)
    finally:
        print('This will be executed wheneverv you want')

divide(8,0)