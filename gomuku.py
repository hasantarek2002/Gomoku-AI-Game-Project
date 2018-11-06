from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import  QtCore
from PyQt5.QtGui import QImage, QPalette, QBrush

from ui import Ui_Play_Game
board = []
for i in range(10):
    board.append('----------')

def evf():
    strings = []

    for i in range(10):
        strings.append(board[i])

    for i in range(10):
        _str = ''
        for j in range(10):
            _str += board[j][i]
        strings.append(_str)

    _str = ''
    for i in range(10):
        _str += board[i][i]

    strings.append(_str)

    strings.append(
        board[0][1] + board[1][2] + board[2][3] + board[3][4] + board[4][5] + board[5][6] + board[6][7] + board[7][8] +
        board[8][9])
    strings.append(
        board[0][2] + board[1][3] + board[2][4] + board[3][5] + board[4][6] + board[5][7] + board[6][8] + board[7][9])
    strings.append(board[0][3] + board[1][4] + board[2][5] + board[3][6] + board[4][7] + board[5][8] + board[6][9])
    strings.append(board[0][4] + board[1][5] + board[2][6] + board[3][7] + board[4][8] + board[5][9])
    strings.append(board[0][5] + board[1][6] + board[2][7] + board[3][8] + board[4][9])

    strings.append(
        board[1][0] + board[2][1] + board[3][2] + board[4][3] + board[5][4] + board[6][5] + board[7][6] + board[8][7] +
        board[9][8])
    strings.append(
        board[2][0] + board[3][1] + board[4][2] + board[5][3] + board[6][4] + board[7][5] + board[8][6] + board[9][7])
    strings.append(board[3][0] + board[4][1] + board[5][2] + board[6][3] + board[7][4] + board[8][5] + board[9][6])
    strings.append(board[4][0] + board[5][1] + board[6][2] + board[7][3] + board[8][4] + board[9][5])
    strings.append(board[5][0] + board[6][1] + board[7][2] + board[8][3] + board[9][4])

    _str = ''
    # for i in range(9, -1, -1):
    #     _str += board[i][i]


    strings.append(board[0][9]+board[1][8]+board[2][7]+board[3][6]+board[4][5]+board[5][4]+board[6][3]+board[7][2]+board[8][1]+board[9][0])

    strings.append(
        board[0][8] + board[1][7] + board[2][6] + board[3][5] + board[4][4] + board[5][3] + board[6][2] + board[7][1] +
        board[8][0])
    strings.append(
        board[0][7] + board[1][6] + board[2][5] + board[3][4] + board[4][3] + board[5][2] + board[6][1] + board[7][0])
    strings.append(board[0][6] + board[1][5] + board[2][4] + board[3][3] + board[4][2] + board[5][1] + board[6][0])
    strings.append(board[0][5] + board[1][4] + board[2][3] + board[3][2] + board[4][1] + board[5][0])
    strings.append(board[0][4] + board[1][3] + board[2][2] + board[3][1] + board[4][0])

    strings.append(
        board[1][9] + board[2][8] + board[3][7] + board[4][6] + board[5][5] + board[6][4] + board[7][3] + board[8][2] +
        board[9][1])
    strings.append(
        board[2][9] + board[3][8] + board[4][7] + board[5][6] + board[6][5] + board[7][4] + board[8][3] + board[9][2])
    strings.append(board[3][9] + board[4][8] + board[5][7] + board[6][6] + board[7][5] + board[8][4] + board[9][3])
    strings.append(board[4][9] + board[5][8] + board[6][7] + board[7][6] + board[8][5] + board[9][4])
    strings.append(board[5][9] + board[6][8] + board[7][7] + board[8][6] + board[9][5])

    # for _str in strings:
    #     if 'xxxxx' in _str:
    #         return 100
    #
    # for _str in strings:
    #     if 'ooooo' in _str:
    #         # print("FIND 00000")
    #         return -100
    #
    # for _str in strings:
    #     if 'oooo-' in _str:
    #         #print("Find 0000-")
    #         return -40
    #     if '-oooo' in _str:
    #         #print("Find  -0000")
    #         return -40
    #     if 'ooo-o' in _str:
    #         return -40
    #     if 'oo-oo' in _str:
    #         return -40
    #     if 'o-ooo' in _str:
    #         return -40
    #
    # for _str in strings:
    #     if 'xxxx-' in _str:
    #         return 40
    #     if '-xxxx' in _str:
    #         return 40
    #     if 'xxx-x' in _str:
    #         return 40
    #     if 'xx-xx' in _str:
    #         return 40
    #     if 'x-xxx' in _str:
    #         return 40
    #
    # for _str in strings:
    #     if 'ooo--' in _str:
    #         return -30
    #     if '-ooo-' in _str:
    #         return -30
    #     if '--ooo' in _str:
    #         return -30
    #     if 'o-o-o' in _str:
    #         return -30
    #     if 'oo-o-' in _str:
    #         return -30
    #     if 'o-oo-' in _str:
    #         return -30
    #     if 'o--oo' in _str:
    #         return -30
    #     if 'oo--o' in _str:
    #         return -30
    #     if '-o-oo' in _str:
    #         return -25
    #     if 'ooo--' in _str:
    #         return -25
    #
    # for _str in strings:
    #     if 'xxx--' in _str:
    #         return 30
    #     if '-xxx-' in _str:
    #         return 30
    #     if '--xxx' in _str:
    #         return 30
    #     if 'x-x-x' in _str:
    #         return 30
    #     if 'xx-x-' in _str:
    #         return 30
    #     if 'x--xx' in _str:
    #         return 30
    #     if 'x--xx' in _str:
    #         return 30
    #     if 'xx--x' in _str:
    #         return 30
    #     if '-x-xx' in _str:
    #         return 25
    #     if 'xxx--' in _str:
    #         return 25

    for _str in strings:
        if 'xxxxx' in _str:
            return 100

    for _str in strings:
        if 'ooooo' in _str:
            # print("FIND 00000")
            return -100

    for _str in strings:
        if 'xxxx-' in _str:
            return 40
        if '-xxxx' in _str:
            return 40
        if 'xxx-x' in _str:
            return 40
        if 'xx-xx' in _str:
            return 40
        if 'x-xxx' in _str:
            return 40


    for _str in strings:
        if 'oooo-' in _str:
            #print("Find 0000-")
            return -40
        if '-oooo' in _str:
            #print("Find  -0000")
            return -40
        if 'ooo-o' in _str:
            return -40
        if 'oo-oo' in _str:
            return -40
        if 'o-ooo' in _str:
            return -40


    for _str in strings:
        if '-xxx-' in _str:
            return 35
        if 'xxx--' in _str:
            return 30
        if '--xxx' in _str:
            return 30
        if 'xx-x-' in _str:
            return 30
        if 'x-xx-' in _str:
            return 30
        if '-x-xx' in _str:
            return 30
        if '-xx-x' in _str:
            return 30
        if 'x--xx' in _str:
            return 25
        if 'xx--x' in _str:
            return 25
        if 'x-x-x' in _str:
            return +25
        if '--xxxo' in _str:
            return 20
        if 'oxxx--' in _str:
            return 20
        if 'oxx-x-' in _str:
            return 20
        if '-x-xxo' in _str:
            return 20
        if '-xx--' in _str:
            return 15
        if "-x-x--" in _str:
            return 10
        if "--x-x-" in _str:
            return 10
        if 'xx---' in _str:
            return 5

    for _str in strings:
        if '-ooo-' in _str:
            return -35
        if 'ooo--' in _str:
            return -30
        if '--ooo' in _str:
            return -30
        if 'oo-o-' in _str:
            return -30
        if 'o-oo-' in _str:
            return -30
        if '-o-oo' in _str:
            return -30
        if '-oo-o' in _str:
            return -30
        if 'o--oo' in _str:
            return -25
        if 'oo--o' in _str:
            return -25
        if 'o-o-o' in _str:
            return -25
        if '--ooox' in _str:
            return -20
        if 'xooo--' in _str:
            return -20
        if 'xoo-o-' in _str:
            return -20
        if '-o-oox' in _str:
            return -20
        if '-oo--' in _str:
            return -15
        if "-o-o--" in _str:
            return -10
        if "--o-o-" in _str:
            return -10
        if 'oo---' in _str:
            return -5

    return 0

