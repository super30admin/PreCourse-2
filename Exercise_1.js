"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.BinarySearch = void 0;
var BinarySearch = /** @class */ (function () {
    function BinarySearch() {
    }
    // Returns index of x if it is present in arr[l.. r], else return -1 
    BinarySearch.prototype.binarySearch = function (arr, l, r, x) {
        //Write your code here
        while (l <= r) {
            var mid = Math.floor((l + r) / 2);
            console.log(mid);
            if (arr[mid] == x)
                return mid;
            (x < arr[mid]) ? r = mid - 1 : l = mid + 1;
        }
        return -1;
    };
    return BinarySearch;
}());
exports.BinarySearch = BinarySearch;
// Driver method to test above 
var ob = new BinarySearch();
var arr = [2, 3, 4, 10, 40];
var n = arr.length;
var x = 10;
var result = ob.binarySearch(arr, 0, n - 1, x);
if (result == -1)
    console.log("Element not present");
else
    console.log("Element found at index " + result);
