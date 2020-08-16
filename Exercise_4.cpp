#include<stdlib.h> 
#include<stdio.h> 

// Merges two subarrays of arr[]. 
// First subarray is arr[l..m] 
// Second subarray is arr[m+1..r] 
void merge(int arr[], int l, int m, int r)
{
    //Your code here
    const int M = m - l + 1; //left array[l,mid]
    const int N = r - m; //right array [mid+1,r]
    int* left_array = new int[M];
    int* right_array = new int[N];
    //to traverse through each array
    

    for (int i = 0;i < M;i++) {
        left_array[i] = arr[l+i];
    }
    for (int i = 0;i < N;i++) {
        right_array[i] = arr[m+1+i];
    }
    int i = 0, j = 0, k = l;
    while (i < M && j < N) {
        if (left_array[i] <= right_array[j]) {
            arr[k++] = left_array[i++];
        }
        else {
            arr[k++] = right_array[j++];
        }
    }

    while (i < M) {
        arr[k++] = left_array[i++];
    }
    while (j < N) {
        arr[k++] = right_array[j++];
    }
    delete [] left_array;
    delete [] right_array;
}

/* l is for left index and r is right index of the
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r)
{
    //Your code here
    if (l < r) {
        int mid = (l + r) / 2;
        mergeSort(arr, l, mid);
        mergeSort(arr, mid + 1, r);
        merge(arr, l, mid, r);
    }
}

/* UTILITY FUNCTIONS */
/* Function to print an array */
void printArray(int A[], int size)
{
    int i;
    for (i = 0; i < size; i++)
        printf("%d ", A[i]);
    printf("\n");
}

/* Driver program to test above functions */
int main()
{
    int arr[] = { 12, 15, 13, 5, 6, 7 };
    int arr_size = sizeof(arr) / sizeof(arr[0]);

    printf("Given array is \n");
    printArray(arr, arr_size);

    mergeSort(arr, 0, arr_size - 1);

    printf("\nSorted array is \n");
    printArray(arr, arr_size);
    return 0;
}