class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
        int leftSize = m-l+1;
        int rightSize = r-m;
       
        List<Integer> leftArray = new ArrayList<>();
        List<Integer> rightArray = new ArrayList<>();  

        for (int i=0; i<leftSize; i++)
            leftArray.add(arr[i]);

        for (int i=0; i<leftSize; i++)
            leftArray.add(arr[i]);

        int i=0;
        int j=0;
        int k=l;
        while (i<leftSize && j<rightSize){
            if (leftArray.get(i)<=rightArray.get(i)) {
                arr[k] = leftArray.get(i);
                i++;
            }
            else {
                arr[k] = rightArray.get(i);
                j++;
            }
            k++;
        }

        while (i<leftSize){
            arr[k] = leftArray.get(i);
            i++;
            k++;
        }

        while (j<rightSize){
            arr[k] = rightArray.get(j);
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
        if (l<r)
            merge(arr, l, r);
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