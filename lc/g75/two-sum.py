from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
    d = {}
    for i, n in enumerate(nums): # O(n)
        if target - n in d.keys(): # O(1)
            return [i, d[target - n]]
        d[n] = i # O(1)
    return []
