def isPalindrome(string):
    # Write your code here.
	reversedString = ""
	for i in reversed(range(len(string))):
		reversedString += string[i]
	return string == reversedString

