"""Valid Sudoku"""

class Solution(object):
    def isValidSudoku(self, board):
        board_transponse = [list(x) for x in zip(*board)]
        board_big = [[[],[],[]],
                     [[],[],[]],
                     [[],[],[]]]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if board[i].count(board[i][j]) > 1:
                        return False   
                if board_transponse[i][j] != ".":
                    if board_transponse[i].count(board_transponse[i][j]) > 1:
                        return False
                board_big[(i)//3][(j)//3].append(board[i][j])
        for i in board_big:
            for j in i:
                for x in j:
                    if x != ".":
                        if j.count(x) > 1:
                            return False
        return True    

board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
        
print(solution.isValidSudoku(board))
