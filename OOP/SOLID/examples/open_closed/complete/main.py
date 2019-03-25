from monsters import FireMonster, IceMonster, StoneMonster, KungfuMonster
from character import Player
from attack_kind import IceAttackKind, FireAttackKind

fm=FireMonster()
im=IceMonster()
sm=StoneMonster()
kfm=KungfuMonster()

monsters=[]
monsters.extend((fm, im, sm, kfm))

player=Player('john', 120, 20, IceAttackKind(), FireAttackKind())
print(player)

for mon in monsters:
    player.attack(mon, 'Fire')

for mon in monsters:
    print(mon)

for mon in monsters:
    print(mon.get_attack_kind())
    mon.attack(player, mon.get_attack_kind())

print(player)
