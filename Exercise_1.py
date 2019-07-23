import math

class BinarySearch:
	def binarySearch(self, arr, l, r, x):
		while True:
			if l > r:
				return -1
			else:
				m = math.floor((l+r)/2)
				if arr[m] < x:
					l = m + 1
				elif arr[m] > x:
					r = m - 1
				else:
					return m

if __name__=="__main__":
	binaryS = BinarySearch()
	arr = [2, 3, 4, 10, 40]
	n = len(arr)
	x = 10
	res = binaryS.binarySearch(arr, 0, n - 1, x)
	if res == -1:
		print("Element not present")
	else:
		print("Element found at index",res)