#abstraction:
from abc import ABC, abstractmethod
#here abc and abstractmethods are predefined methods
class Demo(ABC):
    @abstractmethod
    def ab1(self):
        pass
    @abstractmethod
    def ab2(self):
        pass
class Sub1(Demo):
    def ab1(self):
        print("hai")
    def ab2(self):
        print("hai")

obj=Sub1()
obj.ab1()
obj.ab2()
