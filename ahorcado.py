import random

class Game:
    def __init__(self,palabras):
        self.palabra = palabras
        self.nuevojuego()

    def mostrarpalabra(self, descubrir):
        self.descubrir = descubrir
        self.boolean = False
        while self.boolean != True:
            self.palabra_incognita = []
            for each in self.descubrir:
                valrandom = random.randint(0,9)
                if valrandom in [0,1,2,3] :
                    self.palabra_incognita.append(each)
                else:
                    self.palabra_incognita.append("_") 

            if "".join(self.palabra_incognita) == self.descubrir:
                self.boolean = False
            else:
                self.boolean = True
            
            
        print( "la palabra a descubrir es: "+ " ".join(self.palabra_incognita)) 
        
    def nuevojuego(self):
        print("Bienvenido al ahorcado de Python")
        self.x = input("seleccione un numero: ")
        self.vidas = 6
        self.palabra = palabras[int(self.x)]
        self.mostrarpalabra(self.palabra)
        while self.boolean != False: 
            self.listaca = []
            self.letter = input("Ingresa una palabra: \n")
            if len(self.letter) > 1:
                print("Solo puede agregar una letra")
                self.boolean = True
                continue
            else:
                if self.letter in self.palabra:
                    print("Has pegado en la palabra")
                    for index, lol in enumerate(self.palabra):
                        if lol == self.letter:
                            self.listaca.append(index)
                
                    for rango in self.listaca:
                        self.palabra_incognita[rango] = self.letter
                    print(self.palabra_incognita)

                    if "".join(self.palabra_incognita) == self.palabra:
                        self.boolean = False
                else:
                    self.vidas -= 1
                    print(f"Te has equivocado!. Te quedan {self.vidas} intentos")
                    if self.vidas == 0:
                        print("Has perdido! :( ")
                        break
        if self.vidas == 0:
            pass           
        else:
            print("Has ganado!")

palabras = ["padre", "madre", "hermano", "hijo", "sobrino"]

if __name__=="__main__":
    juego = Game(palabras)

    