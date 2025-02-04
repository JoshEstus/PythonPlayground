class Library():

    def __init__(self, booklist, name):
        self.booklist = booklist
        self.name = name
        self.lendDict = {} # k:book: v:user

    def displayBooks(self):
        """
        Displays all books in the library
        """
        print(f"We have following books in our library: {self.name}")
        for book in self.booklist:
            print(book)


    def booksNotAvailable(self):
        """
        Displays all books in the library that are lended out
        """
        print(f"The following books are borrowed out:")
        for book in self.lendDict.items():
            print("Book:", book[0], "Lender:", book[1])


    def addBook(self, book):
        """
        Takes a book name and adds to the library
        """
        if book in self.booklist:
            print("Book is already in library")
        else:
            self.booklist.append(book)
            bookDatabase = open(databaseName, "a")
            bookDatabase.write("\n")
            bookDatabase.write(book)
            print("Book has been added to the book list")


    def lendBook(self, user, book):
        """
        If book is available, lend it to the user
        """
        if book in self.booklist:
            if book not in self.lendDict.keys():
                self.lendDict.update({book:user})
                print("Lender-Book database has been updated. You can take the book now")
            else:
                print(f"Book is already being used by {self.lendDict[book]}")
        else:
            print("Book is not available in the library")


    def returnBook(self, book):
        """Makes book available to lend"""
        if book in self.booklist:
            self.lendDict.pop(book)
            print("Book has been returned. Thank you!")
        else:
            print("Book is not in the library")


    def removeBook(self, book):
        """
        Removes a book from the library
        """
        if book in self.booklist:
            self.booklist.remove(book)
            bookDatabase = open(databaseName, "r")
            lines = bookDatabase.readlines()
            bookDatabase.close()
            bookDatabase = open(databaseName, "w")
            for line in lines:
                if line.strip("\n") != book:
                    bookDatabase.write(line)
            bookDatabase.close()
            print("Book has been removed from the book list")
        else:
            print("Book is not in the library")


def main():
    while(True):
        # Print Menu
        print(f"Welcome to the {my_library.name} library. Enter your choice to continue")
        choice = """
        1. Display Books
        2. Lend a book
        3. Add a book
        4. Return a book
        5. Books not available
        6. Remove Book
        """
        print(choice)

        userInput = input("Press Q to quit and C to continue. Enter your choice: ").capitalize()
        if userInput == "C":
            userChoice = int(input("Enter your choice: "))
            if userChoice == 1:
                my_library.displayBooks()
            elif userChoice == 2:
                book = input("Enter the name of the book you want to lend: ")
                user = input("Enter your name: ")
                my_library.lendBook(user, book)
            elif userChoice == 3:
                book = input("Enter the name of the book you want to add: ")
                my_library.addBook(book)
            elif userChoice == 4:
                book = input("Enter the name of the book you want to return: ")
                my_library.returnBook(book)
            elif userChoice == 5:
                my_library.booksNotAvailable()
            elif userChoice == 6:
                book = input("Enter the name of the book you want to remove: ")
                my_library.removeBook(book)
            else:
                print("Invalid Choice")

        elif userInput == "Q":
            break

        else:
            print("Invalid Input")


if __name__ == "__main__":
    booklist = []
    databaseName = input("Enter name of Database:")
    bookDatabase = open(databaseName, "r")
    for book in bookDatabase:
        booklist.append(book.rstrip())
    my_library = Library(booklist, "Josh Library")
    main()
