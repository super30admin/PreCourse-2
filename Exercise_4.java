/* TC: O(nlogn)  SC: O(n) */
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       int s1 = m - l + 1;
       int s2 = r- m;
       int[] left = new int[s1];
       int[] right = new int[s2];
       for(int i = 0 ; i < s1; i++){
        left[i] = arr[l+i];
       } 
       for(int i = 0 ; i < s2; i++){
        right[i] = arr[m+i+1];
       }//Your code here  
       int i = 0, j = 0, k = l;
       while( i < s1 && j < s2){
        if(left[i] <= right[j]){
            arr[k] = left[i];
            i++;
        } 
        else{
           arr[k] = right[j];
            j++; 
        }
        k++;
       }
       while(i < s1)
       {
        arr[k] = left[i];
        k++;
        i++;
       }
       while(j < s2)
       {
        arr[k] = right[j];
        k++;
        j++;
       }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
        if(l < r){
            int m = l + (r - l)/2;
            sort(arr,l,m);
            sort(arr,m+1,r);
            merge(arr,l,m,r);
        }
	//Write your code here
        //Call mergeSort from here 
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