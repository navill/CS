
from abc import ABCMeta, abstractmethod


# Results of same methods depend on STATES


# context
class Boiler:
	def __init__(self):
		self.temp=0
		self.state=ColdState()

	def increase_temp(self):
		self.state.increase_temp(self)

	def decrease_temp(self):
		self.state.decrease_temp(self)

	def change_state(self, state):
		self.state=state



# STATE
# state is changed by STATE OBJECT
class TempState(metaclass=ABCMeta):
	@abstractmethod
	def increase_temp(self, boiler):
		pass

	@abstractmethod
	def decrease_temp(self, boiler):
		pass

class ColdState(TempState):
	def increase_temp(self, boiler):
		print(boiler.temp, 'increased in ColdState')
		boiler.temp+=10
		if boiler.temp >= 40:
			boiler.change_state(WarmState())

	def decrease_temp(self, boiler):
		print(boiler.temp, 'decreased in ColdState')
		boiler.temp-=10
		if boiler.temp <= 0:
			print('boiler was turned off')
			boiler.temp=0

class WarmState(TempState):
	def increase_temp(self, boiler):
		print(boiler.temp, 'increased in WarmState')
		boiler.temp+=5
		if boiler.temp>= 70:
			boiler.change_state(HotState())

	def decrease_temp(self, boiler):
		print(boiler.temp, 'decreased in WarmState')
		boiler.temp-=5
		if boiler.temp <= 40:
			boiler.change_state(ColdState())

class HotState(TempState):
	def increase_temp(self, boiler):
		print(boiler.temp, 'increased in HotState')
		boiler.temp+=3
		if boiler.temp >= 120:
			print('Temperature is TOO HIGH!')
			boiler.temp=120

	def decrease_temp(self, boiler):
		print(boiler.temp, 'decreased in HotState')
		boiler.temp-=5
		if boiler.temp <= 70:
			boiler.change_state(WarmState())

if __name__=="__main__":
	boiler=Boiler()
	for _ in range(30):
		boiler.increase_temp()

	for _ in range(25):
		boiler.decrease_temp()


