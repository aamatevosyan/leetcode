class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        results = []

        for i in range(len(nums) - 3):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            for j in range(i + 1, len(nums) - 2):
                if j != i + 1 and nums[j - 1] == nums[j]:
                    continue

                start = j + 1
                end = len(nums) - 1

                while start < end:
                    current_sum = nums[i] + nums[j] + nums[start] + nums[end]

                    if current_sum == target:
                        results.append([nums[i], nums[j], nums[start], nums[end]])
                        start += 1
                        end -= 1
                        
                        while start < end and nums[start] == nums[start - 1]:
                            start += 1
                        
                        while start < end and nums[end] == nums[end + 1]:
                            end -= 1
                    elif current_sum < target:
                        start += 1
                    else:
                        end -= 1
        
        return results