def checkWinner():
    for _str in board:
        if 'xxxxx' in _str:
            return 100
        if 'ooooo' in _str:
            return -100
    strings = []

    for i in range(10):
        _str = ''
        for j in range(10):
            _str += board[j][i]
        strings.append(_str)

    _str = ''
    for i in range(10):
        _str += board[i][i]

    strings.append(_str)

    strings.append(
        board[0][1] + board[1][2] + board[2][3] + board[3][4] + board[4][5] + board[5][6] + board[6][7] + board[7][8] +
        board[8][9])
    strings.append(
        board[0][2] + board[1][3] + board[2][4] + board[3][5] + board[4][6] + board[5][7] + board[6][8] + board[7][9])
    strings.append(board[0][3] + board[1][4] + board[2][5] + board[3][6] + board[4][7] + board[5][8] + board[6][9])
    strings.append(board[0][4] + board[1][5] + board[2][6] + board[3][7] + board[4][8] + board[4][9])
    strings.append(board[0][5] + board[1][6] + board[2][7] + board[3][8] + board[4][9])

    strings.append(
        board[1][0] + board[2][1] + board[3][2] + board[4][3] + board[5][4] + board[6][5] + board[7][6] + board[8][7] +
        board[9][8])
    strings.append(
        board[2][0] + board[3][1] + board[4][2] + board[5][3] + board[6][4] + board[7][5] + board[8][6] + board[9][7])
    strings.append(board[3][0] + board[4][1] + board[5][2] + board[6][3] + board[7][4] + board[8][5] + board[9][6])
    strings.append(board[4][0] + board[5][1] + board[6][2] + board[7][3] + board[8][4] + board[9][5])
    strings.append(board[5][0] + board[6][1] + board[7][2] + board[8][3] + board[9][4])

    strings.append(
        board[0][9] + board[1][8] + board[2][7] + board[3][6] + board[4][5] + board[5][4] + board[6][3] + board[7][2] +
        board[8][1] + board[9][0])

    strings.append(
        board[0][8] + board[1][7] + board[2][6] + board[3][5] + board[4][4] + board[5][3] + board[6][2] + board[7][1] +
        board[8][0])
    strings.append(
        board[0][7] + board[1][6] + board[2][5] + board[3][4] + board[4][3] + board[5][2] + board[6][1] + board[7][0])
    strings.append(board[0][6] + board[1][5] + board[2][4] + board[3][3] + board[4][2] + board[5][1] + board[6][0])
    strings.append(board[0][5] + board[1][4] + board[2][3] + board[3][2] + board[4][1] + board[5][0])
    strings.append(board[0][4] + board[1][3] + board[2][2] + board[3][1] + board[4][0])

    strings.append(
        board[1][9] + board[2][8] + board[3][7] + board[4][6] + board[5][5] + board[6][4] + board[7][3] + board[8][2] +
        board[9][1])
    strings.append(
        board[2][9] + board[3][8] + board[4][7] + board[5][6] + board[6][5] + board[7][4] + board[8][3] + board[9][2])
    strings.append(board[3][9] + board[4][8] + board[5][7] + board[6][6] + board[7][5] + board[8][4] + board[9][3])
    strings.append(board[4][9] + board[5][8] + board[6][7] + board[7][6] + board[8][5] + board[9][4])
    strings.append(board[5][9] + board[6][8] + board[7][7] + board[8][6] + board[9][5])

    for _str in strings:
        if 'xxxxx' in _str:
            return 100
        if 'ooooo' in _str:
            return -100
    return 0

