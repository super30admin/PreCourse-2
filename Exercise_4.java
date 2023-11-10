// Time Complexity : O(n log n)
// Space Complexity :O(n)
// Did this code successfully run on Leetcode : yes
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    private static int[] merge(int left[], int right[]) 
    {  
       //Your code here
       int result[] = new int[left.length + right.length];
       int leftPtr, rightPtr, resultPtr;
       leftPtr = rightPtr = resultPtr = 0;
       while(leftPtr < left.length || rightPtr < right.length){
           if(leftPtr < left.length && rightPtr < right.length){
               if(left[leftPtr] <= right[rightPtr]){
                   result[resultPtr++] = left[leftPtr++];
               }
               else{
                result[resultPtr++] = right[rightPtr++];
               }
           }
           else if(leftPtr < left.length){
            result[resultPtr++] = left[leftPtr++];
           }
           else if(rightPtr < right.length){
            result[resultPtr++] = right[rightPtr++];
        }
    }
    return result;
} 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    private static int[] sort(int arr[]) 
    { 
        //Write your code here
        if(arr.length <= 1){
            return arr;
        }

        int midpoint = arr.length/2;
        int left[] = new int[midpoint];
        int right[];
        
        if(arr.length % 2 == 0){
            right = new int[midpoint];
        }
        else{
            right = new int[midpoint + 1];
        }

        for(int i = 0; i < midpoint; i++){
            left[i] = arr[i];
        }
        for(int j = 0; j < right.length; j++){
            right[j] = arr[midpoint + j];
        }
        //Call mergeSort from here
        int result[] = new int[arr.length];
        left = sort(left);
        right = sort(right);
        result = merge(left, right);
        return result;    
    } 
  
    /* A utility function to print array of size n */
    static void printArray(int arr[]) 
    { 
        int n = arr.length; 
        for (int i=0; i<n; i++) 
            System.out.print(arr[i] + " "); 
        System.out.println(); 
    } 
  
    // Driver method 
    public static void main(String args[]) 
    { 
        int arr[] = {12, 11, 13, 5, 6, 7}; 
  
        System.out.println("Given Array"); 
        printArray(arr); 
  
        
        //ob.sort(arr, 0, arr.length-1);
        arr = sort(arr);
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 