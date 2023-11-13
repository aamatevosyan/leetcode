class Solution:
    def helper(self, path: str, containers: List[str], i: int, result: List[str]):
        if len(containers) == i:
            result.append(path)
            return
        
        for j in range(len(containers[i])):
            self.helper(path + containers[i][j], containers, i + 1, result)
        

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        mappings = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        containers = [mappings[int(digit)] for digit in digits]

        result = []
        self.helper("", containers, 0, result)

        return result
        