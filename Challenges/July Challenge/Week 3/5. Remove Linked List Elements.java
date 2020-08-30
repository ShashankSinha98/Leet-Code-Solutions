/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeElements(ListNode head, int key) {
        
        // empty list
        if(head==null){
            return head;
        }
        // single LL with key node
        if (head.next==null){
            if (head.val==key)
                return null;
            else
                return head;
        }
        
        ListNode prev = null;
        ListNode next = head;
        while(next!=null){
            if(next.val==key){
                if(prev==null){
                    head = head.next;
                    next=head;
                    continue;
                }
                else{
                    if(next.next!=null){
                    prev.next = next.next;
                    next = next.next;
                    continue;
                    } else {
                        prev.next = null;
                        next = null;
                        continue;
                    }
                }
            }
            prev = next;
            next = next.next;     
        }
        
        return head;
    }
}