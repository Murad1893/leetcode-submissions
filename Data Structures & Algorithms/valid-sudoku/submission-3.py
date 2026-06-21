from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # rows, cols = len(board), len(board[0])

        # # check rows
        # for i in range(rows):
        #     seen = set()
        #     for k in range(cols):
        #         num = board[i][k]
        #         if num != '.':
        #             if num in seen: return False
        #             seen.add(num)
            
        
        # # check cols
        # for j in range(cols):
        #     seen = set()
        #     for k in range(rows):
        #         num = board[k][j]
        #         if num != '.':
        #             if num in seen: return False
        #             seen.add(num)

        # # check blocks - always 3
        # grid_size = 3
        # for i in range(0, len(board), grid_size):
        #     for j in range(0, len(board[0]), grid_size):
        #         seen = set()
        #         for k in range(i, i+grid_size):
        #             for l in range(j, j+grid_size):
        #                 num = board[k][l]
        #                 if num != '.':
        #                     if num in seen: return False
        #                     seen.add(num)
        
        # return True

        # maintain hash set per row col and grid in one pass
        # cannot maintain just a single set since we are iterating together - can't reset everytime
        row = defaultdict(set)
        col = defaultdict(set)
        grid = defaultdict(set) # you store r//3,c//3

        for i in range(len(board)):
            for j in range(len(board[0])):
                num = board[i][j]
                if num != '.':
                    if (num in row[i] or num in col[j] or num in grid[(i//3, j//3)]):
                        return False
                    row[i].add(num)
                    col[j].add(num)
                    grid[(i//3,j//3)].add(num)

        return True