class CarOwner:
    def __init__(self, name):
        self.name=name

    def concentrate(self):
        print('{} can not do anything else'.format(self.name))

class Car:
    def __init__(self, owner_name):
        self.owner=CarOwner(owner_name)

    def drive(self):
        self.owner.concentrate()
        print('{} is driving now'.format(self.owner.name))

class SelfDrivingCar(Car):
    def drive(self):
        print('Car is driving by itself')

if __name__=="__main__":
    car=Car('Greg')
    car.drive()
    print()

    s_car=SelfDrivingCar('Mark')
    s_car.drive()
    