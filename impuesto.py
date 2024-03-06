class Ieimpuesto:
    def impuesto(self):
        pass

class IVA1(Ieimpuesto):
    def impuesto(self):
        print("19%")

class IVA2(Ieimpuesto):
    def impuesto(self):
        print("32%")


class Pais:
    def __init__(self, timpuesto):
        self.timpuesto= timpuesto

    def perform_impuesto(self):
        self.timpuesto.impuesto()
    
    def nombre():
        print("Soy un pais")

class Europa(Pais):
    def __init__(self):
        super().__init__(IVA1())
    
    def nombre(self):
        print("Soy Europa")

class Estados_Unidos(Pais):
    def __init__(self):
        super().__init__(IVA2())
    
    def nombre(self):
        print("Soy USA")

if "__main__" == __name__:
    #Pais pais1 = Europa
    
    #iva = IVA1
    #iva.impuesto()

    espania = Europa()
    espania.perform_impuesto()
    espania.nombre()
    #iva = IVA1()
    #print(iva.impuesto)
    #espania=Europa(Pais)
    #espania.perform_impuesto()


