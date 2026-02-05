"""

392. Is Subsequence

	Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

	A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

	Input: s = "abc", t = "ahbgdc"
	Output: true

Example 2:

	Input: s = "axc", t = "ahbgdc"
	Output: false

Constraints:

	- 0 <= s.length <= 100
	- 0 <= t.length <= 10^4
	- s and t consist only of lowercase English letters.

"""

# Time complexity: O(min(N, M))
# Space complexity: O(1)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_ptr, s_len, t_ptr, t_len = 0, len(s), 0, len(t)

        # Loop until we reach the end of either s or t
        while s_ptr < s_len and t_ptr < t_len:
            # If we matched the current s string char with the current t string char, advance the s pointer
            if s[s_ptr] == t[t_ptr]:
                s_ptr += 1

            # Always advance the t string pointer
            t_ptr += 1

        # If we reached the end of the s string, then we have found a subsequence
        if s_ptr == s_len:
            return True

        return False