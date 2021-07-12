function niceChallange(input){
    let a =5; // O(1)
    let b=10; // O(1)
    let c=50; // O(1)

    for(let i=0;i< input;i++){
        let x = i+1; // O(n)
        let y = i+2; // O(n)
        let z = i+3; // O(n)

    }
    for (let j=0; j<input;j++){
        let p= j*2; // O(n)
        let q = j*2; // O(n)
    }
    let whoAmI = "I dont know"; // O(1)
}

// Solution : O(4+5n) --> O(n)

niceChallange(20);


const boxes = [1,2,3,4,5]
let sum = 0
for(let i=0;i<boxes.length;i++){
    for(let j=0;j<boxes.length;j++){
        sum = sum+ (boxes[i]+boxes[j]);
    }
}
console.log(sum)
