class Solution:
    def permutate(self, current: List[str], containers: List[str], ind: int, result: List[str]):
        if len(containers) == ind:
            result.extend(current)
            return
        
        tmp = []

        for i in range(len(containers[ind])):
            for j in range(len(current)):
                tmp.append(current[j] + containers[ind][i])
        
        self.permutate(tmp, containers, ind + 1, result)
        

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        mappings = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        containers = [mappings[int(digit)] for digit in digits]

        result = []
        self.permutate([""], containers, 0, result)

        return result
