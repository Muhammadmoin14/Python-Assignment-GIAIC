# Objective
# Create a command-line Personal Library Manager that allows users to manage their book collection. The program should let users add, remove, and search for books. Each book will be stored as a dictionary with details like title, author, publication year, genre, and read status. The program should also include a menu system, basic statistics, and optional file handling for saving and loading the library.

def menu():
    print("\nPersonal Library Manager")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")
    choice = input("What do you want to do? ")
    return choice

def add_book(library):
    print('\''*25 +'\t'"Add a book" '\t'+ '\''*25)
    
    # Take Input from user
    
    Title = input("Enter the title of the book: ")
    Author = input("Enter the author of the book: ")
    
    # Add error handling for year input
    while True:
        try:
            PublicationYear = int(input("Enter the publication year of the book: "))
            break
        except ValueError:
            print("Please enter a valid year as a number.")
    
    Genre = input("Enter the genre of the book: ")
    
    # Fix the read status logic
    read_input = input("Have you read the book? (yes/no): ").lower()
    if read_input in ['yes', 'y']:
        Read = True
    else:
        Read = False
    
    book = {
        "title" : Title,
        "author" : Author,
        "publication_year" : PublicationYear,
        "genre" : Genre,
        "read_status" : Read
    }
    
    library.append(book)
    
    print("Book added successfully")
    return library

def display_books(books):
    print('\''*25 +'\t'"Display all books" '\t'+ '\''*25)
    if not books:
        print("Your library is empty.")
        return
        
    for i, book in enumerate(books, 1):
        read_status = "Read" if book["read_status"] else "Not read"
        print(f"{i}. {book['title']} by {book['author']} ({book['publication_year']}) - {book['genre']} - {read_status}")

def remove_book(library):
    print('\''*25 +'\t'"Remove a book" '\t'+ '\''*25)
    if not library:
        print("Your library is empty.")
        return library
        
    Title = input("Enter the title of the book to remove: ")
    for i in range(len(library)):
        if library[i]["title"] == Title:
            del library[i]
            print("Book removed successfully")
            return library
    
    print(f"No book with title '{Title}' found.")
    return library

def search_book(library):
    print('\''*25 +'\t'"Search for a book" '\t'+ '\''*25)
    if not library:
        print("Your library is empty.")
        return
        
    search_term = input("Enter search term: ").lower()
    found_books = []
    
    for book in library:
        if (search_term in book["title"].lower() or 
            search_term in book["author"].lower() or 
            search_term in book["genre"].lower()):
            found_books.append(book)
    
    if found_books:
        print(f"Found {len(found_books)} book(s):")
        for book in found_books:
            read_status = "Read" if book["read_status"] else "Not read"
            print(f"{book['title']} by {book['author']} - {read_status}")
    else:
        print("No books found matching your search.")

def display_statistics(library):
    print('\''*25 +'\t'"Library Statistics" '\t'+ '\''*25)
    total_books = len(library)
    read_books = 0
    
    for book in library:
        if book["read_status"]:
            read_books += 1
    
    not_read_books = total_books - read_books
    
    print(f"Total books: {total_books}")
    print(f"Read books: {read_books}")
    print(f"Unread books: {not_read_books}")

def main():
    library = []
    # Remove file handling code which causes errors
    
    condition = True
    while condition:
        choice = menu()
        if choice == "1":
            library = add_book(library)
        elif choice == "2":
            library = remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            condition = False
            print("Goodbye!")
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()