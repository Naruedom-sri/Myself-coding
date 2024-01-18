print('*** Multiplication table ***')
n = int(input('Enter an integer(n) : '))
count = 1
sum = 0
while (count <= 12):
    sum = n * count
    if (count <= 9):
        if (sum < 10):
            print(n, 'x', str(count)+' ', '=', '  '+str(sum))
        elif(sum < 100):
            print(n, 'x', str(count)+' ', '=', ' '+str(sum))
        else:
            print(n, 'x', str(count)+' ', '=', sum)
    else:
        if (sum < 10):
            print(n, 'x', str(count)+' ', '=', '  '+str(sum))
        elif(sum < 100):
            print(n, 'x', count, '=', ' '+str(sum))
        else:
            print(n, 'x', count, '=', sum)
    count += 1
