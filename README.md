# PreCourse_2

# All Instructions are already provided in the respective files.

## Exercise_1 : Binary Search.

```Java

// Time Complexity : O(logN)
// Space Complexity : O(logN)
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : no

class BinarySearch {
    // Returns index of x if it is present in arr[l.. r], else return -1
    int binarySearch(int arr[], int l, int r, int x)
    {   
    //Write your code here
    if(r >= 1){
        int mid = l + (r - 1) / 2;
        //if the element found at the middle itself
        if(arr[mid] == x){
            return mid;
        }
        //If element is smaller than mid, then it should be present in left subarray
        if(x < arr[mid]){
            return binarySearch(arr, l, mid-1, x);
        }
        return binarySearch(arr, mid+1, r, x);
    }
    return -1;
}

    // Driver method to test above 
    public static void main(String args[]) 
    { 
        BinarySearch ob = new BinarySearch(); 
        int arr[] = { 2, 3, 4, 10, 40 }; 
        int n = arr.length; 
        int x = 10; 
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
}
```

## Exercise_2 : Quick sort.

```Java
// Time Complexity : O(n^2)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : no

class QuickSort {
    void swap(int arr[],int i,int j){
    //Your code here
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
    }
    int partition(int arr[], int low, int high) {
    //Write code here for Partition and Swap
    int pivot = arr[high];
    int i = (low-1);
        for(int j=low;j<=high-1;j++){
            if(arr[j] < pivot){
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i+1, high);
        return (i+1);
    } 
    /* The main function that implements QuickSort() 
      arr[] --> Array to be sorted, 
      low  --> Starting index, 
      high  --> Ending index */
    void sort(int arr[], int low, int high) 
    {
        if(low < high){
            int p = partition(arr, low, high);

            sort(arr, low, p-1);
            sort(arr, p+1, high);
        }
            // Recursively sort elements before 
            // partition and after partition 
    } 
  
    /* A utility function to print array of size n */
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
  
        QuickSort ob = new QuickSort(); 
        ob.sort(arr, 0, n-1); 
  
        System.out.println("sorted array"); 
        printArray(arr); 
    } 
}
```

## Exercise_3 : Find Mid Point of a Singly Linked List.

```Java
// Time Complexity : O(n)
// Space Complexity : O(1)
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : no

class MidPointSinglyLL
{ 
    Node head; // head of linked list
  
    /* Linked list node */
    class Node 
    { 
        int data; 
        Node next; 
        Node(int d) 
        { 
            data = d; 
            next = null; 
        } 
    } 
  
    /* Function to print middle of linked list */
   //Complete this function
    public int getLen()
    {
        int length = 0;
        Node temp = head;
        while (temp != null) {
            length++;
            temp = temp.next;
        }
        return length;
    }

    /*Printing the middle element of the list.*/
    public void printMiddle()
    {
        if (head != null) {
            int length = getLen();
            Node temp = head;
            int middleLength = length / 2;
            while (middleLength != 0) {
                temp = temp.next;
                middleLength--;
            }
            System.out.print("The middle element is ["
                    + temp.data + "]");
            System.out.println();
        }
    }
  
    public void push(int new_data) 
    { 
        Node new_node = new Node(new_data); 
        new_node.next = head; 
        head = new_node; 
    } 

    public void printList() 
    { 
        Node tnode = head; 
        while (tnode != null) 
        { 
            System.out.print(tnode.data+"->"); 
            tnode = tnode.next; 
        } 
        System.out.println("NULL"); 
    } 
  
    public static void main(String [] args) 
    {
        MidPointSinglyLL sllist = new MidPointSinglyLL();
        for (int i=15; i>0; --i) 
        { 
            sllist.push(i);
            sllist.printList();
            sllist.printMiddle();
        } 
    } 
} 
```

## Exercise_4 : Merge Sort.

```Java
// Time Complexity : O(nlogn)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : no

class MergeSort
{ 
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int arr[], int l, int m, int r) 
    {  
       //Your code here
        int n1 = m-l+1;
        int n2 = r-m;

        //temp arrays
        int L[] = new int[n1];
        int R[] = new int[n2];

        for(int i=0;i<n1;++i){
            L[i] = arr[l+i];
        }
        for(int j=0;j<n2;++j){
            R[j] = arr[m+l+j];
        }
        int i = 0, j = 0;

        //Initial index of merged subarray array
        int k = l;
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) {
                arr[k] = L[i];
                i++;
            }
            else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }

        //Copy remaining elements of L[] if any
        while (i < n1) {
            arr[k] = L[i];
            i++;
            k++;
        }

        //Copy remaining elements of R[] if any
        while (j < n2) {
            arr[k] = R[j];
            j++;
            k++;
        }
    }

    // Main function that sorts arr[l..r] using
    // merge()
    void sort(int arr[], int l, int r) {
        //Write your code here
        //Call mergeSort from here
        if (l < r) {
            // Find the middle point
            int m = l + (r - l) / 2;

            // Sort first and second halves
            sort(arr, l, m);
            sort(arr, m + 1, r);

            // Merge the sorted halves
            merge(arr, l, m, r);
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
```

## Exercise_5 : Iterative Quick Sort.

```Java
// Time Complexity : O(nlogn)
// Space Complexity : O(n)
// Did this code successfully run on Leetcode : yes
// Any problem you faced while coding this : using stack data structure to remove recursion

class IterativeQuickSort {
    /*void swap(int arr[], int i, int j)
    {
	//Try swapping without extra variable
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;

    } */
  
    //This function is same in both iterative and recursive
    int partition(int arr[], int l, int h) 
    { 
        //Compare elements and swap
        int pivot = arr[h];
        int i = (l - 1); // index of smaller element
        for (int j = l; j <= h - 1; j++) {
            // If current element is smaller than or
            // equal to pivot
            if (arr[j] <= pivot) {
                i++;

                // swap arr[i] and arr[j]
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }

        // swap arr[i+1] and arr[high] (or pivot)
        int temp = arr[i + 1];
        arr[i + 1] = arr[h];
        arr[h] = temp;

        return i + 1;
    }

    // Sorts arr[l..h] using iterative QuickSort 
    void QuickSort(int arr[], int l, int h) 
    { 
        //Try using Stack Data Structure to remove recursion.
        if (l < h) {
            /* pi is partitioning index, arr[pi] is
            now at right place */
            int pi = partition(arr, l, h);

            // Recursively sort elements before
            // partition and after partition
            QuickSort(arr, l, pi - 1);
            QuickSort(arr, pi + 1, h);
        }
    } 
  
    // A utility function to print contents of arr 
    void printArr(int arr[], int n) 
    {
        for (int i = 0; i < n; ++i)
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
```

*After completing the project kindly submit a pull request*
