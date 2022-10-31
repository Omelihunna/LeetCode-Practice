/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {
    let counter = 0;
    a = n
    n = []
    
    for(let x = 1; x <= a; x++) {
        if(x%3 == 0 && x%5 == 0) {
            n[counter] = 'FizzBuzz'
        }
        else if(x%3 == 0) {
            n[counter] = 'Fizz'
        }
        else if(x%5 == 0) {
            n[counter] = 'Buzz'
        }
        else {
            n[counter] = x.toString()
        }
        ++counter
    }
    return n
    
};