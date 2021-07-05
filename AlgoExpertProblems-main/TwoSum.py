##  Solution 1 T= O(n^2), S= (O(1)) ##


def twoNumberSum(array, targetSum):
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array) - 1):
            if array[i] + array[j] == targetSum:
                return [array[i], array[j]]
    return []


print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))

## Solution 2 T= (O^n), S= (O(n)) ##


def twoNumberSum(array, targetSum):
    nums = {}

    for num in array:

        if targetSum - num in nums:
            return [targetSum - num, num]

        else:
            nums[num] = True
    return []


print(twoNumberSum([3, 5, -4, 8, 10, 1, -1, 5], 10))



## Solution 3 T = (O^nlogn), S= (O(1)) ## 

def twoNumberSum(array, targetSum):
  array.sort()
  left = 0
  right = len(array)-1

  while left<right:
    sum = array[left]+ array[right]
    if sum<targetSum:
      left+=1
    elif sum>targetSum:
      right-=1
    else:
      return [array[left],array[right]]
  
  return []


print(twoNumberSum([3, 5, -4, 8, 10, 1, -1, 5], 10))
