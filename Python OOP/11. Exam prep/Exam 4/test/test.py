from project.team import Team
from unittest import TestCase,main


class TestTeam(TestCase):
    def setUp(self) -> None:
        self.t = Team("best")

    def test_init_correct(self):
        self.assertEqual("best", self.t.name)
        self.assertEqual({}, self.t.members)

    def test_name_is_only_alpha(self):
        with self.assertRaises(ValueError) as ex:
            self.b = Team("bbf44444888")

        self.assertEqual("Team Name can contain only letters!", str(ex.exception))

    def test_add_member_name_not_in(self):
        expected = {"kiko": 15}
        actual = self.t.members
        name_age = {"kiko": 15}
        self.t.add_member(**name_age)

        self.assertEqual(expected, actual)

    def test_add_member_returns(self):
        name_age = {"kiko": 15}
        expected = f"Successfully added: kiko"
        actual = self.t.add_member(**name_age)

        self.assertEqual(expected, actual)

    def test_remove_member_name_not_in(self):
        expected = f"Member with name miko does not exist"
        actual = self.t.remove_member("miko")

        self.assertEqual(expected, actual)

    def test_remove_member_correct(self):
        name_age = {"kiko": 15}
        self.t.add_member(**name_age)
        name_age2 = {"miko": 15}
        self.t.add_member(**name_age2)

        expected = f"Member miko removed"
        actual = self.t.remove_member("miko")

        self.assertEqual(expected, actual)

    def test_remove_member_from_members_true(self):
        name_age = {"kiko": 15}
        self.t.add_member(**name_age)
        name_age2 = {"miko": 15}
        self.t.add_member(**name_age2)
        self.t.remove_member("miko")

        expected = {"kiko": 15}
        actual = self.t.members

        self.assertEqual(expected, actual)

    def test__gt__override_returns_True(self):
        self.b = Team("worst")
        name_age = {"kiko": 15}
        self.t.add_member(**name_age)
        name_age2 = {"miko": 15}
        self.t.add_member(**name_age2)
        self.b.add_member(**name_age)

        expected = True
        actual = self.t.__gt__(self.b)

        self.assertEqual(expected, actual)

    def test__gt__override_returns_False(self):
        self.b = Team("worst")
        name_age = {"kiko": 15}
        self.b.add_member(**name_age)
        name_age2 = {"miko": 15}
        self.b.add_member(**name_age2)
        self.t.add_member(**name_age)

        expected = False
        actual = self.t.__gt__(self.b)

        self.assertEqual(expected, actual)

    def test__len__returns_members_len(self):
        name_age = {"kiko": 15}
        self.t.add_member(**name_age)
        name_age2 = {"miko": 15}
        self.t.add_member(**name_age2)

        expected = 2
        actual = self.t.__len__()

        self.assertEqual(expected, actual)

    def test_add_new_team_right_name(self):
        self.b = Team("worst")
        expected = "bestworst"
        actual = self.t.__add__(self.b)

        self.assertEqual(expected, actual.name)

    def test_add_new_team_members_correct(self):
        self.b = Team("worst")
        name_age = {"kiko": 15}
        self.b.add_member(**name_age)
        name_age2 = {"miko": 15}
        self.b.add_member(**name_age2)
        name_age3 = {"diko": 14}
        self.t.add_member(**name_age3)

        expected = {"kiko":15, "miko": 15, "diko": 14}
        actual = self.t.__add__(self.b).members

        self.assertEqual(expected, actual)

    def test_str_correct(self):
        self.b = Team("worst")
        name_age = {"biko": 15}
        self.b.add_member(**name_age)
        name_age2 = {"diko": 17}
        self.b.add_member(**name_age2)

        result = f"Team name: worst\n"
        result += f"Member: diko - 17-years old\n"
        result += f"Member: biko - 15-years old"
        actual = str(self.b)

        self.assertEqual(result, actual)





if __name__ == "__main__":
    main()