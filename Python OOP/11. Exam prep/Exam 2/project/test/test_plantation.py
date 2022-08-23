from project.plantation import Plantation
from unittest import TestCase, main


class PlantationTests(TestCase):
    def setUp(self) -> None:
        self.plant = Plantation(3)

    def test_init_correct(self):
        self.assertEqual(3, self.plant.size)
        self.assertEqual({}, self.plant.plants)
        self.assertEqual([], self.plant.workers)

    def test_size_below_zero_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.plant_zero = Plantation(-50)

        self.assertEqual("Size must be positive number!", str(ex.exception))

    def test_size_value_is_zero(self):
        self.plant_zero_0 = Plantation(0)
        self.assertEqual(0, self.plant_zero_0.size)

    def test_property_size_returns(self):
        self.assertEqual(3, self.plant.size)

    def test_hire_worker_already_in_workers_raises(self):
        self.plant.workers.append("Mike")

        with self.assertRaises(ValueError) as ex:
            self.plant.hire_worker("Mike")

        self.assertEqual("Worker already hired!", str(ex.exception))

    def test_hire_worker_success(self):
       # self.plant.hire_worker("Mike")
        expected = f"Mike successfully hired."
        actual = self.plant.hire_worker("Mike")

        self.assertEqual(expected, actual)

    def test__len__returns_correct(self):
        self.plant.hire_worker("Mike")
        self.plant.planting("Mike", "tree")
        self.plant.planting("Mike", "tree1")
        expected = 2
        actual = len(self.plant)

        self.assertEqual(expected, actual)

    def test__len_no_plants_returns_zero(self):
        expected = 0
        actual = len(self.plant)

        self.assertEqual(expected, actual)

    def test_planting_worker_not_in_workers_raises(self):
        self.plant.hire_worker("Mike")

        with self.assertRaises(ValueError) as ex:
            self.plant.planting("Dave", "Tree")

        self.assertEqual("Worker with name Dave is not hired!", str(ex.exception))

    def test_planting_plantation_is_full_raises(self):
        self.plant.hire_worker("Mike")
        with self.assertRaises(ValueError) as ex:
            self.plant.planting("Mike", "tree")
            self.plant.planting("Mike", "tree1")
            self.plant.planting("Mike", "tree2")
            self.plant.planting("Mike", "tree3")

        self.assertEqual("The plantation is full!", str(ex.exception))

    def test_planting_worker_in_plants_already(self):
        self.plant.hire_worker("Mike")
        self.plant.planting("Mike", "tree")

        expected = f"Mike planted tree1."
        actual = self.plant.planting("Mike", "tree1")
        self.assertEqual(expected, actual)

    def test_planting_first_plant(self):
        self.plant.hire_worker("Mike")

        expected = f"Mike planted it's first tree."
        actual = self.plant.planting("Mike", "tree")

        self.assertEqual(expected, actual)

    def test_str_returns_correct(self):
        self.plant.hire_worker("Mike")
        self.plant.planting("Mike", "tree")
        self.plant.hire_worker("Dave")
        self.plant.planting("Dave", "tree1")
        self.plant.planting("Dave", "tree2")

        expected = f"Plantation size: 3\n"
        expected += "Mike, Dave\n"
        expected += f"Mike planted: tree\n"
        expected += f"Dave planted: tree1, tree2"
        actual = str(self.plant)

        self.assertEqual(expected, actual)

    def test__str_when_no_workers(self):
        expected = f"Plantation size: 3\n"
        actual = str(self.plant)

        self.assertEqual(expected, actual)

    def test__str_when_workers_and_no_plants(self):
        self.plant.hire_worker("Mike")
        self.plant.hire_worker("Dave")
        expected = f"Plantation size: 3\n"
        expected += "Mike, Dave"
        actual = str(self.plant)

        self.assertEqual(expected, actual)


    def test_repr_returns_correct(self):
        self.plant.hire_worker("Mike")
        self.plant.hire_worker("Dave")

        expected = f'Size: 3\n'
        expected += f'Workers: Mike, Dave'
        actual = repr(self.plant)

        self.assertEqual(expected, actual)

    def test_repr_no_workers(self):
        expected = f'Size: 3\n'
        expected += f'Workers: '
        actual = repr(self.plant)

        self.assertEqual(expected, actual)




if __name__ == "__main__":
    main()
