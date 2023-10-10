# ข้อ1
number = int(input("Enter Number : "))
text = ""
text_reverse = ""
half = ""
end = []
end_2 = []
for i in range(0,number+1) :  
  num1 = str(i)*((number-i)+(number-i)+1)
  for j in range(0,i):
    text += str(j)
    text_reverse = text[::-1]
  half = text + num1 + text_reverse
  end.append(half)
  text = ""

for rev in range(len(end)) :
  end_2.append(end[-(rev+1)])

for up in range(len(end)) :
  print(f"{end[up]}")

for un in range(1,len(end_2)) :
  print(f"{end_2[un]}")

# ข้อ2 
number = int(input("Enter Number : "))
text = ""
text_reverse = ""
half = ""
end = []
end_2 = []
for i in range(0,number+1) :  
  num1 = str(i)
  for j in range(0,i):
    text += str(j)
    text_reverse = text[::-1]
  half = ((" "*(number-i)) + text) + num1 + (text_reverse + (" "*(i)))
  end.append(half)
  text = ""

for rev in range(len(end)) :
  end_2.append(end[-(rev+1)])

for up in range(len(end)) :
  print(f"{end[up]}")

for un in range(1,len(end_2)) :
  print(f"{end_2[un]}")

# ข้อ3
import random
data = {}
break_game = False

def display() :
  for i in range(1,7):
    print(f"{i}| {data.get(f'1{i}',' ')} | {data.get(f'2{i}',' ')} | {data.get(f'3{i}',' ')} | {data.get(f'4{i}',' ')} | {data.get(f'5{i}',' ')} | {data.get(f'6{i}',' ')} |")
  print(f"   {1}   {2}   {3}   {4}   {5}   {6}")

def search(x,chack) :
  for y in range(6,0,-1) :
    if (data.get((str(x)+str(y)),False)):
      continue
    else :
      if chack == 1 :
        data[(str(x)+str(y))] = "x"
      elif chack == 2 :
        data[(str(x)+str(y))] = "w"
    chack_win(x,y,chack)
    break
    
def chack_win(x,y,chack) :
  global break_game
  #เช็คแกนX ขวาไปซ้าย
  chack_1 = data.get((str(x)+str(y)),False)
  chack_2 = data.get((str(x-1)+str(y)),False)
  chack_3 = data.get((str(x-2)+str(y)),False)
  if (chack_1 == "x" and chack_2 == "x" and chack_3 == "x") :
    print("Player WIN")
    break_game = True
  elif (chack_1 == "w" and chack_2 == "w" and chack_3 == "w") :
    print("Computer WIN")
    break_game = True
  #เช็คแกนX ซ้ายไปขวา
  chack_1 = data.get((str(x)+str(y)),False)
  chack_2 = data.get((str(x+1)+str(y)),False)
  chack_3 = data.get((str(x+2)+str(y)),False)
  if (chack_1 == "x" and chack_2 == "x" and chack_3 == "x") :
    print("Player WIN")
    break_game = True
  elif (chack_1 == "w" and chack_2 == "w" and chack_3 == "w") :
    print("Computer WIN")
    break_game = True
  #เช็คแกนX กลางออกข้าง
  chack_1 = data.get((str(x)+str(y)),False)
  chack_2 = data.get((str(x-1)+str(y)),False)
  chack_3 = data.get((str(x+1)+str(y)),False)
  if (chack_1 == "x" and chack_2 == "x" and chack_3 == "x") :
    print("Player WIN")
    break_game = True
  elif (chack_1 == "w" and chack_2 == "w" and chack_3 == "w") :
    print("Computer WIN")
    break_game = True
  #เช็คแกนY บนลงล่าง
  chack_1 = data.get((str(x)+str(y)),False)
  chack_2 = data.get((str(x)+str(y+1)),False)
  chack_3 = data.get((str(x)+str(y+2)),False)
  if (chack_1 == "x" and chack_2 == "x" and chack_3 == "x") :
    print("Player WIN")
    break_game = True
  elif (chack_1 == "w" and chack_2 == "w" and chack_3 == "w") :
    print("Computer WIN")
    break_game = True
  #เช็คแกนY ล่างขึ้นบน
  chack_1 = data.get((str(x)+str(y)),False)
  chack_2 = data.get((str(x)+str(y-1)),False)
  chack_3 = data.get((str(x)+str(y-2)),False)
  if (chack_1 == "x" and chack_2 == "x" and chack_3 == "x") :
    print("Player WIN")
    break_game = True
  elif (chack_1 == "w" and chack_2 == "w" and chack_3 == "w") :
    print("Computer WIN")
    break_game = True
 #เช็คแกนY กลางไปบน-ล่าง
  chack_1 = data.get((str(x)+str(y)),False)
  chack_2 = data.get((str(x)+str(y-1)),False)
  chack_3 = data.get((str(x)+str(y+1)),False)
  if (chack_1 == "x" and chack_2 == "x" and chack_3 == "x") :
    print("Player WIN")
    break_game = True
  elif (chack_1 == "w" and chack_2 == "w" and chack_3 == "w") :
    print("Computer WIN")
    break_game = True
 #เช็คแนวเฉียง x
 #            x
 #              x  บนลงล่าง
  chack_1 = data.get((str(x)+str(y)),False)
  chack_2 = data.get((str(x+1)+str(y+1)),False)
  chack_3 = data.get((str(x+2)+str(y+2)),False)
  if (chack_1 == "x" and chack_2 == "x" and chack_3 == "x") :
    print("Player WIN")
    break_game = True
  elif (chack_1 == "w" and chack_2 == "w" and chack_3 == "w") :
    print("Computer WIN")
    break_game = True
 #เช็คแนวเฉียง x
 #            x
 #              x  ล่างขึ้นบน
  chack_1 = data.get((str(x)+str(y)),False)
  chack_2 = data.get((str(x-1)+str(y-1)),False)
  chack_3 = data.get((str(x-2)+str(y-2)),False)
  if (chack_1 == "x" and chack_2 == "x" and chack_3 == "x") :
    print("Player WIN")
    break_game = True
  elif (chack_1 == "w" and chack_2 == "w" and chack_3 == "w") :
    print("Computer WIN")
    break_game = True
 #เช็คแนวเฉียง x
 #            x
 #              x  กลางไปบน-ล่าง
  chack_1 = data.get((str(x)+str(y)),False)
  chack_2 = data.get((str(x-1)+str(y-1)),False)
  chack_3 = data.get((str(x+1)+str(y+1)),False)
  if (chack_1 == "x" and chack_2 == "x" and chack_3 == "x") :
    print("Player WIN")
    break_game = True
  elif (chack_1 == "w" and chack_2 == "w" and chack_3 == "w") :
    print("Computer WIN")
    break_game = True
