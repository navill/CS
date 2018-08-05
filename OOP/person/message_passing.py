class Person:
    def __init__(self, name, money):
        self.name=name
        self.money=money

    def give_money(self, other, money):
        self.money-=money
        #message passing
        other.get_money(money)

    def get_money(self, money):
        self.money+=money

if __name__=="__main__":
    greg=Person('greg', 5000)
    mark=Person('mark', 2000)

    #message passing
    greg.give_money(mark, 2000)
    

