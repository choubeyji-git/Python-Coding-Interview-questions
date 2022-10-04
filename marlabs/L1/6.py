class Test:

    def __init__(self,x):
        self.x = x

    def get_data(self):
        print('some code to fetch data from db')

    def some_data_operation(self):
        self.get_data()

    def action_2(self):
        self.get_data()


def stub_data(self):
    print('Some code to fetch test data')

Test.get_data = stub_data

event_1 = Test(2)

event_1.action_2()