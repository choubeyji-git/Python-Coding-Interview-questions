class Test:
    def __init__(self,x):
        self.a = x

    def get_data(self):
       print('Some code to fetch data from the database')    

    def action_fun(self):
        self.get_data()

    def action_fun_2(self):
        self.get_data()

obj_1 = Test(5)
# obj_1.action_fun()
# obj_1.action_fun_2()

def new_get_data(self):
    print('Some code to fetch stub data')

Test.get_data = new_get_data
print("After monkey patching")

obj_1.action_fun()
obj_1.action_fun_2()

