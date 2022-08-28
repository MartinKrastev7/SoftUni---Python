from project.pet_shop import PetShop
from unittest import TestCase, main


class PetShopTests(TestCase):
    def setUp(self) -> None:
        self.shop = PetShop("kiko")

    def test_init_correct(self):
        self.assertEqual("kiko", self.shop.name)
        self.assertEqual({}, self.shop.food)
        self.assertEqual([], self.shop.pets)

    def test_add_food_qty_less_than_0_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.shop.add_food("mik", -1)

        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))

    def test_add_food_if_name_not_in_food(self):
        self.shop.add_food("mik", 2)
        expected = {"mik": 2}
        actual = self.shop.food

        self.assertEqual(expected, actual)


    def test_add_food_name_in_increase_food_qty(self):
        self.shop.add_food("mik", 2)
        self.shop.add_food("mik", 5)
        expected = {"mik": 7}
        actual = self.shop.food

        self.assertEqual(expected, actual)

    def test_add_food_returns_correct(self):
        expected = f"Successfully added 2.00 grams of mik."
        actual = self.shop.add_food("mik", 2)

        self.assertEqual(expected, actual)

    def test_add_pet_not_in_pets(self):
        self.shop.add_pet("kiko")
        expected = ["kiko"]
        actual = self.shop.pets

        self.assertEqual(expected, actual)

    def test_add_pet_success_returns(self):
        expected = f"Successfully added kiko."
        actual = self.shop.add_pet("kiko")

        self.assertEqual(expected, actual)

    def test_add_pet_already_in_pets_raises(self):
        self.shop.add_pet("kiko")
        with self.assertRaises(Exception) as ex:
            self.shop.add_pet("kiko")

        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_feed_pet_name_not_in_pets_raises(self):
        self.shop.add_food("kik", 2)
        with self.assertRaises(Exception) as ex:
            self.shop.feed_pet("kik", "kiko")

        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_food_name_not_in_foods(self):
        self.shop.add_pet("kiko")
        expected = f'You do not have kik'
        actual = self.shop.feed_pet("kik", "kiko")

        self.assertEqual(expected, actual)

    def test_feed_pet_food_below_100_increases_food(self):
        self.shop.add_food("kik", 50)
        self.shop.add_pet("kiko")
        self.shop.feed_pet("kik", "kiko")

        expected = {"kik": 1050.00}
        actual = self.shop.food

        self.assertEqual(expected, actual)

    def test_feed_pet_food_below_100_returning_correct(self):
        self.shop.add_food("kik", 50)
        self.shop.add_pet("kiko")

        expected = "Adding food..."
        actual = self.shop.feed_pet("kik", "kiko")

        self.assertEqual(expected, actual)

    def test_feed_pet_correct_decrease_food_qty_with_100(self):
        self.shop.add_food("kik", 150)
        self.shop.add_pet("kiko")
        self.shop.feed_pet("kik", "kiko")

        expected = {"kik": 50}
        actual = self.shop.food

        self.assertEqual(expected, actual)

    def test_feed_pet_correct_returns(self):
        self.shop.add_food("kik", 150)
        self.shop.add_pet("kiko")

        expected = f"kiko was successfully fed"
        actual = self.shop.feed_pet("kik", "kiko")

        self.assertEqual(expected, actual)

    def test_repr_returns_correct(self):
        self.shop.add_pet("kikko")
        self.shop.add_pet("kio")

        expected = f'Shop kiko:\n'
        expected += f'Pets: kikko, kio'
        actual = repr(self.shop)

        self.assertEqual(expected, actual)




if __name__ == "__main__":
    main()