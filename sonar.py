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
    # board = [[y for in range(15) if random.randint(0, 1) == 0 ]for i in range(60)]
        #print(len(board), board[x])
    return board

def drawBoard(board):
    #Изобразить структуру данных игрового поля
    tensDigitsLine = ' '
    for i in range(1, 6):
        tensDigitsLine += (' ' * 9) + str(i)

    print(tensDigitsLine)
    print('   ' + ('0123456789' * 6))
    #print()

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
            #print(boardRow, 'board[column][row] = ', board[column][row])
            boardRow += board[column][row]
        print('%s%s %s %s' % (extraSpace, row, boardRow, row))

    #print()
    print('   ' + ('0123456789' * 6))
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
    return 0 <= x <= 59 and 0 <= y <= 14
    #return x >= 0 and x <= 59 and y >= 0 and y <=14

def makeMove(board, chests, x, y):
    #Изменить структуру данных поля, используя символ гидролокатора.
    #Удалить сундукис сокровищами из списка с сундуками, как только их нашли.
    #Вернуть False, если это недопустимый ход.
    #В противном случае, вернуть строку с результатом этого хода."
    smallestDistance = 100
    for cx, cy in chests:
        distance = math.sqrt((cx-x) * (cx-x) + (cy-y) * (cy-y))
        print(chests)
        print(cx, '-', x, '*', cx, '-', x, '+', cy, '-', y, '*', cy, '-', y, '=', distance)
        if distance < smallestDistance:
            smallestDistance = distance
            smallestDistance = round(smallestDistance)
        if smallestDistance == 0:
            chests.remove([x, y])
            board[x][y] = '*'
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

while True:
    sonarDevices = 20
    theBoard = getNewBoard()
    theChests = getRandomChets(3)
    drawBoard(theBoard)
    previousMoves = []
    while sonarDevices > 0:
        # Показать гидролокаторные устройства и сундуки с сокровищами.
        print('Осталось гидролокаторов: %s. Осталось сундуков с сокровищами: %s.' % (sonarDevices, len(theChests)))
        x, y = enterPlayerMove(previousMoves)
        previousMoves.append([x, y])  # Мы должны отслеживать все ходы, чтобы гидролокаторы могли обновляться.
        print(previousMoves) # смотрю список сделаных ходов
        moveResult = makeMove(theBoard, theChests, x, y)
        if moveResult == False:
            continue
        else:
            if moveResult ==  'Вы нашли сундук с сокровищами на затонувшем судне!':
                # Обновить все гидролокаторные устройства, в настоящее время находящиеся на карте.
                for x, y in previousMoves:
                    makeMove(theBoard, theChests, x, y)
            drawBoard(theBoard)
            print(moveResult)
        if len(theChests) == 0:
            print('Вы нашли все сундуки на затонувших короблях!')
            break
        sonarDevices -= 1
        if sonarDevices == 0:
            print('Все гидролокаторы опущены на дно! Придется разворачивать корабль и')
            print('отправляться домой, в порт! Игра окончена.')
            print('Вы не нашли сундуки в следующих местах:')
            for x, y in theChests:
                print('%s, %s' % (x, y))
            print('Хотите сыграть еще раз? (да или нет)')
            if not input().lower().startswith('д'):
                sys.exit()



#a = getNewBoard()
#b = drawBoard(a)
