// Time Complexity: 
// Space Complexity: 

// Merge sort is a divide and conquer approach where we half an 
// unsorted original arrays till individual elements. When this is 
// achieved, while merging, it is compared and placed in correct order.
class MergeSort {

    // Performs merging of the individual elements back into
    // the original size array with the help of temporary arrays
    static void merge(int[] arr, int left, int mid, int right) {
        int tempLength1 = mid - left + 1;
        int tempLength2 = right - mid;

        int tempArray1[] = new int[tempLength1];
        int tempArray2[] = new int[tempLength2];

        for (int i = 0; i < tempLength1; i++) {
            tempArray1[i] = arr[left + i];
        }
        for (int j = 0; j < tempLength2; j++) {
            tempArray2[j] = arr[mid + j + 1];
        }
        int i = 0;
        int j = 0;
        int k = left;

        // When both temp arrays are still yet to exhausted
        while (i < tempLength1 && j < tempLength2) {
            if (tempArray1[i] <= tempArray2[j]) {
                arr[k] = tempArray1[i];
                i++;
            } else {
                arr[k] = tempArray2[j];
                j++;
            }
            k++;
        }
        // Checking for temp1 array exhaustness
        while (i < tempLength1) {
            arr[k] = tempArray1[i];
            i++;
            k++;
        }
        // Checking for temp2 array exhaustness
        while (j < tempLength2) {
            arr[k] = tempArray2[j];
            j++;
            k++;
        }
    }

    // halving and then merging back
    static void sort(int arr[], int left, int right) {
        if (left < right) {
            int mid = left + (right - left) / 2;
            sort(arr, left, mid);
            sort(arr, mid + 1, right);
            merge(arr, left, mid, right);
        }
    }

    // printing the input array
    static void printArray(int nums[]) {
        for (int i = 0; i < nums.length; i++) {
            System.out.print(nums[i] + " ");
        }
        System.out.println();
    }

    // Driver method
    public static void main(String args[]) {
        int arr[] = { 12, 11, 13, 5, 6, 7 };

        System.out.println("Given Array");
        printArray(arr);
        sort(arr, 0, arr.length - 1);

        System.out.println("Sorted Array");
        printArray(arr); // 5 6 7 11 12 13

        System.out.println("********************");
        int arr1[] = { 56, 0, 8, 51, 9 };

        System.out.println("Given Array");
        printArray(arr1);
        sort(arr1, 0, arr1.length - 1);

        System.out.println("Sorted Array");
        printArray(arr1); // 0 8 9 51 56
    }

}