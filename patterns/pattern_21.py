class Solution:
    def pattern21(self, n):
        for i in range(0, n):
            for j in range(0, n):
                if (i == 0) or (i == (n - 1)) or (j == 0) or (j == (n - 1)):
                    print('*', end='')
                else:
                    print(' ', end='')
            
            print()

if __name__ == "__main__":
    sol = Solution()
    n = int(input())

    sol.pattern21(n)