class Solution(object):
    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        cols = len(matrix[0])

        low = 0
        high = rows * cols - 1 # ye high nikaalne k liye agar row x col krenge toh total len mil jaayegi ( matlab matrix m kitne elements h )

        while low <= high:

            mid = (low + high) // 2

            row = mid // cols # mid toh mil gya ab ptaa krna h ki mid matrix m khaa h toh 
                              # row  or col ka pta isse chlegaaa 
            col = mid % cols  

            if matrix[row][col] == target:
                return True

            elif matrix[row][col] < target:
                low = mid + 1

            else:
                high = mid - 1

        return False