"""

643. Maximum Average Subarray I

	You are given an integer array nums consisting of n elements, and an integer k.

	Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Example 1:

	Input: nums = [1,12,-5,-6,50,3], k = 4
	Output: 12.75000
	Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:

	Input: nums = [5], k = 1
	Output: 5.00000
 
Constraints:

	- n == nums.length
	- 1 <= k <= n <= 105
	- -10^4 <= nums[i] <= 10^4

"""

# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
    	# Find the sum of the first k elements, intialize the max_sum value to this
        window_sum = sum(nums[:k])
        max_sum = window_sum

        # Loop through the remaining elements and determine if the next k elemnts has a higher sum or not
        for i in range(k, len(nums)):
            window_sum += nums[i]
            window_sum -= nums[i - k]
            max_sum = max(max_sum, window_sum)
        
        # Return the max average
        return max_sum / k