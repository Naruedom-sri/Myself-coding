print(" *** Min Max Avg ***")
x,y,z = [float(x) for x in input("Enter 3 numbers : ").split()]
average = (x+y+z)/3
list = [x,y,z]
list.sort()
print('min, mid, max ==> ',str('{:.2f}'.format(list[0]))+',',str('{:.2f}'.format(list[1]))+',',str('{:.2f}'.format(list[2])))
print("Average ==> ",'{:.3f}'.format(average))