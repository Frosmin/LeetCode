# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
   
    def addTwoNumbers(self, l1, l2):
        
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
            
        def list_to_listnode(l):
            dummy_root = Solution(0)
            ptr = dummy_root
            for i in l:
                ptr.next = Solution(i)
                ptr = ptr.next

            ptr = dummy_root.next
            return ptr
        
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = self.listTONumber(l1)
        num2 = self.listTONumber(l2)
        suma = num1 + num2
        return self.numberToList(suma)
        
        
        
    def listTONumber(self, l,n=0):
       if l is None:
           return 0
       else:
            return l.val + 10 * self.listTONumber(l.next)
    
    def numberToList(self, n):
        if n == 0:
            return []
        else:
            return [n%10] + self.numberToList(n//10)
          
          

solucion = Solution()
print(solucion.addTwoNumbers([2,4,3], [5,6,4]))
print(solucion.addTwoNumbers([0], [0]))
print(solucion.addTwoNumbers([9,9,9,9,9,9,9], [9,9,9,9]))