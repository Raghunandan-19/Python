class Solution:
    def isomorphicString(self, s, t):
        # Initialize two arrays to keep track of character mappings for both strings
        m1, m2 = [0] * 256, [0] * 256

        n = len(s)

        for i in range(n):
            # If the last seen positions of the current characters don't match, strings aren't isomorphic
            if m1[ord(s[i])] != m2[ord(t[i])]:
                return False

            # Update the last seen positions for both characters
            m1[ord(s[i])] = i + 1
            m2[ord(t[i])] = i + 1

        # If all characters match the mapping, the strings are isomorphic
        return True

if __name__ == "__main__":
    sol = Solution()
    s = str(input())
    t = str(input())

    print(sol.isomorphicString(s, t))