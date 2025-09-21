class Solution:
    # Helper function to find the lower bound of 1.
    def lowerBound(self, arr, n, x):
        low, high = 0, n - 1
        ans = n

        while low <= high:
            mid = (low + high) // 2
                
            """If element at mid is greater than or equal 
            to x then it could be a possible answer."""
            if arr[mid] >= x:
                ans = mid
                    
                # Look for smaller index on the left
                high = mid - 1
            else:
                low = mid + 1
            
        # Return the answer
        return ans
        
    """ Function to find the row 
    with the maximum number of 1's"""
    def rowWithMax1s(self, mat):
        n = len(mat)
        m = len(mat[0])
        
        """ Variable to store the 
        maximum count of 1's found"""
        cnt_max = 0 
        
        """ Variable to store the index
        of the row with max 1's"""
        index = -1  

        # Traverse each row of the matrix
        for i in range(n):
            # Get the number of 1's
            cnt_ones = m - self.lowerBound(mat[i], m, 1)
            
            """ If the current count is greater than 
            maximum, store the index of current row
            and update the maximum count."""
            if cnt_ones > cnt_max:
                cnt_max = cnt_ones
                index = i
        
        """ Return the index of the row 
        with the maximum number of 1's"""
        return index

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    mat = []
    
    for _ in range(n):
        mat.append(list(map(int, input().split())))

    print(sol.rowWithMax1s(mat))