class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {
        int left_size = m - l + 1;
        int right_size = r - m;

        int left[] = new int[left_size];
        int right[] = new int[right_size];

        for (int i = 0; i < left_size; i++){
            left[i] = arr[l + i];
        }

        for (int j = 0; j < right_size; j++){
            right[i] = arr[mid + 1 + j];
        }

        int i =0, j = 0;
        int k = 0;
        while (i < left_size && j < right_size){
            if (left[i] < right[j]){
                arr[k] = left[i];
                i++;
            }
            else if(right[j] < left[i]){
                arr[k] = right[j];
                j++;
            }
            k++;
        }

        while (i < left_size){
            arr[k] = left[i];
            i++;
            k++;
        }
        while (j < right_size){
            arr[k] = right[j];
            j++;
            k++;
        }
       //Your code here  
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        int mid = l + (r - l)/2;
        if(l < r){
            sort(arr,l,mid);
            sort(arr,mid+1,r);
            //Call mergeSort from here
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