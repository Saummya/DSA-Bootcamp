'''
Given two string, represented as linked lists (every character is a node->data in the linked list). Write a function compare() that works similar to strcmp(), i.e., it returns 0 if both strings are same, 1 if first linked list is lexicographically greater, and -1 if second is lexicographically greater.

Input:
First line of input contains number of testcases T. For each testcase, there will be 4 lines of input. First line of which contains length of first linked list and next line contains the linked list, similarly next two lines contains length and linked list respectively.

Output:
Comapare two strings represented as linked list.

User Task:
The task is to complete the function compare() which compares the strings through linked list and returns 0, 1 or -1 accordingly.

Constraints:
1 <= T <= 100
1 <= N, M <= 100

Example:
Input:
2
5
a b a b a
4
a b a a
3
a a b
3
a a b

Output:
1
0

Explanation:
Testcase 1: String consisting of nodes of first linked list is lexicographically greater than the second one. So, the result is 1.
'''


'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
def compare(head1, head2):
    #return 1/-1/0
    n1=head1
    n2=head2
    
    while n1 and n2:
        if n1.data!=n2.data:
            if n1.data>n2.data:
                return 1
            else:
                return -1
        else:
            n1=n1.next
            n2=n2.next
            
    if n1:
            return 1
    if n2:
            return -1
            
    return 0
