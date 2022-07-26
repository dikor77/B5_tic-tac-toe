from random import randrange


#печать поля
def fprint(field):
    print('  0 1 2')
    for i in range(N):
        print(i, ' '.join(field[i]))


#запросить координаты в формате 
def user_input():
    user_cross = []
    while True:
        user_cross = list(map(int, list(input("Ваш ход, поставьте крестик, формат (строка колонка): ").split())))
        if len(user_cross) == 2 and all(list(map(lambda x: x in range(N), user_cross))):
            row, col = user_cross[0], user_cross[1]
            if empty_cell(row, col):
                print("Ваш выбор: ", user_cross)
                return user_cross
            else:
                print("Ячейка уже занята, попробуй еще")
        else:
            print("Ваш ввод не распознан, попробуй еще")


#True если ячейка свободная
def empty_cell(row, col):
    cell = field[row][col]
    if(cell == '-'):
        return True
    else:
        return False


#подсчет свободных ячеек
def count_empty_cells():
    count = 0
    for row in field:
        for cell in row:
            if cell == '-':
                count += 1
    return count


#мой ход, нолик располагается случайным образом
def set_zero():
    val = randrange(0, count_empty_cells())

    for row in range(N):
        for col in range(N):
            if val > 0:
                if empty_cell(row, col):
                    val -= 1
            else:
                if empty_cell(row, col):
                    field[row][col] = 'O'
                    return


#проверка строки на выигрыш
def check_row(row, sym):
    count = 0
    for col in range(N):
        val = field[row][col]
        if(val == sym):
            count += 1
    
    return count == 3


#проверка колонки на выигрыш
def check_col(col, sym):
    count = 0
    for row in range(N):
        val = field[row][col]
        if(val == sym):
            count += 1
    
    return count == 3


#проверка диагонали 1 на выигрыш
def check_diag1(sym):
    count = 0
    for i in range(N):
        val = field[i][i]
        if(val == sym):
            count += 1
    
    return count == 3


#проверка диагонали 2 на выигрыш
def check_diag2(sym):
    count = 0
    for i in range(N):
        val = field[i][N - i - 1]
        if(val == sym):
            count += 1
    
    return count == 3


#проверка на выигрыш всех комбинаций
def check_win(sym):
    check = []

    for i in range(N):
        check.append(check_row(i, sym))
        check.append(check_col(i, sym))
    
    check.append(check_diag1(sym))
    check.append(check_diag2(sym))

    return any(check)



#генерирую поле
N = 3
field = [['-' for i in range(N)] for j in range(N)]


#цикл пока есть свободные ячейки
while count_empty_cells() > 0:
    #рисуем поле
    fprint(field)
    #запрашиваем координаты крестика
    user_cross = user_input()
    #размещаю крестик на поле
    row, col = user_cross[0], user_cross[1]
    field[row][col] = 'X'
    #проверка на выигрыш
    if check_win('X'):
        fprint(field)
        print("Поздравляю, вы выиграли")
        break
    
    #проверка перед размещением нолика
    if(count_empty_cells() > 0):
        #ставим нолик
        set_zero()
        #проверка на выигрыш
    if check_win('O'):
        fprint(field)
        print("Поздравляю, вы проиграли")
        break

print("Конец игры")