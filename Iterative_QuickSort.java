///Time and space complexity
//Time Complexity: O(n*log n)
//Space Complexity: O(n)
package Precourse2;
public class Iterative_QuickSort {
		static int partition(int arr[], int low, int high)
		{
			int pivot = arr[high];
			int i = (low - 1);
			for (int j = low; j <= high - 1; j++) {
				if (arr[j] <= pivot) {
					i++;
					int temp = arr[i];
					arr[i] = arr[j];
					arr[j] = temp;
				}
			}
			int temp = arr[i + 1];
			arr[i + 1] = arr[high];
			arr[high] = temp;
			return i + 1;
		}
		static void quickSortIterative(int arr[], int l, int h)
		{
			int[] stack = new int[h - l + 1];
			int top = -1;
			stack[++top] = l;
			stack[++top] = h;
			while (top >= 0) {
				h = stack[top--];
				l = stack[top--];
				int p = partition(arr, l, h);
				if (p - 1 > l) {
					stack[++top] = l;
					stack[++top] = p - 1;
				}
				if (p + 1 < h) {
					stack[++top] = p + 1;
					stack[++top] = h;
				}
			}
		}
		public static void main(String args[])
		{
			int arr[] = { 9, 5, 5, 2, 1, 7, 1, 2 };
			int n = 8;
			quickSortIterative(arr, 0, n - 1);
			for (int i = 0; i < n; i++) {
				System.out.print(arr[i] + " ");
			}
		}
}
