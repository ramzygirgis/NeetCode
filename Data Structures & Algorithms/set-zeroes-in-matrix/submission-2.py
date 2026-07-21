class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        cols = set()
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            rowIsZero = False
            for j in range(m):
                if matrix[i][j] == 0:
                    if rowIsZero == False:
                        rowIsZero = True
                        for k in range(j):
                            matrix[i][k] = 0
                        for k in range(i):
                            matrix[k][j] = 0
                    cols.add(j)
                if rowIsZero == True or j in cols:
                    matrix[i][j] = 0