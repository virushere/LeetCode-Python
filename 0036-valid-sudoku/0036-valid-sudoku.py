class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # My solution
        rows = [set() for _ in range (9)]
        cols = [set() for _ in range (9)]
        sub_grids = [set() for _ in range (9)]

        for r in range (9):
            for c in range (9):
                num = board[r][c]
                if num == ".":
                    continue
                
                # calculate subgrid index 
                subgrid_index = (r//3)* 3 + (c//3)
                if (num in rows[r] or 
                    num in cols[c] or 
                    num in sub_grids[subgrid_index]):
                    return False

                rows[r].add(num)
                cols[c].add(num)
                sub_grids[subgrid_index].add(num)

        return True

        # Neetcode solutin
        # for row in range(9):
        #     seen = set()
        #     for i in range(9):
        #         if board[row][i] == ".":
        #             continue
        #         if board[row][i] in seen:
        #             return False
        #         seen.add(board[row][i])
            
        # for col in range(9):
        #     seen = set()
        #     for i in range(9):
        #         if board[i][col] == ".":
        #             continue
        #         if board[i][col] in seen:
        #             return False
        #         seen.add(board[i][col])


        # for sq in range(9):
        #     seen = set()
        #     for i in range(3):
        #         for j in range(3):
        #             row = (sq//3) * 3 + i
        #             col = (sq//3) * 3 + j
        #             if board[row][col] == ".":
        #                 continue
        #             if board[row][col] in seen:
        #                 return False
        #             seen.add(board[row][col])
        # return True