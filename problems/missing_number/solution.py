class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        _n = len(nums)
        _total_sum = _n // 2 * (_n + 1) if _n % 2 == 0 else _n * ((_n + 1) // 2)

        for num in nums:
            _total_sum -= num
        
        return _total_sum