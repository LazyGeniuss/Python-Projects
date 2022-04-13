# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book
#
# HarryLibrary = Library(listofbooks, library_name)
#
# dictionary (books-nameofperson)
#
# create a main function and run a infinite loop asking users for their input

class Library:
    # list_of_books = []
    # library_name = ""
    def __init__(self, list_of_books, library_name):
        self.list_of_books = list_of_books
        self.library_name = library_name
        self.lenderslist = {}
        # self.bookname = list_of_books
        # self.lendersname = lendersname

    # @classmethod
    def displaybooks(self):
        print(f"{self.list_of_books}")

    def diplaylenderslist(self):
        print(f"{self.lenderslist}")

    # @classmethod
    def lendbooks(self, bookname, lendersname):
        for item in self.lenderslist:
            if item == bookname:
                 print(f"The book is already taken by {self.lenderslist[bookname]}\n")
                 return
        print(f"the {bookname} has been taken by {lendersname}\n")
        self.lenderslist.update({bookname:lendersname})
        self.list_of_books.remove(bookname)

    # @classmethod
    def addbook(self, bookname):
        print(f"The {bookname} is added successfully in Library\n")
        self.list_of_books.append(bookname)

    # @classmethod
    def returnbook(self, bookname, lendersname):
        print(f"The {bookname} has been returned by {lendersname}\n")
        self.list_of_books.append(bookname)
        self.lenderslist.pop(bookname)

shreyash = Library(["book1" , "book2", "book3", "book4"], "My Library")
print("-------------------LIBRARY MANAGEMENT SYSTEM-----------------------")
while(1):
    a = int(input("Enter 1 to display books\n"
          "Enter 2 to lend books\n"
          "Enter 3 to add book\n"
          "Enter 4 to return books\n"
            "Enter 5 to display lender's list\n"
            "Enter 0 to exit the program\n"))
    if a==1:
        shreyash.displaybooks()
    elif a==2:
        bookname = input("Enter the name of book\n")
        lendersname = input("Enter the name of lender\n")
        shreyash.lendbooks(bookname,lendersname)
    elif a==3:
        bookname = input("Enter the name of book\n")
        shreyash.addbook(bookname)
    elif a==4:
        bookname = input("Enter the name of book\n")
        lendersname = input("Enter the name of lender\n")
        shreyash.returnbook(bookname, lendersname)
    elif a==5:
        shreyash.diplaylenderslist()
    elif a==0:
        break
    else:
        print("Invalid Input\n")
