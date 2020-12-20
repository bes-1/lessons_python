from abc import ABC, abstractmethod

class Clothes:
    sum = 0
    total_thigs = []
    def __init__(self, name):
        self.name = name
    def total_cloth(self):
        for i in Clothes.total_thigs:
            Clothes.sum += i
        return f'Общий расход ткани на {self.name}: {Clothes.sum}'

class MyAbstractClass(ABC):
    @abstractmethod
    def total(self):
        pass

class Coat(MyAbstractClass):
    def __init__(self, size):
        self.size = size

    @property
    def total(self):
        self.spend_cloth_coat = self.size/6.5 + 0.5
        Clothes.total_thigs.append(self.spend_cloth_coat)
        return self.spend_cloth_coat


class Suit(MyAbstractClass):
    def __init__(self, height):
        self.height = height

    @property
    def total(self):
        self.spend_cloth_suit = self.height * 2 + 0.3
        Clothes.total_thigs.append(self.spend_cloth_suit)
        return self.spend_cloth_suit


coat_1 = Coat(6.5)
print(f'Потрачено ткани на пальто: {coat_1.total}')
suit_1 = Suit(1.5)
print(f'Потрачено ткани на костюм {suit_1.total}')
all_cloth = Clothes('DG')
print(all_cloth.total_cloth())
