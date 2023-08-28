class MergeSort 
{
    void merge(int arr[], int l, int m, int r) 
    {  
        int left = m - l + 1;
        int right = r - m;
        int leftArray[] = new int [left];
        int rightArray[] = new int [right];
        for (int i = 0; i < left; ++i)
            leftArray[i] = arr[l + i];
        for (int j = 0; j < right; ++j)
            rightArray[j] = arr[m + 1+ j];
        int i = 0, j = 0, k = l;
        while (i < left && j < right) {
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
        while (i < left) {
            arr[k] = leftArray[i];
            i++;
            k++;
        }
        while (j < right) {
            arr[k] = rightArray[j];
            j++;
            k++;
        }

    } 

    void sort(int arr[], int l, int r) 
    {
        if (l < r) {
            int m = l + (r-l)/2;
            sort(arr, l, m);
            sort(arr , m+1, r);
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