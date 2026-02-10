"""

328. Odd Even Linked List

    Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

    The first node is considered odd, and the second node is even, and so on.

    Note that the relative order inside both the even and odd groups should remain as it was in the input.

    You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Example 1:

    Input: head = [1,2,3,4,5]
    Output: [1,3,5,2,4]

Example 2:

    Input: head = [2,1,3,5,6,4,7]
    Output: [2,3,6,7,1,5,4]

Constraints:

    - The number of nodes in the linked list is in the range [0, 10^4].
    - -10^6 <= Node.val <= 10^6

"""


# Time complexity: O(N)
# Space complexity: O(1)
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If only one item, or empty LL return
        if not head or not head.next:
            return head

        # Remember the first even node for assignment after we've traversed the entire LL
        even_head = head.next

        # Initialize 2nd to last, last and current position pointers, track our depth as well
        second_to_last_ptr, last_ptr, curr_ptr, position = None, None, head, 1

        # Loop through the LL
        while curr_ptr:
            # Second to last node always gets linked to the current node
            if second_to_last_ptr:
                second_to_last_ptr.next = curr_ptr

            # Clear the next pointer from the last node in case this is the last node
            if last_ptr:
                last_ptr.next = None

            # Update pointers and depth position
            second_to_last_ptr = last_ptr
            last_ptr = curr_ptr
            curr_ptr = curr_ptr.next
            position += 1

        # Link the odd and even lists (odd tail -> even head)
        if position % 2 == 0:
            # Last position was even, so our odd tail is in last_ptr
            last_ptr.next = even_head
        else:
            # Last position was odd, so our odd tail is in second_to_last_ptr
            second_to_last_ptr.next = even_head

        return head
