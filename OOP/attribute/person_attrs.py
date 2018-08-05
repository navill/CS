class Person:
    def __init__(self, name, age, money):
        self.name=name
        self.age=age
        self.money=money

    def eat(self, food):
        print('{} eats {}'.format(self.name, food))

    def get_age(self):
        self.age+=1
    
    def earn_money(self, money):
        self.money+=money

if __name__=="__main__":
    greg=Person('greg', 36, 4000)
    mark=Person('mark', 24, 1000)



