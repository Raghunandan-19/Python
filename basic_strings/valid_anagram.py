class Solution:    
    def anagramStrings(self, s, t):
        # Check if the lengths of the strings are different
        if len(s) != len(t):
            return False
        
        # Initialize frequency arrays for both strings (assuming lowercase a-z)
        freq_s = [0] * 26
        freq_t = [0] * 26

        # Count the frequency of each character in both strings
        for i in range(len(s)):
            freq_s[ord(s[i]) - ord('a')] += 1
            freq_t[ord(t[i]) - ord('a')] += 1
        
        # Compare the frequency arrays
        for i in range(26):
            if freq_s[i] != freq_t[i]:
                return False
        
        # If all frequencies match, the strings are anagrams
        return True

if __name__ == "__main__":
    sol = Solution()
    s = str(input())
    t = str(input())
    
    print(sol.anagramStrings(s, t))