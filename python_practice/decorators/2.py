def distinction(dist):
    def dist_marks(marks):
        for i in marks:
            if i >= 75:
                print('Distinction')
        dist(marks)
    return dist_marks        

@distinction
def student_marks(marks):
    for m in marks:
        if m >= 33:
            print('pass')
        else:
            print('fail')
            break
    else:
        print('pass')


m = [75,79,30,81]
student_marks(m)                