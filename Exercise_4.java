import java.util.Arrays;

class MergeSort
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {
        System.out.println("inside merge "+l+m+r);
        int length1 = m - l + 1;
        int length2 = r - m;


        int L[] = new int[length1];
        int R[] = new int[length2];
        for (int i = 0; i < length1; ++i)
            L[i] = arr[l + i];
        for (int j = 0; j < length2; ++j)
            R[j] = arr[m + 1 + j];

        int i = 0, j = 0, k = l;
        while (i < length1 && j < length2) {
            if (L[i] <= R[j]) {
                arr[k] = L[i];
                i++;
            }
            else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }
        while (i < length1) {
            arr[k] = L[i];
            i++;
            k++;
        }
        while (j < length2) {
            arr[k] = R[j];
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
        System.out.println("inside sort l= "+l +" r = "+r);
        if(l<r) {
            int mid = l + (r-l)/ 2;
            sort(arr, l, mid);
            sort(arr, mid + 1, r);
            merge(arr,l,mid,r);
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