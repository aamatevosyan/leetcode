/**
 * @param {number[]} nums
 * @return {number[]}
 */
var runningSum = function(nums) {
    const result = [];
    let curSum = 0;
    
    for (const num of nums) {
        curSum += num;
        result.push(curSum);
    }
    
    return result;
};