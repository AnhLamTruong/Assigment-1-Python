from typing import List


## Testing data
textNum1=[5,7,7,8,8,10]
textNum2=[5,7,7,8,8,10]
textNum3=[]

target1=8
target2=6
target3=0

## Function to solve the problems
def binSearch(array:List[int],target:int,length:int,leftBias: bool)->int:
  low = 0
  high = length - 1
  rec=-1
  while (low <= high):
    #Binary Search
    mid=(low+high)//2
    #If the target is in the left size ([4]...19)
    if(array[mid]>target):
      # Move the high to mid
      high=mid-1
      #If the target is in the left size (19....[23])
    elif(array[mid]<target):
      # Move the low to mid
      low=mid+1
    else:
      #Updating the reccent, and move left because we want to find 1st occur
      rec=mid
      if leftBias:
        high=mid-1
      else:
        low=mid+1
  return rec

def searchRange(nums:List[int], target:int)->List[int]:
  left=binSearch(nums,target,len(nums),True)
  right=binSearch(nums,target,len(nums),False)
  return [left,right]
  
##Driver Code

print(searchRange(textNum1,target1))
print(searchRange(textNum2,target2))
print(searchRange(textNum3,target3))
print('Result')