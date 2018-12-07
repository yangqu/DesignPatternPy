# -*- coding: UTF-8 -*-

"""
类别模式：建造者模式
适用范围：这是一种装配方式，即基本做事的对象种类不会重大变化，但是他们的组合顺序会经常改变
设计思想：如何协调各种对象的工作，就需要一个统一调度者来掌管做事的流程，只要在使用到哪个对象的时候动态去装配就可以了
"""
"""真正的建造者，他有一个属性是调用对象本身的接口，两个方法，一个是get_building，是装配新对象，一个是construct_building，进行任务的协调"""
class Director(object):
    def __init__(self):
        self.builder = None

    def construct_building(self):
        self.builder.new_building()
        self.builder.build_floor()
        self.builder.build_size()

    def get_building(self):
        return self.builder.building


# 做事对象的接口
class Builder(object):
    def __init__(self):
        self.building = None

    def new_building(self):
        self.building = Building()


# 第一个做事对象
class BuilderHouse(Builder):
    def build_floor(self):
        self.building.floor = 'One'

    def build_size(self):
        self.building.size = 'Big'

#第二个做事对象
class BuilderFlat(Builder):
    def build_floor(self):
        self.building.floor = 'More than One'

    def build_size(self):
        self.building.size = 'Small'


# 产品
class Building(object):
    def __init__(self):
        self.floor = None
        self.size = None

    def __repr__(self):
        return 'Floor: %s | Size: %s' % (self.floor, self.size)

def main():
    director = Director()
    director.builder = BuilderHouse()
    director.construct_building()
    building = director.get_building()
    print(building)
    director.builder = BuilderFlat()
    director.construct_building()
    building = director.get_building()
    print(building)

if __name__ == '__main__':
  main()