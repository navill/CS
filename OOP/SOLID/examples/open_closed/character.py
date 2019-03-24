# 추상화 타입을 사용해 프로그래밍
# CLOSED FOR MODIFICATION
# 공격 종류를 확장해도 캐릭터의 공격 코드는 변하지 않는다.

from abc import ABCMeta, abstractmethod
from attack_kind import (AttackKindFactory, FireAttackKind, IceAttackKind,
                         StoneAttackKind, KungfuAttackKind)

class Character(metaclass=ABCMeta):
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
    def __init__(self, name='player', hp=100, power=10, *attack_kinds):
        super().__init__(name, hp, power)

        self.skills=[]
        for attack_kind in attack_kinds:
            self.skills.append(attack_kind)

    def attack(self, other, a_kind):
        for attack_kind in self.skills:
            if a_kind==attack_kind.get_kind():
                other.get_damage(self.power, a_kind)
                attack_kind.attack()

    def get_damage(self, power, a_kind):
        for attack_kind in self.skills:
            if attack_kind.get_kind()==a_kind:
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
        self.attack_kind=AttackKindFactory(self.get_monster_kind())

    def attack(self, other, a_kind):
        if self.attack_kind.get_kind()==a_kind:
            other.get_damage(self.power, a_kind)
            self.attack_kind.attack()

    def get_damage(self, power, a_kind):
        if a_kind==self.attack_kind.get_kind():
            self.hp+=power
        else:
            self.hp-=power

    def get_attack_kind(self):
        return self.attack_kind.get_kind()

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

    player=Player('john', 120, 20, IceAttackKind(), FireAttackKind())

    for mon in monsters:
        player.attack(mon, 'Fire')

    for mon in monsters:
        print(mon)

    for mon in monsters:
        mon.attack(player, mon.get_attack_kind())

    print(player)
