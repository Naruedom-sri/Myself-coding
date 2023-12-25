print(" *** 3-digit odd even ***")
num = input("Enter 3-digit number : ")
list = []
for i in range(3):
    if int(num[i]) % 2 == 0:
       list.append('even')
    else:
       list.append('odd')
print(num + " => ",list[0],list[1],list[2])