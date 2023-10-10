# ข้อ1
r = int(input("Enter Number : "))
m = [10000, 15000, 20000, 25000, 30000, 35000, 40000]
y = [1, 2, 3, 4]
final = []
for a in range(len(y)) :
    for b in range(len(m)) :
        sum = int(m[b])*((1+r/100)**int(y[a]))
        final.append('%.2f' %sum)

print(f"year     1        2         3        4")
for i in range(7): 
    print(f"{m[i]}|{final[i]}|{final[i+7]}|{final[i+14]}|{final[i+21]}|")

# ข้อ2
h1 = int(input("First Hour :"))
m1 = int(input("First Minute :"))
h2 = int(input("Second Hour :"))
m2 = int(input("Second Minute :"))
hour = h2-h1
minute = m2-m1
point = 0

if not(hour == 0 and minute <= 15) :
    if hour == 0 and minute > 15 or hour == 1 and minute == 0 :
        hour = 1
        point = 10*hour
    elif hour == 1 and minute > 0 or hour == 2 and minute == 0:
        hour = 2
        point = 10*hour
    elif hour == 2 and minute > 0 or hour == 3 and minute == 0:
        hour = 3
        point = 10*hour
    elif hour == 3 and minute > 0 or hour == 4 and minute == 0:
        hour = 4
        hour = hour-3
        point = 30+(20*hour)
    elif hour == 4 and minute > 0 or hour == 5 and minute == 0:
        hour = 5
        hour = hour-3
        point = 30+(20*hour)
    elif hour == 5 and minute > 0 or hour == 6 and minute == 0 :
        hour = 6
        point = 200
    elif hour >= 6  :
        point = 200
    print(f"ราคา = {point} บาท")
else :
    print("Free")

# ข้อ 3
prime_factors = [2, 3, 5, 7, 11, 13, 17, 19]
sum = 1

for i in range(len(prime_factors)) :
    n = int(prime_factors[i])
    a = 1
    while True :
        if n**a > 20 :
            sum *= n**(a-1)
            break
        a += 1 
print(int(sum))

# ข้อ 4 
prime_factors = int(input("Enter Number : "))
prime_factors_list = []

i = 2
while True :
    if prime_factors % i == 0 :
        prime_factors = prime_factors / i
        prime_factors_list.append(i)
    elif(prime_factors < i) :
        break
    else :
        i += 1
print(f"Prime Factrs = {prime_factors_list[-1]}")

# ข้อ 5
prime_factors_list = []

i = 2
while len(prime_factors_list) < 1002 :
    j = 2
    while j<=i//j:
        if i%j==0:
            break
        j+=1
    if j > i//j:
        prime_factors_list.append(i)
    i += 1
print(f"Prime Factors = {prime_factors_list[-1]}")

# ข้อ 6
num = int(input("Number = "))
sum_of_the_squares = 0
square_of_the_sum1 = 0

for i in range(1,num+1) :
    sum_of_the_squares += i**2
    square_of_the_sum1 += i
    square_of_the_sum = square_of_the_sum1**2
    sum = square_of_the_sum - sum_of_the_squares

print(f"{square_of_the_sum} - {sum_of_the_squares} = {sum}")

# ช้อ 7 
data_1 = '''73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450'''

data = data_1.replace("\n","")
max = 1
list_max = []
for i in range(0,len(data)) :
    word = data[i:i+8]
    before_max = 1
    for j in range(0,len(word)) :
        before_max *= int(word[j])
    
    if (before_max > max) :
        list_max.clear()
        list_max.append(word)
        max = before_max


print(f"{list_max} = {max}")

# ข้อ8
numinput = [int(x) for x in input("Number : ").split()]
numbers = []

for i in range(0,len(numinput)) :
    if(numinput[i] != 0) :
        numbers.append(numinput[i])

zero_number = []

for j in range(0,len(numinput)) :
    if(numinput[j] == 0) :
        zero_number.append(numinput[j])

check = True
while check :
    check_2 = False
    for i in range(0,len(numbers)) :
        if(i+1 > len(numbers)-1) :
            break
        elif(numbers[i]>numbers[i+1]) :
            numbers[i],numbers[i+1] = numbers[i+1],numbers[i]
            check_2 = True
        
    check = check_2

for j in zero_number :
    numbers.insert(1,zero_number[j])

print(numbers)

# ข้อ9
palindrome = []
sum1 = 0
for i in range(100,1000) :
    for j in range(100,1000) :
        sum1 = i*j
        sum = str(sum1)
        rev = sum[::-1]
        if sum == rev :
            palindrome.append(int(sum))
print(f"Palindrom = {max(palindrome)}")
