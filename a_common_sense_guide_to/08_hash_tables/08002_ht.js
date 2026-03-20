const arr_a = ["a", "b", "c", "d", "e", "f"];
const arr_b = ["b", "d", "f"];
const arr_c = ["b", "d", "f", "h"];

function isSubset(array1, array2) {
    let largerArray;
    let smallerArray;

    if(array1.length > array2.length) {
        largerArray = array1;
        smallerArray = array2;
    } else {
        largerArray = array2;
        smallerArray = array1;
    }

    
    for(let i = 0; i < smallerArray.length; i++) {
        
        let foundMatch = false;

        for(let j = 0; j < largerArray.length; j++) {
            if(smallerArray[i] === largerArray[j]) {
                foundMatch = true;
                break;
            }
            
        }
        
        if(foundMatch === false) {
            return false;
        }
    }

    return true;
}



function isSubsetHash(array1, array2) {
    const hashTable = {}
    let largerArray;
    let smallerArray;

    if(array1.length > array2.length) {
        largerArray = array1;
        smallerArray = array2;
    } else {
        largerArray = array2;
        smallerArray = array1;
    }

    
    for(const value of largerArray) {
        hashTable[value] = true;        
    }

    for(const value of smallerArray) {
        if(!hashTable[value]) {
            return false;
        }
    }

    return true;
}

console.log(isSubset(arr_a, arr_b));
console.log(isSubset(arr_a, arr_c));

console.log(isSubsetHash(arr_a, arr_b));
console.log(isSubsetHash(arr_a, arr_c));



// 1. 

function intersection(array1, array2) {
    const hashTable = {};
    const intersectionArr = [];
    let largerArray;
    let smallerArray;

    if(array1.length > array2.length) {
        largerArray = array1;
        smallerArray = array2;
    } else {
        largerArray = array2;
        smallerArray = array1
    }

    for(const value of largerArray) {
        hashTable[value] = true;
    }

    for(const value of smallerArray) {
        if(hashTable[value]) {
            console.log(`the log: ${value}`)
            intersectionArr.push(value)
        }
    }

    return intersectionArr;
}

console.log(` Intersections:`)
console.log(intersection(arr_a, arr_b));
console.log(intersection(arr_a, arr_c));
console.log(intersection([1, 2, 3, 4, 5], [0, 2, 4, 6, 8]));