x = [-1, -1, -1, 0, 0, 1, 1, 1]
y = [-1, 0, 1, -1, 1, -1, 0, 1]
R = 10
C = 10
global lis
#list = []

def search(matrix, pattern, row, col):
    if not matrix [row][col]== pattern[0]:
        return False
    word_len = len(pattern)
    #print(word_len)
    global lis
    lis = []
    lis.append((row, col))
    for dir in range(8):
        rd = row + x[dir]
        cd = col + y[dir]
        k=0
        for k in range(1,word_len+1):
            if k == word_len:
                break
            #print(k)
            if rd >= R or rd < 0 or cd >= C or cd < 0:
                lis = [lis[0]]
                break
            if not matrix[rd][cd] == pattern[k]:
                lis = [lis[0]]
                break
            lis.append((rd, cd))
            #print(lis)
            rd += x[dir]
            cd += y[dir]
        #print(k)
        if k == word_len:
            #print(lis)
            return True
    return False

def pattern_search(matrix, pattern):
    for row in range(R):
        for col in range(C):
            if search(matrix,pattern, row, col):
                return True
    return False

# def evf():
#     if pattern_search(board,'xxxxx'):
#         return 100
#     if pattern_search(board,'ooooo'):
#         return -100
#
#     if pattern_search(board,'oooo-'):
#         return -40
#     if pattern_search(board,'-oooo'):
#         return -40
#     if pattern_search(board,'ooo-o'):
#         return -40
#     if pattern_search(board,'oo-oo'):
#         return -40
#     if pattern_search(board,'o-ooo'):
#         return -40
#
#     if pattern_search(board,'xxxx-'):
#         return 40
#     if pattern_search(board,'-xxxx'):
#         return 40
#     if pattern_search(board,'xxx-x'):
#         return 40
#     if pattern_search(board,'xx-xx'):
#         return 40
#     if pattern_search(board,'x-xxx'):
#         return 40
#
#     if pattern_search(board,'-ooo-'):
#         return -35
#     if pattern_search(board,'ooo--'):
#         return -30
#     if pattern_search(board,'--ooo'):
#         return -30
#     if pattern_search(board,'o-o-o'):
#         return -30
#     if pattern_search(board,'oo-o-'):
#         return -30
#     if pattern_search(board,'o-oo-'):
#         return -30
#     if pattern_search(board,'-o-oo'):
#         return -30
#     if pattern_search(board,'-oo-o'):
#         return -30
#     if pattern_search(board,'o--oo'):
#         return -25
#     if pattern_search(board,'oo--o'):
#         return -25
#
#
#     if pattern_search(board,'-xxx-'):
#         return 35
#     if pattern_search(board,'xxx--'):
#         return 30
#     if pattern_search(board,'--xxx'):
#         return 30
#     if pattern_search(board,'x-x-x'):
#         return 30
#     if pattern_search(board,'xx-x-'):
#         return 30
#     if pattern_search(board,'x-xx-'):
#         return 30
#     if pattern_search(board,'-x-xx'):
#         return 30
#     if pattern_search(board,'-xx-x'):
#         return 30
#     if pattern_search(board,'x--xx'):
#         return 25
#     if pattern_search(board,'xx--x'):
#         return 25



