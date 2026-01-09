#INHERITANCE

class Base:
    def __init__(self):
        print('Inside Base')

    def read():
        print('Base is reading')

class Derived(Base):
    print('Inside Derived')
    def __init__(self):
        Base().__init__()
        print('Inside Derived init')

    def read1():
        print('Derived is reading')

p1= Derived()