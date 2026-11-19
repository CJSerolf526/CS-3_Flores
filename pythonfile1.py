class Library:
  def __init__(self, name: str):
    self.name = name

  def borrow_book(self, *args):
    if len(args) == 1:
      title = args[0]
      borrower = "Not Specified"
      days = 7
      print(f"Book: {title}")
      print(f"Borrower: {borrower}")
      print(f"Borrowing Period: {days} days\n")

    elif len(args) == 2:
      title, borrower = args
      days = 7
      print(f"Book: {title}")
      print(f"Borrower: {borrower}")
      print(f"Borrowing Period: {days} days\n")

    elif len(args) == 3:
      title, borrower, days = args
      print(f"Book: {title}")
      print(f"Borrower: {borrower}")
      print(f"Borrowing Period: {days} days\n")

library = Library("PSHS-EVCL Library")
library.borrow_book("Noli Me Tangere")
library.borrow_book("El Filibusterismo", "Maria")
library.borrow_book("Florante at Laura", "Jose", 14)
