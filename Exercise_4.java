class MergeSort 
{ 
    // Time Complexity :
    // Space Complexity :
    // Did this code successfully run on Leetcode :
    // Any problem you faced while coding this :
    
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int left, int middle, int right) 
    {  
        //Your code here 
        int n1  = middle - left + 1; 
        int n2 = right - middle;
        int[] leftArray = new int[n1];
        int[] rightArray = new int[n2];

        //copying the data into two arrays 
        for(int i=0 ; i < n1;i++){
            leftArray[i] = arr[left+i];
        }for(int i=0 ; i < n2 ;i++){
            rightArray[i] = arr[middle+1+i];
        }
        //Merge two arrays 
        int leftIndex = 0;
        int rightIndex = 0;
        while(leftIndex < n1 && rightIndex < n2){
            if(leftArray[leftIndex] <= rightArray[rightIndex]){
                arr[left]= leftArray[leftIndex];
                leftIndex++;
            } else {
                arr[left] = rightArray[rightIndex];
                rightIndex++;
            } 
            left++;
        }
        while(leftIndex < n1){
            arr[left] = leftArray[leftIndex];
            leftIndex++;
            left++;    
        }
        while(rightIndex < n2){
            arr[left] = rightArray[rightIndex];
            rightIndex++;
            left++;
        } 
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int left, int right) 
    { 
	//Write your code here
        //Call mergeSort from here 
        if(left < right ) {
            int middle = left+(right-left)/2; 
            /* thinking of this as a the Binary search
                the goal is to divide and go all the way up untill the child
            */ 
            sort(arr, left, middle);
            sort(arr, middle+1, right);
            // now once the left & right sub arrays can be merged 
            merge(arr,left, middle, right);
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
    public static void main(String args[]) 
    { 
        int arr[] = {12, 11, 13, 5, 6, 7}; 
  
        System.out.println("Given Array"); 
        printArray(arr); 
  
        MergeSort ob = new MergeSort(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 