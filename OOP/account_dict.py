
def init(clnt_name, money):
	obj={'clnt_name':clnt_name, 'balance':money}
	obj['deposit']=Account[1]
	obj['witdraw']=Account[2]
	obj['transfer']=Account[3]
	obj['show']=Account[4]
	return obj

def deposit(self, money):
	if money < 0:
		print('money has to be greater than zero!')
		return False
	self['balance']+=money
	return True

def withdraw(self, money):
	if money > self['balance']:
		print('money must be less than your balance')
		return None
	self['balance']-=money
	return money

def transfer(self, other, money):
	available_money=self['witdraw'](self, money)
	if available_money:
		other['deposit'](other, available_money)
		print('transfer succeeded!')
	else:
		print('transfer failed! you must check your account again!')

def show(self):
	print('{} : {}'.format(self['clnt_name'], self['balance']))

Account=init, deposit, withdraw, transfer, show

if __name__=="__main__":
	my_acnt=Account[0]('greg', 5000)
	your_acnt=Account[0]('john', 2000)
	my_acnt['show'](my_acnt)
	your_acnt['show'](your_acnt)

	my_acnt['deposit'](my_acnt, 3000)
	my_acnt['show'](my_acnt)

	my_acnt['witdraw'](my_acnt, 2000)
	my_acnt['show'](my_acnt)

	my_acnt['transfer'](my_acnt, your_acnt, 1000)
	my_acnt['show'](my_acnt)
	your_acnt['show'](your_acnt)


