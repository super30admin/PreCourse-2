class MergeSort 
{ 
    //Time Complexity : O(n log n)
    //Space Complexity : O(n)

    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {
        int leftSubArraySize = m - l +1;  
        int rightSubArraySize = r -m;

        int[] leftSubArray = new int[leftSubArraySize];
        int[] rightSubArray = new int[rightSubArraySize];

        for(int i = 0; i < leftSubArraySize; i++) {
            leftSubArray[i] = arr[l + i];
        }
        for(int j = 0; j < rightSubArraySize; j++) {
            rightSubArray[j] = arr[m+1+j];
        }

        int i = 0; int j = 0; int k = l;
        while(i < leftSubArraySize && j < rightSubArraySize) {
            if(leftSubArray[i] <= rightSubArray[j]) {
                arr[k] = leftSubArray[i];
                i++;
            } else { 
                arr[k] = rightSubArray[j];
                j++;
            }
            k++;
        }

        while(i < leftSubArraySize) {
            arr[k] = leftSubArray[i];
            i++;
            k++;
        }

        while(j < rightSubArraySize) {
            arr[k] = rightSubArray[j];
            j++;
            k++;
        }
    }
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        if(l < r) {
            int mid = l + (r-l) / 2;
            sort(arr, l, mid);
            sort(arr, mid+1, r);
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