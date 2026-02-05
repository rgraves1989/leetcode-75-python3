"""

334. Increasing Triplet Subsequence

	Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Example 1:

	Input: nums = [1,2,3,4,5]
	Output: true
	Explanation: Any triplet where i < j < k is valid.

Example 2:

	Input: nums = [5,4,3,2,1]
	Output: false
	Explanation: No triplet exists.

Example 3:

	Input: nums = [2,1,5,0,4,6]
	Output: true
	Explanation: One of the valid triplet is (1, 4, 5), because nums[1] == 1 < nums[4] == 4 < nums[5] == 6.
 
Constraints:

	- 1 <= nums.length <= 5 * 10^5
	- -2^31 <= nums[i] <= 2^31 - 1

"""

# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        lowest_num, second_lowest_num = float('inf'), float('inf')

        for curr_num in nums:
            if curr_num <= lowest_num:
                lowest_num = curr_num
            elif curr_num <= second_lowest_num:
                second_lowest_num = curr_num
            else:
                return True

        return False