"""

283. Move Zeroes

	Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

	Note that you must do this in-place without making a copy of the array.

Example 1:

	Input: nums = [0,1,0,3,12]
	Output: [1,3,12,0,0]

Example 2:

	Input: nums = [0]
	Output: [0]
 
Constraints:

	- 1 <= nums.length <= 10^4
	- -2^31 <= nums[i] <= 2^31 - 1

"""

# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # Initialize the write pointer, then read through each number in the array
        write_ptr = 0
        for read_ptr in range(len(nums)):
            # Always write non-zeroes numbers to the next write position, this causes all the zeroes to shift to the end
            if nums[read_ptr] != 0:
                nums[write_ptr], nums[read_ptr] = nums[read_ptr], nums[write_ptr]
                write += 1
