class Vehicle:

    color = 'White'

    def __init__(self,engine,gear,tyre):
        self.engine = engine
        self.gear = gear
        self.tyre = tyre

    def run(self):
        return f'A vehicle can run on road with {self.tyre} tyre'

class Bus(Vehicle):

    def __init__(self,engine,gear,tyre,type):
        super().__init__(engine,gear,tyre)
        self.type = type


vehicle_1 = Bus('10000cc','Non-Auto','8','Bus')

print(isinstance(vehicle_1,Vehicle))


