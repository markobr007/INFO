class Recept():
    def __init__(self, naziv, tezina_pripreme, sastojci, opis_pripreme):
        self.naziv = naziv
        self.tezina_pripreme = tezina_pripreme
        self.sastojci = sastojci
        self.opis_pripreme = opis_pripreme

    def __str__(self):
        return f"{self.naziv} ({self.tezina_pripreme})\nSastojci: {', '.join(self.sastojci)}\nPriprema: {self.opis_pripreme}"

class Kuharica():
    def __init__(self):
        self.recepti = []

    def dodaj_recept(self, recept):
        self.recepti.append(recept)

    def prikazi_recepte(self):
        for recept in self.recepti:
            print(recept)
            print("-" * 40)

Moja_kuharica = Kuharica()
recept1 = Recept("Punjene paprike", "Srednja", ["paprike", "riža", "mljeveno meso", "voda"], "Napunite paprike smjesom riže i mljevenog mesa. Stavite ih kuhati u vodu sa pasiranom rajčicom".")
recept2 = Recept("Palačinke", "Laka", ["brašno", "jaja", "mlijeko", "šećer"], "Pomiješajte sastojke i ispecite palačinke na tavi.")
Moja_kuharica.dodaj_recept(recept1)
Moja_kuharica.dodaj_recept(recept2)

Moja_kuharica.prikazi_recepte()
def pronadji_recept_po_nazivu(self, naziv):
    for recept in self.recepti:
        if recept.naziv.lower() == naziv.lower():
            return recept
    return None