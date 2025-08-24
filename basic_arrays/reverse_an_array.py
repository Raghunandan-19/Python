class Solution:
    def reverse(self, arr, n):
        # Initialize two pointers: one at the start and one at the end of the array
        left = 0
        right = n - 1

        # Swap elements from both ends moving towards the center
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]  # Swap the elements
            left += 1   # Move left pointer to the right
            right -= 1  # Move right pointer to the left

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    arr = list(map(int, input().split()))

    sol.reverse(arr, n)
    
    i = 0
    while i < n:
        print(arr[i], end=' ')
        i += 1
    print()
