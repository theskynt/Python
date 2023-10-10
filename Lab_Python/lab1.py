# ข้อ1 
b = int(input("Base : "))
h = int(input("Height : "))
area = (0.5*h*b)
print("Area : ",area)

# ข้อ2
r = int(input("Radius : "))
h = int(input("Height : "))
sum = 3.14*r*r*h
print("Volume : ",sum)

# ข้อ3
h = int(input("Hour : "))
m = int(input("Min : "))
s = int(input("Sec : "))

print(f"{h:02d}:{m:02d}:{s:02d}")

# ข้อ 4
m = int(input("Mid-term : "))
f = int(input("Final : "))
h = int(input("Homework : "))
sum = ((m/100)*40)+((f/100)*50)+((h/100)*10)
print("Total : ",sum)

# ข้อ5 
x1 = int(input("num1 : "))
x2 = int(input("num2 : "))
x3 = int(input("num3 : "))
x4 = int(input("num4 : "))

mean = (x1+x2+x3+x4)/4
print("mean",mean )

# ข้อ6
x1,x2,x3,x4,x5 = input("Input : ").split()

mean =(float(x1)+float(x2)+float(x3)+float(x4)+float(x5))/5

print("mean : "+'%.3f' %mean)

# ข้อ7

a,b,c = input("Input : ").split()
c=int(c)
d=(a+b)*c 
c=str(c)
print("Output : ",a+b+c+d)

# ข้อ8
id = input("Student ID :")
nn = input("Name :")

yy =(id[0]+id[1])
ll =(id[4:])

print("Student ID :",id)
print("Name :",nn)
print("Year Entry :",yy)
print("Last 4 Didit :",ll)
print("Department : Computer Engineering ")

# ข้อ9
a = float(input("a : "))
b = float(input("b : "))
c = float(input("c : "))

x1 = (((-b)+((b**2)-(4*a*c))**0.5)/2*a)
x2 = (((-b)-((b**2)-(4*a*c))**0.5)/2*a)

print("sum1 :",x2)
print("sum2 :",x1)

# ข้อ10
id = input("ID : ")

aa =((int(id[0])*13)+(int(id[1])*12)+(int(id[2])*11)+(int(id[3])*10)+(int(id[4])*9)+(int(id[5])*8)+(int(id[6])*7)+(int(id[7])*6)+(int(id[8])*5)+(int(id[9])*4)+(int(id[10])*3)+(int(id[11])*2))

bb = aa%11
cc = 11-bb

print("sum",cc)

# ข้อพิเศษ
# ******************************
# ex.input : "orange green yello"
#      output : 16
# ******************************
a = (input("input : ").split())
b = len(a[0])
c = len(a[1])
d = len(a[2])
f = b+c+d
print("output",f)
# ข้อพิเศษ
# ******************************
# input: 0:0:0:apple
# output: 8
# class str
# ******************************
a = input("Input : ").split(":")
b = len(a[3])
c = int(a[0])+1
d = int(a[1])+1
e = int(a[2])+1
f = b+c+d+e
h = str(f)
print(f)
print(type(h))
