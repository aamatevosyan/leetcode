class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix, curr_sum = [0], 0
        for num in nums:
            curr_sum += num
            prefix.append(curr_sum)
        prefix.append(prefix[-1])

        for i in range(1, len(prefix) - 1):
            if prefix[i - 1] == prefix[-1] - prefix[i]:
                return i - 1
        
        return -1
        