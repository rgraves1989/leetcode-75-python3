"""

1071. Greatest Common Divisor of Strings

    For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

    Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:

    Input: str1 = "ABCABC", str2 = "ABC"
    Output: "ABC"

Example 2:

    Input: str1 = "ABABAB", str2 = "ABAB"
    Output: "AB"

Example 3:

    Input: str1 = "LEET", str2 = "CODE"
    Output: ""

Example 4:

    Input: str1 = "AAAAAB", str2 = "AAA"
    Output: ""​​​​​​​

Constraints:

    - 1 <= str1.length, str2.length <= 1000
    - str1 and str2 consist of English uppercase letters.

"""

# Time complexity: O(N)
# Space complexity: O(N)
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        max_prefix, read_ptr_str1, read_ptr_str2 = [], 0, 0
        size_str1, size_str2 = len(str1), len(str2)

        # Loop until we've reached the end of either string
        while read_ptr_str1 < size_str1 and read_ptr_str2 < size_str2:
            # Get the current character in each string
            curr_char_str1, curr_char_str2 = str1[read_ptr_str1], str2[read_ptr_str2]

            # If chars don't match there is no GCD
            if not curr_char_str1 == curr_char_str2:
                return ""

            # Otherwise, append the matching char to the max_prefix
            max_prefix.append(curr_char_str1)

            # Advance our pointers
            read_ptr_str1 += 1
            read_ptr_str2 += 1

        # Verify our max_prefix repeats, if we didn't reach the end of both strings
        print(max_prefix)
        read_ptr_max_prefix = 0
        size_max_prefix = len(max_prefix)
        while read_ptr_str1 < size_str1 or read_ptr_str2 < size_str2:
            curr_char = None

            # Get the current char from the string we haven't finished looping through
            if read_ptr_str1 < size_str1:
                print("read str1")
                curr_char = str1[read_ptr_str1]
                read_ptr_str1 += 1
            elif read_ptr_str2 < size_str2:
                print("read str2")
                curr_char = str2[read_ptr_str2]
                read_ptr_str2 += 1

            # Current character doesn't match the max_prefix sequence
            if not curr_char == max_prefix[read_ptr_max_prefix]:
                return ""

            # Reset, or advance the read pointer for max_prefix
            if read_ptr_max_prefix == size_max_prefix - 1:
                read_ptr_max_prefix = 0
            else:
                read_ptr_max_prefix += 1

        # Lastly, find the max length for which max_prefix is GCD of both strings
        max_prefix_end_ptr, max_prefix_len = 1, 1
        while max_prefix_end_ptr <= size_max_prefix:
            if size_str1 % max_prefix_end_ptr == 0 and size_str2 % max_prefix_end_ptr == 0:
                max_prefix_len = max_prefix_end_ptr
            max_prefix_end_ptr += 1

        print(max_prefix_end_ptr)

        return "".join(max_prefix[:max_prefix_len])