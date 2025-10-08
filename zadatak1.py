class Knjiga:
    def __init__(self, naslov, autor, godina_izdanja):
        self.naslov = naslov
        self.autor = autor
        self.godina_izdanja = godina_izdanja

        print(self.naslov)
        print(self.autor)
        print(self.godina_izdanja)

knjiga1= Knjiga("Kiklop", "Ranko Marnković", "1965")
knjiga2= Knjiga("Gospoda Glembajevi", "Miroslav Krleža", "1929")

