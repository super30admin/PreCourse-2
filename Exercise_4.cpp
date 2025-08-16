// Time Complexity :  O(nlogn) n for no of merges + log n for splitting list
// into half each iteration
// Space Complexity : O(n), extra space taken for holding left and right array
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : No
#include <bits/stdc++.h>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

// Merges two subarrays of arr[].
// First subarray is arr[l..m]
// Second subarray is arr[m+1..r]
void merge(int arr[], int l, int m, int r) {
  // Your code here
  // vector<int> arr1;
  // for (int i = l; i <= m; i++) {
  //   arr1.push_back(arr[i]);
  // }
  // vector<int> arr2;
  // for (int i = m + 1; i <= r; i++) {
  //   arr2.push_back(arr[i]);
  // }
  int n1 = m - l + 1;
  int n2 = r - m;
  // int n1 = (int)arr1.size();
  // int n2 = (int)arr2.size();
  int arr1[n1];
  int arr2[n2];
  int k = l;

  for (int i = 0; i < n1; i++) {
    arr1[i] = arr[k++];
  }

  for (int i = 0; i < n2; i++) {
    arr2[i] = arr[k++];
  }

  int i = 0;
  int j = 0;
  k = l;
  while (i < n1 || j < n2) {
    if (j == n2 || (i < n1 && arr1[i] <= arr2[j])) {
      arr[k++] = arr1[i++];
    } else {
      arr[k++] = arr2[j++];
    }
  }
}

/* l is for left index and r is right index of the
   sub-array of arr to be sorted */
void mergeSort(int arr[], int l, int r) {
  // Your code here
  if (l >= r) {
    return;
  }
  int mid = l + (r - l) / 2;
  mergeSort(arr, l, mid);
  mergeSort(arr, mid + 1, r);
  merge(arr, l, mid, r);
}

/* UTILITY FUNCTIONS */
/* Function to print an array */
void printArray(int A[], int size) {
  int i;
  for (i = 0; i < size; i++)
    printf("%d ", A[i]);
  printf("\n");
}

/* Driver program to test above functions */
int main() {
  int arr[] = {12, 11, 13, 5, 6, 7};
  int arr_size = sizeof(arr) / sizeof(arr[0]);

  printf("Given array is \n");
  printArray(arr, arr_size);

  mergeSort(arr, 0, arr_size - 1);

  printf("\nSorted array is \n");
  printArray(arr, arr_size);
  return 0;
}