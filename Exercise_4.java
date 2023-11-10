class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
        int num1 = m - l + 1;
        int num2 = r - m;
        int Left[] = new int[num1];
        int Right[] = new int[num2];
        for (int i = 0; i < num1; ++i)
        {
            Left[i] = arr[l + i];
        }
        for (int j = 0; j < num2; ++j)
        {
            Right[j] = arr[m + 1 + j];
        }
        int i = 0, j = 0;
        int k = l;
        while (i < num1 && j < num2) {
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
        while (i < num1) {
            arr[k] = Left[i];
            i++;
            k++;
        }
        while (j < num2) {
            arr[k] = Right[j];
            j++;
            k++;
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
        if (l < r) {
            int m =l+ (r-l)/2; // calculating middle index here 
            sort(arr, l, m);
            sort(arr, m + 1, r);
            merge(arr, l, m, r);
        }
	//Write your code here
        //Call mergeSort from here 
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

//timr complexity : θ(nLogn)
//space complexity : O(n)
//recursive approach
//ran this code successfully
//faced issues when tried to implement from concept and 
//so many error also faced challenge while time complexity calculation and was difficult for me.
//need to do again and solve it again after this assignment as well:(
