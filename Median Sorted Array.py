from typing import List
import math

# Function to find Median Sorted Array
# This function will use binary search to get time complecity O(log)(m+n))
def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
  #We will try to make first array length smaller than second one
  if(len(nums1))>(len(nums2)):
    return findMedianSortedArrays(nums2,nums1)
  x=len(nums1)
  y=len(nums2)
  
  start,end=0,x;
  while(start<=end):
    positionX=(end+start)/2
    positionY=(x+y+1)/2 - positionX
    
    #if positionX is 0 it means there is nothing on the left side. We can use -INFINITE for maxLeftX
    #if positionX == length of the num1 input it means there is nothing on the right side. We can use +INFINITE for minRightX
    maxLeftX=-math.inf if positionX==0 else nums1[int(positionX-1)]
    minRightX=math.inf if positionX==x else nums1[int(positionX)]
    
    maxLeftY=-math.inf if positionY==0 else nums2[int(positionY-1)]
    minRightY=math.inf if positionY==y else nums2[int(positionY)]
    
    if(maxLeftX<=minRightY & maxLeftY<=minRightX):
      #We have the position int the right way
      #If the combine length of array is even, we do median of MAX(left elements) and MIN(Right elements)
      if((x+y)%2==0):
        return format((max(maxLeftX,maxLeftY)+min(minRightX,minRightY))/2)
      #Max on left for odd length of array
      else:
        return format((max(maxLeftX,maxLeftY)))
    elif(maxLeftX>minRightY):
      #If maxLeftX>minrightY, it means that X position is far from the right=> move left
      end=positionX-1
    else:
      #Else X position is far from the left =? move right 
      start=positionX+1
    
    
test1 = [1,3]
test2 = [2] 
test3 = [1,2] 
test4 = [3,4]

print(findMedianSortedArrays(test1,test2))
print(findMedianSortedArrays(test3,test4))
