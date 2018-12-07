# -*- coding: UTF-8 -*-

"""
类别模式：工厂模式
适用范围：当一个类希望由它的子类来指定它所创建的对象，这个累的关键是get_localizer如何编写
设计思想：python工厂方法的设计思想是讲所有能够使用工厂的类加入到字典，通过字典的key来生产想要创建的对象
"""

class FemaleGetter:
    """获取女性的比例"""

    def __init__(self):
        self.trans = dict(Female=u"44%")

    def get(self, probability):
        try:
            return self.trans[probability]
        except KeyError:
            return str(probability)

class MaleGetter:
    """获取男性比例"""

    def __init__(self):
        self.trans = dict(Male=u"56%")

    def get(self, probability):
        try:
            return self.trans[probability]
        except KeyError:
            return str(probability)

def get_localizer(sex="Male"):
    """工厂类实现通过字典的方式识别要创建的对象"""
    sexd = dict(Male=MaleGetter, Female=FemaleGetter)
    return sexd[sex]()

def main():
    # 通过工厂方法创建对象
    # male, female = get_localizer("Male"), get_localizer("Female")
    # 使用对象中的方法
    for sex in "Male Female".split():
        print(sex +":"+get_localizer(sex).get(sex))

if __name__ == '__main__':
  main()