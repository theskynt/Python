class Car:
    def __init__(self, license, brand, color):
        self.license = license
        self.brand = brand
        self.color = color
        self.report = []

    def __str__(self):
        return "{} - {} {}".format(self.license, self.color, self.brand)

    def __lt__(self, rhs):
        return self.license > rhs.license

    def add_report(self, new_report):
        self.report.append(new_report)

    def totel_payment(self):
        totel_end = 0
        for totel in self.report :
            totel_end += int(totel[2])
        return totel_end

    def max_payment(self):
        if len(self.report) <= 0 :
            return self.report
        else :
            for sort in range(0, len(self.report)) :
                if sort+2 > len(self.report) :
                    break
                elif(int(self.report[sort][2]) < int(self.report[sort+1][2])) :
                    payment = self.report[sort+1]
                elif(int(self.report[sort][2]) > int(self.report[sort+1][2])) :
                    payment = self.report[sort]
            return payment

c1 = Car('AA1234','Honda','White')
c2 = Car('BB1234','Toyota','Red')
c1.add_report(('25 may 2017','change tires','1500'))
c1.add_report(('10 oct 2018','change engine','8500'))

#ข้อ1
#print(c1.license)
#print(c1.brand)
#print(c1.color)
#ข้อ2
#print(c1)
#ข้อ3
#print(c1 > c2)
#ข้อ4
#print(c1.totel_payment())
#ข้อ5
#print(c1.max_payment())

# ------------------------------------------------------------------------
class ShoppingCart:
    def __init__(self, id):
        self.id = id
        self.books = []

    def add_book(self, book, n, total):
        num = 0
        if len(self.books) == 0:
            self.books.append([book, n, total])
        else:
            for search_book in self.books:
                if book in search_book[0]:
                    search_book[1] += n
                    break
                elif book not in self.books :
                    num += 1
                    if num == len(self.books):
                        self.books.append([book, n, total])
                        break

    def delete_book(self, book):
        for delete in range(0, len(self.books)) :
            if book in self.books[delete] :
                self.books.pop(delete)
                break

    def get_total(self):
        max_total = 0
        for total in self.books:
            max_total += (total[1]*total[2])
        return max_total

    def __lt__(self, rhs):
        return self.get_total() < rhs.get_total()
        
        

guy = ShoppingCart(64015068)
guy.add_book('b1', 1, 100)
guy.add_book('b1', 4, 100)
guy.add_book('b2', 3, 200)
guy.add_book('b3', 4, 500)
guy.delete_book('b2')
guy.delete_book('b1')
print(guy.books)
print(guy.get_total())

pom = ShoppingCart(64015020)
pom.add_book('b1', 1, 100)
pom.add_book('b1', 4, 100)
pom.add_book('b2', 3, 200)
pom.add_book('b3', 4, 500)
print(pom.books)
print(pom.get_total())

print(guy > pom)