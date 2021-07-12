const strings = ['a','b','c','d'];

strings[2]

// Accessing in Array(Time Complexity O(1))

strings.push('e')
console.log(strings)
strings.pop()




// Inserting or Deleting in Array( Time Complexity O(n))

strings.unshift('x')

strings.splice(2,0,'alien')

console.log(strings)