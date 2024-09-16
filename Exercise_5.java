import java.util.Stack;

class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	//Try swapping without extra variable
    	if(arr[i] != arr[j]) {
    		arr[i] = arr[i]+arr[j];
    		arr[j] = arr[i] - arr[j];
    		arr[i] = arr[i] - arr[j];
    	}
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap.
    	int i = l-1, pivot = arr[h];
    	for(int j = l; j < h; j++) {
    		if(arr[j] <= pivot) {
    			i++;
    			swap(arr,i,j);
    		}
    	}
    	swap(arr,i+1,h);
    	return i+1;
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
    	int[] curr;
    	Stack<int[]> sc = new Stack<int[]>();
    	sc.push(new int[] {l,h});
    	while(!sc.isEmpty()) {
    		curr = sc.pop();
    		if(curr[0] < curr[1]) {
    			int element = partition(arr, curr[0],curr[1]);
    			sc.push(new int[] {curr[0],(element-1)});
    			sc.push(new int[] {(element+1),curr[1]});
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