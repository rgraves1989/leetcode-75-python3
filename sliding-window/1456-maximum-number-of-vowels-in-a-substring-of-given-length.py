"""

1456. Maximum Number of Vowels in a Substring of Given Length

    Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

    Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:

    Input: s = "abciiidef", k = 3
    Output: 3
    Explanation: The substring "iii" contains 3 vowel letters.

Example 2:

    Input: s = "aeiou", k = 2
    Output: 2
    Explanation: Any substring of length 2 contains 2 vowels.

Example 3:

    Input: s = "leetcode", k = 3
    Output: 2
    Explanation: "lee", "eet" and "ode" contain 2 vowels.

Constraints:

    - 1 <= s.length <= 10^5
    - s consists of lowercase English letters.
    - 1 <= k <= s.length

"""


# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Intialize our sliding window pointers and max_num_vowels
        left_ptr, right_ptr, max_num_vowels = 0, k - 1, 0
        str_len, vowels = len(s), set("aeiou")

        # Determine the number of vowels in the first subarray
        curr_sub_str = s[left_ptr : right_ptr + 1]
        curr_num_vowels = sum(1 for char in curr_sub_str if char in vowels)
        max_num_vowels = curr_num_vowels

        # Loop through the string, updating our sliding window
        while right_ptr < str_len:
            # If the first char is a vowel, we're losing a vowel from the count
            if s[left_ptr] in vowels:
                curr_num_vowels -= 1

            # If the new char is a vowel, we're gainging a vowel to the count
            if right_ptr + 1 < str_len and s[right_ptr + 1] in vowels:
                curr_num_vowels += 1

            # Keep track of the maximum number of vowels encountered
            max_num_vowels = max(max_num_vowels, curr_num_vowels)

            # Slide the window
            left_ptr += 1
            right_ptr += 1

        # Return the maximum number of vowels found
        return max_num_vowels
