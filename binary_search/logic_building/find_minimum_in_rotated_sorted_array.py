class Solution:
    def findMin(self, arr):
        n = len(arr)
        low = 0
        high = n - 1
        mini = float("inf")  # Initialize minimum as infinity

        while low <= high:
            mid = low + (high - low) // 2  # Find the middle index

            # If the subarray is already sorted, the smallest element is at 'low'
            if arr[low] < arr[high]:
                mini = min(arr[low], mini)
            
            # If left half is sorted
            if arr[low] <= arr[mid]:
                mini = min(arr[low], mini)  # Update minimum
                low = mid + 1  # Search in the right half
            else:
                # If right half is sorted
                mini = min(arr[mid], mini)  # Update minimum
                high = mid - 1  # Search in the left half
            
        return mini  # Return the minimum element found

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    arr = list(map(int, input().split()))

    print(sol.findMin(arr))