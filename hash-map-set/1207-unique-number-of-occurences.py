"""

1207. Unique Number of Occurrences

	Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Example 1:

	Input: arr = [1,2,2,1,1,3]
	Output: true
	Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Example 2:

	Input: arr = [1,2]
	Output: false

Example 3:

	Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
	Output: true
 
Constraints:

	- 1 <= arr.length <= 1000
	- -1000 <= arr[i] <= 1000

"""

# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        uniqueVals, counts = set(arr), dict()

        # Loop through each index in the array
        for i in range(len(arr)):
        	# Count the number of times we encounter the value
            val = arr[i]
            if val in counts.keys():
                counts[val] += 1
            else:
                counts[val] = 1

        # Return True if the size of the counts set equals the number of unique values
        return True if len(set(counts.values())) == len(uniqueVals) else False