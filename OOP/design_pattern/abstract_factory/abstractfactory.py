import time
import random

class Player:
	def __init__(self, hp=10):
		self.hp=hp

	def set_hp(self, hp):
		self.hp=hp

	def get_hp(self):
		return self.hp

class MonsterFactory:
	def __init__(self, player_hp):
		self.player_hp=player_hp

	def set_player_hp(self, hp):
		self.player_hp=hp


	def create_monster(self):
		if self.player_hp >= 100:
			return StrongMonster()
		elif self.player_hp >= 60:
			return NormalMonster()
		else:
			return WeakMonster()


class StrongMonster:
	def __init__(self):
		print('Strong Monster!')


class NormalMonster:
	def __init__(self):
		print('Normal Monster!')

class WeakMonster:
	def __init__(self):
		print('Weak Monster')


if __name__=="__main__":
	player=Player()
	monster_factory=MonsterFactory(player.get_hp())
	monsters=[]

	for i in range(10):
		time.sleep(1)
		new_hp=player.get_hp()+10
		player.set_hp(new_hp)
		monster_factory.set_player_hp(player.get_hp())
		print(f'player hp : {player.get_hp()}')
		monsters.append(monster_factory.create_monster())
			
