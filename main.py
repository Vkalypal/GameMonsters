import random


class Creature:
    def __init__(self, name, simbol, health, damage, gold):
        self._name = name
        self._simbol = simbol
        self._health = health
        self._damage = damage
        self._gold = gold
        self._fullHealth = health

    @property  # аннотация геттера
    def name(self): return self._name

    @property  # аннотация геттера
    def simbol(self): return self._simbol

    @property  # аннотация геттера
    def health(self): return self._health

    @property  # аннотация геттера
    def damage(self): return self._damage

    @property  # аннотация геттера
    def gold(self): return self._gold

    def reduceHealth(self, damage):
        self._health = self._health - damage
        return self._health

    def isDead(self):
        if self._health <= 0:
            return True

    def addGold(self, gold):
        self._gold = self._gold + gold
        return self._gold

    def fullHealth(self):
        self._health = self._fullHealth


class Player(Creature):
    __level = 1

    def levelUp(self):
        self.__level = self.__level + 1
        self._damage = self._damage + 1

    def hasWon(self):
        if self.__level == 20:
            return True

    @property
    def level(self): return self.__level


class Monster(Creature):
    DRAGON = Creature('Дракон', 'D', 20, 4, 100)
    ORC = Creature('Орк', 'o', 4, 2, 25)
    SLIME = Creature('Слизняк', 's', 1, 1, 10)
    Monsters = [DRAGON, ORC, SLIME]


def randomMonsters():
    m = Monster.Monsters[random.randint(0, 2)]
    return m


def attackPlayer(m, p):
    if (m.isDead() == True):
        return
    p.reduceHealth(m.damage)
    print(m.name + ' наносит вам ' + str(m.damage) + ' единиц урона.')


def attackMonster(m, p):
    if p.isDead() == True:
        return
    print('Вы бьёте ' + m.name + ' и наносите ' + str(p.damage) + ' единиц урона.')
    m.reduceHealth(p.damage)
    if (m.isDead() == True):
        print('Вы убили ' + m.name + '.')
        p.levelUp()
        print('Ваш уровень ' + str(p.level) + '.')
        print('Вы нашли ' + str(m.gold) + ' золотых.')
        p.addGold(m.gold)

def fightMonster():
    monster = randomMonsters()
    print('Вы встретили ' + monster.name + ' (' + monster.simbol + ')')
    while (p.isDead() != True and monster.isDead() != True):
        choice = input('(Б)ежать или (Д)раться: ')
        if choice == 'Б':
            if (random.randint(0, 1) == 1):
                print('Вы сбежали')
                monster.fullHealth()  #проверить здоровье монстра после удара и побега
                return
            else:
                print('Вам не удалось сбежать')
                attackPlayer(monster, p)
        if choice == 'Д':
            attackMonster(monster, p)
            attackPlayer(monster, p)
            if monster.isDead():
                monster.fullHealth()
                return

pName = input('Как тебя зовут: ')
print('Привет, ' + pName + '.')
p = Player(pName, '@', 10, 1, 0)
while (p.isDead() != True and p.hasWon() != True):
    fightMonster()
if p.isDead():
    print('ТЫ МЕРТВЕТС!!!')
    print('Вы достигли ' + str(p.level) + ' уровня и унесли с собой в могилу '
          + str(p.gold) + ' золотых.')

