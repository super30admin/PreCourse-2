/*
Time Complexity :
    Best case: O(1) if the element is found to be the middle element.
    Worst Case: O(log n) When the element is not present in the array, but we keep
                on diving the array in half till it becomes empty.

Space Complexity :
     O(1) => We are using constant variables like left, right and midElement, without
             using any data structures, so the space will be constant.
             ** This is only applicable since we are using Iterative Approach **

     ** If in case, we were using Recursive approach for Binary Search **
        Space Complexity would have been O(log n) because every time we make a recursive call,
        a new stack frame is created, so max depth or number of calls will determine the max
        space used, here the max number of calls in recursive will be {log n} so space complexity
        will be O(log n)
 */

class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1 
    int binarySearch(int arr[], int l, int r, int x) 
    { 
        /*
           Binary Search can only be implemented on Sorted Arrays, by dividing the array in half and searching on left or
           right side of the array based on the middle element.
           Here, we are going to do it using the Iterative approach
        */

        while (l <= r)
        {
            /*
             We can calculate the middle element in two ways:
             1. (l + r) / 2 => this can work if the elements are small and their addition not exceed the int max size otherwise it can
                lead to Overflow

             2. So here we will use the other approach l + (r - l) / 2 where it can handle the overflow issue
             */
            int midIndex = l + (r - l) / 2;

            //If we found the element, we will return the index
            if (arr[midIndex] == x) {
                return midIndex;
            }

            //If the element to be found is less than the middle element, change the right index to point to (middle index - 1)
            else if (x < arr[midIndex]) {
                r = midIndex - 1;
            }

            //If the element to be found is more than the middle element, change the left index to point to (middle index + 1)
            else {
                l = midIndex + 1;
            }
        }

        return -1; //Element not found
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
