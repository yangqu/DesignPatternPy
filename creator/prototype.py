# -*- coding: UTF-8 -*-

"""
类别模式：原型模式
适用范围：这是一种不需要从类级别进行实例化的方法，在类过多或者过复杂情况下，实例生成实例就方便的多
设计思想：使用copy方法复制一份实例使用
"""

import copy

class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        """注册一个对于选拔个"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """解雇一个对象"""
        del self._objects[name]

    def clone(self, name, **attr):
        """复制一个对象"""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


def main():
    class A:
        def __str__(self):
            return "I am A"

    a = A()
    prototype = Prototype()
    prototype.register_object('a', a)
    b = prototype.clone('a', a=1, b=2, c=3)

    print(a)
    print(b.a, b.b, b.c)


if __name__ == '__main__':
    main()