// Time Complexity : O(nlog n)
// Space Complexity : O(n) worst case
// Your code here along with comments explaining your approach
/*
 * The idea is to split and sort left and right sub arrays recursively first and then eventually merge
 *  using 2 pointers making sure to pick smaller element each time, placing it in main array.
 * */
class MergeSort
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
        int n1 = m - l + 1;
        int n2 = r - m;

        int[] N1 = new int[n1];
        int[] N2 = new int[n2];

        for(int i = 0 ; i < n1 ; i++)
            N1[i] = arr[l + i];
        for(int j = 0 ; j < n2 ; j++)
            N2[j] = arr[m + 1 + j];

        int i = 0, j = 0 , k = l;

        while(i < n1 && j < n2) {
            if(N1[i] < N2[j]) {
                arr[k++] = N1[i++];
            }
            else
                arr[k++] = N2[j++];
        }
        while(i < n1)
            arr[k++] = N1[i++];
        while(j < n2)
            arr[k++] = N2[j++];
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here
        if(l < r) {
            int m = l + (r - l) / 2;
            sort(arr, l, m);
            sort(arr, m + 1, r);

            merge(arr, l , m , r);
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