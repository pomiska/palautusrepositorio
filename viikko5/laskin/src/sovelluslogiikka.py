class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.edellinen_tulos = tulos


class Summa:
    def __init__(self, sovelluslogiikka, lue_syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._lue_syote = lue_syote

    def suorita(self):
        self._sovelluslogiikka.edellinen_tulos = self._sovelluslogiikka.tulos
        syote = int(self._lue_syote())
        self._sovelluslogiikka.tulos += syote

    def kumoa(self):
        self._sovelluslogiikka.tulos = self._sovelluslogiikka.edellinen_tulos


class Erotus:
    def __init__(self, sovelluslogiikka, lue_syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._lue_syote = lue_syote

    def suorita(self):
        self._sovelluslogiikka.edellinen_tulos = self._sovelluslogiikka.tulos
        syote = int(self._lue_syote())
        self._sovelluslogiikka.tulos -= syote

    def kumoa(self):
        self._sovelluslogiikka.tulos = self._sovelluslogiikka.edellinen_tulos


class Nollaus:
    def __init__(self, sovelluslogiikka, lue_syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._lue_syote = lue_syote

    def suorita(self):
        self._sovelluslogiikka.edellinen_tulos = self._sovelluslogiikka.tulos
        self._sovelluslogiikka.tulos = 0

    def kumoa(self):
        self._sovelluslogiikka.tulos = self._sovelluslogiikka.edellinen_tulos


class Kumoa:
    def __init__(self, sovelluslogiikka, lue_edellinen_komento):
        self._sovelluslogiikka = sovelluslogiikka
        self._lue_edellinen_komento = lue_edellinen_komento

    def suorita(self):
        self._lue_edellinen_komento().kumoa()
