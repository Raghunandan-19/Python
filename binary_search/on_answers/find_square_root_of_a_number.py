class Solution:
    def floorSqrt(self, n: int) -> int:
        # Initialize the search range
        low = 1
        high = n

        # Perform binary search
        while low <= high:
            mid = low + (high - low) // 2  # Find the middle value
            val = mid * mid  # Square of mid

            if val <= n:
                # If mid*mid is less than or equal to n, move to the right half
                low = mid + 1
            else:
                # If mid*mid is greater than n, move to the left half
                high = mid - 1
        
        # high will be the floor of the square root of n
        return high

if __name__ == "__main__":
    sol = Solution()
    n = int(input())

    print(sol.floorSqrt(n))