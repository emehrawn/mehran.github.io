#not completed
class Book():
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price

class MyBook(Book):
    def __init__(self,title,author,price):
        Book.__init__(self,title,author)
        self.price = price
    def display(self):
        print("Title: " + self.title)
        print("Author: " + self.author)
        print("Price: " + str(self.price))