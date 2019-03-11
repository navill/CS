
class Attacker:
	def attack(self, attack_kind):
 		if attack_kind=='Fire':
 			print('the fire of the dragon')
 		elif attack_kind=='Ice':
 			print('the ice of the evil')
 		elif attack_kind=='Stone':
 			print('the stone of the people')


if __name__=="__main__":
	at=Attacker()
	at.attack('Fire')



