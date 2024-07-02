import pandas as pd
class BookLover:
    
    def __init__(self, name, email, fav_genre, num_books=0):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
        
   
    def add_book(self, book_name, book_rating):
        #if book_name in self.book_list[self.book_list['book_name']]== book_name:
        if not self.book_list[self.book_list['book_name'] == book_name].empty:
            print('book already in list')
        else:
            new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [book_rating]})
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books += 1
    def has_read(self, book_name):
        return book_name in self.book_list['book_name'].values

    
    def num_books_read(self):
        return self.num_books
    
    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]
        
if __name__ == '__main__':
    
    test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
    test_object.add_book("War of the Worlds", 4)
    print(test_object.book_list)