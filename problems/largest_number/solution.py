class LargerNumKey(str):
    def __lt__(x : str, y: str):
        return x + y > y + x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = sorted(map(str, nums), key=LargerNumKey)
        result = ''.join(str_nums)
        
        return result if result[0] != '0' else '0'
        