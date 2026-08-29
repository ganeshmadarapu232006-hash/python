class Book:
    def __init__(self, title, author, price, pages):
        self.title = title
        self.author = author
        self.price = price
        self.pages = pages

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("Pages:", self.pages)
        print()

book1 = Book("Python Programming", "John Smith", 500, 350)
book2 = Book("Web Development", "David Miller", 450, 300)
book3 = Book("Data Science", "Robert Brown", 600, 400)

book1.display()
book2.display()
book3.display()