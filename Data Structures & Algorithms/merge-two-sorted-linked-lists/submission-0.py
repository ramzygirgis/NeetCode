# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import copy
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        print(f'list 1 val: {list1.val}')
        print(f'list 2 val: {list2.val}')
        if list1.val <= list2.val:
            new_head = copy.deepcopy(list1)
            print("list 1 val bigger")
            new_head.next = self.mergeTwoLists(list1.next, list2)
            return new_head
        else:
            new_head = ListNode(list2.val, list2.next)
            print("list 2 val bigger")
            new_head.next = self.mergeTwoLists(list1, list2.next)
            return new_head