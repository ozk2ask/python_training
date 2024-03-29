"""
Decorator

複数の機能を１つのクラスにまとめる

・Component: 機能を追加する際の中核
・ConcreteComponent: 追加する処理を記載
・Decorator: Componentを継承したクラス、プロパティにComponentを持つ
・ConcreteDecorator: Decoratorの処理を具体的に記述
"""

from abc import ABC, abstractmethod

class Component(ABC):
    def operation(self):
        pass
    
class ShowCharComponent(Component):
    def __init__(self, char):
        self.__char = char
        
    def operation(self):
        print(self.__char * 20)
        

class ShowDecorator(Component):
    def __init__(self, component: Component):
        self._component = component

class ShowMessage(ShowDecorator):
    def __init__(self, component: Component, msg):
        super().__init__(component)
        self.__msg = msg
        
    def operation(self):
        self._component.operation() # Componentのメソッド
        print(self.__msg)   # ShowMessageクラスのメソッド
        self._component.operation()
        
class WriteDecorator(Component):
    def __init__(self, component: Component, file_name, msg):
        self._component = component
        self._file_name = file_name
        self._msg = msg
        

class WriteMessage(WriteDecorator):
    def operation(self):
        self._component.operation()
        with open(self._file_name, 'w') as fh:
            fh.write(self._msg)
            






show_component = ShowCharComponent('-')
# show_component.operation()

show_message = ShowMessage(show_component, 'Hello World')
# show_message.operation()
write_message = WriteMessage(show_message, 'tmp.txt', 'Write Message')
write_message.operation()