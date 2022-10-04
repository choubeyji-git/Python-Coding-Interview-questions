class Test:

    def __init__(self,a):
        self.x = a

    def get_data(self):
        print('Some code to fetch data')

    def action_1(self):
        self.get_data()

    def action_2(self):
        self.get_data()            

def get_stub_data(self):
    print('Some code to fetch stub data')

Test.get_data = get_stub_data

obj_1 = Test(5)
obj_1.action_1()        