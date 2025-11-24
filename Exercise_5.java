// Time Complexity : O(n log n) average case, O(n^2) worst case
// Space Complexity : O(log n) because of the manual stack
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this :
// Understanding the stack-based iterative approach was the main challenge.
// Instead of recursive calls, I used an integer stack to store subarray
// boundaries and process them iteratively.



// I implemented Iterative QuickSort using a stack to simulate the recursion.
// The algorithm pushes left and right subarray boundaries onto the stack.
// For each popping, it calls partition() to place the pivot in the correct spot.
// Then it pushes the boundaries of the left and right subarrays back onto the stack.
// The process continues until the stack is empty.
class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
	if (i == j) return;
	arr[i] = arr[i] + arr[j];
	arr[j] = arr[i] - arr[j];
	arr[i] = arr[i] - arr[j];
	//Try swapping without extra variable 
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
	int pivot = arr[h];
	int i = (l - 1);
	for (int j = l; j <= h - 1; j++){
		if(arr[j] <= pivot){
			i++;
			swap(arr, i, j);
		}
	}
	swap(arr, i + 1, h);
	return (i + 1);
	//Compare elements and swap.
    } 
  
    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        int stack[] = new int[h -l + 1];
	int top = -1;
	stack[++top] = l;
	stack[++top] = h;
	while (top >= 0){
		h = stack[top--];
		l =stack[top--];
		int p = partition(arr, l , h);
		if (p - 1 > l){
			stack[++top] = l;
			stack[++top] = p-1;
		}
		if(p + 1 < h){
			stack[++top] = p + 1;
			stack[++top] = h;
		}
	}//Try using Stack Data Structure to remove recursion.
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
