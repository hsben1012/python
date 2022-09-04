"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    Example 1:
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.
    
    Example 2:
    Input: l1 = [0], l2 = [0]
    Output: [0]
    
    Example 3:
    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]
"""


class ListNode:
    def __init__(self, val=0, nextt=None):
        self.val = val
        self.next = nextt


def addTwoNumbers(x: ListNode, y: ListNode):
    carry = 0
    if x is None:
        return y
    if y is None:
        return x

    while x or y:
        if x:
            carry += x.val
            x = x.next
        if y:
            carry += y.val
            y = y.next
        curr.next = a(carry % 10)
        carry = 1 if carry >= 10 else 0
        return curr.next
    if carry != 0:
        curr.next = a(carry)
        return curr.next


a = [1, 2, 3]
b = [1, 2, 3]
addTwoNumbers(a, b)
