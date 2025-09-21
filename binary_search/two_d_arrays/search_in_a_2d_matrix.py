class Solution:
    # Function to search for a given target in matrix
    def searchMatrix(self, mat, target):
        n = len(mat)
        m = len(mat[0])

        low, high = 0, n * m - 1
        
        # Perform binary search
        while low <= high:
            mid = (low + high) // 2
            
            # Calculate the row and column
            row = mid // m
            col = mid % m
            
            # If target is found return true
            if mat[row][col] == target:
                return True
            elif mat[row][col] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        # Return false if target is not found
        return False

if __name__ == "__main__":
    sol = Solution()
    n, m = map(int, input().split())
    mat = []
    
    for _ in range(n):
        mat.append(list(map(int, input().split())))
    
    target = int(input())
    print(sol.searchMatrix(mat, target))# Helper function to find the lower bound of 1.