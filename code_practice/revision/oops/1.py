import datetime

class Employee:

    raise_amt = 1.10
    emp_count = 0

    def __init__(self,first_name,last_name,pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = self.first_name + '.' + self.last_name + '@' + 'gmail.com'

        Employee.emp_count += 1

    def full_name(self):
        return f'My fullname is {self.first_name} {self.last_name}'

    def apply_raise(self):
        self.pay = int(int(self.pay) * self.raise_amt)
        

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount

    @classmethod
    def emp_string(cls,emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)        

        
    @staticmethod
    def is_workday():
        day_of_week = datetime.datetime.today().weekday()
        if day_of_week > 5:
            return 'Its workday'
        else:
            return 'Weekend'    

obj_1 = Employee('Akhil','Tripathi',90000)     
obj_2 = Employee('Virat','Kohli',80000) 

obj_3 = Employee.emp_string('Viru-Sehwag-80000')

print(obj_3.pay)
obj_3.apply_raise()
print(obj_3.pay)
# Employee.set_raise_amt(1.25)


# print(Employee.emp_count)
# print(Employee.is_workday())