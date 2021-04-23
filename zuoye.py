# 作业1--打印小猫爱吃鱼，小猫要喝水
'''class Cat():
    def __init__(self,animal):
        self.animal=animal
    def eat(self):
        print(f'{self.animal}爱吃鱼')
    def drink(self):
        print(f'{self.animal}要喝水')
eat1=Cat('小猫')
eat1.eat()
drink1=Cat('小猫')
drink1.drink()'''
'''作业2--小明爱跑步，爱吃东西。
1）小明体重75.0公斤
2）每次跑步会减肥0.5公斤
3）每次吃东西体重会增加1公斤
4）小美的体重是45.0公斤'''
'''class Person():
    def __init__(self,name,wight):
        self.name=name
        self.wight=wight
    def dong(self):
        self.wight-=0.5
    def eat(self):
        self.wight+=1
    def __str__(self):
        return '{self.name}的体重是{self.wight}KG'
xiaoming=Person('小明',75)
xiaoming.dong()
xiaoming.eat()
xiaomei=Person('小美',45)
xiaomei.dong()'''

'''3、摆放家具需求：
1）.房子有户型，总面积和家具名称列表
   新房子没有任何的家具
2）.家具有名字和占地面积，其中
   床：占4平米
   衣柜：占2平米
   餐桌：占1.5平米
3）.将以上三件家具添加到房子中
4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表'''

#
# class Furniture:
#     def __init__(self, name, area):
#         self.name = name
#         self.area = area
#
#
# class House:
#     def __init__(self, style, area):
#         self.style = style
#         self.area = area
#         self.remain_area = area
#         self.furniture = []
#
#     def __str__(self):
#         return f'{self.style}户型的房子总面积是{self.area}平米,剩余面积是{self.remain_area}平米,家具名称列表是{self.furniture}'
#
#     def add_furniture(self, item):
#         if self.remain_area >= item.area:
#             self.furniture.append(item.name)
#             self.remain_area -= item.area
#         else:
#             print('家具比空地大了，放不下')
#
#
# fang = House('四室两厅', 1200)
# print(fang)
# bed = Furniture('床', 4)
# fang.add_furniture(bed)
# print(fang)
# closet = Furniture('柜子', 2)
# fang.add_furniture(closet)
# print(fang)
# table = Furniture('餐桌', 2)
# fang.add_furniture(table)
# print(fang)
'''4.士兵开枪需求：
1）.士兵瑞恩有一把AK47
2）.士兵可以开火(士兵开火扣动的是扳机)
3）.枪 能够 发射子弹(把子弹发射出去)
4）.枪 能够 装填子弹 --增加子弹的数量'''


class Soldier():
    def __init__(self, name, gun):
        self.name = name
        self.gun = gun

    def __str__(self):
        return f'{self.name}有一把{self.gun.style}'

    def s_fire(self):
        self.gun.fire()

    def s_add(self):
        self.gun.add()


class Gun():
    def __init__(self, style, bullet):
        self.style = style
        self.bullet = bullet

    def fire(self):
        if self.bullet >= 1:
            self.bullet -= 1
            print('开枪')
            print(f'还剩{self.bullet}颗子弹')
        else:
            print('没子弹了，请装子弹')

    def add(self):
        self.bullet += 1


g1 = Gun('AK47', 3)
n1 = Soldier('瑞恩', g1)
n1.s_fire()
n1.s_fire()
n1.s_fire()
n1.s_fire()
n1.s_add()
n1.s_fire()

