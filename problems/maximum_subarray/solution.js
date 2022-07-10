/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let max = nums[0];
    let localMax = max;
    
    for (let i = 1; i < nums.length; i++) {
        localMax = Math.max(nums[i], localMax + nums[i]);
        
        if (localMax > max) {
            max = localMax;
        }
    }
    
    return max;
};