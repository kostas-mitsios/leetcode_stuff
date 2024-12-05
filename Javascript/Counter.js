/**
 * @param {number} n
 * @return {Function} counter
 */

var createCounter = function(n) {
    let totalCounter = n;
    return function() {
        return totalCounter++;
    };
};