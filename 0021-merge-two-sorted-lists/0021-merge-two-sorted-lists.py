class Solution(object):
    def mergeTwoLists(self, list1, list2):

        arr = []

        while list1:
            arr.append(list1.val)
            list1 = list1.next

        while list2:
            arr.append(list2.val)
            list2 = list2.next

        arr.sort()

        dummy = ListNode(0)
        temp = dummy

        for x in arr:
            temp.next = ListNode(x)
            temp = temp.next

        return dummy.next