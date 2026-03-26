// Exercise
// 1. 

const arr_a = ["a", "b", "c", "d", "e", "f"];
const arr_b = ["b", "d", "f"];
const arr_c = ["b", "d", "f", "h"];

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
            intersectionArr.push(value)
        }
    }

    return intersectionArr;
}

console.log(` Intersections:`)
console.log(intersection(arr_a, arr_b));
console.log(intersection(arr_a, arr_c));
console.log(intersection([1, 2, 3, 4, 5], [0, 2, 4, 6, 8]));
