
class SingletonError(Exception):
	def __init__(self, msg):
		super().__init__(msg)

class Locator:
	locator=None
	
	@classmethod
	def get_instance(cls):
		return cls.locator
		
	def __init__(self, fdreader):
		if Locator.locator:
			raise SingletonError("There is already a singleton object. sorry!")
		self.fdreader=fdreader
	
	def init(self):
		Locator.locator=self
		
	def get_reader(self):
		return self.fdreader
