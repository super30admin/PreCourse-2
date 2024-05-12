class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       int size1 = m - l + 1;
       int size2 = r - m;

       int[] leftArr = new int[size1];
       int[] rightArr = new int[size2];

       for(int i = 0; i < size1; i++) {
        leftArr[i] = arr[l + i];
       }

       for(int i = 0; i < size2; i++) {
        rightArr[i] = arr[m + 1 + i];
       }

       int leftArrIndex = 0;
       int rightArrIndex = 0;

       int k = l;
       while(leftArrIndex < size1 && rightArrIndex < size2) {
        
        if(leftArr[leftArrIndex] <= rightArr[rightArrIndex]) {
            arr[k] = leftArr[leftArrIndex];
            leftArrIndex++;
        } else {
            arr[k] = rightArr[rightArrIndex];
            rightArrIndex++;
        }
        k++;
       }

       while(leftArrIndex < size1) {
           arr[k] = leftArr[leftArrIndex];
           leftArrIndex++;
           k++;
       }

       while(rightArrIndex < size2) {
        arr[k] = rightArr[rightArrIndex];
        rightArrIndex++;
        k++;
    }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
        if(l < r) {
            int mid = l + (r - l)/2;

            sort(arr, l, mid);
            sort(arr, mid + 1, r);

            merge(arr, l, mid, r);
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