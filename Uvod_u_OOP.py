class Ucenik:
    def __init__(self, ime, prezime, razred):
        self.ime = ime
        self.prezime = prezime
        self.razred = razred
        self.ocjene = []
        
    def dodaj_ocjenu(self, ocjena):
        if isinstance(ocjena, int) and 1<= ocjena <=5:
            self.ocjene.append(ocjena)
            print(f"INFO: Učeniku {self.ime} {self.prezime} je upisana ocjena {ocjena}.")
        else:
            print(f"GREŠKA: Ocjena '{ocjena}' nije važeća. Molimo unesite broj od 1 do 5.")
    def izracunaj_prosjek(self):
        if not self.ocjene:
            return 0.0
        else:
            return sum(self.ocjene) / len(self.ocjene)
            
    def info(self):
        print("-" * 30)
        print(f"Ime i prezime: {self.ime} {self.prezime}")
        print(f"Razred: {self.razred}")
        if self.ocjene:
            print(f"Ocjene: {self.ocjene}")
        else:
            print("Ocjene: (nema upisanih ocjena)")
        prosjek = self.izracunaj_proskek()
        print(f"Prosjek ocjena: {prosjek:.2f}")
        print("-" * 30)

ucenik1 = Ucenik("Andrej", "Korelić", "4.c")
ucenik2 = Ucenik("Mak", "Đokić", "4.b")
ucenik3 = Ucenik("Dominik", "Mikohanović", "4.c")

ucenik1.dodaj_ocjenu(5)
ucenik1.dodaj_ocjenu(5)
ucenik1.dodaj_ocjenu(5)
ucenik1.dodaj_ocjenu(4)

ucenik2.dodaj_ocjenu(1)
ucenik2.dodaj_ocjenu(1)
ucenik2.dodaj_ocjenu(5)
ucenik2.dodaj_ocjenu(5)

ucenik3.dodaj_ocjenu(1)
ucenik3.dodaj_ocjenu(2)
ucenik3.dodaj_ocjenu(1)
ucenik3.dodaj_ocjenu(3)

ucenik1.info()
ucenik2.info()
ucenik3.info()