class Solution:
    def upperHalf(self, n):
        for i in range(0, n):
            # stars
            for j in range(0, (i + 1)):
                print('*', end='')
            
            # spaces
            spaces = (2 * n - 2) - (2 * i)
            for j in range(1, (spaces + 1)):
                print(' ', end='')

            # stars
            for j in range(0, (i + 1)):
                print('*', end='')
            
            print()
    
    def lowerHalf(self, n):
        for i in range(1, n):
            # stars
            for j in range(1, ((n - i) + 1)):
                print('*', end='')
            
            # spaces
            spaces = (2 * i)
            for j in range(1, (spaces + 1)):
                print(' ', end='')
            
            # stars
            for j in range(1, ((n - i) + 1)):
                print('*', end='')
            
            print()

    def pattern20(self, n):
        self.upperHalf(n)
        self.lowerHalf(n)

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    
    sol.pattern20(n)