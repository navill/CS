
import random
from abc import ABCMeta, abstractmethod
import time


class Position:
	def __init__(self):
		self.x=0
		self.y=0

	def set_pos(self, x, y):
		self.x=x
		self.y=y

	def get_pos(self):
		return (self.x, self.y)

	def __str__(self):
		return f'({self.x}, {self.y})'

# SUBJECT
# role : add an observer, remove an observer
# role : NOTIFY STATUS
class PlayerSubject:
	def __init__(self):
		self.observers=[]

	def register(self, observer):
		self.observers.append(observer)

	def remove(self, observer):
		self.observers.remove(observer)

	def notify(self, player_pos):
		for observer in self.observers:
			observer.on_find_player(player_pos)
		

# INHERIT FROM SUBJECT
# the one who takes care of observers
class PlayerFinder(PlayerSubject):
	def find(self, find_pos):
		# simulation code 
		is_found=random.randint(0, 1)
		if is_found:
			self.notify(find_pos)
		else:
			print(f'Finder can not find the player on {find_pos}')



# OBSERVER INTERFACE
class Observer(metaclass=ABCMeta):
	@abstractmethod
	def on_find_player(self, player_pos):
		pass

class FireMonster(Observer):
	def on_find_player(self, player_pos):
		print(f'I will attack the player on {player_pos}')

class IceMonster(Observer):
	def on_find_player(self, player_pos):
		print(f'Ice! Ice! on the {player_pos}')
		

class AnotherPlayer(Observer):
	def on_find_player(self, player_pos):
		print(f'I am going to help you on {player_pos}')

if __name__=="__main__":
	player_pos=Position()

	player_finder=PlayerFinder()
	
	fm=FireMonster()
	im=IceMonster()
	ap=AnotherPlayer()

	player_finder.register(fm)
	player_finder.register(im)
	player_finder.register(ap)

	for i in range(10):
		time.sleep(1)
		x=random.randrange(1, 20)
		y=random.randrange(1, 20)
		player_pos.set_pos(x, y)
		player_finder.find(player_pos)
		print()
