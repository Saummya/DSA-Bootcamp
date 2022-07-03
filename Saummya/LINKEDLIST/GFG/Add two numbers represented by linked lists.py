'''
Given two numbers represented by two linked lists of size N and M. The task is to return a sum list.

The sum list is a linked list representation of the addition of two input numbers from the last.

Example 1:

Input:
N = 2
valueN[] = {4,5}
M = 3
valueM[] = {3,4,5}
Output: 3 9 0  
Explanation: For the given two linked
list (4 5) and (3 4 5), after adding
the two linked list resultant linked
list will be (3 9 0).
Example 2:

Input:
N = 2
valueN[] = {6,3}
M = 1
valueM[] = {7}
Output: 7 0
Explanation: For the given two linked
list (6 3) and (7), after adding the
two linked list resultant linked list
will be (7 0).
Your Task:
The task is to complete the function addTwoLists() which has node reference of both the linked lists and returns the head of the sum list.   

Expected Time Complexity: O(N+M)
Expected Auxiliary Space: O(Max(N,M)) for the resultant list.

Constraints:
1 <= N, M <= 5000
'''


class Solution:
    #Function to add two numbers represented by linked list.
    def reverse(self, head):
            prev = None
            temp = head
            while temp:
                nxt = temp.next
                temp.next = prev
                prev = temp
                temp = nxt
            head = prev
            
            return head
    
    
    
    def addTwoLists(self, first, second):
        # code here
        # return head of sum list
        sum1=0
        carry=0
        dummy=Node(-1)
        temp=dummy
        first = self.reverse(first)
        second = self.reverse(second)
        
        while(first is not None or second is not None or carry !=0):
            s = 0
            if first is not None:
                s += first.data
                first = first.next
            if second is not None:
                s += second.data
                second = second.next
                
            s += carry
            carry = s//10
            
            temp.next = Node(s%10)
            temp = temp.next
