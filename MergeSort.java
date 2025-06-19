// Implements Merge Sort to sort an array using divide and conquer.
// Time Complexity: O(n log n)
// Space Complexity: O(n)

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
       int leftLength = m-l+1;
       int rightLength = r-m;
       int a[] = new int[leftLength];
       int b[] = new int[rightLength];

       for(int i=0; i<leftLength; i++){
            a[i] = arr[l+i];
       }

       for(int i=0; i<rightLength; i++){
            b[i] = arr[m+1+i];
       }

       int k = l;
       int i = 0;
       int j = 0;
       while(i < leftLength && j < rightLength){
            if(a[i] < b[j]){
                arr[k++] = a[i++];
            }else{
                arr[k++] = b[j++];
            }
       }

       while(i < leftLength){
            arr[k++] = a[i++];
       }

       while(j < rightLength){
            arr[k++] = b[j++];
       }

    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 
        if(r-l <= 0){
            return;
        }

        int mid = l + (r-l)/2;

        sort(arr, l, mid);
        sort(arr, mid+1, r);

        merge(arr, l, mid, r);

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