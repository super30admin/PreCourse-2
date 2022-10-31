#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <iostream>
// Merges two subarrays of arr[].
// First subarray is arr[l..m]
// Second subarray is arr[m+1..r]
void merge(int arr[], int l, int m, int r)
{
    // Your code here
    int left = m - l + 1;
    int right = r - m;

    int *left_arr = new int[left];
    int *right_arr = new int[right];

    for (int i = 0; i < left; i++)
    {
        /* code */
        left_arr[i] = arr[l + i];
    }
    // std::cout << "Left arr complete";

    for (int j = 0; j < right; j++)
    {
        /* code */
        right_arr[j] = arr[m + 1 + j];
    }
    // std::cout << "Right Arr complete";
    int index_arr_one = 0;
    int index_arr_two = 0;
    int main_arr_index = l;

    while (index_arr_one < left && index_arr_two < right)
    {
        // std::cout << "In while";
        if (left_arr[index_arr_one] > right_arr[index_arr_two])
        {
            arr[main_arr_index] = right_arr[index_arr_two];
            index_arr_two++;
        }

        else
        {
            arr[main_arr_index] = left_arr[index_arr_one];
            index_arr_one++;
        }

        main_arr_index++;
    }

    while (index_arr_one < left)
    {
        arr[main_arr_index] = left_arr[index_arr_one];
        index_arr_one++;
        main_arr_index++;
    }

    while (index_arr_two < right)
    {
        arr[main_arr_index] = right_arr[index_arr_two];
        index_arr_two++;
        main_arr_index++;
    }
    // std::cout << "merge complete";
}

/* l is for left index and r is right index of the
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r)
{
    // Your code here
    if (l < r)
    {
        int m = floor((l + r) / 2);
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
        merge(arr, l, m, r);
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
    int arr[] = {12, 11, 13, 5, 6, 7};
    int arr_size = sizeof(arr) / sizeof(arr[0]);

    printf("Given array is \n");
    printArray(arr, arr_size);

    mergeSort(arr, 0, arr_size - 1);

    printf("\nSorted array is \n");
    printArray(arr, arr_size);
    return 0;
}
