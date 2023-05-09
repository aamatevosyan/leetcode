class Solution:
    def countBits(self, n: int) -> List[int]:
        memo = [0]

        for i in range(1, n + 1):
            remainer, divider = i % 2, i // 2
            memo.append(remainer + memo[divider])

        return memo