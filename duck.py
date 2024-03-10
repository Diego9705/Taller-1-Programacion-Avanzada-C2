#Interface
class IFlyBehavior():
    def fly():
        pass

class FlyWithWings(IFlyBehavior):
    def fly():
        print("Tengo alas y vuelo")

class FlyNoWay(IFlyBehavior):
    def fly():
        print("No puedo volar")

class Duck:
    def __init__(self,fly_behavior: IFlyBehavior):
        self._fly_behavior = fly_behavior
    
    def perform_Fly(self):
        self._fly_behavior.fly()

    def swim(self):
        print("Nado")

    def quack(self):
        print("Quack")

    def display(self):
        print("Soy un pato")



class MallarDuck(Duck):

    def __init__(self):
        super().__init__(FlyWithWings())

    def display(self):
        print("Soy un pato MallarDuck")
    
class RedHeadDuck(Duck):

    def __init__(self):
        super().__init__(FlyWithWings())

    def display(self):
        print("Soy un pato RedHeadDuck")

class RubberDuck(Duck):
    def __init__(self):
        super().__init__(FlyNoWay())

    def display(self):
        print("Soy un pato de goma")


