class Solution:
    def pattern16(self, n):
        char = ord('A')

        for i in range(1, (n + 1)):
            for j in range(1, (i + 1)):
                print(chr(char), end='')
            
            char += 1
            
            print()

if __name__ == "__main__":
    sol = Solution()
    n = int(input())

    sol.pattern16(n)