class BookNotAvailableError(Exception):
    pass


try:
    available_books = ["Python", "Java", "Django", "HTML"]

    book = input("Enter book name: ")

    if book not in available_books:
        raise BookNotAvailableError("Book is not available in the library.")

    print("Book is available.")

except BookNotAvailableError as e:
    print("Error:", e)