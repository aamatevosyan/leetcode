class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return nums
        
        _sum, _max, _map = 0, 0, { 0: -1 }

        for i in range(len(nums)):
            _sum += nums[i] if nums[i] == 1 else -1

            if _sum in _map:
                _max = max(_max, i - _map[_sum])
            else:
                _map[_sum] = i

        return _max
