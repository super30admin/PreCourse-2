// Time Complexity : O(nlogn)
// Space Complexity : O(n)
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here 
       int lsize = m-l+1;
       int rsize = r-m;

       int larr[] = new int[lsize];
       int rarr[] = new int[rsize]; 

       for(int i=0; i<lsize; i++){
           larr[i] = arr[l+i];
        }
       for(int j=0; j<rsize; j++){
           rarr[j] = arr[m+1+j];
        }

        int i = 0;
        int j = 0;
        int mergedindex = l;

        while(i<lsize && j<rsize){
            if(larr[i] <= rarr[j]){
                arr[mergedindex] = larr[i];
                i++;
            }else{
                arr[mergedindex] = rarr[j];
                j++;
            }
            mergedindex++;
        }

        while(i<lsize){
            arr[mergedindex] = larr[i];
            i++;
            mergedindex++;
        }

        while(j<rsize){
            arr[mergedindex] = rarr[j];
            j++;
            mergedindex++;
        }

    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
        if(l<r){
            int m = l + (r-l)/2;
            sort(arr, l, m);
            sort(arr, m+1, r);

            merge(arr, l, m, r);
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