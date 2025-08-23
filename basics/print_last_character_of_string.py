class Solution:
    def lastChar(self, s):
        return s[-1]
    
if __name__ == "__main__":
    sol = Solution()
    s = str(input())

    print(sol.lastChar(s))