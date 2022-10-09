/**
 * @param {number} n
 * @return {number}
 */
var smallestEvenMultiple = function(n) {
   for (var i = 1;i < 10000000 ;i++) {
       if (i % 2 == 0 && i % n == 0) {
           return i
       }
   }
};