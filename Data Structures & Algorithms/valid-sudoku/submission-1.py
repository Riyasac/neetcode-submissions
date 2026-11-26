class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        rows = defaultdict(set)
        cols = defaultdict(set)
        box = defaultdict(set)

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                square = (i//3, j//3)
                
                if val == ".":
                    continue

                if (
                    val in rows[i] or
                    val in cols[j] or
                    val in box[square]
                    ):
                        return False
                rows[i].add(val)
                cols[j].add(val)
                box[square].add(val)
        return True
        
        