#เช็คแนวเฉียง     x
 #            x
 #          x      บนลงล่าง
  chack_1 = data.get((str(x)+str(y)),False)
  chack_2 = data.get((str(x-1)+str(y+1)),False)
  chack_3 = data.get((str(x-2)+str(y+2)),False)
  if (chack_1 == "x" and chack_2 == "x" and chack_3 == "x") :
    print("Player WIN")
    break_game = True
  elif (chack_1 == "w" and chack_2 == "w" and chack_3 == "w") :
    print("Computer WIN")
    break_game = True
#เช็คแนวเฉียง     x
 #            x
 #          x      ล่างขึ้นบน
  chack_1 = data.get((str(x)+str(y)),False)
  chack_2 = data.get((str(x+1)+str(y-1)),False)
  chack_3 = data.get((str(x+2)+str(y-2)),False)
  if (chack_1 == "x" and chack_2 == "x" and chack_3 == "x") :
    print("Player WIN")
    break_game = True
  elif (chack_1 == "w" and chack_2 == "w" and chack_3 == "w") :
    print("Computer WIN")
    break_game = True
#เช็คแนวเฉียง     x
 #            x
 #          x      กลางไปบน-ล่าง
  chack_1 = data.get((str(x)+str(y)),False)
  chack_2 = data.get((str(x+1)+str(y-1)),False)
  chack_3 = data.get((str(x-1)+str(y+1)),False)
  if (chack_1 == "x" and chack_2 == "x" and chack_3 == "x") :
    print("Player WIN")
    break_game = True
  elif (chack_1 == "w" and chack_2 == "w" and chack_3 == "w") :
    print("Computer WIN")
    break_game = True

while True :
  while True :
    inputplayer = int(input("Input Number 1-6 :")) 
    search(inputplayer,1)
    display()
    if break_game == True :
      play_again = input("Play Again ? [Y/N] :")
      if play_again in "Yy" :
        data.clear()
        break_game = False
      elif play_again in "Nn" :
        break
      break
    com = random.randint(1,6)
    search(com,2)
    display()
    if break_game == True :
      play_again = input("Play Again ? [Y/N] :")
      if play_again in "Yy" :
        data.clear()
        break_game = False
      elif play_again in "Nn" :
        break
      break
  if play_again in "Nn" :
    break

# ข้อ4 
display_kmitl = ['*****',
	    		'*MM**',
				'*KIK*',
				'*IT**',
				'**L**',
			    ]
for dis in range(len(display_kmitl)) :
	print(display_kmitl[dis])

k_list = []
kmitl_list = []
kmitl_count = 0
lock_number = 0

def search_position(y,x,char) : 
    position = []
    for axis_y in range(-1,2): 
        for axis_x in range(-1,2): 
            if (display_kmitl[y-axis_y][x-axis_x] == char):
                position.append(f"{y-axis_y},{x-axis_x}")
    return position

#หาตัวK
for axis_y in range(len(display_kmitl)):
	if 'K' in display_kmitl[axis_y]:
		for axis_x in range(len(display_kmitl)):
			if display_kmitl[axis_y][axis_x]=='K':
				k_list.append(f"{axis_y},{axis_x}")


for search_num_k in k_list :
    k_output = f"({int(search_num_k[0])+1},{int(search_num_k[2])+1})"
    for search_num_m in search_position(int(search_num_k[0]),int(search_num_k[2]),"M"):
        m_output = f"({int(search_num_m[0])+1},{int(search_num_m[2])+1})"
        for search_num_i in search_position(int(search_num_m[0]),int(search_num_m[2]),"I"):
            i_output = f"({int(search_num_i[0])+1},{int(search_num_i[2])+1})"
            for search_num_t in search_position(int(search_num_i[0]),int(search_num_i[2]),"T"):
                t_output = f"({int(search_num_t[0])+1},{int(search_num_t[2])+1})"
                for search_num_l in search_position(int(search_num_t[0]),int(search_num_t[2]),"L"):
                    l_output = f"({int(search_num_l[0])+1},{int(search_num_l[2])+1})"
                    kmitl_count += 1
                    kmitl_list.append(f"K:{k_output} M:{m_output} I:{i_output} T:{t_output} L:{l_output}")


print(f'KMITL COUNT : {kmitl_count}')
for kmitl in range(len(kmitl_list)) :
	print(kmitl_list[kmitl])