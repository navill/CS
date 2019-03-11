from abc import ABCMeta, abstractmethod
import random

# execution flow object
class LookingMonster:
	def chase(self):
		is_there=self.look()

		if is_there:
			self.notify()
			self.move()

	@abstractmethod
	def look(self):
		pass

	@abstractmethod
	def notify(self):
		pass

	@abstractmethod
	def move(self):
		pass

class LeftLookingMonster(LookingMonster):
	def look(self):
		print('I am looking left')
		return random.randint(0, 1)

	def notify(self):
		print('I am howling')

	def move(self):
		print('I am running left')
		

class RightLookingMonster(LookingMonster):
	def look(self):
		print('I am looking right')
		return random.randint(0, 1)
	
	def notify(self):
		print('I am growing')

	def move(self):
		print('I am running right')

class UpLookingMonster(LookingMonster):
	def look(self):
		print('I am looking up')
		return random.randint(0, 1)

	def notify(self):
		print('I am squealing')

	def move(self):
		print('I am flying up')

class DownLookingMonster(LookingMonster):
	def look(self):
		print('I am looking down')

	def notify(self):
		print('I am yelling')

	def move(self):
		print('I am digging down')

if __name__=="__main__":
	monsters=[LeftLookingMonster(), RightLookingMonster(), UpLookingMonster(), DownLookingMonster()]
	for monster in monsters:
		monster.chase()
