class Computer:
    def __init__(self, cpu,ram):
        self.CPU=cpu
        self.RAM=ram

    def browse(self):
        print('browse')

    def work(self):
        print('work')

class Laptop(Computer):
    def __init__(self, cpu, ram, battery):
        super().__init__(cpu, ram)
        self.battery=battery
    
    def move(self, to):
        print('move to {}'.format(to))

if __name__=="__main__":
    lap=Laptop('intel', 16, 'powerful')
    lap.browse()
    lap.work()
    lap.move('office')