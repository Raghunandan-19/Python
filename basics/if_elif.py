class Solution:
    def studentGrade(self, marks):
        if marks >= 90.0:
            print("Grade A")
        elif marks >= 70.0:
            print("Grade B")
        elif marks >= 50.0:
            print("Grade C")
        elif marks >= 35.0:
            print("Grade D")
        else:
            print("Fail")

if __name__ == "__main__":
    sol = Solution()
    marks = float(input())
    sol.studentGrade(marks)