print(' *** Digit count and Summation ***')
x = int(input('Enter an integer : '))
y = str(x)
current = x
comma = ''
digit = 0
sum = 0
num = 0
list = []
while (x > 0):
    if (int(len(y)) % 3 == 0):
        if (digit % 3 != 0 or digit == 0):
            comma += y[digit]
        elif (digit % 3 == 0):
            comma += ","
            comma += y[digit]
    elif (int(len(y)) % 3 == 1):
        if (digit % 3 != 0 or digit == len(y)-1):
            comma += y[digit]
        elif (digit % 3 == 0):
            comma += y[digit]
            comma += ","
    elif (len(y) <= 3):
        comma += y[digit]
    sum += x % 10
    x = x // 10
    digit += 1

if (int(len(y)) % 3 == 2):
    digit = 0
    while (current > 0):
        num = current % 10
        current = current // 10
        if (digit % 3 != 0) or digit == len(y) or digit == 0:
            list.append(num)
        elif (digit % 3 == 0 ):
            list.append(str(num) +',')
        digit += 1
    list.reverse()
    digit = 0
    print(list)
    while(digit != len(y)):
        comma += str(list[digit])
        digit += 1
print('Entered number =',comma)
print('Total digits are: ', digit)
print('Summation =', sum)
