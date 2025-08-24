class Solution:
    def arraySortedOrNot(self, arr, n):
        # Iterate through the array starting from the second element
        for i in range(1, n):
            # If the previous element is greater than the current, array is not sorted
            if arr[i - 1] > arr[i]:
                return False
        
        # If no such pair is found, the array is sorted
        return True

if __name__ == "__main__":
    sol = Solution()
    n = int(input())

    arr = list(map(int, input().split()))

    print(sol.arraySortedOrNot(arr, n))