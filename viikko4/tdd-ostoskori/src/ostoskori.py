from tuote import Tuote
from ostos import Ostos


class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self.yhteishinta = 0
        self.ostokset_list = []

    def tavaroita_korissa(self):
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2
        summa = 0
        for obj in self.ostokset_list:
            summa += obj.lukumaara()
        return summa

    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan
        return self.yhteishinta

    def lisaa_tuote(self, lisattava: Tuote):
        ostos_listalla = False
        for i, obj in enumerate(self.ostokset_list):
            if obj.tuotteen_nimi() == lisattava.nimi():
                ostos_listalla = True
                self.ostokset_list[i].muuta_lukumaaraa(1)
        if (not ostos_listalla):
            self.ostokset_list.append(Ostos(lisattava))
        self.yhteishinta += lisattava.hinta()

    def poista_tuote(self, poistettava: Tuote):
        for i, obj in enumerate(self.ostokset_list):
            if obj.tuotteen_nimi() == poistettava.nimi():
                self.ostokset_list[i].muuta_lukumaaraa(-1)
                self.yhteishinta -= poistettava.hinta()
                if self.ostokset_list[i].lukumaara() == 0:
                    del self.ostokset_list[i]

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
        return self.ostokset_list
