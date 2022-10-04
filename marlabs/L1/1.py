from abc import ABC,abstractmethod


class Computer(ABC):

    @abstractmethod
    def process(self):
        pass


class Laptop(Computer):
    def process(self):
        print('I am laptop')


asset_1 = Computer()
asset_1.process()