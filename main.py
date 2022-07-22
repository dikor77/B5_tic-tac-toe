#генерирую поле
N = 3
field = [['-' for i in range(N)] for j in range(N)]

#печать поля
def fprint(field):
    print('  0 1 2')
    for i in range(N):
        print(i, ' '.join(field[i]))




#начало
fprint(field)


while True:
    user_cross = list(map(int,[x for x in input("Ваш ход, поставьте крестик, формат (x y)").split()]))
    if len(user_cross) == 2 and all(list(map(lambda x: x in range(N), user_cross))):
        print("Ваш выбор: ", user_cross)
        break;
    else:
        print("Ваш ввод не распознан, попробуй еще")
