class Solution:
    def is_valid(self, s: str) -> bool:
        cnt = 0

        for c in s:
            if c == '(':
                cnt += 1
            elif c == ')':
                cnt -= 1
            
            if cnt < 0 or cnt * 2 > len(s):
                return False 

        return cnt == 0

    def backtrack(self, i: int, curr: str, s: str, result: Set[str]):
        if i == len(s):
            if self.is_valid(curr):
                result.add(curr)
            return
        
        self.backtrack(i + 1, curr + s[i], s, result)

        if s[i] in ('(', ')'):
            self.backtrack(i + 1, curr[:i] + curr[i + 1:], s, result)

    def removeInvalidParentheses(self, s: str) -> List[str]:
        result = set()

        self.backtrack(0, "", s, result)

        max_len = max(map(len, result))

        return [item for item in result if len(item) == max_len]


        