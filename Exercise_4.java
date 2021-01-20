class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
       int ll = m - l + 1;
       int rs = r - m;
       int[] LeftTmpArray = new int[ll];
       int[] rightTmpArray = new int[rs];
       int i, j;
       for (i = 0; i < ll; i++) {
           LeftTmpArray[i] = arr[l + i];
       }
       for (i = 0; i < rs; i++) {
           rightTmpArray[i] = arr[m + 1 + i];
       }
       i = 0;
       j = 0;
       int k = l;
       while (i < ll && j < rs) {
           if (LeftTmpArray[i] < rightTmpArray[j])
               arr[k++] = LeftTmpArray[i++];
           else arr[k++] = rightTmpArray[j++];
       }
       while (i < ll)
           arr[k++] = LeftTmpArray[i++];
       while (j < rs)
           arr[k++] = rightTmpArray[j++];

    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int[] arr, int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 

        if(l >= r) {
            return;
        }

        int middle = (l + r) / 2;
        sort(arr, l, middle);
        sort(arr, middle + 1, r);
        merge(arr, l, middle, r);
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

//Time complexity - O(nlogn)
// Space Complexity - O(n)