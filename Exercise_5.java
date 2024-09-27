import java.util.Stack;

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
    	arr[i] = arr[i]+arr[j]; 
    	arr[j] = arr[i] - arr[j];
    	arr[i] = arr[i] - arr[j];
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int low, int high) 
    { 
    	int pValue = arr[high];
    	int i = low;
    	for (int j = low+1; j < high; j++)
    	{
    		if (arr[j] < pValue)
    		{
    			swap(arr, i,j);
    			i++;
    		}
    	}
    	if (arr[i] > arr[high])
    	{
    		swap(arr, i, high);
    	}
    	
		return i;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
	{
		Stack<Integer> sk = new Stack<Integer>();
		sk.push(l);
		sk.push(h);
		while (!sk.isEmpty()) {
			h = sk.pop();
			l = sk.pop();
			int pivot = partition(arr, l, h);
			if (pivot - 1 > l) {
				sk.push(l);
				sk.push(pivot - 1);
			}

			if (pivot + 1 < h) {
				sk.push(pivot + 1);
				sk.push(h);
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