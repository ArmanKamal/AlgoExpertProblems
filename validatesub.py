def isValidSubsequence(array, sequence):
    # Write your code here.
    array_pos = 0
	seq_pos = 0
	
	while array_pos < len(array) and seq_pos < len(sequence):
		if array[array_pos] == sequence[seq_pos]:
			seq_pos +=1
		array_pos +=1
	return seq_pos == len(sequence)
			
		 
def isValidSubsequence(array, sequence):
    seq_pos = 0
	for x in array:
		if seq_pos == len(sequence):
			break
		if x == sequence[seq_pos]:
			seq_pos+=1
	return seq_pos == len(sequence)

