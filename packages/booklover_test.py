import pandas as pd
import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    def test_1_add_book(self):
        lover_books = BookLover('Billy Batson', 'shazam69420@aol.edu', 'comics')
        lover_books.add_book('Flashpoint', 5)
        self.assertTrue('Flashpoint' in lover_books.book_list['book_name'].values)
    
    
    def test_2_add_book(self):
        lover_books = BookLover('Billy Batson', 'shazam69420@aol.edu', 'comics')
        lover_books.add_book('Flashpoint', 5)
        lover_books.add_book('Flashpoint', 5)
        self.assertEqual(test_object.book_list['book_name'].value_counts().get("War of the Worlds", 0), 1)
    
    def test_3_has_read(self):
        lover_books = BookLover('Billy Batson', 'shazam69420@aol.edu', 'comics')
        lover_books.add_book('Flashpoint', 5)
        self.assertTrue(lover_books.has_read("Flashpoint"))

    def test_4_has_read(self):
        lover_books = BookLover('Billy Batson', 'shazam69420@aol.edu', 'comics')
        lover_books.add_book('Flashpoint', 5)
        self.assertFalse(lover_books.has_read('Batman Year One'))
    
    def test_5_num_books_read(self):
        lover_books = BookLover('Billy Batson', 'shazam69420@aol.edu', 'comics')
        lover_books.add_book('Flashpoint', 5)
        lover_books.add_book('Crisis on Infinite Earths', 5)
        lover_books.add_book('Spider-Man #1', 3)
        self.assertEqual(lover_books.num_books_read(), 3)

    
    def test_6_fav_books(self):
        lover_books = BookLover('Billy Batson', 'shazam69420@aol.edu', 'comics')
        lover_books.add_book('Flashpoint', 5)
        lover_books.add_book('Crisis on Infinite Earths', 5)
        lover_books.add_book('Mockingjay', 2)
        fav_books = lover_books.fav_books()
        self.assertTrue(all(fav_books['book_rating'] > 3))
    
    if __name__ == '__main__':
        unittest.main(argv=['first-arg-is-ignored'],exit=False)