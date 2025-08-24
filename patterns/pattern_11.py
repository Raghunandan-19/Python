class Solution:
    def pattern11(self, n):
        for i in range(1, (n + 1)):
            start = 1

            if i % 2 == 0: start = 0
            
            for j in range(1, (i + 1)):
                print(start, end='')
                start = 1 - start
                print(' ', end='')
            
            print()

if __name__ == "__main__":
    sol = Solution()
    n = int(input())

    sol.pattern11(n)