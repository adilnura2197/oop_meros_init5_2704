class Kampyuter:
    def __init__(self, cpu):
        self.cpu = cpu

    def info(self):
        print(f"Cpu: {self.cpu}")


class Noutbuk(Kampyuter):
    def __init__(self, cpu, batareya):
        super().__init__(cpu)
        self.batareya = batareya

    def info(self):
        super().info()
        print(f"Batareya: {self.batareya}")


n = Noutbuk("i17", "5 soat")
n.info()


class Oyinchi:
    def __init__(self, ism):
        self.ism = ism

    def info(self):
        print(f"Ism: {self.ism}")


class ProOyinchi(Oyinchi):
    def __init__(self, ism, reyting):
        super().__init__(ism)
        self.reyting = reyting

    def info(self):
        super().info()
        print(f"Reyting: {self.reyting}")


p = ProOyinchi("Ali", 2500)
p.info()
