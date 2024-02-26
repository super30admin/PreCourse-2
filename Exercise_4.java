class MergeSort
/*Time Complexity: O(logn);
 * 
 * Space Complexity:O(n); where n is number of elements in the array
 * 
 * Output : 
Given Array
12 11 13 5 6 7 

Sorted array
5 6 7 11 12 13
 */ 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {
        int n1 = m - l + 1;
        int n2 = r -m;
        
        int lArr[] = new int[n1];
        int rArr[] = new int[n2];

        for (int x=0; x<n1;x++){
            lArr[x] = arr[l+x];
        }
        for (int x=0; x<n2;x++){
            rArr[x] = arr[m+1+x];
        }

        int i = 0;
        int j = 0;
        int k = l;

        while(i<n1 && j<n2){

            if (lArr[i] <= rArr[j]){
                arr[k] = lArr[i];
                i++;
            }else{
                arr[k] = rArr[j];
                j++;
            }
            k++;

        }
        while (i<n1){
            arr[k] = lArr[i];
            i++;
            k++;
        }
        while (j<n2){
            arr[k] = rArr[j];
            j++;
            k++;
        }
       //Your code here  
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    {
        if (l<r){
            int m = (l + (r-1))/2;
            sort(arr, l, m);
            sort(arr, m+1, r);

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