class MergeSort 
{
    //Time Complexity is o(NlogN)

    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
       if (arr[m-1] <= arr[m]){
           return;
       }
       int i = l;
       int j = m;
       int tempIndex = 0;
       int[] tempArray = new int[r-l];
        while (i < m && j < r){
            tempArray[tempIndex++] = arr[i] <= arr[j] ? arr[i++] : arr[j++];
        }
       System.arraycopy(arr, i, arr, l+tempIndex, m-i);
       System.arraycopy(tempArray, 0, arr, l, tempIndex);
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here
        if ((r-l) < 2){
            return;
        }
        int midpoint = (l+r) / 2;
        sort(arr, l, midpoint);
        sort(arr, midpoint, r);
        merge(arr, l, midpoint, r);
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
        ob.sort(arr, 0, arr.length);
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 