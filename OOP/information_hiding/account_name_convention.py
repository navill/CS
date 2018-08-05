class Account:
    def __init__(self, money):
        self.__balance=money

    def get_balance(self):
        return self.__balance

    def set_balance(self, money):
        if money < 0:
            return
        self.__balance=money

if __name__=="__main__":
    my_acnt=Account(5000)
    my_acnt.__balance=-3000

    print(my_acnt.get_balance())
