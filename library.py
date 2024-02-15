
class Library:
    def __init__ (self):
        self.f = open("books.txt", "a+")
    def __del__(self):
        self.f.close()
    def ListBooks(self):
        self.f.seek(0)
        list = self.f.read().splitlines()
        for each in list:
            words =each.split(",")
            print(words[0], words[1])
    def AddBook(self):
        bookName = input("Book title\n")
        bookAuthor = input("Book author\n")
        year = input("Release year\n")
        pages = input("Pages\n")
        toplamveri = (f"{bookName}, {bookAuthor}, {year}, {pages}\n")
        print(toplamveri)
        self.f.write(toplamveri)
    def RemoveBook(self):
        self.f.seek(0)
        bookName = input("Book name: ")
        list = self.f.read().splitlines()
        for each in list:
            words = each.split(",")
            if bookName == words[0]:
                list.remove(each)
                break
        self.f.seek(0)
        self.f.truncate()
        for each in list:
            self.f.write(f"{each}\n")
lib = Library()

while(True):
    print("***MENU***\n" "1) List Books\n" "2) Add Book\n" "3) Remove Book\n" "4) QUİT\n")
    user = input("Seçiniz ")
    if user == "a":
        lib.ListBooks()
    elif user == "b":
        lib.AddBook()
    elif  user == "c":
        lib.RemoveBook()
    elif user == "q":
        break
    else :
        print("Bitti")