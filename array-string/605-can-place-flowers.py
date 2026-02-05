"""

605. Can Place Flowers

	You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

	Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Example 1:

	Input: flowerbed = [1,0,0,0,1], n = 1
	Output: true

Example 2:

	Input: flowerbed = [1,0,0,0,1], n = 2
	Output: false
 
Constraints:

    - 1 <= flowerbed.length <= 2 * 10^4
    - flowerbed[i] is 0 or 1.
    - There are no two adjacent flowers in flowerbed.
    - 0 <= n <= flowerbed.length

"""

# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    	# Track the # of remaining flowers left to place
        leftToPlace = n

        # Loop through the flowerbed positions
        for i in range(len(flowerbed)):
            # No flowers left to place, break
            if leftToPlace == 0:
                break

            # There's lready a flower here, skip
            if flowerbed[i] == 1:
                continue
            
            # Check whether the left plot is clear or not
            leftIndex, leftValid = i - 1, False
            if leftIndex < 0 or (leftIndex >= 0 and flowerbed[leftIndex] == 0):
                leftValid = True

            # Check whether the right plot is clear or not
            rightIndex, rightValid= i + 1, False
            if rightIndex >= len(flowerbed) or (rightIndex < len(flowerbed) and flowerbed[rightIndex] == 0):
                rightValid = True
            
            # If left and right are valid, we can place a flower
            if leftValid and rightValid:
                flowerbed[i] = 1
                leftToPlace -= 1

        return True if leftToPlace == 0 else False