/*
 * Time Complexity : O(NLogN)
 * Space Complexity : O(N) as this is using extra space for merging the array every time 
 */

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
        int i1 = l;
        int i2 = m+1;
        int[] tempArr = new int[r-l+1];
        int index = 0;
        
        while(i1<=m && i2 <=r){
                
            if(arr[i1] <= arr[i2]){
                
                tempArr[index] = arr[i1];
                i1++;
            }
            else{
                
                tempArr[index] = arr[i2];
                i2++;
            }
            index++;

        }
        while(i1<=m){
            tempArr[index] = arr[i1];
            i1++;
            index++;
        }
        while(i2<=r){
            tempArr[index] = arr[i2];
            i2++;
            index++;
        }
        
        int arr_index = l;
        for(int i=0; i<r-l+1; i++){
            arr[arr_index] = tempArr[i];
            arr_index++;
        }
        


        
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
        if(l<r){    
            
            int middle = l+(r-l)/2;
        
            sort(arr, l, middle );
            sort(arr, middle+1, r);
            
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
        int arr[] = {8,19,12, 11, 13, 5, 6, 7, 1,4, 34,12,353}; 
  
        System.out.println("Given Array"); 
        printArray(arr); 
  
        MergeSort ob = new MergeSort(); 
        ob.sort(arr, 0, arr.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 