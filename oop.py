from abc import ABC, abstractmethod


class Factory:
    def __init__(self, Bt, Et, Tyres):
        self.Bt = Bt
        self.Et = Et
        self.Tyres = Tyres

    def showdets(self):
        print("Body Type: ", self.Bt)
        print("Engine Type: ", self.Et)
        print("Tyres: ", self.Tyres)


class Factory2:
    def __init__(self, meterial):
        self.meterial = meterial


class Honda(Factory, Factory2):
    def __init__(self, Bt, Et, Tyres, glass, meterial):
        super().__init__(Bt, Et, Tyres)
        self.glass = glass
        self.meterial = meterial

    def showdets(self):
        super().showdets()
        print("glass type", self.glass)
        print("meterial type", self.meterial)


farari = Factory("covered", "2 cycles", 4)
alto = Factory("not covered", "1 cycle", 2)
supara = Honda("covered", "1 cycle", 2, "glass", "iron")
farari.showdets()
alto.showdets()
supara.showdets()


class Shape(ABC):
    @abstractmethod
    def area():
        pass

    @abstractmethod
    def perimeter():
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area():
        pass

    def perimeter():
        pass


cir1 = Circle(12)
print(cir1.radius)
