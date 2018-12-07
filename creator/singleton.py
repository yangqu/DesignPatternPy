# -*- coding: UTF-8 -*-

"""
类别模式：单例模式
适用范围：一般适用于可复用的对象，通常在服务中看到较多，非常省内存
设计思想：创建实例前先检查是否存在，不存在再创建
"""


class Singleton(object):
    """ 一个python版本的单例模式"""

    def __new__(cls, *args, **kw):
        #判断是否存在实例，不存在则初始化
        if not hasattr(cls, '_instance'):
            org = super(Singleton, cls)
            cls._instance = org.__new__(cls)
        return cls._instance


if __name__ == '__main__':
    """一个类继承了单例模式"""
    class SingleSpam(Singleton):
        def __init__(self, s):
            self.s = s

        def __str__(self):
            return self.s


    s1 = SingleSpam('spam')
    print
    id(s1), s1
    s2 = SingleSpam('spa')
    print
    id(s2), s2
    print
    id(s1), s1