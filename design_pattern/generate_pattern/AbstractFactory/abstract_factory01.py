"""
Abstract Factory

                    AbstractFactory   ←        ←       ←       ←
       ↓                 ↓                ↓                       ↑
AbstractProduct3  AbstractProduct2   AbstractProduct1
       ↑                 ↑                ↑                       ↑
ConcreteProduct3  ConcreteProduct2   ConcreteProduct1
       ↑                 ↑                ↑                       ↑
                    ConcreteFactory   →        →       →       →

AbstractFactory
・IFもしくは抽象クラス
・抽象的な部品であるAbstractProductを生成するためのAPIを定義

AbstractProduct
・IFもしくは抽象クラス
・部品ごとのAPIを定義

ConcreteFactory
・AbstractFactoryを継承する子クラス

ConcreteProduct
・ConcreteFactoryから返される具体的な部品
"""
from abc import ABCMeta, abstractmethod

# AbstractProduct1
class Button(metaclass=ABCMeta):
    @abstractmethod
    def press(self):
        pass
    
# AbstractProduct2
class Checkbox(metaclass=ABCMeta):
    @abstractmethod
    def switch(self):
        pass

# AbstractFactory
class GUIFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_button(self) -> Button:
        pass
    
    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

# ConcreteProduct1
class WindowsButton(Button):
    def press(self):
        print('Windowsのボタンが押されました。')

# ConcreteProduct2
class WindowsCheckbox(Checkbox):
    def switch(self):
        print('Windowsのチェックボックスが切り替えられました。')

# ConcreteFactory1
class WindowsGUIFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()
    
# ConcreteProduct3
class MacButton(Button):
    def press(self):
        print('Macのボタンが押されました。')

# ConcreteProduct4
class MacCheckbox(Checkbox):
    def switch(self):
        print('Macのチェックボックスが切り替えられました。')

# ConcreteFactory2
class MacGUIFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()
    
def run(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    button.press()
    checkbox.switch()
    
    
if __name__ == '__main__':
    run(WindowsGUIFactory())
    run(MacGUIFactory())