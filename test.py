def twoSum(nums: list[int], target: int) -> list[int]:
    indeces = {nums[0] : 0}

    for index, i  in enumerate(nums):
        if (index == 0):
            continue
        if indeces.get(target - i, None) != None:
            return [indeces.get(target - i), index]
        indeces[i] = index
        
        

r = twoSum([2,7,11,15], 9)
print(r)