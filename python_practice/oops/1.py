class Employee:

    raise_amt = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

    def fullname(self):
        return f'My fullname is {self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


dev_1 = Developer('Akhil', 'Tripathi', 50000,'Python')

print(dev_1.email)
print(dev_1.apply_raise())
print(dev_1.pay)
