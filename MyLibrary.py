class Book :
    def __init__(self , bookName , writer , isbn , status , jenre ) :
        self.bookName=bookName
        self.writer=writer
        self.isbn=isbn
        self.status=bool(status)
        self.jenre=jenre
# -------------------------------------------------------------
    def __str__(self):
        return f"BookName : {self.bookName}\t\t\tWriter : {self.writer}\t\t\tISBN : {self.isbn}\t\t\t Borrowed : {self.status}"
#*********************************"""New Class"""*********************************

class Member :
    def __init__(self , name , id) :
        self.name=name
        self.id=id
        self.borrowedBookList=[]
        self.memberInfo={}
#///////////////////////////////////////"""Shows their Borrowed Books"""///////////////////////////////////////
    def borrowedBooks(self , bookName) :
            if bookName in self.borrowedBookList:
                print("Book Already Borrowed ")
            else:
                self.borrowedBookList.append(bookName)
                return self.borrowedBookList
#///////////////////////////////////////"""Removes Returned Books"""///////////////////////////////////////
    def returnBooks(self, bookName):
        if bookName in self.borrowedBookList:
            self.borrowedBookList.remove(bookName)
            print("Book Removed !")
            return True
        else:
            print("Book Does Not Exist !")
        return False
# -------------------------------------------------------------
    def __str__(self):
        return f"Name :{self.name}\t\t\tID: {self.id}\t\t\tBorrowedBooks: {self.borrowedBookList}"
#*********************************"""New Class"""*********************************
class Library :
    def __init__(self ,libraryName) :
        self.LibraryName=libraryName
        self.books={}
        self.members={}
        self.jenre=set()
#///////////////////////////////////////"""Adds Book to the Library"""///////////////////////////////////////
    def AddBook(self) :
        number=int(input("How Many Books do You Want to Add ?"))
        for i in range(number) :
            name=input("Enter BookName :")
            writer=input("Enter Writer :")
            status=input("Is it Available : (True/False)")
            status=(status=="True")
            isb=input("Enter isbn :")
            jenre=input("Enter jenre :")

            self.books[isb]=Book(name , writer , isb,  status , jenre)
            print(f"{name} Added!")
        return self.books
#///////////////////////////////////////"""Adds Member to the Library"""///////////////////////////////////////
    def AddMember (self):
        try :
            mem=int(input("How Many People do You Want to Add ?"))
        except ValueError:
            print("Please Enter a Valid Number")
            return self.members
        for m in range (mem) :
            name=input("Enter Name :")
            id=input("Enter id :")
            self.members[id]=Member(name , id)
            print(f"{name} Added!")
        return self.members
#///////////////////////////////////////"""Gets Jenres"""///////////////////////////////////////
    def EnterJenre(self) :
        try :
            number=int(input("How many Jenres do we have ? "))
        except ValueError:
            print("Please Enter a Valid Number")
            return self.jenre
        for n in range (number) :
            janre=input("Enter Janare : ")
            self.jenre.add(janre)
        return self.jenre
#///////////////////////////////////////"""Lends Books to Members"""///////////////////////////////////////
    def LendBook(self):
        isbn=input("Enter ISBN :")
        memberID=input("Enter Member ID :")
        if isbn in self.books :
            book=self.books[isbn]
            if book.status==True:
                if memberID in self.members:
                    book.status = False
                    member = self.members[memberID]
                    member.borrowedBookList.append(isbn)
                    print(f"Book Lended to {memberID}!")
                else:
                    print("Member not found")
            else:
                print("Book Not Available")
        else:
            print("Book not found")                   
#///////////////////////////////////////"""Returns Books from Members"""///////////////////////////////////////
    def returnBook(self):
        isbn = input("Enter ISBN :")
        if isbn in self.books:
            book = self.books[isbn]
            memberID = input("Enter Member Id :")
            if memberID in self.members:
                member = self.members[memberID]
                success = member.returnBooks(isbn)
                if success:
                    book.status = True
                    print("Book Returned !")
                else:
                    print("This book was not borrowed by this member")
            else:
                print("Member Not Found!")
        else:
            print("Book Not Found!")
#///////////////////////////////////////"""Searches Writers"""///////////////////////////////////////
    def searchByWriter (self) :
        res=[]
        name=input("Enter Writer Name :")
        for isbn in self.books :
            book=self.books[isbn]
            if book.writer==name :
                res.append(book)
        if res:
            print("BookName : ")
            return res
        else:
            print("Writer Not Found !")
            return res
#///////////////////////////////////////"""Shows Available Books"""///////////////////////////////////////
    def availableBooks (self) :
        avblBooks=[]
        for isbn in self.books :
            book=self.books[isbn]
            if book.status==True :
                avblBooks.append(book)
        print("Available books : ")
        return avblBooks
#///////////////////////////////////////"""Shows the Most Active Member"""///////////////////////////////////////
    def mostActiveMember(self):
        maxCount = 0
        activeMember = None
        for memberID in self.members:
            member = self.members[memberID]
            count = len(member.borrowedBookList)
            if count > maxCount:
                maxCount = count
                activeMember = member
        print(f"{activeMember} is ActiveMember :")
        return activeMember
# -------------------------------------------------------------
    def __str__(self) :
        booksInfo = ""
        for isbn in self.books:
            booksInfo += str(self.books[isbn]) + "\n"
        return f"Library: {self.LibraryName}\n{booksInfo}"
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
lib = Library(input("Enter Library Name :"))
def main():
    while True:
        print("""
1. Add Book
2. Add Member
3. Lend Book
4. Return Book
5. Search by Writer
6. Available Books
7. Most Active Member
8. Exit
""")
        choice = input("Choose an option :")
        if choice == "1":
            lib.AddBook()
        elif choice == "2":
            lib.AddMember()
        elif choice == "3" :
            lib.LendBook()
        elif choice == "4" :
            lib.returnBook()
        elif choice == "5" :
            results = lib.searchByWriter()
            print("BookName :")
            for book in results:
                print(book)
        elif choice == "6" :
                avl=lib.availableBooks()
                for book in avl:
                    print(book)
        elif choice == "7" :
                lib.mostActiveMember()
        elif choice == "8":
            print("GoodBye")
            break
        else:
            print("Invalid option")
        x = int(input("Press '1' to continue / 0 to Exit :"))
        if x == 0:
            break
main()