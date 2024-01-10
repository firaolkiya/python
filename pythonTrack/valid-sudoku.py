class Solution(object):
    def isValidSudoku(self, board):
        for i in board:
            counter = Counter(i)
            print(counter)
            for j in i:
                if counter[j]>1 and j!=".":
                    return False
        
        for i in range(9):
            set4=set()
            for j in range(9):
                if board[j][i] in set4 and board[j][i]!=".":
                    return False
                set4.add(board[j][i])

        for i in range(1,9,3):
            for j in range(1,9,3):
                set1=[]
                print(i,j)
                set1.append(board[i-1][j-1])
                set1.append(board[i-1][j])
                set1.append(board[i-1][j+1])
                set1.append(board[i][j-1])
                set1.append(board[i][j])
                set1.append(board[i][j+1])
                set1.append(board[i+1][j-1])
                set1.append(board[i+1][j])
                set1.append(board[i+1][j+1])
                co = Counter(set1)
                for j in co:
                    if co[j]>1 and j!=".":
                        return False
        return True