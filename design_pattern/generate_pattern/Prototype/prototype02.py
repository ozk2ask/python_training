"""
Prototype
あるインスタンスから同じインスタンスをコピーして簡単に複製作業できるようにする
・Prototype:複製するOBJの構成要素を定義するIF
・ConcretePrototype：Prototypeを具体化したクラス（複数クラス作成）
・Manager：ConcretePrototypeを登録し、複製を作成するクラス
"""

from abc import ABC, abstractmethod
from copy import deepcopy

class Prototype(ABC):
    @abstractmethod
    def use(self, msg):
        pass
    
    @abstractmethod
    def _clone(self):
        pass
    

class MessageBox(Prototype):
    def __init__(self, decoration_char):
        self.__decoration_char = decoration_char
        
    def use(self, msg):
        str_msg = str(msg)
        print(self.__decoration_char * (len(str_msg) + 4))
        print(self.__decoration_char + ' ' + str_msg + ' ' + self.__decoration_char)
        print(self.__decoration_char * (len(str_msg) + 4))
    
    def _clone(self):
        print('MessageBoxのクローンを作成します')
        return deepcopy(self)
    
    @property
    def decoration_char(self):
        return self.__decoration_char
    
    @decoration_char.setter
    def decoration_char(self, decoration_char):
        self.__decoration_char = decoration_char
        
class UnderlinePen(Prototype):
    def __init__(self, underline_char):
        self.__underline_char = underline_char
        
    def use(self, msg):
        str_msg = str(msg)
        print(str_msg)
        print(self.__underline_char * len(str_msg))
        
    def _clone(self):
        print('UnderlinePenのコピーを作成します。')
        return deepcopy(self)
    
    @property
    def underline_char(self):
        return self.__underline_char
    
    @underline_char.setter
    def underline_char(self, underline_char):
        self.__underline_char = underline_char


class Manager:
    def __init__(self):
        self.__products = {}
        
    def register(self, name, prototype: Prototype):
        self.__products[name] = deepcopy(prototype)
    
    def create_product(self, name):
        product = self.__products.get(name)
        return product._clone()



manager = Manager()

        
m_box = MessageBox('*')
m_box.use('Hello')

u_pen = UnderlinePen('-')
u_pen.use('Hello')

manager.register('message_box', m_box)
manager.register('underline_pen', u_pen)


new_m_box = manager.create_product('message_box')
new_m_box.use('NewBox')

m_box.decoration_char = '~'
m_box.use('Hello')


# m_box_clone = m_box._clone()
m_box_clone = manager.create_product('message_box')
m_box_clone.use('hello2')

