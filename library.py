class Book:
    def __init__(self, author, bookcode):
        self.author = author
        self.bookcode = bookcode
        self.book_status = False
    def __str__(self):
        status = "Borrowed" if self.book_status else "Available"
        return f"[{self.bookcode}] by {self.author} - {status}"



class Member:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.borrowed_books = []
    def __str__(self):
        return f"{self.name} (ID: {self.id})"

class Library:
    def __init__(self):
        self.memberList = {}
        self.bookList = {}

    def add_book(self, author, bookcode):
        new_book = Book(author, bookcode)
        self.bookList[bookcode] = new_book

    def add_member(self, name, id):
        new_member = Member(name, id)
        self.memberList[id] = new_member

    def borrowing_book(self, bookcode, member_id):
        if bookcode not in self.bookList:
            print("The book is not in the library.")
            return
        if member_id not in self.memberList:
            print("Member does not exist.")
            return

        book = self.bookList[bookcode]
        member = self.memberList[member_id]

        if not book.book_status:
            member.borrowed_books.append(book.bookcode)
            book.book_status = True
            print(f"{member.name} borrowed the book {book.bookcode}.")
        else:
            print(f"The book {book.bookcode} is already borrowed.")
    
    
    def return_book(self, bookcode, member_id):
        if member_id not in self.memberList:
            print(" Member does not exist.")
            return
        if bookcode not in self.bookList:
            print(" Book does not exist in library.")
            return

        book = self.bookList[bookcode]
        member = self.memberList[member_id]

        if bookcode in member.borrowed_books:
            member.borrowed_books.remove(bookcode)
            book.book_status = False
            print(f"'{book.title}' returned by {member.name}.")
        else:
            print(f" {member.name} did not borrow '{book.bookcode}'.")


    def show_books(self):
        print("\n All Books in Library:")
        for book in self.bookList.values():
            print("  ", book)

    def show_members(self):
        print("\nLibrary Members:")
        for member in self.memberList.values():
            print(f" {member}")
            if member.borrowed_books:
                print("   Borrowed:", member.borrowed_books)
            else:
                print("   No borrowed books.")
