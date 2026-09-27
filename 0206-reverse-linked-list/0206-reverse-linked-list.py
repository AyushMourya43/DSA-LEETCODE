class Solution(object):
    def reverseList(self, head):

        # stack = []

        # temp = head

        # # values stack mein store
        # while temp is not None:
        #     stack.append(temp.val)
        #     temp = temp.next

        # # head se dobara traverse
        # temp = head

        # # stack se reverse values daalo
        # while temp is not None:
        #     e = stack.pop()
        #     temp.val = e
        #     temp = temp.next

        # return head

        prev = None
        current = head

        while current is not None:
            next_node = current.next
            current.next = prev

            prev = current
            current = next_node

        return prev    