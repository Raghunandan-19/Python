class Solution:
    def pattern2(self, n):
        for i in range(n):
            for j in range(i + 1):
                print('*', end='')
            
            print()

if __name__ == "__main__":
    sol = Solution()
    n = int(input())

    sol.pattern2(n)