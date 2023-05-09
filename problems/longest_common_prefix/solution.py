class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        ans = ""
        
        for i in range(len(strs[0])):
            c = strs[0][i]

            for j in range(1, len(strs)):
                s = strs[j]
                if i >= len(s) or s[i] != c:
                    return ans
            
            ans += c
        
        return ans