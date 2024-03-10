class IMovimiento:
    def tipo_movimiento(self):
        pass

class velocidad_baja(IMovimiento):

    def tipo_movimiento(self):
        print("Se mueve 1 unidad")

class velocidad_media(IMovimiento):

    def tipo_movimiento(self):
        print("Se mueve 2 unidades")

class velocidad_alta(IMovimiento):

    def tipo_movimiento(self):
        print("Se mueve 3 unidades")


class IAtaque:
    def tipo_ataque(self):
        pass
   
class espada_ligera(IAtaque):
    def tipo_ataque(self):
        print("Atacando rapido")

class espada_pesada(IAtaque):
    def tipo_ataque(self):
        print("Atacando lento pero eficaz")

class arco(IAtaque):
    def tipo_ataque(self):
        print("Atacando a distancia")

class Campeon:

    def __init__(self,ataque:IAtaque,movimiento:IMovimiento):
        self.ataque = ataque
        self.movimiento = movimiento
    
    def perform_ataque(self):
        self.ataque.tipo_ataque()

    def perform_movimiento(self):
        self.movimiento.tipo_movimiento()

    def discurso(self):
        print("Por demacia")

class Garen_caballero(Campeon):
    def __init__(self):
        super().__init__(espada_pesada(),velocidad_media())
        
    def discurso(self):
        print("Garen reportandose, POOOOR DEMACIAA")

    

class Fiora_soldado(Campeon):
    def __init__(self):
        super().__init__(espada_ligera(),velocidad_alta())


    def discurso(self):
        print("Fiora reportandose, Porrgg demaciaa")

class Vayne_arquera(Campeon):
    def __init__(self):
        super().__init__(arco(),velocidad_media())
  

    def discurso(self):
        print("Vayne reportandose, entre las sombras")  

class Aatrox_caballero(Campeon):
    def __init__(self):
        super().__init__(espada_pesada(),velocidad_baja())
    

    def discurso(self):
        print("Soy el destructor de mundos")      
    

if "__main__" == __name__:

    garen1 = Garen_caballero()
    garen1.discurso()
    garen1.perform_ataque()
    garen1.perform_movimiento()
    print("\n")
    fiora1 = Fiora_soldado()
    fiora1.discurso()
    fiora1.perform_ataque()
    fiora1.perform_movimiento()
    print("\n")
    vayne1 = Vayne_arquera()
    vayne1.discurso()
    vayne1.perform_ataque()
    vayne1.perform_movimiento()
    print("\n")
    aatrox1= Aatrox_caballero()
    aatrox1.discurso()
    aatrox1.perform_ataque()
    aatrox1.perform_movimiento()
