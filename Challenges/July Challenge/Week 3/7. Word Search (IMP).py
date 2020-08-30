# Amazon

board = [['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']]


def search(board,key):
    n,m = len(board),len(board[0])

    for i in range(n):
        for j in range(m):
            if board[i][j] == key[0] and recc_search(board,i,j,n,m,0,key,len(key)):
                return True
    
    return False


def recc_search(board,i,j,n,m,idx,key,key_len):

    if idx == key_len:
        return True

    if i<0 or i>=n or j<0 or j>=m:
        return False
    
    if board[i][j] != key[idx]:
        return False
    
    temp = board[i][j]
    board[i][j] = '0'

    found_rest = recc_search(board,i+1,j,n,m,idx+1,key,key_len) or recc_search(board,i-1,j,n,m,idx+1,key,key_len) or recc_search(board,i,j+1,n,m,idx+1,key,key_len) or recc_search(board,i,j-1,n,m,idx+1,key,key_len)

    board[i][j] = temp

    return found_rest        



key = input()
res = search(board,key)
print(res)
