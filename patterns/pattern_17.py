class Solution:
    def pattern17(self, n):
        for i in range(n):
            # spaces
            for j in range(n - i - 1):
                print(" ", end="")
            
            # characters
            ch = 'A'
            breakpoint = (2 * i + 1) // 2

            for j in range(1, 2 * i + 2):
                print(ch, end="")
                if j <= breakpoint:
                    ch = chr(ord(ch) + 1)
                else:
                    ch = chr(ord(ch) - 1)
            
            print()

if __name__ == "__main__":
    sol = Solution()
    n = int(input())

    sol.pattern17(n)