//Time Complexity: O(Nlog(N)
//Space complexity: O(N)
class MergeSort
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       int merged[] = new int[r-l+1];

       int index1 = l;
       int index2 = m +1;
       int x =0;

       while(index1<=m && index2<=r){

           if(arr[index1] <= arr[index2]){
               merged[x++] = arr[index1++];
           }
           else{
               merged[x++] = arr[index2++];
           }
       }
       while(index1 <= m){
           merged[x++] = arr[index1++];
       }

       while(index2 <=r){
           merged[x++] = arr[index2++];
       }

       for(int i=0, j=l; i<merged.length; i++,j++ ){
           arr[j] = merged[i];
       }


    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    {
       if(l<r) {
           int mid = (l + r) / 2;
           sort(arr, l, mid);
           sort(arr, mid + 1, r);

           //Call mergeSort from here
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