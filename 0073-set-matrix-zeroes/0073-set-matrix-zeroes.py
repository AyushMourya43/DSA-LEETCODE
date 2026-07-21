class Solution(object):
    def setZeroes(self, matrix):
        
        rows = len(matrix)
        cols = len(matrix[0])

        zeros = []

        # phle check krenge kha kha zero h matrix m 
        for i in range(rows):
            for j in range(cols):
              if matrix[i][j] == 0:
                zeros.append((i,j))

        # ab rows or colums ko 0 bnaayenge
        for i , j in zeros:

            for c in range(cols):
                matrix[i][c] = 0

            for r in range(rows):
                matrix[r][j] = 0





               