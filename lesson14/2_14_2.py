
class Library:

    def __init__(self, name):
        self.name = name
        self.all_books = []
        self.authors = []

    def __repr__(self):
        return f'Для {self.name} есть книги: {self.all_books}'

    def new_book(self, name, year, author):
        book = Book(name, year, author)
        self.all_books.append(book)
        self.authors.append(author)
        return book

    def add_book(self, new_book):
        self.all_books.append(new_book)

    def group_by_author(self, author):
        return author.authors

    def group_by_year(self, year):
        year_list = []
        for book in self.all_books:
            if year in book.year:
                year_list.append(book)
        return year_list


class Book:
    amount_of_all_books = 0

    def __init__(self, name, year, author):
        self.book_name = name
        self.book_year = year
        self.book_author = author
        self.amount_of_all_books += 1

    def __repr__(self):
        return f'{self.book_name}, книга {self.book_year} года выпуска, {self.book_author}\n'


class Author:

    def __init__(self, name, country, birthday):
        self.author_name = name
        self.author_country = country
        self.author_birthday = birthday
        self.books = []

    def __repr__(self):
        return f'Автор: {self.author_name}, из {self.author_country}, родился {self.author_birthday}'

    # def new_book(self, name, year, author):
    #     book = Book(name, year, author)
    #     self.books.append(book)
    #     # self.authors.append(author)
    #     return book


lib = Library
auth = Author
boo = Book
dostoevskii = Library('Достоевский')
pushkin = Library('Пушкин')

author_dostoevskii = Author('Федор Михайлович Достоевский', 'Россия', '30.10.1821')
author_pushkin = Author('Александр Сергеевич Пушкин', 'Россия', '06.06.1799')

book1 = boo('Преступление и наказание', 1866, 'Федор Михайлович Достоевский')
book2 = Book('Братья Карамазовы', 1880, 'Федор Михайлович Достоевский')

book3 = Book('Евгений Онегин', 1837, 'Александр Сергеевич Пушкин')
book4 = Book('Сказка о царе Салтане', 1831, 'Александр Сергеевич Пушкин')

dostoevskii.new_book(book1, 1866, author_dostoevskii)
dostoevskii.new_book(book2, 1880, author_dostoevskii)
pushkin.new_book(book3, 1837, author_pushkin)
pushkin.new_book(book4, 1831, author_pushkin)
# print(dostoevskii.group_by_author)
# print(pushkin.group_by_year)
# print(Book.amount_of_all_books)
print()
dostoevskii.add_book(author_dostoevskii.new_book('Преступление и наказание', 1866, 'Федор Михайлович Достоевский'))
dostoevskii.add_book(author_dostoevskii.new_book('Братья Карамазовы', 1880, 'Федор Михайлович Достоевский'))
print(Book.amount_of_all_books)
