#генерирую поле
N = 3
field = [['-' for i in range(N)] for j in range(N)]

#печать поля
def fprint(field):
    print('  0 1 2')
    for i in range(N):
        print(i, ' '.join(field[i]))


def user_input():
    user_cross = []
    while True:
        user_cross = list(map(int, list(input("Ваш ход, поставьте крестик, формат (x y)").split())))
        if len(user_cross) == 2 and all(list(map(lambda x: x in range(N), user_cross))):
            print("Ваш выбор: ", user_cross)
            return user_cross
        else:
            print("Ваш ввод не распознан, попробуй еще")
        
#начало
fprint(field)

user_cross = user_input()

