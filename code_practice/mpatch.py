class Test:

    def __init__(self,x):
        self.x = x

    def get_data(self):
        print('some code to fetch data')

    def action_1(self):
        self.get_data()

    def action_2(self):
        self.get_data()

def get_stub_data(self):
    print('Some code to fetch stub data')

Test.get_data = get_stub_data 

obj1 = Test(5)

print(obj1.action_1())