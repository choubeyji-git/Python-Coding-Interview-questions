class Employee:
    raise_amt = 1.04
    number_of_emps = 0

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@mail.com'

        Employee.number_of_emps += 1

    def fullname(self):
        return f'My fullname is {self.first} {self.last}'

    def raised_amt(self):
        self.pay = int(self.pay * self.raise_amt)
        return self.pay    

emp_1 = Employee('Akhil', 'Tripathi', 50000)
emp_2 = Employee('Aadil', 'Shakil', 60000)
emp_2.raise_amt = 1.08

print(emp_2.raised_amt())

print(Employee.number_of_emps)