class Carro:

    def __init__(self):
        self.Conbustivel = 0
        self.Quilometragem = 0
        self.Passageiros = 0

    def getPassageiros(self):
        return self.Passageiros

    def getCombustivel(self):
        return self.Conbustivel

    def getQuilometragem(self):
        return self.Quilometragem

    def embarcar(self):
        if self.Passageiros < 2:
            self.Passageiros += 1
            return True
        return False

    def desembarcar(self):
        if self.Passageiros > 0:
            self.Passageiros -= 1
            return True
        return False

    def dirigir(self, distancia):
        dist = distancia
        percorido = 0
        if self.Passageiros > 0 and self.Conbustivel > 0:
            while self.Conbustivel > 0 and dist > 0:
                self.Conbustivel -= 1
                dist -= 1
                percorido += 1
                self.Quilometragem += 1
            if dist == 0:
                print(f"Foi percorrido {percorido}Km")
                return True
            elif self.Conbustivel == 0:
                print(f"Foi percorrido {percorido}Km")
                return False
        else:
            return False

    def abastecer(self, quantidade):
        quant = quantidade
        if quantidade > 0:
            while quant > 0:
                if self.Conbustivel < 100:
                    self.Conbustivel += 1
                quant -= 1
            return True
        else:
            return False