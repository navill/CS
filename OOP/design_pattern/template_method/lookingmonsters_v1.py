import random

# executing flow is the same!
# but small steps are different!

class LeftLookingMonster:
	def chase(self):
# watch leftside
		is_there=self.lookleft()
		
		if is_there:
			self.howl()
			self.runleft()

	def lookleft(self):
		print('I am looking left')
		return random.randint(0, 1)

	def runleft(self):
		print('I am running left!')

	def howl(self):
		print('I am howling!!')

class RightLookingMonster:
	def chase(self):
		is_there=self.lookright()

		if is_there:
			self.growl()
			self.runright()

	def lookright(self):
		print('I am looking right')
		return random.randint(0, 1)
	
	def growl(self):
		print('I am growling')

	def runright(self):
		print('I am running right')

class UpLookingMonster:
	def chase(self):
		is_there=self.lookup()

		if is_there:
			self.squeal()
			self.flyup()

	def lookup(self):
		print('I am looking up')
		return random.randint(0, 1)

	def squeal(self):
		print('I am squealing')

	def flyup(self):
		print('I am flying up')

class DownLookingMonster:
	def chase(self):
		is_there=self.lookdown()

		if is_there:
			self.yell()
			self.digdown()

	def lookdown(self):
		print('I am looking down')
		return random.randint(0, 1)

	def yell(self):
		print('I am yelling')

	def digdown(self):
		print('I am digging down')

if __name__=="__main__":
	monsters=[LeftLookingMonster(), RightLookingMonster(), UpLookingMonster(), DownLookingMonster()]
	for monster in monsters:
		monster.chase()
