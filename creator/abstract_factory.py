# -*- coding: UTF-8 -*-

"""
类别模式：抽象工厂
适用范围：当提供一部分类库，而只想显示它们的接口而不是实现，一般是可能要对应多个工厂的多个类别，这种设计模式的关键地方在于PetShop
设计思想：python抽象工厂的设计思想是讲所有工厂类加入到字典，通过字典的key来生产得到具体工厂，再生成想要的对象
"""

import random


class PetShop:
    """创造工厂的抽象方法"""

    def __init__(self, animal_factory=None):
        """pet_factory是一个抽象类"""

        self.pet_factory = animal_factory

    def show_pet(self):
        """通过抽象工厂创建并展示一个对象"""

        pet = self.pet_factory.get_pet()
        print("This is a lovely", str(pet))
        print("It says", pet.speak())
        print("It eats", self.pet_factory.get_food())

class Dog:
    def speak(self):
        return "woof"

    def __str__(self):
        return "Dog"


class Cat:
    def speak(self):
        return "meow"

    def __str__(self):
        return "Cat"

class DogFactory:
    def get_pet(self):
        return Dog()

    def get_food(self):
        return "dog food"

class CatFactory:
    def get_pet(self):
        return Cat()

    def get_food(self):
        return "cat food"

def get_factory():
    """传入各个工厂的实体"""
    return random.choice([DogFactory, CatFactory])()

def main():
    shop = PetShop()
    for i in range(3):
        shop.pet_factory = get_factory()
        shop.show_pet()
        print("=" * 20)

if __name__ == '__main__':
  main()