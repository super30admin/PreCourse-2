public class MergeSort 
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int leftArr[], int rightArr[], int arr[]) 
    {  
       //Your code here  
    	int nL = leftArr.length;
    	int nR = rightArr.length;
    	int i = 0, j = 0, k = 0;
    	
    	while(i < nL && j < nR) {
    		if(leftArr[i] <= rightArr[j]) {
    			arr[k] = leftArr[i];
    			i++;
    		} else {
    			arr[k] = rightArr[j];
    			j++;
    		}
    		k++;
    	}
    	while(i < nL) {
    		arr[k] = leftArr[i];
			i++;
			k++;
    	}
    	while(j < nR) {
    		arr[k] = rightArr[j];
			j++;
			k++;
    	}
    } 
  
    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int arr[]) 
    { 
	//Write your code here
        //Call mergeSort from here 
    	int length = arr.length;
    	if(length < 2)
    		return;
    	int mid = length / 2;
    	int[] leftArr = new int[mid];
    	int[] rightArr = new int[length - mid];
    	for(int i = 0; i < mid; i++) {
    		leftArr[i] = arr[i];
    	}
    	for(int i = mid; i < length; i++) {
    		rightArr[i - mid] = arr[i];
    	}
    	sort(leftArr);
    	sort(rightArr);
    	merge(leftArr, rightArr, arr);
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