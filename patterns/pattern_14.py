class Solution:
    def pattern14(self, n):
        for i in range(1, (n + 1)):
            char = ord('A')

            for j in range(1, (i + 1)):
                print(chr(char), end='')
                char += 1
            
            print()

if __name__ == "__main__":
    sol = Solution()
    n = int(input())

    sol.pattern14(n)