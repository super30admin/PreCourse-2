//Time complexity = O(nlogn)
//space Complexity = O(n)

class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
        
      int p1 = m - l + 1;
      int p2 = r - m;
    
      //Dividing arrays acc to l, m, r values so that they be merged  in sorted order in given range
      int leftArr[] = new int[p1];
      int rightArr[] = new int[p2];
      for(int i = 0; i < p1; i++){
          leftArr[i] = arr[i + l]; 
      }
      for(int i = 0; i < p2; i++){
          rightArr[i] = arr[i + m + 1]; 
      }
     
     int i = 0, j = 0;
     int k = l;
     //sorting and merging the arrays   
     while( i < p1 && j < p2){
         
         if(leftArr[i] <= rightArr[j] ){
             arr[k] = leftArr[i];
             i++;
         } else {
             arr[k] = rightArr[j];
             j++;       
         }
         k++;
     }
     
        while(i < p1){
            arr[k] = leftArr[i];
            i++;
            k++;
        }
        while( j < p2){
            arr[k] = rightArr[j];
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
            // Finding the midpoint
            int m = l+ (r-l)/2;
  
            // Sort first half
            sort(arr, l, m);
             // Sort second half
            sort(arr, m + 1, r);
            // Merge the sorted halves
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
        ob.sort(arr, 0, arr.length - 1); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 
