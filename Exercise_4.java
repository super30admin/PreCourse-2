// Time Complexity :O(nlogn)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : N/A
// Any problem you faced while coding this :
class MergeSort
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[])
    { 
	//Write your code here
        //Call mergeSort from here
        int arrLength = arr.length;

        if(arrLength < 2){ // If the length of the array is less than 2 i.e. single or 0 element then return
            return;
        }

        int mid = arrLength/2; // calculating middle element to divide the array
        int[] leftArray = new int[mid]; // Creating left array
        int[] rightArray = new int[arrLength-mid]; // creating right array

        for(int i=0;i<mid;i++){ // filling elements in the left array
            leftArray[i] = arr[i];
        }
        for(int i=mid;i<arrLength;i++){ // filling elements in the right array
            rightArray[i-mid] = arr[i];
        }
        sort(leftArray); // repeating the sort in the left array
        sort(rightArray);// repeating the sort in the right array

        int leftPointer =0, rightPointer =0,mainPointer =0; // setting pointers for the left, right and main array to help in merge

        while(leftPointer < leftArray.length && rightPointer < rightArray.length){ // setting conditions
            if(leftArray[leftPointer] < rightArray[rightPointer]){ // comparing the left and the right array's first element
                arr[mainPointer] = leftArray[leftPointer];
                leftPointer++;
            } else{
                arr[mainPointer] = rightArray[rightPointer];
                rightPointer++;
            }
            mainPointer++;
        }
        while(leftPointer < leftArray.length){ // when either of the left or right array is completely filled, then filling the other array in the main array
            arr[mainPointer] = leftArray[leftPointer];
            leftPointer++;
            mainPointer++;
        }
        while(rightPointer < rightArray.length){
            arr[mainPointer] = rightArray[rightPointer];
            mainPointer++;
            rightPointer++;
        }
    }
  
    /* A utility function to print array of size n */
    static void printArray(int arr[]) 
    { 
        int n = arr.length; 
        for (int i=0; i<n; ++i) 
            System.out.print(arr[i] + " "); 
        System.out.println(); 
    } 
  
    // Driver method 
//    public static void main(String args[])
//    {
//        int arr4[] = {12, 11, 13, 5, 6, 7};
//
//        System.out.println("Exercise 4: Given Array");
//        printArray(arr4);
//
//        MergeSort ob = new MergeSort();
//        ob.sort(arr4, 0, arr4.length-1);
//
//        System.out.println("\nSorted array");
//        printArray(arr4);
//    }
} 