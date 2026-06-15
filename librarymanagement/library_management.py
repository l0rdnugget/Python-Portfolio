def main():
    """
 ACOTAR/Romantasy themed    """
    library = [
        {"title": "A Court of Thorns and Roses", "author": "Sarah J. Maas", "copies": 3},
        {"title": "A Court of Mist and Fury", "author": "Sarah J. Maas", "copies": 2},
        {"title": "A Court of Silver Flames", "author": "Sarah J. Maas", "copies": 1},
        {"title": "Fourth Wing", "author": "Rebecca Yarros", "copies": 4},
        {"title": "Iron Flame", "author": "Rebecca Yarros", "copies": 2},
        {"title": "A Dawn of Onyx", "author": "Kate Golden", "copies": 3},
        {"title": "A Promise of Peridot", "author": "Kate Golden", "copies": 2},
        {"title": "A Reign of Rose", "author": "Kate Golden", "copies": 2},
        {"title": "The Serpent and the Wings of Night", "author": "Carissa Broadbent", "copies": 3},
        {"title": "The Ashes and the Star-Cursed King", "author": "Carissa Broadbent", "copies": 2},
        {"title": "The Songbird and the Heart of Stone", "author": "Carissa Broadbent", "copies": 2},
        {"title": "The Fallen and the Kiss of Dusk", "author": "Carissa Broadbent", "copies": 2},
    ]

    print("=" * 50)
    print("   Welcome to the Velaris Reading Wing")
    print("        Library Management System")
    print("=" * 50)

    while True:
        print("\n--- Library Menu ---")
        print("1. Add New Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Display Inventory")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_book(library)
        elif choice == "2":
            borrow_book(library)
        elif choice == "3":
            return_book(library)
        elif choice == "4":
            display_inventory(library)
        elif choice == "5":
            print("\nMay the stars light your way home. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number 1-5.")


def add_book(library):
    title = input("Enter the book title: ").strip()
    while title == "":
        print("Title cannot be empty.")
        title = input("Enter the book title: ").strip()

    for book in library:
        if book["title"].lower() == title.lower():
            while True:
                copies_input = input(f"'{title}' already exists. How many copies to add? ").strip()
                if copies_input.isdigit() and int(copies_input) > 0:
                    book["copies"] += int(copies_input)
                    print(f"Updated '{title}' to {book['copies']} copies.")
                    return
                else:
                    print("Number of copies must be a positive whole number.")

    author = input("Enter the author's name: ").strip()
    while author == "":
        print("Author cannot be empty.")
        author = input("Enter the author's name: ").strip()

    while True:
        copies_input = input("Enter the number of copies: ").strip()
        if copies_input.isdigit() and int(copies_input) > 0:
            copies = int(copies_input)
            break
        else:
            print("Number of copies must be a positive whole number.")

    new_book = {"title": title, "author": author, "copies": copies}
    library.append(new_book)
    print(f"'{title}' by {author} added with {copies} copies.")


def borrow_book(library):
    title = input("Enter the title of the book to borrow: ").strip()
    while title == "":
        print("Title cannot be empty.")
        title = input("Enter the title of the book to borrow: ").strip()

    for book in library:
        if book["title"].lower() == title.lower():
            if book["copies"] > 0:
                book["copies"] -= 1
                print(f"You borrowed '{book['title']}'. {book['copies']} copies remaining.")
            else:
                print(f"Sorry, '{book['title']}' is currently out of stock.")
            return

    print(f"'{title}' was not found in the library.")


def return_book(library):
    title = input("Enter the title of the book to return: ").strip()
    while title == "":
        print("Title cannot be empty.")
        title = input("Enter the title of the book to return: ").strip()

    for book in library:
        if book["title"].lower() == title.lower():
            book["copies"] += 1
            print(f"'{book['title']}' returned. {book['copies']} copies now available.")
            return

    print(f"'{title}' was not found in the library.")


def display_inventory(library):
    if not library:
        print("\nThe library is currently empty.")
        return

    print("\n--- Library Inventory ---")
    print(f"{'Title':<35} {'Author':<25} {'Copies':<6}")
    print("-" * 68)
    for book in library:
        print(f"{book['title']:<35} {book['author']:<25} {book['copies']:<6}")


main()
