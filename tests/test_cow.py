import pytest
from farm.cow import Cow
from farm.animal import Animal

class TestCow:
    def test_is_animal_subclass(self):
        """İnek, Animal sınıfından türemiş mi?"""
        assert issubclass(Cow, Animal)

    def test_initial_energy(self):
        """İnek başlangıçta 0 enerjiye sahip mi?"""
        cow = Cow()
        assert cow.energy == 0

    def test_initial_milk(self):
        """İnek başlangıçta 0 süt üretmiş mi?"""
        cow = Cow()
        assert cow.milk == 0

    def test_talk(self):
        """İnek doğru sesi çıkarıyor mu?"""
        cow = Cow()
        assert cow.talk() == "moo"

    def test_feed_increases_energy(self):
        """Beslenince enerji 1 artıyor mu?"""
        cow = Cow()
        cow.feed()
        assert cow.energy == 1

    def test_feed_produces_milk(self):
        """Beslenince 2 litre süt üretiyor mu?"""
        cow = Cow()
        cow.feed()
        assert cow.milk == 2
        
        cow.feed()
        assert cow.milk == 4