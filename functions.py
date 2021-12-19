def get_min(nums):
	min_idx = 0

	for idx in range(len(nums)):
		if (nums[idx] < nums[min_idx]):
			min_idx = idx 

	return nums[min_idx]

def get_max(nums):
	max_idx = 0

	for idx in range(len(nums)):
		if (nums[idx] > nums[max_idx]):
			max_idx = idx 

	return nums[max_idx]

def get_sum(nums):
	summ = 0

	for num in nums:
		summ += num

	return summ

def get_mul(nums):
	mul = 1

	for num in nums:
		mul *= num

	return mul 