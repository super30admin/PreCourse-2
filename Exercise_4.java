class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       int leftArr = m + 1 - l;
       int rightArr = r - m;

       int[] leftArray = new int[leftArr];
       int[] rightArray = new int[rightArr];

       for(int i = 0; i < leftArr; i++){
           leftArray[i] = arr[i];
       }

       for(int i =0; i < rightArr; i++) {
           rightArray[i] = arr[m + i + 1];
       }

       int indexLeft = 0, indexRight = 0, mergedIndex = l;

       while(indexLeft < leftArr && indexRight < rightArr) {

           if(leftArray[indexLeft] <= rightArray[indexRight]) {
               arr[mergedIndex] = leftArray[indexLeft];
               indexLeft++;
           }
           else {
               arr[mergedIndex] = rightArray[indexRight];
               indexRight++;
           }
           mergedIndex++;
       }

       while(indexLeft < leftArr) {
           arr[mergedIndex] = leftArray[indexLeft];
           indexLeft++;
           mergedIndex++;
       }

       while(indexRight < rightArr) {
           arr[mergedIndex] = rightArray[indexRight];
           indexRight++;
           mergedIndex++;
       }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    {
        //Write your code here
        //Call mergeSort from here
        if(l >= r) {
            return;
        }
        int m = (l + r) / 2;
        sort(arr, l, m);
        sort(arr , m + 1, r);

        merge(arr , l, m, r);

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