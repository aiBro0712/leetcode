from typing import List


def two_sum(nums:List[int],target:int) -> List[int]:
    n = len(nums)
    for i in range(n-1):
        for j in range(i+1,n):
            if nums[i]+nums[j] == target:
                return [i,j]
    return []
print(two_sum([3,2,4],6))
print(two_sum([3,3],6))
  
