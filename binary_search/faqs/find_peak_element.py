class Solution:
    def findPeakElement(self, arr):
        n = len(arr)

        # If there is only one element, it's the peak
        if n == 1:
            return 0
        
        # Check if the first element is a peak
        if arr[0] > arr[1]:
            return 0
        
        # Check if the last element is a peak
        if arr[n - 1] > arr[n - 2]:
            return n - 1
        
        # Binary search between the second and second last elements
        low = 1
        high = n - 2

        while low <= high:
            mid = low + (high - low) // 2

            # Check if mid is a peak
            if (arr[mid - 1] < arr[mid]) and (arr[mid] > arr[mid + 1]):
                return mid
            
            # If the left neighbor is greater, move left
            if arr[mid] < arr[mid - 1]:
                high = mid - 1
            else:
            # Otherwise, move right
                low = mid + 1

        # If no peak is found (should not happen for valid input)
        return -1

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    arr = list(map(int, input().split()))

    print(sol.findPeakElement(arr))