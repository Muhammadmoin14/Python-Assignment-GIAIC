# Objective

# Create a command-line Personal Library Manager that allows users to manage their book collection. The program should let users add, remove, and search for books. Each book will be stored as a dictionary with details like title, author, publication year, genre, and read status. The program should also include a menu system, basic statistics, and optional file handling for saving and loading the library.

import streamlit as st

# Initialize session state to store the library
if 'library' not in st.session_state:
    st.session_state.library = []

def menu():
    st.title("Personal Library Manager")
    choice = st.selectbox("What do you want to do?", ["Add a book", "Remove a book", "Search for a book", "Display all books", "Display statistics", "Exit"])
    return choice

def add_book():
    st.subheader("Add a book")
    
    # Take Input from user
    with st.form("add_book_form"):
        Title = st.text_input("Enter the title of the book:")
        Author = st.text_input("Enter the author of the book:")
        # Using number input for year instead of date input for simplicity
        PublicationYear = st.number_input("Enter the publication year:", min_value=1000, max_value=2100, value=2000)
        Genre = st.text_input("Enter the genre of the book:")
        
        # Fix the read status logic
        read_input = st.radio("Have you read the book?", ["yes", "no"])
        Read = True if read_input == "yes" else False
        
        submitted = st.form_submit_button("Add Book")
        
        if submitted and Title and Author:  # Basic validation
            book = {
                "title": Title,
                "author": Author,
                "publication_year": int(PublicationYear),
                "genre": Genre,
                "read_status": Read
            }
            
            st.session_state.library.append(book)
            st.success("Book added successfully")

def display_books():
    st.subheader("Display all books")
    
    if not st.session_state.library:
        st.info("Your library is empty.")
        return
    
    # Create a better display with a table
    books_data = []
    for book in st.session_state.library:
        read_status = "Read" if book["read_status"] else "Not read"
        books_data.append({
            "Title": book["title"],
            "Author": book["author"],
            "Year": book["publication_year"],
            "Genre": book["genre"],
            "Status": read_status
        })
    
    st.table(books_data)

def remove_book():
    st.subheader("Remove a book")
    
    if not st.session_state.library:
        st.info("Your library is empty. There are no books to remove.")
        return
    
    # Create a list of book titles for selection
    book_titles = [book["title"] for book in st.session_state.library]
    selected_title = st.selectbox("Select a book to remove:", book_titles)
    
    if st.button("Remove Book"):
        # Find and remove the selected book
        for i, book in enumerate(st.session_state.library):
            if book["title"] == selected_title:
                del st.session_state.library[i]
                st.success(f"Book '{selected_title}' removed successfully")
                break

def search_book():
    st.subheader("Search for a book")
    
    if not st.session_state.library:
        st.info("Your library is empty. There are no books to search.")
        return
    
    search_term = st.text_input("Enter search term:").lower()
    search_button = st.button("Search")
    
    if search_button and search_term:
        found_books = []
        
        for book in st.session_state.library:
            if (search_term in book["title"].lower() or 
                search_term in book["author"].lower() or 
                search_term in book["genre"].lower()):
                found_books.append(book)
        
        if found_books:
            st.success(f"Found {len(found_books)} book(s):")
            
            # Display found books in a table
            books_data = []
            for book in found_books:
                read_status = "Read" if book["read_status"] else "Not read"
                books_data.append({
                    "Title": book["title"],
                    "Author": book["author"],
                    "Year": book["publication_year"],
                    "Genre": book["genre"],
                    "Status": read_status
                })
            
            st.table(books_data)
        else:
            st.warning("No books found matching your search.")

def display_statistics():
    st.subheader("Library Statistics")
    
    if not st.session_state.library:
        st.info("Your library is empty. There are no statistics to display.")
        return
    
    total_books = len(st.session_state.library)
    read_books = 0
    
    for book in st.session_state.library:
        if book["read_status"]:
            read_books += 1
    
    not_read_books = total_books - read_books
    
    # Display basic statistics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Books", total_books)
    with col2:
        st.metric("Read Books", read_books)
    with col3:
        st.metric("Unread Books", not_read_books)

def main():
    choice = menu()
    
    if choice == "Add a book":
        add_book()
    elif choice == "Remove a book":
        remove_book()
    elif choice == "Search for a book":
        search_book()
    elif choice == "Display all books":
        display_books()
    elif choice == "Display statistics":
        display_statistics()
    elif choice == "Exit":
        st.write("To exit, simply close this browser tab.")

if __name__ == "__main__":
    main()