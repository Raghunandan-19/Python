class Solution:
    def pattern7(self, n):
        for i in range(1, n + 1):
            # spaces
            for j in range(1, (n - i + 1)):
                print(" ", end='')
            
            # stars
            for j in range(1, (2 * i - 1) + 1):
                print('*', end='')
            
            print()

if __name__ == "__main__":
    sol = Solution()
    n = int(input())

    sol.pattern7(n)