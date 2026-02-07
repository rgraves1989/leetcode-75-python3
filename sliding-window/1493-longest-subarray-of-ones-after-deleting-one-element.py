"""

1493. Longest Subarray of 1's After Deleting One Element

    Given a binary array nums, you should delete one element from it.

    Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

Example 1:

    Input: nums = [1,1,0,1]
    Output: 3
    Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

Example 2:

    Input: nums = [0,1,1,1,0,1,1,0,1]
    Output: 5
    Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

Example 3:

    Input: nums = [1,1,1]
    Output: 2
    Explanation: You must delete one element. 

Constraints:

    - 1 <= nums.length <= 10^5
    - nums[i] is either 0 or 1.

"""


# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Initialize our sliding window pointers and zero_count
        left_ptr, zero_count, max_len = 0, 0, 0

        # Maintain a sliding witndow with up to one zero in it
        for right_ptr in range(len(nums)):
            # Next digit is a zero, add to our count
            if nums[right_ptr] == 0:
                zero_count += 1

            # We have more than 1 zero in the window, advance the left pointer until we don't anymore
            while zero_count > 1:
                # Leaving digit is a zero, subtract from our count
                if nums[left_ptr] == 0:
                    zero_count -= 1
                left_ptr += 1

            # Keep track of the longest window length
            max_len = max(max_len, right_ptr - left_ptr)

        return max_len
