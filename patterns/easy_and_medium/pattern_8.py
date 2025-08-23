class Solution:
    def pattern8(self, n):
        for i in range(0, n):
            # space
            for j in range(0, i):
                print(" ", end='')
            
            # star
            for j in range(0, (n * 2) - (2 * i + 1)):
                print('*', end='')
            
            print()

if __name__ == "__main__":
    sol = Solution()
    n = int(input())

    sol.pattern8(n)