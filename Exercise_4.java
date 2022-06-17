//Time Complexity: O(N logN)
//Space Complexity: O(N)

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
        int leftArraySize = m - l + 1;
        int rightArraySize = r - m;
 
        int left[] = new int[leftArraySize];
        int right[] = new int[rightArraySize];
 
        for (int i = 0; i < leftArraySize; i++){
            left[i] = arr[l + i];
        }for (int j = 0; j < rightArraySize; ++j){
            right[j] = arr[m+j+1];
        }
        int i = 0;
        int j = 0;
        int k = l;
        while (i < leftArraySize && j < rightArraySize){
            if(left[i] <= right[j]){
                arr[k] = left[i];
                i++;
            } else{
                arr[k] = right[j];
                j++;
            }
            k++;
        }
 
        while (i < leftArraySize) {
            arr[k] = left[i];
            i++;
            k++;
        } while (j < rightArraySize) {
            arr[k] = right[j];
            j++;
            k++;
        }

    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
        //Write your code here
        if(l<r){
            int m = (l + r) / 2;
            sort(arr, l, m);
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
  
        MergeSort ob = new MergeSort(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 