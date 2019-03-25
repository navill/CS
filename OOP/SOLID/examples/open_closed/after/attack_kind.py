# (계속 변화하는)공격 종류를 추상화한다.
# 다형성을 이용 
# OPEN FOR EXTENSION
# 공격 종류를 확장한다.

from abc import ABCMeta, abstractmethod

def AttackKindFactory(kind):
    if kind=='Fire':
        return FireAttackKind()
    elif kind=='Ice':
        return IceAttackKind()
    elif kind=='Stone':
        return StoneAttackKind()
    elif kind=='Kungfu':
        return KungfuAttackKind()

class AttackKind(metaclass=ABCMeta):
    @classmethod
    def __get_attack_kind(cls):
        return cls.__name__.replace('AttackKind', '')

    def __init__(self):
        self.kind=self.__get_attack_kind()

    def get_kind(self):
        return self.kind

    @abstractmethod
    def attack(self):
        pass

# 게임 개발 초기에 확정된 두 개의 공격 종류

class FireAttackKind(AttackKind):
    def attack(self):
        print(f"under the attack of {self.get_kind()}")

class IceAttackKind(AttackKind):
    def attack(self):
        print(f'under the attack of {self.get_kind()}')

# 추후 게임 규모가 커지면서 두 개의 공격 종류가 확장(EXTENSION)

class StoneAttackKind(AttackKind):
    def attack(self):
        print('Aimming at the player!')

class KungfuAttackKind(AttackKind):
    def attack(self):
        print('Kungfu!!')

if __name__=="__main__":
    fa=FireAttackKind()
    fa.attack()
    ia=IceAttackKind()
    ia.attack()
    ak=AttackKind()



