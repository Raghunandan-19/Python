class Solution:
    # Function to find the upper bound of an element in a row
    def upperBound(self, arr, x, m):
        low, high = 0, m - 1
        ans = m

        # Apply binary search
        while low <= high:
            mid = (low + high) // 2

            # If arr[mid] > x, it can be a possible upper bound
            if arr[mid] > x:
                ans = mid
                # Look for smaller bound on the left
                high = mid - 1
            else:
                low = mid + 1

        return ans

    # Function to count how many elements in matrix are less than or equal to x
    def countSmallEqual(self, matrix, n, m, x):
        cnt = 0
        for i in range(n):
            cnt += self.upperBound(matrix[i], x, m)
        return cnt

    # Function to find the median in the matrix
    def findMedian(self, matrix):
        n, m = len(matrix), len(matrix[0])
        low, high = float('inf'), float('-inf')

        # Find the minimum and maximum values
        for i in range(n):
            low = min(low, matrix[i][0])
            high = max(high, matrix[i][m - 1])

        req = (n * m) // 2

        # Binary search to find the median
        while low <= high:
            mid = (low + high) // 2

            smallEqual = self.countSmallEqual(matrix, n, m, mid)

            if smallEqual <= req:
                low = mid + 1
            else:
                high = mid - 1

        return low

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    print(sol.findMedian(matrix))