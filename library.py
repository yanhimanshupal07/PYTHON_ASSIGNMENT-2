books = {}
borrowed = {}

def add_book():
    print("\n--- Add New Book ---")
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    copies = int(input("Enter Number of Copies: "))

    books[book_id] = {
        "title": title,
        "author": author,
        "copies": copies
    }

    print("\nBook Added Successfully!")


def display_books():
    print("\n\t========= BOOK LIST =========")
    print("-" * 60)
    print(f"{'Book ID':<10} {'Title':<20} {'Author':<15} {'Copies':<10}")
    print("-" * 60)

    for b, d in books.items():
        print(f"{b:<10} {d['title']:<20} {d['author']:<15} {d['copies']:<10}")

    print("-" * 60)


def search_by_id(book_id):
    if book_id in books:
        print("\nBook Found:")
        print(books[book_id])
    else:
        print("\nBook Not Found")


def search_by_title(keyword):
    found = False
    for b, d in books.items():
        if keyword.lower() in d["title"].lower():
            print("\nBook Found:")
            print(b, d)
            found = True
    if not found:
        print("\nBook Not Found")


def borrow_book():
    print("\n--- Borrow Book ---")
    student = input("Enter Student Name: ")
    book_id = input("Enter Book ID: ")

    if book_id in books:
        if books[book_id]["copies"] > 0:
            books[book_id]["copies"] -= 1
            borrowed[student] = book_id
            print("\nBook Borrowed Successfully!")
            print(f"Remaining Copies: {books[book_id]['copies']}")
        else:
            print("\nNo Copies Available")
    else:
        print("\nInvalid Book ID")


def return_book():
    student = input("\nEnter Student Name: ")
    book_id = input("Enter Book ID to Return: ")

    if student in borrowed:
        if borrowed[student] == book_id:
            books[book_id]["copies"] += 1
            del borrowed[student]
            print("\nBook Returned Successfully!")
        else:
            print("\nBook ID does not match record")
    else:
        print("\nNo Borrowing Record Found")


def show_borrowed_list():
    print("\n\t=== Borrowed Books ===")
    borrowed_list = [f"{s} -> {b}" for s, b in borrowed.items()]
    for entry in borrowed_list:
        print(entry)
    if not borrowed_list:
        print("No Books Borrowed")


def save_to_csv():
    with open("books.csv", "w") as f:
        f.write("BookID,Title,Author,Copies\n")
        for b, d in books.items():
            f.write(f"{b},{d['title']},{d['author']},{d['copies']}\n")
    print("\nBooks Saved to books.csv")


def load_from_csv():
    try:
        with open("books.csv", "r") as f:
            data = f.readlines()[1:]
            for line in data:
                b, t, a, c = line.strip().split(",")
                books[b] = {"title": t, "author": a, "copies": int(c)}
        print("\nBooks Loaded Successfully!")
    except:
        print("\nCSV File Not Found")


def main_menu():
    while True:
        print("\n\n========== LIBRARY MENU ==========")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Borrowed List")
        print("7. Save to CSV (Bonus)")
        print("8. Load from CSV (Bonus)")
        print("9. Exit")

        choice = input("\nEnter Your Choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            display_books()
        elif choice == "3":
            print("\nSearch Options:")
            print("a. By ID")
            print("b. By Title")
            sc = input("Choose option: ")
            if sc == "a":
                search_by_id(input("Enter Book ID: "))
            else:
                search_by_title(input("Enter Title Keyword: "))
        elif choice == "4":
            borrow_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            show_borrowed_list()
        elif choice == "7":
            save_to_csv()
        elif choice == "8":
            load_from_csv()
        elif choice == "9":
            print("\nExiting Program... Goodbye!")
            break
        else:
            print("\nInvalid Choice. Try Again.")


main_menu()
