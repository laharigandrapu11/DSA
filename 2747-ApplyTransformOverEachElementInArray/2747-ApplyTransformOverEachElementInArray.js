// Last updated: 7/15/2025, 4:46:40 PM
/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    let arrayNew = []
    for(let i=0;i<arr.length;i++){
        arrayNew[i] = fn(arr[i], i)
    }
    return arrayNew
};