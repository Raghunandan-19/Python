class Solution:
    def pattern6(self, n):
        for i in range(1, n + 1):
            for j in range(1, n - i + 2):
                print(j, end='')
            
            print()

if __name__ == "__main__":
    sol = Solution()
    n = int(input())

    sol.pattern6(n)