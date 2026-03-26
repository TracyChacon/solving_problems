
// Exercise
// 3. 


/********************************************************************************** 
A pangram is
a sentence or phrase that contains all 26 letters of the English alphabet at least once. Often used for testing fonts, keyboards, and handwriting, these phrases can be short or long, with the most concise version known as a "perfect" pangram (using each letter only once). 
************************************************************************************/


function findMissingLetter(str) {
    const alphabet = "abcdefghijklmnopqrstuvwxyz ";
    const charInAlphabet = {}

    for(let char of str) {
        charInAlphabet[char] = true;
    }

    for(let char of alphabet) {
        if(!charInAlphabet[char]) {
            return char;
        }
    }
}

const inputStr = "the quick brown box jumps over teh lazy dog"

console.log(findMissingLetter(inputStr));

