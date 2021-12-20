class Author:
    def __init__(self, name, country, birsday):
        self.name = name
        self.country = country
        self.birsday = birsday
        self.books = []
        
    def __repr__(self):
        return f'"{self.name}"'
        
class Book:
    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        
    def __repr__(self):
        return f'"{self.name}, {self.year}"'
        
class Library:
    def __init(self, name):
        self.name = name
        self.book = []
        self.author = []
        
    def new_book(self,name,year, author):
    
        if author not in self.authors:
            self.authors.append(author)
            
        b = Book(name,year, author)
        self.books.append(b)
        author.books.append(b)
        
        return b
        
    def group_by_author(self, author):
        pass
            
    def group_by_year(self, year): 
        pass
        
l = Library('Читать')
a1 = Authors('Дашвар','uk',1986)
l.new_book('Покров', 2014, a1)
l.new_book('Молоко с кровю', 2010, a1)
print(a1,a1.books[0].author.name,a1.books[0].author.birsday, a1.books[0].author.country, a1.books[0].author.books, a1.books[0].author.books[0].author.books[1])
