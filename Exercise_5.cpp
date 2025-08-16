// Time Complexity :  O(nlogn)
// Space Complexity : O(1), Auxilary stack space: no space since we did it
// iteratively
// Did this code successfully run on Leetcode : Yes Any problem you
// faced while coding this : No
#include <bits/stdc++.h>
using namespace std;

// A utility function to swap two elements
void swap(int *a, int *b) {
  int t = *a;
  *a = *b;
  *b = t;
}

/* This function is same in both iterative and recursive*/
int partition(int arr[], int l, int h) {
  // Do the comparison and swapping here
  // taking pivot as the high element
  int pivot = arr[h];
  int pivot_index = l;

  for (int j = l; j < h; j++) {
    if (pivot > arr[j]) {
      swap(arr[pivot_index], arr[j]);
      pivot_index++;
    }
  }
  swap(arr[h], arr[pivot_index]);
  return pivot_index;
}

int low_partition(int arr[], int l, int h) {
  // Do the comparison and swapping here
  // taking pivot as the first element
  int pivot = arr[l];
  int pivot_index = l + 1;

  for (int j = l + 1; j <= h; j++) {
    if (pivot > arr[j]) {
      swap(arr[pivot_index], arr[j]);
      pivot_index++;
    }
  }
  swap(arr[l], arr[pivot_index - 1]);
  return pivot_index - 1;
}

/* A[] --> Array to be sorted,
l --> Starting index,
h --> Ending index */
void quickSortIterative(int arr[], int l, int h) {
  // Try to think that how you can use stack here to remove recursion.
  stack<int> s;
  s.push(l);
  s.push(h);
  while (!s.empty()) {
    h = s.top();
    s.pop();
    l = s.top();
    s.pop();
    int partition_index = partition(arr, l, h);
    if (partition_index - 1 > l) {
      s.push(l);
      s.push(partition_index - 1);
    }
    if (partition_index + 1 < h) {
      s.push(partition_index + 1);
      s.push(h);
    }
  }
}

// A utility function to print contents of arr
void printArr(int arr[], int n) {
  int i;
  for (i = 0; i < n; ++i)
    cout << arr[i] << " ";
}

// Driver code
int main() {
  int arr[] = {4, 3, 5, 2, 1, 3, 2, 3};
  int n = sizeof(arr) / sizeof(*arr);
  quickSortIterative(arr, 0, n - 1);
  printArr(arr, n);
  return 0;
}