# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        l1 = [2,4,3]
        l2 = [5,6,4]

        first_number = ""
        second_number = ""
        l1.reverse()
        l2.reverse()

        counter = 0
        for x in l1:
            first_number += str(x)
        for x in l2:
            second_number += str(x)

        result = int(first_number)+int(second_number)
        l3 = []

        for x in str(result):
            if head is None:
                head = ListNode(x)
                current = head
            else:
                new_node = ListNode(x)
                current.next = new_node
                current = new_node