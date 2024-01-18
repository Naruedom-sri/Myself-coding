print(' *** Word Triangle ***')
x = input('Enter Word: ')
for row in range(len(x)):
    for colum in range(row +1):
        print(x[colum],end="")
    print()
        
    
    