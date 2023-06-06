class Telefon:
    def __init__(self, broj, pozivni_broj, proizvodac):
        self.__broj = broj
        self.__pozivni_broj = pozivni_broj
        self.__proizvodac = proizvodac
    @property
    def broj(self):
        return self.__broj
    @broj.setter
    def broj(self, broj):
        self.__broj = broj
    @property
    def pozivni_broj(self):
        return self.__pozivni_broj

    @pozivni_broj.setter
    def pozivni_broj(self, pozivni_broj):
        self.__pozivni_broj = pozivni_broj
    @property
    def proizvodac(self):
        return self.__proizvodac

    @proizvodac.setter
    def proizvodac(self, proizvodac):
        self.__proizvodac = proizvodac
    def ispis(self):
        print("Informacije o telefonu: ")
        print(f"\t Broj: {self.__broj}")
        print(f"\t Pozivni broj: {self.__pozivni_broj}")
        print(f"\t Proizvodac: {self.__proizvodac}")