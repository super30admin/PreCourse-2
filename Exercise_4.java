class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       int[] one = new int[m-l+1];
       int[] two = new int[r-m];

       for(int i = 0 ; i < one.length; i++){
           one[i] = arr[l+i];
       }

       for(int j = 0; j < two.length; j++){
           two[j] = arr[j+m+1];
       }

       int indexOne = 0;
       int indexTwo = 0;
       int resultsIndex = l;

       while(indexOne < one.length && indexTwo < two.length){
           if(one[indexOne] < two[indexTwo]){
               arr[resultsIndex] = one[indexOne];
               indexOne++;
           }else{
               arr[resultsIndex] = two[indexTwo];
               indexTwo++;
           }
           resultsIndex++;
       }

       while(indexOne < one.length){
            arr[resultsIndex] = one[indexOne];
            indexOne++;
            resultsIndex++;
       }

       while(indexTwo < two.length){
            arr[resultsIndex] = two[indexTwo];
            indexTwo++;
            resultsIndex++;
       }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
        //Call mergeSort from here 
        if(l < r){
            int mid = (l+r) / 2;
            sort(arr,l,mid);
            sort(arr,mid+1,r);
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