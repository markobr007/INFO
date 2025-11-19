class nekretnina:

    def __init__(self, adresa, kvadratura, bazna_cijena):
        self.adresa = adresa
        self.kvadratura = kvadratura
        self.bazna_cijena = bazna_cijena

    def izracunaj_cijenu(self):
        return self.bazna_cijena * self.kvadratura
    

    def ispisi_info(self):
        return f"Adresa: {self.adresa}, Kvadratura: {self.kvadratura}, Bazna Cijena: {self.bazna_cijena} EUR"

class stan(nekretnina):

    def __init__(self, adresa, kvadratura, bazna_cijena, kat, ima_lift):
        super().__init__(adresa, kvadratura, bazna_cijena)
        self.kat = kat
        self.ima_lift = ima_lift

    def izracunaj_cijenu(self):
        cijena = super().izracunaj_cijenu()
        if self.ima_lift:
            cijena *= 1.05
        elif self.kat > 2:
            cijena *= 0.9
        return cijena
        
    def ispisi_info(self):
        return f"Stan je na {self.kat} katu, Ima lift {self.ima_lift}, Adresa: {self.adresa}, Kvadratura: {self.kvadratura}, Bazna Cijena: {self.bazna_cijena} EUR"

class kuca(nekretnina):

    def __init__(self, adresa, kvadratura, bazna_cijena, povrsina_okucnice):
        super().__init__(adresa, kvadratura, bazna_cijena)
        self.povrsina_okucnice = povrsina_okucnice

    def izracunja_cijenu(self):
        cijena = super().izracunaj_cijenu()
        cijena = self.povrsina_okucoince * 100
        return cijena

    def ispisi_info(self):
        return f"Kuća sa površinom okućnice {self.povrsina_okucnice}m² - " + super().ispisi_info()
    
def ispisi_izbornik():
    print("Izbornik:")
    print("1. Unesi stan")
    print("2. Unesi kuću")
    print("3. Prikaže nekretnine")
    print("4. Prodaja nekretnine")
    print("5. Izlaz")

nekretnine = []
while True:
    ispisi_izbornik()
    try:
        izbor = input("Unesite izbor (0/1/2/3/4/5): ")
        if izbor == "1":
            adresa = input("Unesite adresu stana: ")
        while True:
            try:
            kvadratura = float(input("Unesite kvadraturu stana (m²): "))
            expect ValueError:
                print("Pogreška u unosu podataka")

        while True:
            try:
            bazna_cijena = float(input("Unesite baznu cijenu po m² (EUR): "))
            expect ValueError:
                print("Pogreška u unosu podataka")
        while True:
            try:
            kat = int(input("Unesite kat na kojem se stan nalazi: "))
            expect ValueError:
                print("Pogreška u unosu podataka")
            ima_lift = input("Ima li lift (da/ne): ").lower() == "da"
            novi_stan = stan(adresa, kvadratura, bazna_cijena, kat, ima_lift)
            nekretnine.append(novi_stan)
            print("Stan uspješno unesen.")
        elif izbor == "2":
            adresa = input("Unesite adresu kuće: ")
        while True:
            try:
            kvadratura = float(input("Unesite kvadraturu kuće (m²): "))
            expect ValueError:
                print("Pogreška u unosu podataka")
        while True:
            try:
            bazna_cijena = float(input("Unesite baznu cijenu po m² (EUR): "))
            expect ValueError:
                print("Pogreška u unosu podataka")
        while True:
            try:
            povrsina_okucnice = float(input("Unesite površinu okućnice (m²): "))
            expect ValueError:
                print("Pogreška u unosu podataka")
            nova_kuca = kuca(adresa, kvadratura, bazna_cijena, povrsina_okucnice)
            nekretnine.append(nova_kuca)
            print("Kuća uspješno unesena.")
        elif izbor == "3":
            for i in nekretnine:
                print(i.ispisi_info())
        
        elif izbor == 4:
            adresa = input("Unesite adresu nekretnine: ")
            for nekretnina in nekretnine:
                if nekretnina.adresa == adresa:
                    nekretnina.remove()
            
        else:
            print("Pogreška u unosu podataka")
            
    except ValueError:
        print("Pogreška u unosu podataka")