from functions import *

def main():
	line = open('nums.txt', 'r').read()
	nums = [int(i) for i in line.split(' ')]

	print("Минимальное число: ", get_min(nums))
	print("Максимальное число: ", get_max(nums))
	print("Сумма чисел: ", get_sum(nums))
	print("Произведение чисел: ", get_mul(nums))

main()
