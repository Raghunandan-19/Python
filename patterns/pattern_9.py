class Solution:
    def upperHalf(self, n):
        for i in range(1, n + 1):
            # spaces
            for j in range(1, (n - i + 1)):
                print(" ", end='')
            
            # stars
            for j in range(1, (2 * i - 1) + 1):
                print('*', end='')
            
            print()
    
    def lowerHalf(self, n):
        for i in range(0, n):
            # space
            for j in range(0, i):
                print(" ", end='')
            
            # star
            for j in range(0, (n * 2) - (2 * i + 1)):
                print('*', end='')
            
            print()

    def pattern9(self, n):
        self.upperHalf(n)
        self.lowerHalf(n)

if __name__ == "__main__":
    sol = Solution()
    n = int(input())

    sol.pattern9(n)