from typing import List
## Testing data

textNum1=[2,7,11,15]
textNum2=[3,2,4]
textNum3=[3,3]

target1=9
target2=6
target3=6

## Function to solve the problems
def twoSum(nums:List[int],target:int)->List[int]:
  #Making a dictionary to store data, so we just need to loop over the array 1 times
  values={}
  #Similar to for each function
  for i,value in enumerate(nums):
    #if there is a value in nums Array that similar to some value, return that, or storing that if need 
    if target-value in values:
      return [values[target-value],i]
    else:
      #Storing the value and the index in the dictionary
      values[value]=i

#Driver Code
print(twoSum(textNum1,target1))
print(twoSum(textNum2,target2))
print(twoSum(textNum3,target3))