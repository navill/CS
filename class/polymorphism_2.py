from abc import ABCMeta, abstractmethod
class Animal(metaclass=ABCMeta):
    #몸체가 없는 함수
    #상속 받은 클래스에서 반드시 오버라이딩해야 한다.
    @abstractmethod
    def eat(self):
        pass

class Lion(Animal):
    def eat(self):
        print('eat meat')

class Deer(Animal):
    def eat(self):
        print('eat grass')

class Human(Animal):
    def eat(self):
        print('eat meat and grass')

if __name__=="__main__":
    animals=[]
    animals.append(Lion())
    animals.append(Deer())
    animals.append(Human())

    for animal in animals:
        animal.eat()

    #TypeError: Can't instantiate abstract class Animal with abstract methods eat
    a=Animal()
