class Solution:
    def upperHalf(self, n):
        for i in range(1, (n + 1)):
            for j in range(1, (i + 1)):
                print('*', end='')
            
            print()

    def lowerHalf(self, n):
        for i in range(1, (n + 1)):
            for j in range(0, (n - i + 1)):
                print('*', end='')
            
            print()

    def pattern10(self, n):
        self.upperHalf(n)
        self.lowerHalf(n - 1)

if __name__ == "__main__":
    sol = Solution()
    n = int(input())

    sol.pattern10(n)