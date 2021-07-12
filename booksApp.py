def add_book():
    book_name = input("Insert a book name -> ")
    author_name = input("Insert an author name -> ")
    # import csv library
    import csv
    # standard implementation from the csv library
    with open("booksDB.csv", mode="w") as file:
        # insert the table header
        writer = csv.DictWriter(file, fieldnames=[
            "BookName", "AuthorName", "SharedWith", "IsRead"
        ])
        # add content to each option
        writer.writerow({"BookName": book_name,
                         "AuthorName": author_name,
                         "SharedWith": 'None',
                         "IsRead": False
                         })

        print("Book was added successfully")


def list_books():
    import csv
    with open("booksDB.csv", mode="r") as file:
        # extract all the data from the data base
        rows = csv.DictReader(file, fieldnames=("BookName", "AuthorName", "SharedWith", "IsRead"))
        # each row/element is go through one by one
        for row in rows:
            # print(f"The book name is: {row.get('BookName')}")
            # print(f"The author name is: {row.get('AuthorName')}")
            # print(f"The book is shared with: {row.get('SharedWith')}")
            # print(f"The book is read: {row.get('IsRead')}")

            # we use the formatted version
            print(
                f"Book name is: {row.get('BookName')}, Author Name: {row.get('AuthorName')}, "
                f"Is Shared: {row.get('ShareWith')}, Is Read {row.get('IsRead', False )}.")


def update_book():
    book_name = input("Enter the book name: ")
    book_read = input("Is the book read? (Y/N)?")
    if book_read == "Y":
        book_read = True
    else:
        book_read = False
    import csv
    rows = []
    with open("booksDB.csv", mode="r") as file:
        rows = list(csv.DictReader(file, fieldnames=["BookName", "AuthorName", "SharedWith", "IsRead"]))
        for row in rows:
            # we are looking for a key/book in dictionary using get
            if row.get("BookName") == book_name:
                row["IsRead"] = book_read
                break
    # open csv file with write mode
    with open("booksDB.csv", mode="w") as file:
        csv_writer = csv.DictWriter(file, fieldnames=[
            "BookName", "AuthorName", "SharedWith", "IsRead"
        ])
        csv_writer.writerows([{"BookName": row.get("BookName"),
                               "AuthorName": row.get("AuthorName"),
                               "SharedWith": row.get("SharedWith"),
                               "IsRead": book_read
                               }])
    print("Book was updated successfully.")


def share_book():
    book_name = input("Enter the book that you want to share ->")
    shared_with = input("Who do you want to share the book with?")
    import csv
    with open("booksDB.csv", mode="r") as file:
        rows = list(csv.DictReader(file, fieldnames=("BookName", "AuthorName", "SharedWith", "IsRead")))
        for row in rows:
            if row["BookName"] == book_name:
                row["SharedWith"] = shared_with
                break
            else:
                print("The book is not in DB")
        with open("booksDB.csv", mode="w") as file:
            csv_writer = csv.DictWriter(file, fieldnames=[
                "BookName", "AuthorName", "SharedWith", "IsRead"
            ])
            csv_writer.writerow({"BookName": row.get("BookName"),
                                 "AuthorName": row.get("AuthorName"),
                                 "SharedWith": shared_with,
                                 "IsRead": row.get("IsRead")}
                                )
    print("Share a book option")


# Main menu for user
print("Menu: ")
print("1: Add a book")
print("2: List books")
print("3: Update book")
print("4: Share book")
option = int(input("Select one option -> "))

# we set the decisions according to the user's option
if option == 1:
    add_book()
elif option == 2:
    list_books()
elif option == 3:
    update_book()
elif option == 4:
    share_book()
else:
    print("Not a valid option.")
