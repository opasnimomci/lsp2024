class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.rezlista = []

    def saberi(self):
        rez = self.a + self.b
        self.rezlista.append(f'Sabiranje: {self.a} + {self.b} = {rez}')
        return rez

    def oduzmi(self):
        rez = self.a - self.b
        self.rezlista.append(f'Oduzimanje: {self.a} - {self.b} = {rez}')
        return rez

    def pomnozi(self):
        rez = self.a * self.b
        self.rezlista.append(f'Množenje: {self.a} * {self.b} = {rez}')
        return rez

    def podeli(self):
        if self.b == 0:
            raise ValueError("Deljenje nulom nije dozvoljeno.")
        rez = self.a / self.b
        self.rezlista.append(f'Deljenje: {self.a} / {self.b} = {rez}')
        return rez

    def gcd(self):
        x = self.a
        y = self.b
        while y != 0:
            (x, y) = (y, x % y)
        self.rezlista.append(f'Najveći zajednički delilac ({self.a}, {self.b}): {x}')
        return x
calc = Kalkulator(24, 8)
print("Rezultati aritmetičkih operacija:")
print("Sabiranje:", calc.saberi())
print("Oduzimanje:", calc.oduzmi())
print("Množenje:", calc.pomnozi())
print("Deljenje:", calc.podeli())
print("Najveći zajednički delilac:", calc.gcd())
print("\nSvi rezultati:")
for rez in calc.rezlista:
    print(rez)
