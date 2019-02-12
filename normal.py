class Person:
    def __init__(self, name):
        self.health = 100
        self.armor = 100
        self.damage = 40
        self.name = name

    def _damage(self, player):
        if self.armor > 0:
            self.armor -= player.damage
            return 0
        else:
            self.health = self.health - self.damage
            if self.health <= 0:
                print('Вы {} - победили!'.format(self.name))
                return 1
            else:
                return 0

    def attack(self, player):
        return self._damage(player)


class Player(Person):
    def __init__(self, name):
        Person.__init__(self, name)


class Enemy(Person):
    def __init__(self, name):
        Person.__init__(self, name)


class Fight:
    def __init__(self, player1, player2):
        self.player1 = Player(player1)
        self.player2 = Enemy(player2)

    def fight(self):
        i = 0
        while i != 1:
            i = self.player1.attack(self.player2)
            if i == 1:
                break
            i = self.player2.attack(self.player1)
            if i == 1:
                break


name1 = input('Введите имя первго игрока: ')
name2 = input('Введите имя второго игрока: ')
Fight1 = Fight(name1, name2)
Fight1.fight()
