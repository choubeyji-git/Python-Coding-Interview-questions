import datetime


class Employee:

    raise_amt = 1.10

    def __init__(self,first_name,last_name,pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '@' + last_name


    def fullname(self):
        return f'My fullname is {self.first_name} {self.last_name}'    



class Developer(Employee):
    def __init__(self,first_name,last_name,pay,lang):
        super().__init__(first_name,last_name,pay)
        self.lang = lang

    @property
    def lang_to_work(self):
        return f'I work on {self.lang}'

    @classmethod
    def set_raise_amt(cls,amt):
        cls.raise_amt = amt 

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
                return False
        return True        


dev_1 = Developer('Akhil','Tripathi',40000,'python')
print(dev_1.fullname())
print(dev_1.lang_to_work)
dev_1.set_raise_amt(1.40)

print(dev_1.raise_amt)

mydate = datetime.date(2022,9,9)

print(dev_1.is_workday(mydate))

