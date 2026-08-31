from books import manage_books


def show_main_menu():
    print("\n" + "=" * 40)
    print("       LIBRANEXUS")
    print("   Library Management System")
    print("=" * 40)

    print("1. Manage Books")
    print("2. Manage Members")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Search Books")
    print("6. Exit")

    print("=" * 40)


def main():
    while True:
        show_main_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            manage_books()

        elif choice == "2":
            print("\nManage Members selected.")

        elif choice == "3":
            print("\nBorrow Book selected.")

        elif choice == "4":
            print("\nReturn Book selected.")

        elif choice == "5":
            print("\nSearch Books selected.")

        elif choice == "6":
            print("\nThank you for using LibraNexus!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()