def coordinate(icor, jcor):
    icor0, icor1 = 0, 9
    jcor0, jcor1 = 0, 9
    #print("Mp", icor, jcor)

    if icor + 4 > 9:
        icor1 = 9
    else:
        icor1 = icor+4

    if icor - 4 < 0:
        icor0 = 0
    else:
        icor0 = icor-4

    if jcor + 4 > 9:
        jcor1 = 9
    else:
        jcor1 = jcor+4

    if jcor - 4 < 0:
        jcor0 = 0
    else:
        jcor0 = jcor-4

    #print("here",icor0, icor1, jcor0, jcor1)
    return icor0, icor1, jcor0, jcor1


def correct(icor, jcor):
    if (0 <= icor <= 9) and (0 <= jcor <= 9):
        return 1
    return 0

def rep_char_in_string(string, index, char):
    return string[:index] + char + string[index + 1:]

def reform_string(string, index):
    return string[:index] + '-' + string[index + 1:]

def minimax(icor0, icor1, jcor0, jcor1, turn, depth, count, alpha, beta):

    if count == 100:
        return 0

    if depth == 3:
        check =evf()
        if check:
            return check
        return 0

    if not turn:
        best = 1000
        for i in range(icor0, icor1 + 1):
            for j in range(jcor0, jcor1 + 1):
                if board[i][j] == '-':
                    board[i] = rep_char_in_string(board[i], j, 'o')
                    count += 1
                    best = min(best, minimax(icor0, icor1, jcor0, jcor1, 1, depth + 1, count, alpha, beta))
                    board[i] = reform_string(board[i], j)
                    count -= 1
                    beta = min(beta, best)

                    if beta <= alpha:
                        break
        return best

    if turn:
        best = -1000
        for i in range(icor0, icor1 + 1):
            for j in range(jcor0, jcor1 + 1):
                if board[i][j] == '-':
                    board[i] = rep_char_in_string(board[i], j, 'x')
                    count += 1
                    best = max(best, minimax(icor0, icor1, jcor0, jcor1, 0, depth + 1, count, alpha, beta))
                    board[i] = reform_string(board[i], j)
                    count -= 1
                    alpha = max(alpha, best)

                    if beta <= alpha:
                        break
        return best

