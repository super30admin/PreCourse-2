// Time Complexity : O(NLogN)
// Space Complexity : O(N) for Array
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : Had to refer GFG. Did it for the first time. Went the most difficult amongst all 5 questions


// Your code here along with comments explaining your approach
// Merge Sort
class Exercise_4 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
        //Your code here  
        // Finding sizes of both arrays
        int s1 = m-l+1;
        int s2 = r-m;

        //Copying data of both arrays
        int L[] = new int[s1];
        for(int i=0; i<s1; i++){
            L[i] = arr[l+i];
        }

        int R[] = new int[s2];
        for(int j=0; j<s2; j++){
            R[j] = arr[m+1+j];
        }

        //Indexes of both arrays
        int li = 0;
        int ri = 0;

        //Index of merged array
        int k = l;

        while(li < s1 && ri < s2){
            if(L[li] <= R[ri]){
                arr[k] = L[li];
                li++;
            }else
            {
                arr[k] = R[ri];
                ri++;
            }
            k++;
        }

        //Copy remaining elements

        while (li < s1) {
            arr[k] = L[li];
            li++;
            k++;
        }

        while(ri<s2){
            arr[k] = R[ri];
            ri++;
            k++;
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here 

        if(l < r){
            int m = l + (r-l)/2;
            //Sort the first & second halves anf then merge them
            sort(arr, l ,m);
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
  
        Exercise_4 ob = new Exercise_4(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 