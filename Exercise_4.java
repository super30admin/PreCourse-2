//Time complexity: O(n log n)
//Space complexity: O(n)
//code successfully run on the local
//I didnt find any problem while running the code  
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

       int leftArray[] = new int[leftLength];
       for(int i=0; i<leftLength; i++){
           leftArray[i] = arr[l + i];
       }
       int rightArray[] = new int[rightLength];
       for(int j=0; j<rightLength; j++){
           rightArray[j] = arr[m + 1 + j];
       }

       int i = 0;
       int j = 0;

       int k = l;
       while(i < leftLength && j< rightLength){
            if(leftArray[i] <= rightArray[j]){
                arr[k] = leftArray[i];
                i++;
            }else{
                arr[k] = rightArray[j];
                j++;
            }
            k++;
        }

       while(i <  leftLength){
            arr[k] = leftArray[i];
            i++;
            k++;
       }
       while(j < rightLength){
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
        if(l < r){
            int mid = (l+ r) / 2;
            sort(arr, l , mid);
            sort(arr, mid+1, r);
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