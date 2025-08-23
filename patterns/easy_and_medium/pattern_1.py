class Solution:
    def pattern1(self, n):
        for _ in range(n):
            for _ in range(n):
                print('*', end='')
            
            print()


if __name__ == "__main__":
    sol = Solution()
    n = int(input())

    sol.pattern1(n)