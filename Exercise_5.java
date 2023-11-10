class IterativeQuickSort { 
    void swap(int arr[], int i, int j) 
    { 
    
        // arr[i] = arr[i] + arr[j];
        // arr[j] = arr[i] - arr[j];
        // arr[i] = arr[i] - arr[j];
        //******NOTE******** : tried without extra variable some how didnt worked some elements giving 0 after swaping :(
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
	//Try swapping without extra variable 
    } 
  
    /* This function is same in both iterative and 
       recursive*/
    int partition(int arr[], int l, int h) 
    { 
        int n = arr[h];
        int i = (l - 1);
        for (int j = l; j <= h - 1; j++) {
            if (arr[j] <= n) {
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
        int s[] = new int[h - l + 1];
        int top = -1;
        s[++top] = l;
        s[++top] = h;
        while (top >= 0) {
            h = s[top--];
            l = s[top--];
            int pivot = partition(arr, l, h);
            if (pivot - 1 > l) {
                s[++top] = l;
                s[++top] = pivot - 1;
            }
            if (pivot + 1 < h) {
                s[++top] = pivot + 1;
                s[++top] = h;
            }
        }
        //Try using Stack Data Structure to remove recursion.
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
        int arr1[] = { 0, 3, 5, 0, 1, 0, 2, 3 }; 
        ob.QuickSort(arr, 0, arr.length - 1); 
        ob.printArr(arr, arr.length); 
        System.out.println("\n");
        ob.QuickSort(arr1, 0, arr1.length - 1); 
        ob.printArr(arr1, arr1.length); 
    } 
} 

//time complexity : O(N log N)
//space complexity:  O(log N)
//approach : iterative using stack
//I read about this question and researched on internet and could not implement on my own. I faced so many difficulties to write this code.Specificallty with using stack and iterative solutions. 
//I tried to swap the elements without temporary variable but getting wrong answer. Would like to have a hint on it. Why it didnt worked? 
//Most difficulties I faced is for egde cases were not running when i tried to use my logic and than I had to look online for solution and understand it.
// Ran this solution and its successfully runnning..
