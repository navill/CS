from abc import ABCMeta, abstractmethod

# strategy
class AttackKind(metaclass=ABCMeta):
	@abstractmethod
	def attack(self, other):
		pass
  
class FireAttackKind(AttackKind):
	def attack(self):
		print('the fire of the dragon')
  
class IceAttackKind(AttackKind):
	def attack(self):
		print('the ice of the evil')
  
class StoneAttackKind(AttackKind):
	def attack(self):
		print('the sone of the people')
  
# ... new attackkind can be added without modifying the context of Attacker
