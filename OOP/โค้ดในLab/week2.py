class Book:
    _counter = 1

    def __init__(self, title, subject, dds_number):
        self._isbn = Book._counter
        self._authors = []
        self._title = title
        self._subject = subject
        self._dds_number = dds_number
        Book._counter += 1

    @property #isbn
    def isbn(self):
        return self._isbn
    
    @property #author
    def authors(self):
        return self._authors
    def add_author(self, author_obj):
        self._authors.append(author_obj)
 
    @property #title
    def title(self):
        return self._title
    @title.setter
    def title(self, new_value):
        self._title = new_value

    @property #subject
    def subject(self):
        return self._subject

    @property #dds
    def DDSnumber(self):
        return self._dds_number

    def delete(self):
        del self._isbn
        del self._authors
        del self._title
        del self._subject
        del self._dds_number 

class Author:
    def __init__(self, name):
        self._name = name

    @property #name
    def name(self):
        return self._name

class Catalog:
    book_list = []
    
    def search(self, key):
        global search_result
        search_result = []
        counter = 0
        for book in self.book_list:
            if key in str(book.isbn):
                search_result.append(book)
                counter += 1
            elif key in book.title:
                search_result.append(book)
                counter += 1
            elif key in book.subject:
                search_result.append(book)
                counter += 1
            elif key in book.DDSnumber:
                search_result.append(book)
                counter += 1
            for author in book.authors:
                if key in author.name:
                    search_result.append(book)
                    counter += 1
        if counter == 0: print('Search not found anything!')
        Catalog.display(catalog, search_result)

    def delete(self, isbn):
        if isinstance(isbn, int):
            for book in self.book_list:
                if(book.isbn == isbn):
                    self.book_list.remove(book)
                    Book.delete(book)
        else:
            print('Delete Fail!')

    def display(self, list_book):
        for book in list_book:
            print('ISBN :', book.isbn)
            print('Title :', book.title)
            print('Subject :', book.subject)
            print('Authors :')
            for item in book.authors:
                print('   ', item.name)
            print('DDS number :', book.DDSnumber)
            print('-------------------------------')


catalog = Catalog() #create library

#Create authors
author1 = Author('ชิษ')
author2 = Author('รน')
author3 = Author('ปักกา')

#create Books
A = Book('ทำลาบ','อาหาร','0001')
A.add_author(author1)
A.add_author(author3)
B = Book('ชงเหล้า','อาหาร','0002')
B.add_author(author2)
C = Book('ปลูกต้นไม้','ต้นไม้','0003')
C.add_author(author3)
D = Book('คนเจียงใหม่','ท่องเที่ยว','0004')
D.add_author(author1)

#Add to library
catalog.book_list.append(A)
catalog.book_list.append(B)
catalog.book_list.append(C)
catalog.book_list.append(D)

#Test search
catalog.search('01')
catalog.delete(4)
print('\n\n\n')
catalog.search('4')
print('\n\n\n')
catalog.search('0')