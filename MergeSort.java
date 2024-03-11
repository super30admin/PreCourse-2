
//TC: θ(Nlog(N)) in all 3 cases (worst, average, and best)
//SC: O(N), all elements are copied into an auxiliary array.
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
        int leftLength = m - l + 1;
        int rightLength = r - m;

        int[] leftArray = new int[leftLength];
        int[] rightArray = new int[rightLength];

        for (int i = 0; i < leftLength; i++) {
            leftArray[i] = arr[l + i];
        }
        for (int j = 0; j < rightLength; j++) {
            rightArray[j] = arr[m + 1 + j];
        }
        //Let's iterate over both temp arrays and copy the smaller of current elements to original array
        int i = 0;
        int j = 0;
        int k = l;

        while (i < leftLength && j < rightLength) {
            if (leftArray[i] <= rightArray[j]) {
                arr[k] = leftArray[i];
                i++;
            }
            else {
                arr[k] = rightArray[j];
                j++;
            }
            k++;
        }

        while (i < leftLength) {
            arr[k] = leftArray[i];
            i++;
            k++;
        }

        while (j < rightLength) {
            arr[k] = rightArray[j];
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
        if (arr == null) {
            System.out.println("Null input");
            return;
        }
        // We will perform sort only when l < r. Ie array has at least one element.
        if (l < r) {
            int m = l + (r - l) / 2;

            //Recursively call sort on left and right sub array
            sort(arr, l, m);
            sort(arr, m + 1, r);

            //Merge left and right sub arrays
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
  
        MergeSort ob = new MergeSort(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 