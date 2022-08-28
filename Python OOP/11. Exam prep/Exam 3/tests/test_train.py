from unittest import TestCase, main

from project.train.train import Train


class TrainTests(TestCase):
    def setUp(self) -> None:
        self.t = Train("BDZ", 3)

    def test_init_correct(self):
        self.assertEqual("BDZ", self.t.name)
        self.assertEqual(3, self.t.capacity)
        self.assertEqual([], self.t.passengers)

    def test_add_len_pass_equal_to_capacity_raises(self):
        self.t.passengers.append("f")
        self.t.passengers.append("k")
        self.t.passengers.append("g")

        with self.assertRaises(ValueError) as ex:
            self.t.add("o")

        self.assertEqual("Train is full", str(ex.exception))

    def test_add_pass_already_in_pass_raises(self):
        self.t.passengers.append("k")

        with self.assertRaises(ValueError) as ex:
            self.t.add("k")

        self.assertEqual("Passenger k Exists", str(ex.exception))

    def test_add_correct(self):
        expected = "Added passenger l"
        actual = self.t.add("l")

        self.assertEqual(expected, actual)

    def test_remove_pass_not_in_pass_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.t.remove("k")

        self.assertEqual("Passenger Not Found", str(ex.exception))

    def test_remove_correct(self):
        self.t.passengers.append("k")
        expected = "Removed k"
        actual = self.t.remove("k")

        self.assertEqual(expected, actual)



if __name__ == "__main__":
    main()