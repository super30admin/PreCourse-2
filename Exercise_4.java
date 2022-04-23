// Time Complexity : O(N*logN) 
// Space Complexity : O(N)
class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Create elements s1,s2 these will hold the size of the two subarrays
       int s1 = m -l + 1;
       int s2 = r - m;
       //Create two arrays of size s1,s2
       int leftHalf[] = new int[s1];
       int rightHalf[] = new int[s2];
       //Insert the data into the arrays
       for(int i=0; i<s1; ++i){
           leftHalf[i]=arr[l +i ];
       }
       for(int i=0; i<s2; ++i){
           rightHalf[i]=arr[m + 1 + i];
       }
       //Initialize indexes of first subarray snd second subarray
       int i=0,j=0;
       //Initialize index of merged subarrays
       int k=l;
       while(i<s1 && j<s2){
           if(leftHalf[i]<=rightHalf[j]){
               arr[k]=leftHalf[i];
               i++;
           }
           else{
               arr[k]=rightHalf[j];
               j++;
           }
           k++;

       }
       //If any elements remain after merging the two arrays copy to the array
       while(i<s1){
           arr[k]=leftHalf[i];
           i++;
           k++;
       }
       while(j<s2){
           arr[k]=rightHalf[j];
           j++;
           k++;
       }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
    
    if(l < r){
        //create an int variable m which will be middle the array and separate the array
        int m = l+(r-l)/2;
        //sort the arrays
        sort(arr,l,m);
        sort(arr,m+1,r);
        //Call mergeSort from here 
        merge(arr,l,m,r);
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