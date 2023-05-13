class Solution:
    def helper(
        self,
        nums: List[int],
        permutation: List[int],
        rest: List[int],
        result: List[List[int]],
    ):
        if len(rest) == 0:
            result.append(permutation[:])
            return
        
        for i, item in enumerate(rest):
            permutation.append(item)
            self.helper(nums, permutation, rest[:i] + rest[i + 1:], result)

            permutation.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        self.helper(nums, [], nums[:], result)

        return result