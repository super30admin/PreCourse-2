/*
** Time Complexity - O(nlogn)
** Space Complexity - O(n)
** Did this code successfully run on Leetcode : Yes
** Any problem you faced while coding this : No
*/

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Find the size of two sub arrays
        int size1 = m-l+1;
        int size2 = r-m;
        System.out.println("size1: " + size1 + " size2: "+ size2);

        //creating two sub array
        int L[] = new int[size1];
        int R[] = new int[size2];

        //copy the array elements into the sub array
        for(int i = 0; i< size1; i++){
            L[i] = arr[l+i];
        }
        for(int j = 0; j< size2; j++){
            R[j] = arr[m+1+j];
        }
        //merge two temp arrays
        int i=0, j=0;
        int k=l;
        while(i<size1 && j<size2) {
            //compare the elements of left and right sub array, copy the smaller element in main array
            if(L[i] <= R[j]) {
                arr[k] = L[i];
                i++;
            } else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }
        //Copy remaining elements of both left and right sub array in main array
        while (i<size1){
            arr[k] = L[i];
            i++;
            k++;
        }
        while (j<size2){
            arr[k] = R[j];
            j++;
            k++;
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
       if(l < r) {
           System.out.println("left :"+ l+ " right: "+r);
           int mid = (l + r ) / 2;
           sort(arr, l, mid);
           sort(arr, mid + 1, r);

           //merge sorted each half
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