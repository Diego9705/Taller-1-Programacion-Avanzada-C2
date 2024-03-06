class IAtaque:
    def tipo_ataque(self):
        pass
    def movimiento(self):
        pass

class espada_ligera(IAtaque):
    def tipo_ataque(self):
        print("Atacando rapido")
    
    def movimiento(self):
        print("Se mueve 3 unidades")

class espada_pesada(IAtaque):
    def tipo_ataque(self):
        print("Atacando lento pero eficaz")

    def movimiento(self):
        print("Se mueve 1 unidad")

class arco(IAtaque):
    def tipo_ataque(self):
        print("Atacando a distancia")

    def movimiento(self):
        print("Se mueve 2 unidades")


class Campeon:

    def __init__(self,ataque:IAtaque):
        self.ataque = ataque
    
    def perform_ataque(self):
        self.ataque.tipo_ataque()

    def perform_movimiento(self):
        self.ataque.movimiento()

    def discurso(self):
        print("Por demacia")

class Garen_caballero(Campeon):
    def __init__(self):
        super().__init__(espada_pesada())

    def discurso(self):
        print("POOR DEMACIAA")

    

class Fiora_soldado(Campeon):
    def __init__(self):
        super().__init__(espada_ligera())

    def discurso(self):
        print("Porrgg demaciaa")

class Vayne_arquera(Campeon):
    def __init__(self):
        super().__init__(arco())

    def discurso(self):
        print("Entre las sombras")       
    

if "__main__" == __name__:

    garen1 = Garen_caballero()
    garen1.perform_ataque()
    garen1.perform_movimiento()

    fiora1 = Fiora_soldado()
    fiora1.perform_ataque()
    fiora1.perform_movimiento()

    vayne1 = Vayne_arquera()
    vayne1.perform_ataque()
    vayne1.perform_movimiento()