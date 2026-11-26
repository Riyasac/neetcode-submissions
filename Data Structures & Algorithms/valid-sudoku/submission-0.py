class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            rows = set()
            columns = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in rows:
                        return False
                    else:
                        rows.add(board[i][j])
                
                if board[j][i] != ".":
                    if board[j][i] in columns:
                        return False
                    else:
                        columns.add(board[j][i])
    
    
        for k in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (k//3) * 3 + i
                    col = (k%3) * 3 + j
                    if board[row][col] != ".":
                        if board[row][col] in seen:
                            return False
                        else:
                            seen.add(board[row][col])
        return True
        
        