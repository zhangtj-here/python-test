# user1 = {'name': 'tom', 'hp': 100}
# user2 = {'name': 'jerry', 'hp': 80}
#
#
# def print_role(rolename):
#     print('name is %s , hp is %s' % (rolename['name'], rolename['hp']))
#
#
# print_role(user1)
# print_role(user2)


class Player():
    def __init__(self, name, hp, occu):
        self.__name = name
        self.hp = hp
        self.occu = occu

    def print_role(self):
        print('name is %s, hp is %s, occu is %s' %
              (self.__name, self.hp, self.occu))

    def updateName(self, newname):
        self.__name = newname


class Monster():
    '定义一个类'

    def __init__(self, hp=100):
        self.hp = hp

    def run(self):
        print('移动到某个位置')

    def whoami(self):
        print('我是动物父类')


class Animals(Monster):
    '普通的动物'

    def __init__(self, hp=10):
        # self.hp = hp
        super().__init__(hp)


class Boss(Monster):
    '特殊动物'

    def __init__(self, hp=600):
        super().__init__(hp)

    def whoami(self):
        print('我是boss类')


a1 = Monster()
# print(a1.hp)
# a1.run()
#
a2 = Animals()
# print(a2.hp)
# a2.run()
# a2.whoami()
#
a3 = Boss()
# print(a3.hp)
# a3.whoami()

print('a1的类型 %s' % type(a1))
print('a2的类型 %s' % type(a2))
print('a3的类型 %s' % type(a3))

a = '123'
print(type(a))
print(isinstance(a, object))

print(isinstance(a1, object))
print(isinstance(a1, Monster))
print(isinstance(a2, Monster))
print(isinstance(a3, Monster))

#
# user1 = Player('tom', 100, 'war')
# user2 = Player('jerry', 80, 'master')
# user1.print_role()
# user2.print_role()
# user1.updateName('tom1')
# user1.__name = 'tom2'
# user1.print_role()
