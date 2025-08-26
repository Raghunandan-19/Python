class Solution:  
    def longestCommonPrefix(self, st):
        # Sort the list of strings lexicographically
        st.sort()
        n = len(st)

        # The common prefix must be shared between the first and last strings after sorting
        first = str(st[0])
        last = str(st[-1])

        ans = []
        # Compare characters of the first and last strings
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                # Return the prefix found so far if characters differ
                return ''.join(ans)

            # If characters match, add to the answer
            ans.append(first[i])
        
        # Return the complete common prefix
        return ''.join(ans)
    
if __name__ == "__main__":
    sol = Solution()
    st = list(map(str, input().split()))

    print(sol.longestCommonPrefix(st))