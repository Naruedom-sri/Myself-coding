word = input("Enter a word : ")
list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numdot = 0
numunderscore = 0
checkstr = 0
for i in word:
    for j in range(len(list)):
        if i == list[j]:
            checkstr += 1
    if i == ".":
        numdot += 1
    elif i == "_":
        numunderscore += 1
if numdot == 1:
    print('{:.3f}'.format(float(word)), "/ 3 = ",
          '{:.3f}'.format(float(word)/3))
elif numdot > 1 or numunderscore >= 1 or checkstr >= 1:
    print((word + " ") * 3)
else:
    print(word, "* 2 =", int(word)*2)
