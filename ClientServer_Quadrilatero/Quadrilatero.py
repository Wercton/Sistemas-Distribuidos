class Quadrilatero:
    
    lado1, lado2, lado3, lado4 = 0, 0, 0, 0
    tipoQuadrilatero = ""
    
    def le_dados(self, lado1, lado2, lado3, lado4):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.lado4 = lado4
        
    def indica_tipo_quadrilatero(self):
        if self.lado1 == 0:
            self.tipoQuadrilatero = "Inválido"
        elif self.lado1 == self.lado2 and self.lado2 == self.lado3 and self.lado3 == self.lado4:
            self.tipoQuadrilatero = "Quadrado"
        elif self.lado1 == self.lado3 and self.lado2 == self.lado4:
            self.tipoQuadrilatero = "Retangulo"
        else:
            self.tipoQuadrilatero = "Losangulo"

        return self.tipoQuadrilatero
    
    def mostra_dados(self):
        print("\nQuadrilatero do tipo:" + self.tipoQuadrilatero)
        print("Dimensões:", self.lado1, "x", self.lado2, "x", self.lado3, "x", self.lado4, end="\n")

        