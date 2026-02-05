"""

238. Product of Array Except Self

	Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

	The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

	You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

	Input: nums = [1,2,3,4]
	Output: [24,12,8,6]

Example 2:

	Input: nums = [-1,1,0,-3,3]
	Output: [0,0,9,0,0]

Constraints:

	- 2 <= nums.length <= 10^5
	- -30 <= nums[i] <= 30
	- The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

"""

# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
	def productExceptSelf(self, nums: List[int]) -> List[int]:
		# Intialize our answer, prefix_product, and suffix_product arrays
		size = len(nums)
		answer, prefix_products, suffix_products = [1] * size, [1] * size, [1] * size

		# Pre-compute prefix and suffix product values
		previous_prefix_val, previous_suffix_val = 1, 1
		for num_index in range(size):
			prefix_products[num_index] = previous_prefix_val * nums[num_index]
			suffix_products[size - num_index - 1] = previous_suffix_val * nums[size - num_index - 1]
			previous_prefix_val, previous_suffix_val = prefix_products[num_index], suffix_products[size - num_index - 1]

		# Calculate answers using the prefix product to the left times the suffix product to the right of the current index
		for num_index in range(size):
			if num_index - 1 >= 0:
				answer[num_index] *= prefix_products[num_index - 1]
			if num_index + 1 < size:
				answer[num_index] *= suffix_products[num_index + 1]

		return answer