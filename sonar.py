import random
import sys
import math

def getNewBoard():
    board = []
    for x in range(60):
        board.append([])
        for y in range(15):
            if random.randint(0, 1) == 0:
                board[x].append('~')
            else:
                board[x].append('`')
    # board = [[]for i in range(15)]
    return board

def drawBoard(board):
    #Изобразить структуру данных игрового поля
    tensDigitsLine = ' '
    for i in range(1, 6):
        tensDigitsLine += (' ' * 9) + str(i)

    print(tensDigitsLine)
    print(' ' + ('0123456789' * 6))
    print()

    # Вывести каждые из 15 рядов
    for row in range(15):
        # Коднозначным числам нужно добавить пробел
        if row <10:
            extraSpace = ' '
        else:
            extraSpace = ''
        # Создать строку для этого ряда на игровом поле
        boardRow = ''
        for column in range(60):
            boardRow += board[column][row]
        print('%s%s %s %s' % (extraSpace, row, boardRow, row))

    print()
    print(' ' + ('0123456789' * 6))
    print(tensDigitsLine)

def getRandomChets(numChets):
    #Создать список структур данных сундука
    chests = []
    while len(chests) < numChets:
        newChets = [random.randint(0, 59), random.randint(0, 14)]
        if newChets not in chests: # Убедиться, что сундука здесь нет.
            chests.append(newChets)
    return chests

def isOnBoard(x, y):
    # Возвращает True если координаты есть на поле.
    return x >= 0 and x <= 59 and y >= 0 and y <=14

def makeMove(board, chests, x, y):
    #Изменить структуру данных поля, используя символ гидролокатора.
    #Удалить сундукис сокровищами из списка с сундуками, как только их нашли.
    #Вернуть False, если это недопустимый ход.
    #В противном случае, вернуть строку с результатом этого хода."
    for cx, cy in chests:
        distance = math.sqrt((cx-x) * (cx-x) + (cy-y) * (cy-y))
        if distance < smallestDistance:
            smallestDistance = distance
            smallestDistance = round(smallestDistance)
        if smallestDistance == 0:
            chests.remove([x, y])
            return 'Вы нашли сундук с сокровищами на затонувшем судне.'
        else:
            if smallestDistance < 10:
                board[x][y] = str(smallestDistance)
                return 'Сундук с сокровищами обнаружен на расстоянии %s от гидролокатора.' % (smallestDistance)
            else:
                board[x][y] = 'X'
                return 'Гидролокатор ничего не обнаружил.'

def enterPlayerMove(previousMoves):
    #Позволить игроку сделать ход
    print('Где следует опустить гидролокатор? (координаты: 0-59 0-14) (или введите "выход")')
    while True:
        move = input()
        if move.lower() == 'выход':
            print('Спасибо за игру!')
            sys.exit()
        move = move.split()
        if len(move) == 2 and move[0].isdigit() and move[1].isdigit() and isOnBoard(int(move[0]), int(move[1])):
            if [int(move[0]), int(move[1])] in previousMoves:
                print('Здесь вы уже опускали гидролокатор')
                continue
            return [int(move[0]), int(move[1])]
        print('Введите число от 0 до 59, потом пробел, а затем число от 0 до 14.')       

a = getNewBoard()
b = drawBoard(a)
