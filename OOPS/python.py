class Book:
    def __init__(self, title, author, bookid):
        self.title = title
        self.author = author
        self.bookid = bookid
        self.checked_out = False

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            print(f"{self.title} has been checked out.")
        else:
            print(f"{self.title} is already checked out.")

    def return_book(self):
        if self.checked_out:
            self.checked_out = False
            print(f"Thank you for returning {self.title}.")
        else:
            print(f"{self.title} is not checked out.")

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print("The library is empty.")
        else:
            print("Books available in the library:")
            for book in self.books:
                print(book)

    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

if __name__ == "__main__":
    library = Library()

    book1 = Book("Music", "Steve", "1234")
    book2 = Book("Movie", "Louis", "5678")
    book3 = Book("Game", "Frank", "9011")
    book4 = Book("Story", "Luther", "1213")
    book5 = Book("Riddles", "Martin", "1415")


    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)
    library.add_book(book5)

    while True:
        print("\nLibrary Management System")
        print("1. Books available in library")
        print("2. Enter the name of the book to check for availability")
        print("3. Please enter the book name for check out")
        print("4. Enter the book name to return")
        print("5. Exit from library..")

        choice = input("Enter your choice: ")

        if choice == "1":
            library.display_books()
        elif choice == "2":
            title = input("Enter the name of the book to check for availability:")
            book = library.search_book(title)
            if book:
                print(f"Book is available in library: {book}")
            else:
                print("Book not found in the library (or) Please enter valid book name.")
        elif choice == "3":
            title = input("Please Enter the name of the book for checkout: ")
            book = library.search_book(title)
            if book:
                book.check_out()
            else:
                print("Book not found in the library.")
        elif choice == "4":
            title = input("Enter the name of the book you want to return: ")
            book = library.search_book(title)
            if book:
                book.return_book()
            else:
                print("Please enter the valid book name.")
        elif choice == "5":
            print("THANK YOU FOR VISITING THE LIBRARY..!.")
            break
        else:
            print("Invalid choice. Please try again.")