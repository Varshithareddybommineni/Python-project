class Book:
    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Year: {self.year}"

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self):
        book_id = int(input("Enter book ID: "))
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        year = int(input("Enter year of publication: "))
        
        new_book = Book(book_id, title, author, year)
        self.books.append(new_book)
        print("Book added successfully.")
    
    def display_books(self):
        if not self.books:
            print("No books available in the library.")
            return
        
        print("\nList of Books:")
        print("---------------------------------------------------")
        for book in self.books:
            print(book)
        print("---------------------------------------------------")
    
    def delete_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print(f"Book with ID {book_id} has been deleted successfully.")
                return
        print(f"Book with ID {book_id} not found.")
    
    def search_book_by_id(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                print("\nBook Found:")
                print(book)
                return
        print(f"Book with ID {book_id} not found.")
    
    def menu(self):
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Delete Book")
        print("4. Search Book by ID")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            self.add_book()
        elif choice == 2:
            self.display_books()
        elif choice == 3:
            book_id = int(input("Enter book ID to delete: "))
            self.delete_book(book_id)
        elif choice == 4:
            book_id = int(input("Enter book ID to search: "))
            self.search_book_by_id(book_id)
        elif choice == 5:
            print("Exiting the system.")
            exit()
        else:
            print("Invalid choice, please try again.")

def main():
    library = Library()
    
    while True:
        library.menu()

if __name__ == "__main__":
    main()
