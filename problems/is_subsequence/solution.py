class Solution:
    def isSubsequence(self, pattern: str, line: str) -> bool:
        if len(pattern) == 0:
            return True

        if len(line) == 0:
            return False

        ind = 0
        ans = True

        for c in pattern:
            if ind >= len(line):
                ans = False
                break

            found = False

            while ind < len(line) and not found:
                if line[ind] == c:
                    found = True
                ind += 1

            if not found:
                return False

        return ans