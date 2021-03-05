// Time complexity O(n)log(n) and Space complexity o(n) //

def sortedSquaredArray(array):
    # Write your code here.
	new_array = []
	for x in array:
		new_array.append(x*x)
	new_array.sort()
    return new_array

  
// Time complexity O(n) and Space complexity O(n)  //

def sortedSquaredArray(array):
    sortedSqaures = [0 for _ in array]
	smallerValueIdx = 0
	largerValueIndex = len(array) - 1
	
	for idx in reversed(range(len(array))):
		smallerValue = array[smallerValueIdx]
		largerValue = array[largerValueIndex]
		
		if abs(smallerValue) > abs(largerValue):
			sortedSqaures[idx] = smallerValue * smallerValue
			smallerValueIdx += 1
		else:
			sortedSqaures[idx] = largerValue * largerValue
			largerValueIndex -= 1
		
    return sortedSqaures
