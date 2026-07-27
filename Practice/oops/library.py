class LibraryItem:
    __slots__ = ['title', 'item_id']

    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id

    def get_info(self):
        return f"Item: {self.title} | ID: {self.item_id}"


class Borrowable:
    def __init__(self):
        self.is_borrowed = False

    def borrow(self, user):
        if self.is_borrowed:
            print(f"'{self.title}' is already borrowed!")
        else:
            self.is_borrowed = True
            print(f"'{self.title}' borrowed by {user}")

    def return_item(self):
        self.is_borrowed = False
        print(f"'{self.title}' returned successfully!")


class Book(LibraryItem, Borrowable):
    def __init__(self, title, item_id, author):
        LibraryItem.__init__(self, title, item_id)
        Borrowable.__init__(self)
        self.author = author

    def __str__(self):
        available = "No" if self.is_borrowed else "Yes"
        return f"Book: {self.title} | Author: {self.author} | Available: {available}"

    def __eq__(self, other):
        return self.item_id == other.item_id


class Magazine(LibraryItem, Borrowable):
    def __init__(self, title, item_id, issue_number):
        LibraryItem.__init__(self, title, item_id)
        Borrowable.__init__(self)
        self.issue_number = issue_number

    def __str__(self):
        available = "No" if self.is_borrowed else "Yes"
        return f"Magazine: {self.title} | Issue: {self.issue_number} | Available: {available}"


class Library:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Added: {item.title}")

    def find_by_title(self, title):
        for item in self.items:
            if item.title == title:
                return item
        return None

    def show_all(self):
        print("\n--- Library Collection ---")
        for item in self.items:
            print(item)

    def __len__(self):
        return len(self.items)


# Test
b1 = Book("Python Basics", "001", "Aryan")
b2 = Book("Clean Code", "002", "Robert")
m1 = Magazine("Tech Today", "003", 42)

lib = Library()
lib.add_item(b1)
lib.add_item(b2)
lib.add_item(m1)

print(f"\nTotal items: {len(lib)}")
lib.show_all()

print()
b1.borrow("Ramu")
print(b1)
b1.borrow("Shyam")
b1.return_item()
print(b1)

print("\nInspecting b1:")
try:
    print(b1.__dict__)         # __slots__ ki wajah se error!
except AttributeError as e:
    print(f"__dict__ not available: {e}")

found = lib.find_by_title("Python Basics")
print(f"\nFound: {found}")