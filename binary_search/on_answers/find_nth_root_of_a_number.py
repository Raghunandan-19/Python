class Solution:
    def NthRoot(self, n, m):
        # Initialize the search range
        low = 1
        high = m 

        # Binary search to find the nth root
        while low <= high:
            mid = low + (high - low) // 2
            val = pow(mid, n)  # Calculate mid raised to the power n

            if val == m:
                return mid  # Found the nth root

            if val < m:
                low = mid + 1  # Search in the higher half
            else:
                high = mid - 1  # Search in the lower half

        # If no integer nth root exists, return -1
        return -1

if __name__ == "__main__":
    sol = Solution()
    n, m = map(int, input().split())

    print(sol.NthRoot(n, m))