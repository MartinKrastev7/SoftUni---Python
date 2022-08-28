from project.student_report_card import StudentReportCard
from unittest import TestCase, main


class StudentReportCardTests(TestCase):
    def setUp(self) -> None:
        self.student = StudentReportCard("Pesho", 5)

    def test_init_correct(self):
        self.assertEqual("Pesho", self.student.student_name)
        self.assertEqual(5, self.student.school_year)
        self.assertEqual({}, self.student.grades_by_subject)

    def test_student_name_with_empty_value_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.student_test = StudentReportCard("", 1)

        self.assertEqual("Student Name cannot be an empty string!", str(ex.exception))

    def test_school_year_below_1_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.student_test = StudentReportCard("Pepi", -1)

        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

    def test_school_year_equal_1(self):
        self.assertTrue(StudentReportCard("Pepi", 1), True)

    def test_school_year_above_12_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.student_test = StudentReportCard("Pepi", 14)

        self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

    def test_school_year_equal_12(self):
        self.assertTrue(StudentReportCard("Pepi", 12), True)

    def test_add_subject_not_in_subjects_dict(self):
        self.student.add_grade("Math", 5)
        expected = {"Math": [5]}
        actual = self.student.grades_by_subject
        self.assertEqual(expected, actual)

    def test_add_subject_already_in_subjects(self):
        self.student.add_grade("Math", 5)
        self.student.add_grade("Math", 6)
        expected = {"Math": [5, 6]}
        actual = self.student.grades_by_subject
        self.assertEqual(expected, actual)

    def test_average_grade_by_subject(self):
        self.student.add_grade("Math", 5)
        self.student.add_grade("Math", 6)
        self.student.add_grade("Bio", 4)
        self.student.add_grade("Bio", 6)

        expected = f"Math: 5.50\n"
        expected += f"Bio: 5.00"
        actual = self.student.average_grade_by_subject()
        self.assertEqual(expected, actual)

    def test_average_grade_for_all_subject(self):
        self.student.add_grade("Math", 5)
        self.student.add_grade("Math", 6)
        self.student.add_grade("Bio", 4)
        self.student.add_grade("Bio", 6)

        expected = f"Average Grade: 5.25"
        actual = self.student.average_grade_for_all_subjects()

        self.assertEqual(expected, actual)

    def test_repr_correct(self):
        self.student.add_grade("Math", 5)
        self.student.add_grade("Math", 6)
        self.student.add_grade("Bio", 4)
        self.student.add_grade("Bio", 6)

        expected = "Name: Pesho\n"
        expected += "Year: 5\n"
        expected += "----------\n"
        expected += "Math: 5.50\n"
        expected += "Bio: 5.00\n"
        expected += "----------\n"
        expected += "Average Grade: 5.25"

        actual = repr(self.student)
        self.assertEqual(expected, actual)



if __name__ == '__main__':
    main()