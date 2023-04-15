from hero.project.hero import Hero

import unittest


class TestHero(unittest.TestCase):

    def setUp(self) -> None:
        self.hero = Hero('Iron Man', 2, 100.0, 10.0)

    def test_initialization(self):
        self.assertEqual(self.hero.username, 'Iron Man')
        self.assertEqual(self.hero.level, 2)
        self.assertEqual(self.hero.health, 100.0)
        self.assertEqual(self.hero.damage, 10.0)

    def test_battle_fight_yourself(self):
        enemy_hero = Hero('Iron Man', 20, 100.0, 0.0)
        with self.assertRaises(Exception) as context:
            self.hero.battle(enemy_hero)
        self.assertEqual(str(context.exception), "You cannot fight yourself")

    def test_battle_no_health(self):
        enemy_hero = Hero('Tanos', 20, 100.0, 0.0)
        self.hero.health = 0
        with self.assertRaises(Exception) as context:
            self.hero.battle(enemy_hero)
        self.assertEqual(str(context.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_battle_negative_health(self):
        enemy_hero = Hero('Tanos', 20, 100.0, 0.0)
        self.hero.health = -10.0
        with self.assertRaises(Exception) as context:
            self.hero.battle(enemy_hero)
        self.assertEqual(str(context.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_battle_no_enemy_health(self):
        enemy_hero = Hero('Tanos', 20, 0.0, 100.0)
        with self.assertRaises(Exception) as context:
            self.hero.battle(enemy_hero)
        self.assertEqual(str(context.exception), "You cannot fight Tanos. He needs to rest")

    def test_battle_negative_enemy_health(self):
        enemy_hero = Hero('Tanos', 20, -10.0, 100.0)
        with self.assertRaises(Exception) as context:
            self.hero.battle(enemy_hero)
        self.assertEqual(str(context.exception), "You cannot fight Tanos. He needs to rest")

    def test_battle_decrease_health(self):
        enemy_hero = Hero('Tanos', 1, 90.0, 10.0)
        self.hero.battle(enemy_hero)
        self.assertEqual(self.hero.health, 90)

    def test_battle_draw(self):
        enemy_hero = Hero('Tanos', 10, 90.0, 10.0)
        self.hero.level = 10
        self.assertEqual(self.hero.battle(enemy_hero), "Draw")

    def test_battle_win(self):
        enemy_hero = Hero('Tanos', 1, 90.0, 10.0)
        self.hero.level = 10
        self.assertEqual(self.hero.battle(enemy_hero), "You win")

    def test_battle_lose(self):
        enemy_hero = Hero('Tanos', 1, 90.0, 10.0)
        self.assertEqual(self.hero.battle(enemy_hero), "You lose")

    def test_attributes_after_battle_wining(self):
        enemy_hero = Hero('Tanos', 1, 90.0, 10.0)
        self.hero.level = 10
        self.hero.battle(enemy_hero)
        self.assertEqual(self.hero.level, 11)
        self.assertEqual(self.hero.health, 95.0)
        self.assertEqual(self.hero.damage, 15.0)

    def test_enemy_attributes_after_battle_wining(self):
        enemy_hero = Hero('Tanos', 1, 90.0, 10.0)
        self.hero.battle(enemy_hero)
        self.assertEqual(enemy_hero.level, 2)
        self.assertEqual(enemy_hero.health, 75.0)
        self.assertEqual(enemy_hero.damage, 15.0)

    def test_print_info(self):
        self.assertEqual(str(self.hero), f"Hero Iron Man: 2 lvl\n" +
                         f"Health: 100.0\n" +
                         f"Damage: 10.0\n")


if __name__ == '__main__':
    unittest.main()
