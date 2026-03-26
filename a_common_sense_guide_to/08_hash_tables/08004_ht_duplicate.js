// Exercise
// 2. 



const arr_a = ["a", "b", "c", "d", "c", "e", "f"];
const arr_b = ["b", "d", "f"];
const arr_c = ["b", "d", "f", "h"];

function duplicates(array1) {
    const frequency_counter = {}

    for(value of array1) {
        frequency_counter[value] = (frequency_counter[value] || 0) + 1;

        if (frequency_counter[value] > 1) {

            return value;

        }
    }

}


console.log(duplicates(arr_a))