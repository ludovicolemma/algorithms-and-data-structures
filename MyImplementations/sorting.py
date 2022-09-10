def SelectionSort(A):
	for i in range(len(A)-1):
		minimum = i
		for j in range(len(A[i:])):
			if A[i+j] < A[minimum]:
				minimum = i+j
		A[i], A[minimum] = A[minimum], A[i]
	return A

def InsertionSort(A):
	for i in range(len(A)):
		first_el = A[i]
		j = i-1
		while j >= 0 and A[j] > first_el:
			A[j + 1] = A[j]
			j -= 1
		A[j + 1] = first_el
	return A

def MergeSort(A):
	def merge(A, l, m, r):
		n1 = m - l + 1
		n2 = r - m
		
		L = [A[l+lix] for lix in range(n1)]
		R = [A[m + 1 + rix] for rix in range(n2)]
		
		lix, rix, merged_ix = 0, 0, l
		
		while lix < n1 and rix < n2:
			if L[lix] <= R[rix]:
				A[merged_ix] = L[lix]
				lix += 1
			
			else:
				A[merged_ix] = R[rix]
				rix += 1
			merged_ix += 1
		
		while lix < n1:
			A[merged_ix] = L[lix]
			lix += 1
			merged_ix += 1
		
		while rix < n2:
			A[merged_ix] = R[rix]
			rix += 1
			merged_ix += 1
	
	def divide_merge(A, l, r):
		if l < r:
			#(l+r)//2, but avoids overflow for large l and h 
			m = (l+(r-1))//2
			# Sort first and second halves
			divide_merge(A, l, m)
			divide_merge(A, m+1, r)
			merge(A, l, m, r)
   
	divide_merge(A, 0, len(A)-1)
	return A


def partition(A, low, high):
	pivot = A[high] 
	i = low-1 #getting a index to track where the left hand side ends
	
	for j in range(low, high):
		
		if A[j] <= pivot:
			i = i+1
			A[i], A[j] = A[j], A[i]
			
	A[i+1], A[high] = A[high], A[i+1] #center the pivot
	return i+1 #it returns the index to consider for the left hand side

def QuickSort(A):
	def part_sort(A, low, high):
		if low < high: #until the array is of length 1
				pi = partition(A, low, high) #divide the array into two sub arrays
				part_sort(A, low, pi-1) #it recursively repeat on the left
				part_sort(A, pi+1, high) #the same on the right side
	part_sort(A, 0, len(A)-1)
	return A

def QuickSelect(A, k):
	def part_select(A, i, low, high):
		if low == high: #if the remaining element is 1 just return it
			return A[low]
		if low < high: #if there are elements in the partition
			pi = partition(A, low, high) #partition it
			k = high - pi + 1 #RIGHT numbers higher than pivot, included
			if k == i: #if the number in the right is equal to the request
				return A[k] #return kth largest element
			if k > i: #if RIGHT partition is still greater
				part_select(A, i, pi + 1, high)
			else: #if the RIGHT is smaller the kth el. is on the left
				part_select(A, i-k, low, pi-1)
	part_select(A, k, 0, len(A)-1)
	k_largest = A[-k:]
	return k_largest
