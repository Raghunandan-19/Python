class Solution:    
    def rotateString(self, s, goal):
        # Check if the lengths of s and goal are different
        if len(s) != len(goal):
            return False
        
        # Concatenate s with itself to cover all possible rotations
        doubled_s = s + s

        # Check if goal is a substring of the doubled string
        return goal in doubled_s

if __name__ == "__main__":
    sol = Solution()
    s = str(input())
    goal = str(input())

    print(sol.rotateString(s, goal))