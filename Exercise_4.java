//Time complexity: O(n log n)
//Space Complexity: O(n)
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
        int leftsubLength = m - l + 1;
        int rightsubLength = r-m;
        int leftsub[] = new int[leftsubLength];
        int rightsub[] = new int[rightsubLength];
 
        
        for (int i = 0; i <leftsubLength; ++i)
            leftsub[i] = arr[l + i];
        for (int j = 0; j < rightsubLength; ++j)
            rightsub[j] = arr[m + 1 + j];
 
        int i = 0, j = 0, k = l;
        while (i < leftsubLength && j < rightsubLength) {
            if (leftsub[i] <= rightsub[j]) {
                arr[k] = leftsub[i];
                i++;
            }
            else {
                arr[k] = rightsub[j];
                j++;
            }
            k++;
        }
        //Copy remaining elements of subarrays
        while (i < leftsubLength) {
            arr[k] = leftsub[i];
            i++;
            k++;
        }
        while (j < rightsubLength) {
            arr[k] = rightsub[j];
            j++;
            k++;
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
        if(l<r){
        int middle = l+(r-l)/2;

        sort(arr, l, middle);
        sort(arr, middle+1, r);
         //Call mergeSort from here 
        merge(arr, l, middle, r);}
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