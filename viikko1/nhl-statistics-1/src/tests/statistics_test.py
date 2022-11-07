import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.stats = Statistics(
            PlayerReaderStub()
        )

    def test_haku_palauttaa_oikean(self):
        pelaaja = self.stats.search("Semenko")
        self.assertEqual(pelaaja.name, "Semenko")       

    def test_haku_palauttaa_none_jos_ei_loydy(self):
        self.assertEqual(str(self.stats.search("Litmanen")), "None")

    def test_tiimihaku_toimii(self):
        edmonton = self.stats.team("EDM")
        self.assertEqual(len(edmonton), 3)

    def test_sort_by_points(self):
        paras = self.stats.top(1)
        self.assertEqual(paras[0].name, "Gretzky")

    def test_top_haku_palauttaa_oikean_maaran(self):
        top_kolme = self.stats.top(3)
        self.assertEqual(len(top_kolme), 3)