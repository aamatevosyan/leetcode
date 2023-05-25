class Solution:
    def generate(self, curr: List[str], opened: int, closed: int, n: int, result: List[str]):
        if opened + closed == 2 * n:
            result.append(''.join(curr))
            return
        
        if opened < n:
            curr.append('(')
            self.generate(curr, opened + 1, closed, n, result)
            curr.pop()
        
        if closed < opened:
            curr.append(')')
            self.generate(curr, opened, closed + 1, n, result)
            curr.pop()

    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.generate([], 0, 0, n, result)

        return result
