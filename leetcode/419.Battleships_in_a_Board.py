class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        R = len(board)
        if R == 0:
            return 0
        C = len(board[0])
        onboard = False
        counter = 0
        for j in range(C):
            if board[0][j] == "X":
                if onboard == False:
                    counter += 1
                    onboard = True
            else:
                onboard = False

        for i in range(1, R, 1):
            onboard = False
            for j in range(C):
                if board[i][j] == "X":
                    if onboard == False and board[i - 1][j] != "X":
                        counter += 1
                        onboard = True
                else:
                        onboard = False
        return counter


print Solution().countBattleships(
    [[".", "X", ".", ".", "X"], ["X", ".", ".", "X", "."], [".", "X", ".", ".", "X"], [".", "X", ".", "X", "."],
     ["X", ".", "X", ".", "X"]])
