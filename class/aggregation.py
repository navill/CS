class Gun:
    def __init__(self, kind):
        self.kind=kind

    def bang(self):
        print('bang bang!')

class Police:
    def __init__(self):
        self.gun=None

    def acquire_gun(self, gun):
        self.gun=gun

    def release_gun(self):
        gun=self.gun
        self.gun=None
        return gun

    def shoot(self):
        if self.gun:
            self.gun.bang()
        else:
            print('Unable to shoot')

if __name__=="__main__":
    p1=Police()
    p1.shoot()
    print()

    revolver=Gun('Revolver')
    p1.acquire_gun(revolver)
    
    revolver=None

    p1.shoot()
    print()

    revolver=p1.release_gun()

    p1.shoot()