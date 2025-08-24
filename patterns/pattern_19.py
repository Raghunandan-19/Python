class Solution:
    def upperHalf(self, n):
        for i in range(0, n):
            # star
            for j in range(1, (n - i + 1)):
                print('*', end='')
            
            # space
            for j in range(1, (2 * i + 1)):
                print(' ', end='')
            
            # star
            for j in range(1, (n - i + 1)):
                print('*', end='')
            
            print()

    def lowerHalf(self, n):
        for i in range(0, n):
            spaces = (2 * n - 2) - (2 * i)

            # star
            for j in range(1, (i + 2)):
                print('*', end='')
            
            # space
            for j in range(1, (spaces + 1)):
                print(' ', end='')
            
            # star
            for j in range(1, (i + 2)):
                print('*', end='')
            
            print()

    def pattern19(self, n):
        self.upperHalf(n)
        self.lowerHalf(n)

if __name__ == "__main__":
    sol = Solution()
    n = int(input())

    sol.pattern19(n)