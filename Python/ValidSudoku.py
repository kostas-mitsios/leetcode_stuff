class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row by row comparison
        for row in board:
            digitSet = [x for x in row if x.isdigit()]
            rowSet = set(digitSet)
            if len(digitSet) == len(rowSet):
                continue
            else:
                return False
            
        #columb by column check
        board = [list(col) for col in zip(*board)]
        for column in board:
            digitSet = [x for x in column if x.isdigit()]
            columnSet = set(digitSet)
            if len(digitSet) == len(columnSet):
                continue
            else:
                return False
            
        #check inside box for duplicates
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                digitSet = []
                for i in range(row, row+3):
                    for j in range(col, col+3):
                        if board[i][j].isdigit():
                            digitSet.append(board[i][j])
                squareSet = set(digitSet)
                if len(digitSet) == len(squareSet):
                    continue
                else:
                    return False

        return True