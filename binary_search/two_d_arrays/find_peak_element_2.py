class Solution:
    """Helper function to find the index of the row
    with the maximum element in a given column"""
    def maxElement(self, arr, col):
        n = len(arr)
        max_val = float('-inf')
        index = -1
        
        """Iterate through each row to find the
        maximum element in the specified column"""
        for i in range(n):
            if arr[i][col] > max_val:
                max_val = arr[i][col]
                index = i
                
        # Return the index
        return index
    
    """Function to find a peak element in 
    the 2D matrix using binary search """
    def findPeakGrid(self, arr):
        n = len(arr)    
        m = len(arr[0])  
        
        """Initialize the lower bound for 
        and upper bound for binary search"""
        low = 0           
        high = m - 1      
        
        # Perform binary search on columns
        while low <= high:
            mid = (low + high) // 2 
            
            """Find the index of the row with the 
            maximum element in the middle column"""
            row = self.maxElement(arr, mid)
            
            """ Determine the elements to left and 
            right of middle element in the found row """
            left = arr[row][mid - 1] if mid - 1 >= 0 else float('-inf')
            right = arr[row][mid + 1] if mid + 1 < m else float('-inf')
            
            """ Check if the middle element 
            is greater than its neighbors """
            if arr[row][mid] > left and arr[row][mid] > right:
                return [row, mid]  
            elif left > arr[row][mid]:
                high = mid - 1  
            else:
                low = mid + 1  
        
        # Return [-1, -1] if no peak element is found
        return [-1, -1]
    
if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().split())))
    
    print(sol.findPeakGrid(arr))