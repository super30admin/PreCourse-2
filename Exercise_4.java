//Time Complexity: O(nlogn)
//Space Complexity: O(n)

class MergeSort
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {
        int s1 = m - l + 1;
        int s2 = r - m;

        int[] temp1 = new int[s1];
        int[] temp2 = new int[s2];

        //copy the data to temp arrays
        System.arraycopy(arr, l, temp1, 0, s1);
        System.arraycopy(arr, m+1, temp2, 0, s2);

        int i=0, j =0;
        int k = l;
        while (i<s1 && j<s2) {
            if(temp1[i] <= temp2[j]){
                arr[k] = temp1[i];
                i++;
            }else {
                arr[k] = temp2[j];
                j++;
            }
            k++;
        }

        while (i < s1){
            arr[k] = temp1[i];
            i++;
            k++;
        }

        while (j< s2){
            arr[k] = temp2[j];
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
        if(l < r){
            int mid = (l+r)/2;

            sort(arr, l, mid);
            sort(arr, mid + 1, r);
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