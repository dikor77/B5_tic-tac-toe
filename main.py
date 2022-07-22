#генерирую поле
N = 3
field = [['-' for i in range(N)] for j in range(N)]

#печать поля
def fprint(field):
    print('  0 1 2')
    for i in range(N):
        print(i, ' '.join(field[i]))
            
        

fprint(field)