class Solution:
    def longestPalindrome(self, s: str) -> int:
        res, char_count = 0, Counter(s)

        for _, cnt  in char_count.items():
            mod = cnt % 2

            if mod == 1 and res % 2 == 0:
                res += 1
            
            res += cnt - mod

        return res

        