# ข้อ 1 
x = int(input("enter x number : "))
if x%5 == 0 :
    print(x, "is divisible by 5")
else :
    print(x, "is not divisible by 5")

# ข้อ 2
x = int(input("enter x number : "))
if 80 <= x <= 100 :
    print(x, "ได้เกรด G")
elif 50 <= x < 80 :
    print(x, "ได้เกรด P")
elif 0 <= x < 50 :
    print(x, "ได้เกรด F")
elif 0 > x :
    print("Error")

# ข้อ 3
mid = int(input("Mid-term = "))
final = int(input("Final-term = "))
hw = int(input("Homework = "))

mmid = (mid/100)*40
ffinal = (final/100)*50
hhw = (hw/100)*10
x = mmid+ffinal+hhw

if 0 <= x < 50 :
    print("Error")
elif 0 <= x < 50 :
    print("F")
elif 50 <= x < 55 :
    print("D")
elif 55 <= x < 60 :
    print("D+")
elif 60 <= x < 70 :
    print("C")
elif 70 <= x < 80 :
    print("C+")
elif 80 <= x < 85 :
    print("B")
elif 85 <= x < 90 :
    print("B+")
elif 90 <= x <= 100 :
    print("A")

# ข้อ 4
x = int(input("X = "))
y = int(input("Y = "))

if x > y :
    print("Maximum = X",x)
else :
    print("Maximum = Y",y)

# ข้อ 5
a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))

if  a > b and a < c or a < b and a > c :
     print("ค่ากลาง = ",a)
else :
    if  b > a and b < c or b < a and b > c :
     print("ค่ากลาง = ",b)
    else :
         if  c > a and c < b or c < a and c > b :
             print("ค่ากลาง = ",c)

# ข้อ 6
age = int(input("age = "))

if age < 0 :
    print("Error")
elif age <= 10 :
    print(age, "Children")
elif age <= 20 :
     print(age, "Teenage")
elif age <= 35 :
     print(age, "Adult")
elif age <= 55 :
     print(age, "Middle age")
else :
    print(age, "Old age")

# ข้อ 7
select = int(input("1.(Rectangle) or 2.(Triangle): "))

if select == 1 :
    width = int(input("Width = "))
    length = int(input("length = "))
    sum1 = width*length
    print("Rectangle Area = ",sum1)
elif select == 2 :
    base = int(input("Base = "))
    height = int(input("Height = "))
    sum2 = (0.5)*base*height
    print("Triangle Area = ",sum2)

# ข้อ 8 
x = int(input("Enter a number : "))
xx = x-1
list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
print("Month = ",list[xx])

# ข้อ 9 
n = int(input("Enter an integer N = "))
if n < 0 :
    n = n*-1
num = n%10
list = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
print(num,list[num])

# ข้อ 10
year = int(input("Enter Year = "))

if year < 0 :
    print("Error")
elif year%400 == 0 and year%4 == 0 :
    print("Leap year")
elif year%100 != 0 and year%4 == 0 :
    print("Leap year")
else :
    print("Not Leap year")


# ข้อ 11 
num1,num2,num3,num4,num5 = input("Enter Number = ").split()
num_1 = int(num1)
num_2 = int(num2)
num_3 = int(num3)
num_4 = int(num4)
num_5 = int(num5)
if num_1<num_2<num_3<num_4<num_5 :
    print("True")
else :
    print("False") 
# ข้อ12 
num1,num2,num3,num4 = input("Enter Number = ").split()
num_1 = int(num1)
num_2 = int(num2)
num_3 = int(num3)
num_4 = int(num4)

sum1 = num_1+num_2+num_3+num_4

if  num_1>num_2 and num_1>num_3 and num_1>num_4 :
    nummax = num_1
elif num_2>num_1 and num_2>num_3 and num_2>num_4:
    nummax = num_2
elif num_3>num_1 and num_3>num_2 and num_3>num_4:
    nummax = num_3
elif num_4>num_1 and num_4>num_2 and num_4>num_3:
    nummax = num_4
if num_1<num_2 and num_1<num_3 and num_1<num_4:
    nummin = num_1
elif num_2<num_1 and num_2<num_3 and num_2<num_4:
    nummin = num_2
elif num_3<num_1 and num_3<num_2 and num_3<num_4:
    nummin = num_3
elif num_4<num_1 and num_4<num_2 and num_4<num_3:
    nummin = num_4

sum = sum1 - nummax - nummin
print("sum : ",sum)

# ข้อ13
select_pizza = int(input("1.ถาดเล็ก 99 บาท \n2.ถาดกลาง 199 บาท \n3.ถาดใหญ่ 299 บาท \n: "))
money=0
if select_pizza == 1 :
    money = money + 99
    cheese_1 = input("เพิ่มซีสไหม[Y/N] \n: ")
    if cheese_1 in "Yy"  :
        money = money + 20
    elif cheese_1 in "Nn" :
        money = money        
    else :
        money = "Error"

    face_1 = input("เพิ่มหน้าไหม[Y/N] \n: ")
    if face_1  in "Yy" :
        money = money + 20
    elif face_1 in "Nn":
        money = money
    else :
        money = "Error"        

if select_pizza == 2 :
    money = money + 199
    cheese_2 = input("เพิ่มซีสไหม[Y/N] \n: ")
    if cheese_2 in "Yy"  :
        money = money + 30
    elif cheese_2 in "Nn" :
        money = money        
    else :
        money = "Error"

    face_2 = input("เพิ่มหน้าไหม[Y/N] \n: ")
    if face_2  in "Yy" :
        money = money + 20
    elif face_2 in "Nn":
        money = money
    else :
        money = "Error"

if select_pizza == 3 :
    money = money + 299
    cheese_3 = input("เพิ่มซีสไหม[Y/N] \n: ")
    if cheese_3 in "Yy"  :
        money = money + 40
    elif cheese_3 in "Nn" :
        money = money        
    else :
        money = "Error"

    face_3 = input("เพิ่มหน้าไหม[Y/N] \n: ")
    if face_3  in "Yy" :
        money = money + 20
    elif face_3 in "Nn":
        money = money
    else :
        money = "Error"  
print(f"money = {money}") 
 
 
 