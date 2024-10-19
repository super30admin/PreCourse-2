// Avg Time Complexity : o(nlogn)
// worst Time Complexity : o(nlogn)
// Space Complexity : o(n) // additional space needed for temporary array used for merging
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       // find sizes of two subarrays to be merged
       int n1= m-l+1;
       int n2=r-m;

       // create two temp arrays
       int L[]=new int[n1];
       int R[]=new int [n2];

       // copy data to the two temp arrays
       for (int i=0;i<n1;i++){
            L[i]=arr[l+i];
       }
       for (int j=0;j<n2;j++){
            R[j]=arr[m+1+j]
       }

       // Merge the temp left and right arrays
       int i=0,j=0;
       int k=0;
       while(i<n1 && j<n2){
            if (L[i]<R[j]){
                arr[k]=L[i];
                i++;
            } else{
                arr[k]=R[j];
                j++;
            }
            k++;
       }
       // copy the remaining elements from left array
       while(i<n1){
        arr[k]=L[i];
        i++;
        k++;
       }

       // Copy the remaining elements from right array
       while(j<n2){
        arr[k]=R[j];
        j++;
        k++;
       }

      
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
        // merge sort code here
        if(l<r){
            int m = l+ (r-1)/2;

            // sort first and second halves
            sort(arr,l,m);
            sort(arr,m+1,r);

            // merge the sorted halves
            merge(arr,l,m,r)
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