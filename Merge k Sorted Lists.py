from ast import Delete
from heapq import merge
from queue import PriorityQueue
from typing import Optional
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.values = val
        self.next = next

class Solution:
    
    # def Enquiry(self,lis1):
    #     if len(lis1) == 0:
    #         return 0
    #     else:
    #         return 1
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # minHeap=[]
        # #Loop through array of list 
        # for List in lists:
        #     #Loop through Node in Array
        #     while List != None:
        #         minHeap.append(List.val);
        #         head=head.next
        # givenLists=ListNode(-1)
        # head= givenLists
        # while self.Enquiry(minHeap):
        #     head.next=ListNode(minHeap.remove)
        #     head=head.next
        # return givenLists.next
        if lists==None or len(lists)==0:
            return None
        return self.mergeKList(lists,0,len(lists)-1)
    
    def __mergeKList(self,lists: List[Optional[ListNode]],start:int,end:int)-> Optional[ListNode]:
        if (start==end):return lists[start]
        mid=start+(end-start)/2
        leftList=self.mergeKList(lists,start,mid)
        rightList=self.mergeKList(lists,mid+1,end)
        return merge(leftList,rightList)
    def __merge(self,l1:ListNode,l2:ListNode)->Optional[ListNode]:
        result=ListNode(-1)
        curr=result;
        while l1!=None or l2 !=None:
            if l1==None:
                curr.next=l2
                l2=l2.next
            elif l2==None:
                curr.next=l1
                l1=l1.next
            elif l1.values<l2.values:
                curr.next=l1
                l1=l1.next
            else:
                curr.next=l2
                l2=l2.next
            curr=curr.next
        return result.next