
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

board2 = [
    [".",".",".",".","5",".",".","1","."],
    [".","4",".","3",".",".",".",".","."],
    [".",".",".",".",".","3",".",".","1"],
    ["8",".",".",".",".",".",".","2","."],
    [".",".","2",".","7",".",".",".","."],
    [".","1","5",".",".",".",".",".","."],
    [".",".",".",".",".","2",".",".","."],
    [".","2",".","9",".",".",".",".","."],
    [".",".","4",".",".",".",".",".","."]
]


class Solution:
    def isValidSudoku(self, board=[]) -> bool:
        row_count = []
        column_count = []
        mini_cube_count = []
        for row in board:
            for column in row:
                if not column in column_count and column != '.':
                    column_count.append(column)
                elif column in column_count:
                    '''Code used for testing'''
                    # print("Column Failure: "+ column)
                    return False
            column_count = []
            
        for i in range(len(board[0])):
            for row in board:
                if not row[i] in row_count and row[i] != '.':
                    row_count.append(row[i])
                elif row[i] in row_count:
                    '''Code used for testing'''
                    # print("Row failure: "+ str(i) + " " + row[i])
                    # print(row_count)
                    return False
            row_count = []
        
        for y in range(0,9,3):
            for x in range(0,9,3):
                for a in range(3):
                    for b in range(3):
                        if (not board[y + b][x + a] in mini_cube_count) and (
                        board[y + b][x + a] != "."
                        ):
                            mini_cube_count.append(board[y + b][x + a])
                        elif board[y + b][x + a] in mini_cube_count:
                            print("Mini square failure: "+ str(y+b) +" "+ str(x + a) +" "+ board[y+b][x + a])
                            return False
                mini_cube_count = []
        return True

new = Solution()
new.isValidSudoku(board2)