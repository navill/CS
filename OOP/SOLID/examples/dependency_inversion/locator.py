class Locator:
    locator=None
    
    @classmethod
    def get_instance(cls):
        return cls.locator

    def __init__(self, fdreader):
        self.fdreader=fdreader

    def init(self):
        Locator.locator=self

    def get_reader(self):
        return self.fdreader