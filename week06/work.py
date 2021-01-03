#!/usr/bin/env python

'''
1.定义“动物”、“猫”、“狗”、“动物园”四个类，动物类不允许被实例化。
2.动物类要求定义“类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性，是否属于凶猛动物的判断标准是：“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”。
3.猫类要求有“叫声”、“是否适合作为宠物”以及“名字”三个属性，
其中“叫声”作为类属性，除凶猛动物外都适合作为宠物，猫类继承自动物类。
狗类属性与猫类相同，继承自动物类。
4.动物园类要求有“名字”属性和“添加动物”的方法，“添加动物”方法要实现同一只动物（同一个动物实例）不能被重复添加的功能。
'''
from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    # 定义“类型”、“体型”、“性格”、“是否属于凶猛动物”属性
    def __init__(self, name, animal_type, size_type, character_type):
        self.name = name
        self._animal_type = animal_type
        self._size_type = size_type
        self._character_type = character_type

    @property
    def animal_type(self):
        return self._animal_type

    @animal_type.setter
    def animal_type(self, value):
        if value not in ('食肉', '食草', '混食'):
            raise TypeError('动物类型为[ 食肉 | 食草 | 混食 ]')
        self._animal_type = value

    @property
    def size_type(self):
        return self._size_type

    @size_type.setter
    def size_type(self, value):
        if value not in ('大', '中', '小'):
            raise TypeError("动物大小为[ 大 |中 |小 ]")
        self._size_type = value

    @property
    def character_type():
        return self._character_type

    @character_type.setter
    def character_type(self, value):
        if value not in ('温顺', '凶猛'):
            raise TypeError("动物性格为[ 温顺 | 凶猛]")
        self._character_type = value

    @property
    def check_is_fierce(self):
        n = {
            '大': 3,
            '中': 2,
            '小': 1
        }[self.size_type]
        if n >= 2 and self._animal_type == '食肉' and self._character_type == '凶猛':
            return f'{self.name} 是凶猛动物, 不可作为宠物!!!'
        return f'{self.name} 不是凶猛动物，可以作为宠物'

    @abstractmethod
    def animal_sound():
        pass


class Cat(Animal):
    @property
    def animal_sound(self):
        return "喵喵... ..."

    def pet(self):
        return self.check_is_fierce


class Dog(Animal):
    @property
    def animal_sound(self):
        return "汪汪... ..."

    def pet(self):
        return self.check_is_fierce


class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        # 判断是否同一只
        for a in self.animals:
            if a == animal:
                print(f"同一只{ animal }不能重复添加")
                return
        self.animals.append(animal)

    def is_hasattr(self, type_name):
        for a in self.animals:
            if type(a).__name__ == type_name:
                return f"{self.name} 有 {type_name}"
        return f"{self.name} 没有 {type_name}"


def hasattr(zoo, name):
    return zoo.is_hasattr(name)


if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')
    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    # 增加一只猫到动物园
    z.add_animal(cat1)
    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')
    print(have_cat)
    # 判断是否是凶猛动物
    print(cat1.check_is_fierce)
    # 添加一只狮子到动物园
    zangao1 = Dog('藏獒 1', '食肉', '中', '凶猛')
    z.add_animal(zangao1)
    print(z.animals)
    # 判断狮子是否是凶猛动物
    print(zangao1.check_is_fierce)

