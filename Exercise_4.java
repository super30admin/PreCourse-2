class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
        int p1 = 0;
        int p2 = 0;
        int n1 = m-l+1;
        int n2 = r-m;
        int[] temp1 = new int[n1];
        int[] temp2 = new int[n2];

        for(int i=0; i<n1;i++){
            temp1[i] = arr[l+i];
        }
        for(int i=0; i<n2; i++){
            temp2[i] = arr[m+1+i];
        }
        int i = l;
        while(p1<n1 && p2<n2) {
           if(temp1[p1]< temp2[p2]){
               arr[i] = temp1[p1];
               i++;
               p1++;
           } else {
               arr[i] = temp2[p2];
               i++;
               p2++;
           }
        }
        while(p1<n1){
            arr[i] = temp1[p1];
            i++;
            p1++;
        }
        while(p2<n2){
            arr[i] = temp2[p2];
            i++;
            p2++;
        }
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[], int l, int r) 
    { 
	//Write your code here
        //Call mergeSort from here
        if(l >= r) {
            return;
        }
        int middle = l + (r-l)/2;
        sort(arr, l, middle);
        sort(arr, middle+1, r);
        merge(arr, l, middle, r);
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
