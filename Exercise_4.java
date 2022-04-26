//Time Complexity: O(nlogn)
//Space Complexity(For arrays): O(n)

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

        int Left[] = new int[n1];
        int Right[] = new int[n2];

        for(int i = 0; i < n1; i++) {
            Left[i] = arr[l + i];
        }
        for(int j = 0; j < n2; j++) {
            Right[j] = arr[m + j + 1];
        }

        int i = 0;
        int j = 0;
        int k = l;
        while(i < n1 && j < n2) {
            if(Left[i] <= Right[j]) {
                arr[k] = Left[i];
                i++;
            }
            else {
                arr[k] = Right[j];
                j++;
            }
            k++;
        }

        while(i < n1) {
            arr[k] = Left[i];
            i++;
            k++;
        }

        while(j < n2) {
            arr[k] = Right[j];
            j++;
            k++;
        }

    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here
        if(l < r) {
            int m = l + (r-l)/2;
            sort(arr, l, m);
            sort(arr, m+1, r);
            merge(arr, l, m ,r);
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