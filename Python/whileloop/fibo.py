print(' *** Fibonacci sequence ***')
a0, a1, n = [int(x) for x in input("Enter a0 a1 n : ").split()]
count = 2
sum = 0
list = [a0, a1]
output = ''
while (count < int(n)):
    list.append(list[count - 2] + list[count-1])
    count += 1
count = 0
while (count < len(list)):
    if (count == len(list)-1):
        output += str(list[count])
    else:
        output += str(list[count]) + ", "
    count += 1
print(output)
print('===== End of program =====')
