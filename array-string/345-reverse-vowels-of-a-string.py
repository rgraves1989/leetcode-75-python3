"""

345. Reverse Vowels of a String

    Given a string s, reverse only all the vowels in the string and return it.

    The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:

    Input: s = "IceCreAm"
    Output: "AceCreIm"
    Explanation: The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

    Input: s = "leetcode"
    Output: "leotcede"

Constraints:

    - 1 <= s.length <= 3 * 10^5
    - s consist of printable ASCII characters.

"""

# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def reverseVowels(self, s: str) -> str:
        # Initialize vowel set, left and right pointers, 
        vowels = set('aeiouAEUIO')
        left_ptr, right_ptr, reverse_vowels_str = 0, len(s) - 1, list(s)

        # Loop until the left pointer passes the right pointer
        while left_ptr < right_ptr:
            # Move the left pointer rightward until we find a vowel
            while left_ptr < right_ptr and reverse_vowels_str[left_ptr] not in vowels:
                left_ptr += 1

            # Move the right pointer leftward until we find a vowel
            while left_ptr < right_ptr and reverse_vowels_str[right_ptr] not in vowels:
                right_ptr -= 1

            # Swap the left and right vowels and advance our pointers
            reverse_vowels_str[left_ptr], reverse_vowels_str[right_ptr] = reverse_vowels_str[right_ptr], reverse_vowels_str[left_ptr]
            left_ptr += 1
            right_ptr -= 1

        # Recombine the reverse_vowels_str list into a string
        return "".join(reverse_vowels_str)