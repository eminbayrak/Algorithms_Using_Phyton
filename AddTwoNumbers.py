#You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order and each of their nodes contain a single digit. 
# Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = ''
        head = l1
        while head:
            num1 += str(head.val)
            head = head.next
        num2 = ''
        head = l2
        while head:
            num2 += str(head.val)
            head = head.next
        result = str(int(num1[::-1])+int(num2[::-1]))[::-1]
        head = temp = ListNode(int(result[0]))
        for digit in result[1:]:
            temp.next = ListNode(int(digit))
            temp = temp.next
        return head