class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        temp_l = []

        while list1:
            temp_l.append(list1.val)
            list1 = list1.next
        while list2:
            temp_l.append(list2.val)
            list2 = list2.next

        temp_l.sort()

        dummy = ListNode()
        cur = dummy
        for v in temp_l:
            cur.next = ListNode(v)
            cur = cur.next
            
        return dummy.next
