//Time complexity = O(N LOGN)

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp; 
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int low, int high) 
    { 
        int x = arr[high];
	int i = (low-1);
	for(int j=low;j<=high-1;j++){
		if(arr[j] <=x ){
			i++;
			swap(arr,i,j);
		}
	
	
	}
	    swap(arr,i+1,high);
	    return (i+1);
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int low, int high) 
    { 
        int [] stack = new int[high-low+1];
	int top = -1;
	stack[++top] = low;
	stack[++top] = high;
	while(top>=0){
		high = stack[top--];
		low = stack[top--];
		int pivot = partition(arr,low,high);
		if(pivot-1>low){
			stack[++top] = low;
		        stack[++top] = pivot-1;
		}
		if(pivot+1<high){
			stack[++top] = pivot + 1;
			stack[++top] = high;
		}
	
	
	
	
	}
    } 
  
    // A utility function to print contents of arr 
    void printArr(int arr[], int n) 
    { 
        int i; 
        for (i = 0; i < n; ++i) 
            System.out.print(arr[i] + " "); 
    } 
  
    // Driver code to test above 
    public static void main(String args[]) 
    { 
        IterativeQuickSort ob = new IterativeQuickSort(); 
        int arr[] = { 4, 3, 5, 2, 1, 3, 2, 3 }; 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
    } 
} 
