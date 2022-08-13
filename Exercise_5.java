import java.util.Arrays;
import java.util.Stack;
class IterativeQuickSort
{
	private final int x;
	private final int y;

	IterativeQuickSort(int x, int y)
	{
		this.x = x;
		this.y = y;
	}

	public int getX() { return x; }
	public int getY() { return y; }

	public static void swap (int[] arr, int i, int j)
	{   //for swapping
		int temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
	}

	public static int partition(int a[], int start, int end)
	{   //partition function for dividing array
		int pivot = a[end];
        int pIndex = start;
        for (int i = start; i < end; i++)
		{
			if (a[i] <= pivot)
			{
				swap(a, i, pIndex);
				pIndex++;
			}
		}
        swap (a, pIndex, end);
        return pIndex;
	}


	public static void iterativeQuicksort(int[] a)
	{
		Stack<IterativeQuickSort> stack = new Stack<>();
		int start = 0;
		int end = a.length - 1;
		stack.push(new IterativeQuickSort(start, end));
		while (!stack.empty())
		{   start = stack.peek().getX();
		end = stack.peek().getY();
		stack.pop();
		int pivot = partition(a, start, end);
		if (pivot - 1 > start) {
			stack.push(new IterativeQuickSort(start, pivot - 1));
		}
		if (pivot + 1 < end) {
			stack.push(new IterativeQuickSort(pivot + 1, end));
		}
		}
	}

	public static void main(String[] args)
	{
		int a[] = { 9, -3, 5, 2, 6, 8, -6, 1, 3 };
		iterativeQuicksort(a);
		System.out.println("Sorted Array"+Arrays.toString(a));
	}
}
