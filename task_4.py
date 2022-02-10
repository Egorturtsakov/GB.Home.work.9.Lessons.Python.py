class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        if self.speed != 0:
            print('Машина едет')

    def stop(self):
        if self.speed == 0:
            print('Машина остановилась')

    def turn(self, side):
        if side == 1:
            print('Машина поворачивает влево')
        if side == 2:
            print('Машина поворачивает вправо')


TownCar = Car(0, 'yello', 'Priora', '')
SportCar = Car(120, 'Red', 'Lambo', '')
WorkCar = Car(35, 'gray', 'gazelle', '')
PoliceCar = Car(200, 'hakky', 'bobik', '...')