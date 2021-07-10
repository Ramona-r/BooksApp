def add_book():
    print("Add a book option")


def list_books():
    print("List books option")


def update_book():
    print("Update a book option")


def share_book():
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
