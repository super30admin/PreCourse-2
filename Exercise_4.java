import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

/*
Exercise_4 : Merge Sort.
// Time Complexity: O(N log(N))
// Space Complexity: O(N)
 */
class MergeSort {
    // Merges two subarrays of arr[]. 
    // First subarray is arr[l..m] 
    // Second subarray is arr[m+1..r] 
    void merge(int[] arr, int l, int m, int r) {

        int n1 = m - l + 1;
        int n2 = r - m;

        int[] L = Arrays.copyOfRange(arr, l, m + 1);
        int[] R = Arrays.copyOfRange(arr, m + 1, r + 1);

        final int[] i = {0};
        final int[] j = {0};
        int k = l;

        List<Integer> merged = IntStream.range(0, n1 + n2)
                .map(index -> {
                    if (i[0] < n1 && (j[0] >= n2 || L[i[0]] <= R[j[0]])) {
                        return L[i[0]++];
                    } else {
                        return R[j[0]++];
                    }
                })
                .boxed()
                .toList();

        for (int num : merged) {
            arr[k++] = num;
        }

    }

    // Main function that sorts arr[l..r] using 
    // merge() 
    void sort(int[] arr, int l, int r) {
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
    static void printArray(int arr[]) {
        int n = arr.length;
        for (int j : arr) System.out.print(j + " ");
        System.out.println();
    }

    // Driver method 
    public static void main(String args[]) {
        int[] arr = {12, 11, 13, 5, 6, 7};

        System.out.println("Given Array");
        printArray(arr);

        MergeSort ob = new MergeSort();
        ob.sort(arr, 0, arr.length - 1);

        System.out.println("\nSorted array");
        printArray(arr);
    }
} 