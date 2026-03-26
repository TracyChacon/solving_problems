// Exercise
// 4. 

function findNonDuplicateChar(str) {
    const frequency_counter = {};
    str = str.toLowerCase();
    
    for(let char of str) {
        frequency_counter[char] = (frequency_counter[char] || 0) + 1;
    }

    for(let char of str) {
        if(frequency_counter[char] === 1) {
            return char;
        }
    }

    return null;
}

const str = "minimum";
console.log(findNonDuplicateChar(str));