class TownCar:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина - {}, едет прямо со скоростью {}.'.format(self.name, self.speed))

    def stop(self):
        print('Машина - {}, остановилась.'.format(self.name))

    def turn(self, direction):
        print('Машина - {}, повернула на{}.'.format(self.name, direction))


class SportCar(TownCar):
    def __init__(self, speed, color, name, is_police):
        TownCar.__init__(self, speed, color, name, is_police)


class WorkCar(TownCar):
    def __init__(self, speed, color, name, is_police):
        TownCar.__init__(self, speed, color, name, is_police)


class PoliceCar(TownCar):
    def __init__(self, speed, color, name, is_police):
        TownCar.__init__(self, speed, color, name, is_police)


car1 = TownCar("10", "зеленая", "Skoda Octavia", "False")
car1.go()
car1.stop()
car1.turn("право")

car2 = SportCar("100", "зеленая", "Audi A6", "False")
car2.go()
car2.stop()
car2.turn("право")

car3 = WorkCar("10", "зеленая", "Mercedes Actros", "False")
car3.go()
car3.stop()
car3.turn("лево")

car4 = PoliceCar("10", "зеленая", "Ford", "True")
car4.go()
car4.stop()
car4.turn("лево")
