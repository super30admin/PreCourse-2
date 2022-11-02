"""
	Problem Statement: Implement merge sort.

	Time Complexity: 
	partition(): O(n log n)
	quick_sort(): O(n)

    Space Complexity:
    Auxiliary Space: O(1)

"""
#include <cmath>
#include <iostream>

using namespace std;

void merge(int arr[], int left, int mid, int right) 
{
    int leftArrLength = mid - left + 1;
    int rightArrLength = right - mid;

    int *temp = new int[right - left + 1];

    int leftIdx = left;
    int rightIdx = mid + 1;
    int idx = 0;

    while (leftIdx <= mid && rightIdx <= right) {
        temp[idx++] = arr[leftIdx] < arr[rightIdx] ? arr[leftIdx++] : arr[rightIdx++];
    }

    while (leftIdx <= mid) {
        temp[idx++] = arr[leftIdx++];
    }

    while (rightIdx <= right) {
        temp[idx++] = arr[rightIdx++];
    }

    for (int i = left; i <= right; i++) {
        arr[i] = temp[i-left];
    }

    delete[] temp;
} 

void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        int mid = floor((left + right) / 2);

        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
} 
  
/* UTILITY FUNCTIONS */
/* Function to print an array */
void printArray(int arr[], int size) {  
    for (int i=0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
} 
  
/* Driver program to test above functions */
int main() { 
    int arr[] = {12, 11, 13, 5, 6, 7}; 
    int arr_size = sizeof(arr)/sizeof(arr[0]); 
  
    printf("Given array is \n");
    printArray(arr, arr_size); 
  
    mergeSort(arr, 0, arr_size - 1); 
  
    printf("\nSorted array is \n"); 
    printArray(arr, arr_size); 
    return 0; 
}