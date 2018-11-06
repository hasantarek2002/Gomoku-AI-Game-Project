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
            print(lis)
            return True
    return False

def pattern_search(matrix, pattern):
    for row in range(R):
        for col in range(C):
            if search(matrix,pattern, row, col):

                return True
    return False

board = ["--X--O----",
         "XXX-O-OXXO",
         "XOO--OXO--",
         "--XOOOXOO-",
         "----XOOX--",
         "OXOOOXOO-O",
         "OX-----OXO",
         "OO--------",
         "----OOO---",
         "--OOX-----"]
S = pattern_search(board, "OOO--")
print(S , lis)