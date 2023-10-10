# ข้อ 1
n = int(input("Enter number :"))
sum = 0
for i in range(5, n+1, 5):
    sum = sum+i
print(sum)

# ข้อ 2 
number = []
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0 :
        number.append(i)

print("output = ",number)

# ข้อ 3
number = int(input("Number = "))
sum = 0
for i in range(1, number+1) :
    if i % 2 != 0 and i % 3 != 0 or i % 2 == 0 and i % 3 == 0 :
        sum = sum + i
        print(i,end=" ")
print("Output : ",sum)

# ข้อ4 
char = str(input("Ener String = "))
lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
l = 0
u = 0
for i in char :
    if i in lower :
        l = l + 1
    elif i in upper :
        u = u + 1

if l == 0:
    print(f"Upper = {u}")
elif u == 0:
    print(f"Lower = {l}")
else :
    print(f"Lower = {l} Upper = {u}")

# ข้อ5
lists = []
for i in range(1000, 3001) : 
    if i % 2000 < 1000 and i % 200 < 100 and i % 20 < 10 and i % 2 == 0 :
        lists.append(i)
print("Output : ",lists)


# ข้อ7 
num1,num2 = input("Input Number1 and Number2 : ").split()
num1 = int(num1)
num2 = int(num2)
sum = 0
if num1 == 0 or num2 == 0 :
    print("ใส่ค่าใหม่")
elif num1 > 9999 or num2 > 9999 :
    print("ใส่ค่าใหม่")
else :
    for i in range(1,10000) :
        if num1 % i == 0 and num2 % i == 0 :
            sum =  i
    print("ห.ร.ม คือ ",sum)

# ข้อ9
num = input("Input: ")
num2 = []
for i in range(1,5):
    num *= i
    num2.append(num)
    num = num2[0]
sum = int(num2[0])+int(num2[1])+int(num2[2])+int(num2[3])
print("Sum = ",sum)

# ข้อ10
rominput=input("Enter a RomanNumber:")
text=['I','V','X','L','C','D','M']
number=[1,5,10,50,100,500,1000]
sum = 0
check = 1
for i in range(len(rominput)) : 
    if i > 0 and number[text.index(rominput[i])] > number[text.index(rominput[i-1])] :
        if i > 1 and number[text.index(rominput[i-1])] >= number[text.index(rominput[i-2])] :
            check = 0
            break
        sum += number[text.index(rominput[i])]- (2 * number[text.index(rominput[i-1])])
    else : 
        sum += number[text.index(rominput[i])]

if check == 1 :
    print("เลขแอโรบิคคือ",sum)
else :
    print("Error")


# ข้อ11
max = int(input("Enter Number : "))
a = 0
b = 1
num = [a,b]
for i in range(0,max):
    a,b = b,a+b
    num.append(b)
    if a+b > max :
        break 
print(num)