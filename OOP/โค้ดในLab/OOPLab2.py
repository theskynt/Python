class Author ():
    name = ["Wanburhan","Chidsanupong"]


class Catalog ():
    def __init__ (self,search):
        self.search = search
        for i in Blist:
            if self.search == i.title:
                print (i)
            elif self.search == i.authors:
                print (i)
            elif self.search == i._dds_number:
                print (i)
            elif self.search == i._isbn:
                print (i)

class Book ():
    isbn = 1
    _Booklist = []
    def __init__(self, authors , title ,subject , dds_number):
        self._isbn = Book.isbn
        self.authors = authors
        self.title = title
        self.subject = subject
        self._dds_number = dds_number
        Book.isbn +=1
        self._Booklist.append([self._isbn,self.authors,self.title,self.subject,self._dds_number])
        # print (self._Booklist)

    def __str__(self):
        return f'{ self._isbn,self.authors,self.title,self.subject,self._dds_number}'
    
    def get_dds_number (self):
        return self._dds_number
    def set_dds_number (self , new_dds_number):
        if isinstance (new_dds_number, int):
            self._dds_number = new_dds_number

    dds_number = property(get_dds_number , set_dds_number)

book1 = Book (Author.name[0]+","+Author.name[1], "Math1999" , "Math" , 10)
print (book1)
book2 = Book (Author.name[1], "Chemecal" , "scient" , 20)
print (book2)
Author.name.append("Phongpipat")
# print (Author.name)
book3 = Book (Author.name[2], "Art" , "Art" , 30)
print (book3)
Author.name.append("Narunart")
book4 = Book (Author.name[3], "Digital Hardware" , "computer" , 40)
print (book4)
book5 = Book (Author.name[0], "Gamer" , "computer" , 40)
book5.dds_number = 50
print (book5)
Book._Booklist.pop(3)
print(Book._Booklist)
Blist = [book1,book2,book3,book4,book5]
People = Catalog("Math1999")



