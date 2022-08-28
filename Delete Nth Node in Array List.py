from ast import Delete
from asyncio.windows_events import NULL
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=NULL):
        self.values = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
      if (head==NULL):
        return NULL
      firstPointer=head
      secondPointer=head
      for i in range(n):
        firstPointer=firstPointer.next
      if(firstPointer==NULL):
        return head.next
      while(firstPointer.next):
        firstPointer=firstPointer.next
        secondPointer=secondPointer.next
      temp=ListNode()
      temp=secondPointer.next
      secondPointer.next=temp.next
      del temp
      return head
    
      
    