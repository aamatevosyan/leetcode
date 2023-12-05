class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        seq = []

        for num in nums:
            if len(seq) == 0 or seq[-1] < num:
                seq.append(num)
            else:
                ind = bisect_left(seq, num)
                seq[ind] = num

        return len(seq)