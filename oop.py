class Factory:
    def __init__(self, Bt, Et, Tyres):
        self.Bt = Bt
        self.Et = Et
        self.Tyres = Tyres

    def showdets(self):
        print("Body Type: ", self.Bt)
        print("Engine Type: ", self.Et)
        print("Tyres: ", self.Tyres)


class Honda(Factory):
    def __init__(self, Bt, Et, Tyres, glass):
        super().__init__(Bt, Et, Tyres)
        self.glass = glass

    def showdets(self):
        super().showdets()
        print("glass type", self.glass)


farari = Factory("covered", "2 cycles", 4)
alto = Factory("not covered", "1 cycle", 2)
supara = Honda("covered", "1 cycle", 2, "glass")
farari.showdets()
alto.showdets()
supara.showdets()
