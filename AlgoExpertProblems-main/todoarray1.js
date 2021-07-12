// Push Front //

const array = [20,30,40]

for(let i=array.length;i>0;i--){
  array[i] = array[i-1]
}
array[0] = 10

console.log(array)

// Pop Front //

function popArray(array){
  let x = array[0];
  for(let i=0;i<array.length;i++){
    array[i] = array[i+1];
  }
  array.length = array.length-1
  return x;
}
popArray(array)
console.log(array)

// Insert at first //

function insertArray(array, position, val){
  for(let i=array.length;i>position;i--){
    array[i] = array[i-1]
  }
  array[position] = val
}

insertArray(array,0,10)
insertArray(array,3,21)
console.log(array)


// Remove array //

function removeArray(array, position){
  for(let i=position;i<array.length;i++){
    array[i] = array[i+1]
  }
  array.length = array.length-1
}

removeArray(array,2)
console.log(array)


// Swap Array //

function swapArray(array){
  for(let i=0;i<array.length-1;i=i+2)
  {
    let temp = array[i]
    array[i] = array[i+1]
    array[i+1] = temp
  }

  return array
}

console.log(swapArray(array))
console.log(swapArray(["John","Mathew",true,false]))

// Remove Duplicate // 

function removeDuplicate(array){
  let newArr=[]
  array.sort()
  for(let i=0;i<array.length;i++){
    if(array[i] !== array[i+1]){
      newArr.push(array[i])
    }
  }
  return newArr
}

console.log(removeDuplicate([3,1,3,2,6,2]))