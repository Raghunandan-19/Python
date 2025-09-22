class Solution:
    # Function to search for a given target in matrix
    def searchMatrix(self, matrix, target):
        n = len(matrix)
        m = len(matrix[0])
        
        # Initialize the row and col
        row, col = 0, m - 1

        # Traverse the matrix from (0, m-1):
        while row < n and col >= 0:
            
            # Return true if target is found
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        
        # Return false if target not found
        return False

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    matrix = []
    rows = int(input())
    cols = int(input())

    for _ in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    target = int(input("Enter target value: "))
    
    print(sol.searchMatrix(matrix, target))