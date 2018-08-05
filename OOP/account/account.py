class Account:
    #class member
    num_acnt=0

    #class method
    @classmethod
    def get_num_acnt(cls):
        """
        get_num_acnt()->integer
        returns the number of accounts
        """
        return cls.num_acnt

    def __init__(self, name, money):
        #instance member
        self.user=name
        self.balance=money
        Account.num_acnt+=1

    def deposit(self, money):
        if money < 0:
            return
        self.balance+=money

    def withdraw(self, money):
        """
        withdraw(money)-> money or None
        인출하려는 돈이 잔고보다 작으면 금액을 반환
        잔고보다 크면 None을 반환합니다.
        """
        if money > 0 and money <=self.balance:
            self.balance -= money
            return money
        else:
            return None

    def transfer(self, other, money):
        """
        transfer(other, money)->bool
        other : 돈을 받는 사람
        money : 송금할 돈

        잔고가 충분하다면 송금 후 True 반환
        아니면 False 반환
        """
        mon=self.withdraw(money)
        if mon:
            other.deposit(money)
            return True
        else:
            return False
        
    def __str__(self):
        return 'user:{}, balance:{}'.format(self.user, self.balance)

if __name__=="__main__":
    print('class member')
    print(Account.num_acnt)
    print()

    print('class method')
    print('The number of accounts:{}'.format(Account.get_num_acnt()))

    my_acnt=Account('greg', 5000)
    your_acnt=Account('mark', 2000)

    print(my_acnt)
    print(your_acnt)
    print()

    print('deposit')
    my_acnt.deposit(500)
    print(my_acnt)
    print()

    print('withdraw')
    money=my_acnt.withdraw(1500)
    if money:
        print('withrawn money:{}'.format(money))
    else:
        print('Not enough to withdraw')
    print()

    print('class member')
    print(Account.num_acnt)
    print()

    print('class method')
    print('The number of accounts:{}'.format(Account.get_num_acnt()))

    print("message passing")
    print(my_acnt)
    print(your_acnt)
    res=my_acnt.transfer(your_acnt, 2000)
    if res:
        print('transfer succeeded')
    else:
        print('transfer failed')
    print(my_acnt)
    print(your_acnt)
    
        
    