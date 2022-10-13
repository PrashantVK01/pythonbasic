#abc is package,import abstract class ABC,and method 
from abc import ABC,abstractmethod

class AbstractDemo(ABC):
 #abstract method
   @abstractmethod
   def absFunc(self):
        None
#inherited and implemented abstract
class ConcreteClass(AbstractDemo):
    def absFunc(self):
       print("this is abstract function")

obj = ConcreteClass()
obj.absFunc()

