from abc import ABC, abstractmethod

class MyAbsClass(ABC):
    @abstractmethod
    def coat(self):
        pass

    @abstractmethod
    def costume(self):
        pass

class Clothes(MyAbsClass):
    def coat(self, v):
        coat_expense = float(v/6.5 + 0.5)
        return coat_expense


    def costume(self, h):
        costume_expense = float(2*h + 0.3)
        return costume_expense

    @property
    def my_expenses(self):
        my_exp = float(self.coat(2) + self.costume(3))
        return my_exp

my_class = Clothes()
print(my_class.coat(2))
print(my_class.coat(3))
print(my_class.my_expenses)
