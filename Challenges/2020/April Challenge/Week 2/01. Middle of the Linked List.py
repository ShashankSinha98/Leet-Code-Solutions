class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        
        a = head
        b = None
        
        if a.next != None:
            b = head.next
            
            while b.next!=None and b.next.next!=None:
                b = b.next.next
                a = a.next
                
        return a if b==None else a.next