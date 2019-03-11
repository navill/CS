# strategy
# what in charge of behavior : CONTEXT
# what in charge of algorithm : STRATEGY

# separate STRATEGY from CONTEXT : strategy pattern

# if you add some attack_kinds, this code will be longer than you expected
# it is soooo hard to change this code
# Single responsibility + Open-closed + Liskov + Dependency inversion

from attackkinds import IceAttackKind, FireAttackKind

# context
class Attacker:
	# attack_kind obj
	attackkind=None
	
	def __init__(self, attack_kind):
		Attacker.attackkind=attack_kind

	def attack(self):
		self.attackkind.attack()

if __name__=="__main__":
	ak=IceAttackKind() 
	at=Attacker(ak)
	at.attack()

	ak2=FireAttackKind()
	at2=Attacker(ak2)
	at2.attack()
