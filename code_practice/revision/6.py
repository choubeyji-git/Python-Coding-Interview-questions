def distinction(max_marks):
    def stu_marks(marks):
        for i in marks:
            if i >= 75:
                print('distinction')
        max_marks(marks)
    return stu_marks            

@distinction
def student_marks(marks):
    for i in marks:
        if i >= 33:
            print('pass')
        else:
            print('fail')    

student_marks([35,75,80])
           