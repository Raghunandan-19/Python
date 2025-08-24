class Solution:
    def countOdd(self, arr, n):
        # Initialize counter for odd numbers
        count_odd = 0

        # Iterate through the array
        for i in range(n):
            # Check if the current element is odd
            if arr[i] % 2 == 1:
                count_odd += 1  # Increment counter if odd
        
        # Return the total count of odd numbers
        return count_odd

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    arr = list(map(int, input().split()))

    print(sol.countOdd(arr, n))