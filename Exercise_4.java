class MergeSort 
{ 
    // Time Complexity : O(Nlog(N))
    // Space Complexity : O(N)
    // Did this code successfully run on Leetcode : Yes
    // Any problem you faced while coding this : No

    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr1[], int arr2[], int arr[]) 
    {  

       int i=0;
       int j=0;
       int k=0;
       while(i<arr1.length && j<arr2.length){
           if(arr1[i]<arr2[j]){
               arr[k]=arr1[i];
               k++;
               i++;

           }else{
               arr[k]=arr2[j];
               j++;
               k++;
           }
       }

       while(i<arr1.length){
            arr[k]=arr1[i];
            k++;
            i++;
       }
       while(j<arr2.length){
            arr[k]=arr2[j];
            k++;
            j++;
       }

    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[]) 
    { 
	
        
        if(arr.length<= 1){
            return;
        }
        int a[] = new int[arr.length/2];
        int b[] = new int[arr.length-a.length];
        for(int i=0;i<arr.length/2;i++) {
			a[i]=arr[i];
		}
		for(int i=arr.length/2;i<arr.length;i++) {
			b[i-(arr.length/2)]=arr[i];
		}
        //Call mergeSort from here 
        sort(a);
        sort(b);
        merge(a,b,arr);

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
        ob.sort(arr); 
  
        System.out.println("\nSorted array"); 
        printArray(arr); 
    } 
} 