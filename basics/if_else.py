class Solution:
    def isAdult(self, age):
        if age >= 18:
            print("Adult")
        else:
            print("Teen")

if __name__ == "__main__":
    sol = Solution()
    age = int(input())
    sol.isAdult(age)