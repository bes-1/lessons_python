from time import sleep


class Car:
    speed_list = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 80, 90, 100, 120, 140, 150, 200, 220, 240, 260]

    def __init__(self, name, color, speed, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def info(self):
        information = {'name': self.name, 'color': self.color, 'speed': self.speed, 'is_police': self.is_police}
        return information

    def go(self):
        print(f'The {self.name}  is going')

    def stop(self):
        print(f'The {self.name}  is stopped')

    def turn(self, direction):
        print(f'The {self.name} is turned to {direction}')

    def show_speed(self):
        for i in Car.speed_list:
            print(f'speed {self.name} now: {i}')
            sleep(1)


class TownCar(Car):

    def show_speed(self):
        for i in Car.speed_list:
            print(f'speed {self.name} now: {i}')
            sleep(1)
            if i > 60:
                print('Your speed more 60')
                break


class SportCar(Car):
    def __init__(self, name, color, speed, race=False):
        super().__init__(name, color, speed)
        self.race = race
        print(f'The car is in a race: {self.race}')

    def show_speed(self):
        for i in Car.speed_list:
            print(f'speed {self.name} now: {i}')
            sleep(0.5)
            if i >= 80 and self.race == False:
                print(F'Your speed {i}, you do not participate in a race! Limitation of speed 80')
                break
            if i > 80 and self.race == True:
                print(f'Your speed {i}, you participate in a race! No limitation of speed')


class WorkCar(Car):
    def show_speed(self):
        for i in Car.speed_list:
            print(f'speed {self.name} now: {i}')
            sleep(1)
            if i > 40:
                print('Your speed more 40')
                break


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police, pursuit=False):
        super().__init__(name, color, speed, is_police)
        self.pursuit = pursuit
        print(f'The car is pursuit now: {self.pursuit}')

    def show_speed(self):
        for i in Car.speed_list:
            print(f'speed {self.name} now: {i}')
            sleep(1)
            if 100 < i < 150:
                print(F'Your speed more {i}, to be attention!')
            if i >= 150:
                print(F'Your speed {i}, you are driving for max speed!')
                break


towns_car = TownCar('towns_car', 'red', 80)
towns_car.go()
works_car = WorkCar('works_car', 'pink', 77)
works_car.go()
works_car.turn('right')
print(f'Information about {works_car.name}: {works_car.info()}')
police_car = PoliceCar('policeman_car', 'blue', 80, True, True)
print(f'Information about {police_car.name}: {police_car.info()}')
# police_car.show_speed()
sport_car = SportCar('sport_car', 'black', 120)
print(f'Information about {sport_car.name}: {sport_car.info()}')
sport_car.show_speed()
sport_car.stop()
