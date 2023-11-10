#Time Complexity:O(nlog(n))
#Space COmplexity:O(nlog(n))
def partition(arr, l, h):
  pivot=arr[h]
  i=l -1
  j=l
  while(j<h):
    if arr[j]<=pivot:
        i=i+1
        (arr[i], arr[j]) = (arr[j], arr[i])
    j=j+1
  (arr[i + 1], arr[h]) = (arr[h], arr[i + 1])
  return i+1


def quickSortIterative(arr, l, h):
	size = h - l + 1
	stack = [0] * size
	top = -1
	top = top + 1
	stack[top] = l
	top = top + 1
	stack[top] = h
	while top >= 0:
		h = stack[top]
		top = top - 1
		l = stack[top]
		top = top - 1
		p = partition( arr, l, h )
		if p-1 > l:
			top = top + 1
			stack[top] = l
			top = top + 1
			stack[top] = p - 1
		if p+1 < h:
			top = top + 1
			stack[top] = p + 1
			top = top + 1
			stack[top] = h
