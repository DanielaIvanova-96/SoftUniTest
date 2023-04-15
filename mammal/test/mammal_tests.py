from mammal.project.mammal_class import Mammal
import unittest


class TestMammal(unittest.TestCase):

    def setUp(self) -> None:
        self.mammal = Mammal('Marcel', 'cat', 'mew')

    def test_initialization(self):
        self.assertEqual(self.mammal.name, 'Marcel')
        self.assertEqual(self.mammal.type, 'cat')
        self.assertEqual(self.mammal.sound, 'mew')

    def test_make_sound(self):
        self.assertEqual(self.mammal.make_sound(), f"Marcel makes mew")

    def test_get_kingdom(self):
        self.assertEqual(self.mammal.get_kingdom(), "animals")

    def test_get_info(self):
        result = self.mammal.info()
        self.assertEqual(result, f"Marcel is of type cat")


if __name__ == '__main__':
    unittest.main()
