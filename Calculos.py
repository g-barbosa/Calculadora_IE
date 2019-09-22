import math

class Calculos:
    def __init__(self, comodo, largura, comprimento):
        self.comodo = comodo.upper()
        self.largura = largura
        self.comprimento = comprimento
        self.area = 0
        self.perimetro = 0
        self.qntTom = 0
        self.pot = 0

    def calculo_area(self):
        self.area = float(self.largura) * float(self.comprimento)
        return self.area

    def calculo_perimetro(self):
        self.perimetro = (float(self.largura)*2)+(float(self.comprimento)*2)
        return self.perimetro

    def potmin_lamp(self):
        area = self.calculo_area()
        if (area <= 6):
            self.pot = 100

        else:
            area -= 6
            self.pot = 100

            while (area >= 6):
                area -= 4
                self.pot += 60
            return self.pot
        return self.pot

    def qntmin_tom(self):
        area = self.calculo_area()
        perimetro = self.calculo_perimetro()
        if(self.comodo == "COZINHA") or (self.comodo == "COPA") or (self.comodo == "AREA DE SERVIÇO"):
            self.qntTom = (perimetro/3.5)+1

        elif (area > 6):
            self.qntTom = (perimetro/5)+1

        else:
            self.qntTom = 1

        return math.floor(self.qntTom)
