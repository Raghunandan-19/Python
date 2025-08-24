class Solution:
    def arraySortedOrNot(self, arr, n):
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                return False
        
        return True

if __name__ == "__main__":
    sol = Solution()
    n = int(input())

    arr = list(map(int, input().split()))

    print(sol.arraySortedOrNot(arr, n))