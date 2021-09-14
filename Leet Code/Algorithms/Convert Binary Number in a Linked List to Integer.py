# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        node = head
        num = ''
        while node:
            num += str(node.val)
            node = node.next
        return int(num, 2)
