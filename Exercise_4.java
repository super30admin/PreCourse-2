class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
        
        int leftArraySize = m+1-l;
        int rightArraySize = r-m;
        
       //Your code here  
       int leftArray[] = new int[leftArraySize];
       int rightArray[] = new int[rightArraySize];
       
       for(int i=0; i<leftArraySize; i++)
       {
           leftArray[i] = arr[i+l];    //creating the left sub array
       }
       for(int i=0; i<rightArraySize; i++)
       {
           rightArray[i] = arr[i+m+1];   //creating the right sub array
       }
    
       int i=0, j=0, k=l;   //  initialize k pointer to the lower index of the sub array
       
       while(i<leftArraySize && j<rightArraySize)
       {
           if(leftArray[i] <= rightArray[j])    //checking whether value in left array is smaller than the value in right array
           {
               arr[k] = leftArray[i];   //add the smaller value to the final array
               i++;
           }
           else
           {
               arr[k] = rightArray[j];  //add the smaller value to the final array
               j++;
           }
           k++;
       }
       
       while(i<leftArraySize)   //left over elements of left sub array is added to the final array
       {
           arr[k] = leftArray[i];
           i++;
           k++;
       }
       while(j<rightArraySize)  //left over elements of right sub array is added to the final array
       {
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
        if(l < r)
        {
            int m = l+(r-l)/2;  // find the middle index
            
            sort(arr, l, m);    //divide the array into two sub arrays
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