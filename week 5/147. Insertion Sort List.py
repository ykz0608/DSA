class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        new_linked_list = ListNode(None)
        while head :
            insert_vale = head.val
            current_node = new_linked_list
            while ((current_node) and (current_node.val < insert_vale)):
                pre_node = current_node
                current_node = current_node.next
                
            pre_node.next = ListNode(insert_vale)
            pre_node.next.next = current_node
            head = head.next
        return new_linked_list.next 
