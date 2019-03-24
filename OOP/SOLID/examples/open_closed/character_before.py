# 확장할 때 마다 Character 클래스와
# Monster 클래스의 코드가 변한다.

from abc import ABCMeta, abstractmethod
from attack_before import Attacks

class Character(metaclass=ABCMeta):
    attacks=Attacks()
    def __init__(self, name, hp, power):
        self.name=name
        self.hp=hp
        self.power=power

    @abstractmethod
    def attack(self, other, kind):
        pass

    @abstractmethod
    def get_damage(self, power, attack_kind):
        pass

    def __str__(self):
        return f'{self.name} : {self.hp}'

class Player(Character):
    def __init__(self, name='player', hp=100, power=10, *a_kinds):
        super().__init__(name, hp, power)

        self.skills=[]
        for attack_kind in a_kinds:
            self.skills.append(attack_kind)

    def attack(self, other, a_kind):
        if a_kind in self.skills:
            other.get_damage(self.power, a_kind)
            if a_kind=='Fire':
                self.attacks.fire_attack()
            elif a_kind=='Ice':
                self.attacks.ice_attack()
            elif a_kind=='Stone':
                self.attacks.stone_attack()
            elif a_kind=='Kungfu':
                self.attacks.kungfu_attack()

    def get_damage(self, power, a_kind):
        if a_kind in self.skills:
            self.hp-=(power//2)
        else:
            self.hp-=power

class Monster(Character):
    @classmethod
    def get_monster_kind(cls):
        return cls.__name__.replace('Monster', '')

    def __init__(self, name='Monster', hp=50, power=5):
        super().__init__(name, hp, power)
        self.name=self.get_monster_kind()+name
        self.attack_kind=self.get_monster_kind()

    def attack(self, other, a_kind):
        if a_kind==self.attack_kind:
            other.get_damage(self.power, a_kind)
            if a_kind=='Fire':
                self.attacks.fire_attack()
            elif a_kind=='Ice':
                self.attacks.ice_attack()
            elif a_kind=='Stone':
                self.attacks.stone_attack()
            elif a_kind=='Kungfu':
                self.attacks.kungfu_attack()

    def get_damage(self, power, a_kind):
        if a_kind==self.attack_kind:
            self.hp+=power
        else:
            self.hp-=power

    def get_attack_kind(self):
        return self.attack_kind

    @abstractmethod
    def generate_gold(self):
        pass

# 게임 개발 초기의 몬스터 종류는 두 가지
class FireMonster(Monster):
    def generate_gold(self):
        return 10

class IceMonster(Monster):
    def __init__(self):
        super().__init__()
        self.hp=100

    def generate_gold(self):
        return 20

# 게임 규모가 커지면서 추가된 몬스터 
class StoneMonster(Monster):
    def generate_gold(self):
        return 0

class KungfuMonster(Monster):
    def generate_gold(self):
        return 1000

if __name__=="__main__":
    fm=FireMonster()
    im=IceMonster()
    sm=StoneMonster()
    kfm=KungfuMonster()

    monsters=[]
    monsters.extend((fm, im, sm, kfm))

    player=Player('john', 120, 20,'Fire', 'Ice')

    for mon in monsters:
        player.attack(mon, 'Fire')

    for mon in monsters:
        print(mon)

    for mon in monsters:
        print(mon.get_attack_kind())
        mon.attack(player, mon.get_attack_kind())

    print(player)
