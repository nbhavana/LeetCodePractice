"""
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

#Solution:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printLinkedList(head):
    current = head
    while current:
        print(current.val, end="")
        if current.next:
            print(" -> ", end="")
        current = current.next
    print()
    
def mergeTwoLists(l1, l2):
    # Initialize a dummy node for the merged list
    dummy = ListNode()
    # Pointer to the current node of the merged list
    current = dummy

    # Iterate through both lists
    while l1 and l2:
        # Compare the values of the current nodes of both lists
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        # Move the pointer of the merged list forward
        current = current.next

    # If one list is exhausted, append the rest of the other list
    if l1:
        current.next = l1
    else:
        current.next = l2

    # Return the head of the merged list (skipping the dummy node)
    print(dummy)
    return dummy.next

list1 = [1, 2, 4]
list2 = [1, 3, 4]

list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
merged_list = mergeTwoLists(list1,list2)
printLinkedList(merged_list)