class Solution:
    def whichWeekDay(self, day):
        if day < 1 or day > 7:
            print("Invalid")
            return
        
        match day:
            case 1:
                print("Monday")
            case 2:
                print("Tuesday")
            case 3:
                print("Wednesday")
            case 4:
                print("Thursday")
            case 5:
                print("Friday")
            case 6:
                print("Saturday")
            case 7:
                print("Sunday")

if __name__ == "__main__":
    sol = Solution()
    day = int(input())

    sol.whichWeekDay(day)