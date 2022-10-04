class Stack:
    def __init__(self,s=[]):
        self.s = s

    def push(self,data):
        self.s.append(data)

    def print(self):
        if len(self.s) == 0:
            print('Stack is empty')
            return

        print(self.s) 

    def remove_elemnt(self):
        self.s.pop()   

stack_item = Stack()
stack_item.push(10)
stack_item.remove_elemnt()
stack_item.print()                               