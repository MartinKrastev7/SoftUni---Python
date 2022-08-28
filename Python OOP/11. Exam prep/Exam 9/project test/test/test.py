from project.library import Library
from unittest import TestCase, main


class LibraryTests(TestCase):
    def setUp(self) -> None:
        self.lib = Library("classic")

    def test_init_correct(self):
        self.assertEqual("classic", self.lib.name)
        self.assertEqual({}, self.lib.books_by_authors)
        self.assertEqual({}, self.lib.readers)

    def test_name_empty_str_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.lib_em = Library("")

        self.assertEqual("Name cannot be empty string!", str(ex.exception))

    def test_add_book_author_not_in_authors(self):
        expected = {"mike": ["kiko"]}
        self.lib.add_book("mike", "kiko")
        actual = self.lib.books_by_authors

        self.assertEqual(expected, actual)

    def test_add_book_author_in_authors_append_book(self):
        self.lib.add_book("mike", "kiko")
        self.lib.add_book("mike", "dada")
        expected = {"mike": ["kiko", "dada"]}
        actual = self.lib.books_by_authors

        self.assertEqual(expected, actual)

    def test_add_reader_not_in_readers(self):
        expected = {"tito": []}
        self.lib.add_reader("tito")
        actual = self.lib.readers

        self.assertEqual(expected, actual)

    def test_add_reader_in_readers_returns(self):
        self.lib.add_reader("tito")
        expected = f"tito is already registered in the classic library."
        actual = self.lib.add_reader("tito")

        self.assertEqual(expected, actual)

    def test_rent_book_reader_not_in_readers(self):
        self.lib.add_book("miko", "kiko")
        expected = f"tito is not registered in the classic Library."
        actual = self.lib.rent_book("tito", "miko", "kiko")

        self.assertEqual(expected, actual)

    def test_rent_book_author_not_in_authors(self):
        self.lib.add_reader("tito")
        expected = f"classic Library does not have any miko's books."
        actual = self.lib.rent_book("tito", "miko", "kiko")

        self.assertEqual(expected, actual)

    def test_rent_book_book_not_in_books(self):
        self.lib.add_reader("tito")
        self.lib.add_book("mike", "fff")
        expected = f"""classic Library does not have mike's "kiko"."""
        actual = self.lib.rent_book("tito", "mike", "kiko")

        self.assertEqual(expected, actual)

    def test_rent_book_correct_in_readers(self):
        self.lib.add_reader("tito")
        self.lib.add_book("miko", "kiko")
        self.lib.add_book("miko", "ffff")

        self.lib.rent_book("tito", "miko", "kiko")
        expected = {"tito": [{"miko": "kiko"}]}
        actual = self.lib.readers

        self.assertEqual(expected, actual)

    def test_rent_book_take_from_books(self):
        self.lib.add_reader("tito")
        self.lib.add_book("miko", "kiko")
        self.lib.add_book("miko", "ffff")

        self.lib.rent_book("tito", "miko", "kiko")
        expected = {"miko": ["ffff"]}
        actual = self.lib.books_by_authors

        self.assertEqual(expected, actual)




if __name__ == "__main__":
    main()