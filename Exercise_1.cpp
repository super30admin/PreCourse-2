/*
	Problem Statement: Implement Iterative Binary Search

	Time Complexity: 
	binarySearch(): O(log n)

	Space Complexity:
	binarySearch(): O(1)
*/
#include <cmath>
#include <iostream> 

using namespace std;

int binarySearch(int arr[], int l, int r, int target) {   
    while (l < r) {
        int mid = floor((l + r) / 2);
        
        if (arr[mid] == target) {
            return mid;
        }

        if (arr[mid] < target) {
            l = mid + 1;
        } else {
            r = mid;
        }
    }
    return -1;
} 
  
int main(void) 
{ 
    int arr[] = { 2, 3, 4, 10, 40 }; 
    int n = sizeof(arr) / sizeof(arr[0]); 
    int x = 10; 
    int result = binarySearch(arr, 0, n - 1, x); 
    (result == -1) ? printf("Element is not present in array.\n") 
                   : printf("Element is present at index %d.\n", 
                            result); 
    return 0; 
} 