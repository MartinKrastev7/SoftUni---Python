from project.plantation import Plantation
from unittest import TestCase, main


class PlantationTest(TestCase):
    def setUp(self) -> None:
        self.p = Plantation(3)

    def test_init_correct(self):
        self.assertEqual(3, self.p.size)
        self.assertEqual({}, self.p.plants)
        self.assertEqual([], self.p.workers)

    def test_size_under_0_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.b = Plantation(-10)

        self.assertEqual("Size must be positive number!", str(ex.exception))

    def test_hire_worker_already_in_workers_raises(self):
        self.p.hire_worker("mike")
        with self.assertRaises(ValueError) as ex:
            self.p.hire_worker("mike")

        self.assertEqual("Worker already hired!", str(ex.exception))

    def test_hire_worker_correct(self):
        self.p.hire_worker("mike")
        expected = ["mike"]
        actual = self.p.workers

        self.assertEqual(expected, actual)

    def test_hire_worker_correct_returns(self):
        expected = f"mike successfully hired."
        actual = self.p.hire_worker("mike")

        self.assertEqual(expected, actual)

    def test_len_returns_count_of_plants_0(self):
        expected = 0
        actual = self.p.__len__()

        self.assertEqual(expected, actual)

    def test_planting_worker_not_in_workers_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.p.planting("mike", "durvo")

        self.assertEqual(f"Worker with name mike is not hired!", str(ex.exception))

    def test_planting_plants_equal_than_size_raises(self):
        self.p.hire_worker("mike")
        self.p.planting("mike", "durvo")
        self.p.planting("mike", "durvo1")
        self.p.planting("mike", "durvo2")

        with self.assertRaises(ValueError) as ex:
            self.p.planting("mike", "durvo3")

        self.assertEqual("The plantation is full!", str(ex.exception))

    def test_planting_plants_more_size_raises(self):
        self.p.hire_worker("mike")
        self.p.planting("mike", "durvo")
        self.p.planting("mike", "durvo1")
        self.p.planting("mike", "durvo4")
        self.p.planting("mike", "durvo5")

        with self.assertRaises(ValueError) as ex:
            self.p.planting("mike", "durvo3")

        self.assertEqual("The plantation is full!", str(ex.exception))


    def test_planting_if_worker_already_has_plants(self):
        self.p.hire_worker("mike")
        self.p.planting("mike", "durvo")
        expected = f"mike planted durvo1."
        actual = self.p.planting("mike", "durvo1")

        self.assertEqual(expected, actual)

    def test_planting_worker_first_plant(self):
        self.p.hire_worker("mike")
        expected = f"mike planted it's first durvo."
        actual = self.p.planting("mike", "durvo")

        self.assertEqual(expected, actual)

    def test_len_returns_correct(self):
        self.p.hire_worker("mike")
        self.p.planting("mike", "durvo")
        self.p.planting("mike", "durvo1")

        expected = 2
        actual = self.p.__len__()

        self.assertEqual(expected, actual)

    def test_str_returns_correct(self):
        self.p.hire_worker("mike")
        self.p.planting("mike", "durvo")
        self.p.planting("mike", "durvo1")
        result = f"Plantation size: 3\n"
        result += f'mike\n'
        result += f"mike planted: durvo, durvo1"
        actual = str(self.p)

        self.assertEqual(result, actual)

    def test_str_returns_no_workers(self):
        result = f"Plantation size: 3\n"
        actual = str(self.p)

        self.assertEqual(result, actual)

    def test_str_returns_no_plants(self):
        self.p.hire_worker("mike")
        result = f"Plantation size: 3\n"
        result += f'mike'
        actual = str(self.p)

        self.assertEqual(result, actual)

    def test_repr_returns_correct(self):
        self.p.hire_worker("mike")
        result = f'Size: 3\n'
        result += f'Workers: mike'
        actual = repr(self.p)

        self.assertEqual(result, actual)

    def test_repr_returns_no_workers(self):
        result = f'Size: 3\n'
        result += "Workers: "
        actual = repr(self.p)

        self.assertEqual(result, actual)



if __name__ == "__main__":
    main()