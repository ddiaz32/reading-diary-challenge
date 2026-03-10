from datetime import datetime

# TODO: Add code here

class Note:
    def __init__(self, text: str, page: int, date:datetime):
        self.text = text
        self.page = page
        self.date = date 

    def __str__(self):
        return f"{self.date} - page {self.page}: {self.text}"
    

class Book:
    EXCELLENT = 3
    GOOD = 2
    BAD = 1
    UNRATED = -1

    def __init__(self, isbn: str, title: str, author: str, pages: int):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.pages = pages
        self.rating = Book.UNRATED
        self.notes = []

    def add_note(self, text: str, page: int, date: datetime) -> bool:

        if page > self.pages:
            return False
        

        note = Note(text, page, date)

        self.notes.append(note)

        return True
    
    def set_rating(self, rating: int) -> bool:

        if rating not in (Book.EXCELLENT, Book.GOOD, Book.BAD):
            return False
        
        self.rating = rating
        return True
    
    def get_notes_of_page(self, page: int) -> list[Note]:

        notes_page = []

        for note in self.notes:
            if note.page == page:
                notes_page.append(note)


        return notes_page
    
    def page_with_most_notes(self) -> int:

        if len(self.notes) == 0:
            return -1
        
        counter = {}

        for note in self.notes:
            counter[note.page] = counter.get(note.page, 0) + 1

        return max(counter, key=counter.get)
    
    def __str__(self) -> str:


        if self.rating == Book.EXCELLENT:
            rating_str = "excellent"
        elif self.rating == Book.GOOD:
            rating_str = "good"
        elif self.rating == Book.BAD:
            rating_str = "bad"
        else:
            rating_str = "unrated"

        return f"""     
        ISBN: {self.isbn}
        Title: {self.title}
        Author: {self.author}
        Pages: {self.pages}
        Rating: {rating_str}
                """



class ReadinDiary:

    def __init__(self):
        self.books: dict[str, Book] = {}

    def add_book(self, isbn: str, title: str, author: str, pages: int) -> bool:
        if isbn in self.books:
            return False
        
        book = Book(isbn, title, author, pages)
        self.books[isbn] = book

        return True
    def search_by_isbn(self, isbn: str) -> Book | None:
            for book in self.books:
                if book.isbn == isbn:
                    return book
            return None



    def add_note_to_book(self, isbn: str, text: str, page: int, date: datetime) -> bool:
        

        book = self.search_by_isbn(isbn)

        if book is None:
            return False

        return book.add_note(text, page, date)

    

    


book = Book("978123", "Python Avanzado", "David Diaz", 350)

book.set_rating(Book.BAD)

print(book)




  

