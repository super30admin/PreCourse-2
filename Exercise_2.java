package precourse2;

class QuickSort 
{ 
	public static void quickSort(int[] array, int startIdx, int endIdx){
		if(startIdx >= endIdx){
			return;
		}
		int pivotIdx = startIdx;
		int leftIdx = startIdx + 1;
		int rightIdx = endIdx;
		while(leftIdx <= rightIdx){
			if(array[leftIdx] > array[pivotIdx] && array[rightIdx] < array[pivotIdx]){
				swap(leftIdx, rightIdx, array);
			}
			if(array[leftIdx] <= array[pivotIdx]){
				leftIdx += 1;
			}
			if(array[rightIdx] >= array[pivotIdx]){
				rightIdx -= 1;
			}
		}
		swap(pivotIdx, rightIdx, array);
		boolean leftSubarrayIsSmaller = rightIdx - 1 - startIdx < endIdx - (rightIdx + 1);
		if(leftSubarrayIsSmaller){
			quickSort(array, startIdx, rightIdx - 1);
			quickSort(array, rightIdx+1, endIdx);
		}else{
			quickSort(array, rightIdx + 1, endIdx);
			quickSort(array, startIdx, rightIdx - 1);
		}
	}
	
	public static void swap(int i, int j, int[] array){
		int temp = array[j];
		array[j] = array[i];
		array[i] = temp;
	}
	
	static void printArray(int arr[]) 
    { 
        int n = arr.length; 
        for (int i=0; i<n; ++i) 
            System.out.print(arr[i]+" "); 
        System.out.println(); 
    } 
  
    // Driver program 
    public static void main(String args[]) 
    { 
        int arr[] = {10, 7, 8, 9, 1, 5}; 
        int n = arr.length; 
   
        quickSort(arr, 0, n-1); 
  
        System.out.println("sorted array"); 
        printArray(arr); 
    } 
} 