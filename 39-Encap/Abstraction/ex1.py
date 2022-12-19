# An abstract class can be considered as a blueprint for other classes.
# It allows you to create a set of methods that must be created within any child classes built from the abstract class.
# A class which contains one or more abstract methods is called an abstract class.
# An abstract method is a method that has a declaration but does not have an implementation.
# While we are designing large functional units we use an abstract class.
# When we want to provide a common interface for different implementations of a component, we use an abstract class


from abc import ABC, abstractmethod
class Mobile(ABC):
    @abstractmethod
    def Mehtod1(self):
       pass


ob=Mobile()
ob.Mehtod1()
# TypeError: Can't instantiate abstract class Mobile with abstract method Mehtod1