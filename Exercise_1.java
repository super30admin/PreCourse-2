/*

Time Complexity: O(logN)
Space Complexity: O(1)

No problem faced
ALGORITHM:
    since the array si already sorted, then at each step
        determine the center(midIndex) of the array under consideration
        if the element at midIndex is equal to the targetValue then return that index
        else if element at midIndex is greater than the targetValue then if it exists, it will lie in the left side of the midIndex
        else if the element exists it will lie in the right side of the midIndex
 */
class BinarySearch {

    public final int NOT_FOUND = -1;

    // Returns index of targetValue if it is present in input[l.. r], else return -1
    int binarySearch(int input[], int left, int right, int targetValue)
    {
        //Write your code here

        /**
         *
         */

        if (left > right) {
            return this.NOT_FOUND;
        }

        int midIndex = (left + right)/2;
        int midValue = input[midIndex];

        if (midValue == targetValue) {
            return midIndex;
        }
        else if(midValue > targetValue) {
            // element if exist will lie towards the left side of the midIndex value
            return binarySearch(input, left, midIndex -1, targetValue);
        } else {
            // element if exist will lie towards the right side of the midIndex value
            return binarySearch(input, midIndex + 1, right, targetValue);
        }
    }

    // Driver method to test above
    public static void main(String args[])
    {
        BinarySearch ob = new BinarySearch();
        int arr[] = { 2, 3, 4, 10, 40 };
        int n = arr.length;
        int x = 10;
        int result = ob.binarySearch(arr, 0, n - 1, x);
        if (result == -1)
            System.out.println("Element not present");
        else
            System.out.println("Element found at index " + result);
    }
}
