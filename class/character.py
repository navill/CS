from abc import ABCMeta, abstractmethod

#추상 클래스
class Character(metaclass=ABCMeta):
    def __init__(self, name, hp, power):
        self.name=name
        self.hp=hp
        self.power=power

    @abstractmethod
    def attack(self, other, attack_kind):
        pass

    @abstractmethod
    def get_damage(self, power, attack_kind):
        pass

    def __str__(self):
        return '{} : {}'.format(self.name, self.hp)

class Player(Character):
    def __init__(self, name='player', hp=100, power=10, *attack_kinds):
        super().__init__(name, hp, power)

        self.skills=[]
        for attack_kind in attack_kinds:
            self.skills.append(attack_kind)

    def attack(self, other, attack_kind):
        if attack_kind in self.skills:
            other.get_damage(self.power, attack_kind)

    def get_damage(self, power, attack_kind):
        """
        attack_kind가 self.skills에 있으면 피해가 반감
        """
        if attack_kind in self.skills:
            self.hp-= (power//2)
        else:
            self.hp-=power

#공통된 부분은 부모 클래스로 만들어 둔다.
class Monster(Character):
    def __init__(self, name, hp, power):
        super().__init__(name, hp, power)
        self.attack_kind=None

    def attack(self, other, attack_kind):
        if self.attack_kind==attack_kind:
            other.get_damage(self.power, attack_kind)

    #공격 받을 때 
    #불 몬스터의 경우 불 공격을 받으면 오히려 체력이 증가!!
    #얼음 공격을 받으면 체력이 깎인다.
    def get_damage(self, power, attack_kind):
        """
        몬스터는 같은 속성의 공격을 받으면 체력이 증가!!
        """
        if self.attack_kind==attack_kind:
            self.hp+=power
        else:
            self.hp-=power

    def get_attack_kind(self):
        return self.attack_kind

class IceMonster(Monster):
    def __init__(self, name='Ice monster', hp=50, power=10):
        super().__init__(name, hp, power)
        self.attack_kind='ICE'

class FireMosnter(Monster):
    def __init__(self, name='Fire monster', hp=50, power=20):
        super().__init__(name, hp, power)
        self.attack_kind='FIRE'

if __name__=="__main__":
    player=Player('sword master', 100, 30, 'ICE')
    monsters=[]
    monsters.append(IceMonster())
    monsters.append(FireMosnter())

    for monster in monsters:
        print(monster)

    for monster in monsters:
        player.attack(monster, 'ICE')

    print('after the player attacked')
    for monster in monsters:
        print(monster)
    print()

    print(player)

    for monster in monsters:
        #플레이어가 ICE 공격 가짐
        #아이스 몬스터 공격시 5만 깎임
        #파이어 몬스터 공격시 20이 깎임
        monster.attack(player, monster.get_attack_kind())
    
    print('after monsters attacked')
    print(player)
