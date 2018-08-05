class Account:
    def __init__(self, money):
        self.balance=money

    def get_balance(self):
        return self.balance

    def set_balance(self, money):
        if money < 0:
            return
        self.balance=money

if __name__=="__main__":
    my_acnt=Account(5000)
    my_acnt.balance=-3000

    print(my_acnt.balance)