def winOrDefend():
    for coordinate in lis:
        if board[coordinate[0]][coordinate[1]] == '-':
            return coordinate[0],coordinate[1]

def computer(icor:int, jcor:int, count):
    flag =pattern_search(board,'xxxx-')
    if flag:
        a,b =winOrDefend()
        board[a] =rep_char_in_string(board[a],b,'x')
        #print(flag)
        #print('xxxx-',lis)
        return count+1,a,b
    flag = pattern_search(board, 'xxx-x')
    if flag:
        a,b =winOrDefend()
        board[a] = rep_char_in_string(board[a], b, 'x')
        #print(flag)
        #print('xxx-x', lis)
        return count+1,a,b
    flag = pattern_search(board, 'xx-xx')
    if flag:
        a,b =winOrDefend()
        board[a] = rep_char_in_string(board[a], b, 'x')
        #print(flag)
        #print('xx-xx', lis)
        return count+1,a,b
    flag = pattern_search(board, 'xxxx-')
    if flag:
        a,b =winOrDefend()
        board[a] = rep_char_in_string(board[a], b, 'x')
        #print(flag)
        #print('xxxx-', lis)
        return count+1,a,b
    flag = pattern_search(board, 'x-xxx')
    if flag:
        a,b =winOrDefend()
        board[a] = rep_char_in_string(board[a], b, 'x')
        #print(flag)
        #print('x-xxx', lis)
        return count+1,a,b
    flag = pattern_search(board, '-xxxx')
    if flag:
        a,b =winOrDefend()
        board[a] = rep_char_in_string(board[a], b, 'x')
        #print(flag)
        #print('-xxxx', lis)
        return count+1,a,b
    flag = pattern_search(board, 'oooo-')
    if flag:
        a,b =winOrDefend()
        board[a] = rep_char_in_string(board[a], b, 'x')
        #print(flag)
        #print('oooo-', lis)
        return count+1,a,b
    flag = pattern_search(board, 'ooo-o')
    if flag:
        a,b =winOrDefend()
        board[a] = rep_char_in_string(board[a], b, 'x')
        #print(flag)
        #print('ooo-o', lis)
        return count+1,a,b
    flag = pattern_search(board, 'oo-oo')
    if flag:
        a,b =winOrDefend()
        board[a] = rep_char_in_string(board[a], b, 'x')
        #print(flag)
        #print('oo-oo', lis)
        return count+1,a,b
    flag = pattern_search(board, 'o-ooo')
    if flag:
        a,b =winOrDefend()
        board[a] = rep_char_in_string(board[a], b, 'x')
        #print(flag)
        #print('o-ooo', lis)
        return count+1,a,b
    flag = pattern_search(board, '-oooo')
    if flag:
        a,b =winOrDefend()
        board[a] = rep_char_in_string(board[a], b, 'x')
        #print(flag)
        #print('-oooo', lis)
        return count+1,a,b

    flag = pattern_search(board, '-xxx--')
    if flag:
        a, b = winOrDefend()
        board[a] = rep_char_in_string(board[a], b, 'x')
        #print(flag)
        #print('-xxx--', lis)
        return count + 1, a, b

    flag = pattern_search(board, '-ooo--')
    if flag:
        a, b = winOrDefend()
        board[a] = rep_char_in_string(board[a], b, 'x')
        #print(flag)
        #print('-ooo--', lis)
        return count + 1, a, b

    #print('kono pattern milw nai')
    best = -1000
    imove, jmove = 0, 0

    imoves = [1, -1, 0, 0, 1, -1, -1, 1, 2, -2, 0, 0, 2, -2, 2, -2]
    jmoves = [0, 0, 1, -1, 1, -1, 1, -1, 0, 0, 2, -2, 2, -2, -2, 2]

    icor0, icor1, jcor0, jcor1 = coordinate(icor, jcor)

    #if moves(icor0, icor1, jcor0, jcor1) <= 4:
    if count < 4:
        from random import randint
        while True:
            i = randint(1, 15)
            if correct(icor + imoves[i], jcor + jmoves[i]) and board[icor + imoves[i]][jcor + jmoves[i]] == '-':
               # print('random move:', icor + imoves[i], jcor + jmoves[i])
                board[icor + imoves[i]] = rep_char_in_string(board[icor + imoves[i]], jcor + jmoves[i], 'x')
                count += 1
                #print_board()
                return count, icor + imoves[i],jcor + jmoves[i]

    for i in range(icor0, icor1 + 1):
        for j in range(jcor0, jcor1 + 1):
            if board[i][j] == '-':
                board[i] = rep_char_in_string(board[i], j, 'x')
                count += 1
                temp = minimax(icor0, icor1, jcor0, jcor1, 0, 1, count, -10000, 10000)
                #print('min max value',temp,i,j)
                if temp > best:
                    best = temp
                    imove = i
                    jmove = j
                board[i] = reform_string(board[i], j)
                #print_board()
                count -= 1
    #board[imove] = rep_char_in_string(board[imove], jmove, 'x')


    count += 1
    #print(count)
    #print('final best',best)
    board[imove] =rep_char_in_string(board[imove],jmove,'x')
    return count, imove, jmove

