class Solution:
    def pattern15(self, n):
        for i in range(1, (n + 1)):
            char = ord('A')

            for j in range(1, (n - i + 2)):
                print(chr(char), end='')
                char += 1
            
            print()

if __name__ == "__main__":
    sol = Solution()
    n = int(input())

    sol.pattern15(n)