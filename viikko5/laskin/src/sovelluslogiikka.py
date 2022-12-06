class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos

class Summa:
        def __init__(self, sovelluslogiikka, lue_syote):
            self._sovelluslogiikka = sovelluslogiikka
            self._lue_syote = lue_syote

        def suorita(self):
            syote = int(self._lue_syote())
            self._sovelluslogiikka.tulos += syote

class Erotus:
        def __init__(self, sovelluslogiikka, lue_syote):
            self._sovelluslogiikka = sovelluslogiikka
            self._lue_syote = lue_syote

        def suorita(self):
            syote = int(self._lue_syote())
            self._sovelluslogiikka.tulos -= syote

class Nollaus:
        def __init__(self, sovelluslogiikka, lue_syote):
            self._sovelluslogiikka = sovelluslogiikka
            self._lue_syote = lue_syote

        def suorita(self):
            self._sovelluslogiikka.tulos = 0

class Kumoa:
        def __init__(self, sovelluslogiikka, lue_syote):
            pass

        def suorita(self):
            pass
