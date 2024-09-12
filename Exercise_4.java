class MergeSort 
//edited
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here  
    	int number1 = m - l + 1;
    	int number2 = r-m;
    	
    	int Left[] = new int[number1];
        int Right[] = new int[number2];
        
        for(int i = 0; i < number1; i++) 
        {
        	Left[i] = arr[l + i];
        	
        }
        for(int j = 0; j < number2; j++) 
        {
        	Right[j] = arr[m + 1 + j];
        	
        }
        
        int i = 0, j = 0;
        
        int k = l;
        
        while (i < number1 && j < number2) {
            if (Left[i] <= Right[j]) {
                arr[k] = Left[i];
                i++;
            }
            else {
                arr[k] = Right[j];
                j++;
            }
            k++;
        }
 
        while (i < number1) {
            arr[k] = Left[i];
            i++;
            k++;
        }
 
        while (j < number2) {
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
    	if (l < r) {
            // Find the middle point
            int middle = (l + r) / 2;
 
            // Sort first and second halves
            sort(arr, l, middle);
            sort(arr, middle + 1, r);
 
            // Merge the sorted halves
            merge(arr, l, middle, r);
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