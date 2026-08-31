# Temporary list to store books
books = []


def add_book():
    print("\n--- ADD NEW BOOK ---")

    title = input("Enter book title: ")
    author = input("Enter author name: ")
    category = input("Enter category: ")

    while True:
        try:
            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Quantity must be greater than 0.")
            else:
                break

        except ValueError:
            print("Please enter a valid number.")

    book = {
        "id": len(books) + 1,
        "title": title,
        "author": author,
        "category": category,
        "quantity": quantity,
        "available": quantity
    }

    books.append(book)

    print("\nBook added successfully!")


def view_books():
    print("\n--- ALL BOOKS ---")

    if not books:
        print("No books available.")
        return

    for book in books:
        print("\n" + "-" * 30)
        print(f"Book ID: {book['id']}")
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Category: {book['category']}")
        print(f"Total Quantity: {book['quantity']}")
        print(f"Available: {book['available']}")
        print("-" * 30)


def manage_books():
    while True:
        print("\n" + "=" * 40)
        print("        BOOK MANAGEMENT")
        print("=" * 40)

        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Back to Main Menu")

        print("=" * 40)

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            view_books()

        elif choice == "3":
            print("\nSearch Book feature coming next.")

        elif choice == "4":
            print("\nUpdate Book feature coming next.")

        elif choice == "5":
            print("\nDelete Book feature coming next.")

        elif choice == "6":
            break

        else:
            print("\nInvalid choice. Please try again.")