def print_board():
    for i in range(10):
        print(board[i])
    print()

count = 0
i,j =0,0
botton_col=None
#print_boa
# rd()

def labeltext(text,button,ob):
    global count
    global board

    if not button.text() == 'X' and not button.text() == 'O':
        count+=1
        #button.setText('O')
        button.setIcon(QIcon(QPixmap("black.png")))
        button.clearFocus()
        button.setEnabled(False)
        i,j =text.split('_')
        #print (i,j)
        i,j =int(i),int(j)
        i =i-1
        j =j-1
        board[i] =rep_char_in_string(board[i],j,'o')
        if checkWinner() == -100:
            from PyQt5.QtCore import pyqtSlot, QSize, Qt
            print("Human Win")
            object_name = "label"
            viewe = getattr(ob, object_name)
            viewe.setAttribute(Qt.WA_TranslucentBackground, True)
            _translate = QtCore.QCoreApplication.translate
            viewe.setHidden(False)
            viewe.setText(_translate("Play_Game",
                                     "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                     "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                     "p, li { white-space: pre-wrap; }\n"
                                     "</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                     "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:15pt; font-weight:600;\">Human Win</span></p></body></html>"))
            for i in range(1, 11):
                for j in range(1, 11):
                    object_name = "pushButton_" + str(i) + "_" + str(j)
                    button_ob = getattr(ob, object_name)
                    button_ob.setEnabled(False)
                    button_ob.setStyleSheet("border: 2px solid rgb(111, 78, 55);\n"
                                  "background: transparent;")

            #exit()
        count,imove,jmove =computer(i,j,count)
        #print("Move")
        #print('computer',imove, jmove)
        global botton_col
    # = Ui_Play_Game()
        #count, imove, jmove = computer(i, j, count)
        object_name = "pushButton_" + str(imove + 1) + "_" + str(jmove + 1)
        button_obj = getattr(ob, object_name)
        #print_board()
        #print("obj",a)
        from PyQt5.QtCore import pyqtSlot, QSize, Qt
        #button_obj.setEnabled(False)
        button_obj.setIcon(QIcon(QPixmap("white.png")))

        #button_obj.setText('X')
        #button_obj.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        button_obj.setStyleSheet("border: 3px solid black; color: black; border-color:red ;")
        button_obj.setEnabled(False)
        if not botton_col == None:
            botton_col.setStyleSheet("border: 2px solid rgb(111, 78, 55);")
        botton_col = button_obj
        #print('computer move is done')
        if checkWinner() == 100:
            print("Computer Win")
            object_name = "label"

            viewe = getattr(ob, object_name)
            viewe.setHidden(False)
            viewe.setAttribute(Qt.WA_TranslucentBackground, True)
            _translate = QtCore.QCoreApplication.translate
            viewe.setText(_translate("Play_Game", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p  align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Computer Win</span></p></body></html>"))
            for i in range(1, 11):
                for j in range(1, 11):
                    object_name = "pushButton_" + str(i) + "_" + str(j)
                    button_ob = getattr(ob, object_name)
                    button_ob.setEnabled(False)
                    button_ob.setStyleSheet("border: 2px solid rgb(111, 78, 55);\n"
                                  "background: transparent;")