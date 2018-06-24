class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # row_sets = [set() for _ in range(9)]
        # col_sets = [set() for _ in range(9)]
        # sub_sets = [[set() for _ in range(3)] for _ in range(3)]
        # for i in range(9):
        #     for j in range(9):
        #         b = board[i][j]
        #         if b != '.':
        #             if b in row_sets[i]:
        #                 return False
        #             else:
        #                 row_sets[i].add(b)
        #             if b in col_sets[j]:
        #                 return False
        #             else:
        #                 col_sets[j].add(b)
        #             if b in sub_sets[i / 3][j / 3]:
        #                 return False
        #             else:
        #                 sub_sets[i / 3][j / 3].add(b)
        # return True
        seen = []
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c != '.':
                    seen += (c,j),(c,i+10),(i/3,j/3,c),
        return len(seen) == len(set(seen))

seen =[(8,0),('8',0)]
for a,b in seen:
    print a,b

print Solution().isValidSudoku([
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
])
