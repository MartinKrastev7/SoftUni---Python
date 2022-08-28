from unittest import TestCase, main

from project.factory.paint_factory import PaintFactory


class PaintFactoryTests(TestCase):
    def setUp(self) -> None:
        self.fac = PaintFactory("Bau", 10)

    def test_init_correct(self):
        self.assertEqual("Bau", self.fac.name)
        self.assertEqual(10, self.fac.capacity)
        self.assertEqual({}, self.fac.ingredients)

    def test_valid_ingredients(self):
        expected = ["white", "yellow", "blue", "green", "red"]
        actual = self.fac.valid_ingredients

        self.assertEqual(expected, actual)

    def test_add_ingredient_not_in_valid_ingredients_raises(self):
        with self.assertRaises(TypeError) as ex:
            self.fac.add_ingredient("black", 5)

        self.assertEqual(f"Ingredient of type black not allowed in PaintFactory", str(ex.exception))

    def test_add_ingredient_not_enough_space_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.fac.add_ingredient("white", 20)

        self.assertEqual("Not enough space in factory", str(ex.exception))

    def test_add_ingredient_not_in_ingredients_success(self):
        self.fac.add_ingredient("white", 5)
        expected = {"white": 5}
        actual = self.fac.ingredients

        self.assertEqual(expected, actual)

    def test_add_ingredient_already_in_ingredients_increase_value(self):
        self.fac.add_ingredient("white", 2)
        self.fac.add_ingredient("white", 4)

        expected = {"white": 6}
        actual = self.fac.ingredients

        self.assertEqual(expected, actual)

    def test_can_add_value(self):
        self.fac.ingredients = {"white": 5, "black": 3}
        self.assertTrue(self.fac.can_add(1))
        self.assertFalse(self.fac.can_add(3))

    def test_repr_returns_correct(self):
        self.fac.ingredients = {"white": 5, "black": 3}
        expected = f"Factory name: Bau with capacity 10.\n"
        expected += f"white: 5\n"
        expected += f"black: 3\n"
        actual = repr(self.fac)
        self.assertEqual(expected, actual)

    def test_remove_ingredient_not_in_ingredients_raises(self):
        with self.assertRaises(KeyError) as context:
            self.fac.remove_ingredient("white", 5)

        self.assertEqual("'No such ingredient in the factory'", str(context.exception))

    def test_remove_ingredient_in_ingredients_result_below_0(self):
        self.fac.add_ingredient("white", 5)
        with self.assertRaises(ValueError) as ex:
            self.fac.remove_ingredient("white", 6)

        self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))

    def test_remove_ingredient_success(self):
        self.fac.add_ingredient("white", 5)
        self.fac.remove_ingredient("white", 3)
        expected = {"white": 2}
        actual = self.fac.ingredients

        self.assertEqual(expected, actual)

    def test_product_returns_correct(self):
        self.fac.add_ingredient("white", 5)
        expected = {"white": 5}
        actual = self.fac.products

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    main()