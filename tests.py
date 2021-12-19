from functions import *

import unittest
import random
import math 

def gen_nums(size):
	nums = []
	for _ in range(size):
		nums.append(random.randint(100, 1000))
	return nums

def gen_negative_nums(size):
	nums = []
	for _ in range(size):
		nums.append(random.randint(-10000, 0))
	return nums

class CommonTest(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(CommonTest, self).__init__(*args, **kwargs)
		self.nums = gen_nums(1000)

	def test_min(self):
		self.assertEqual(get_min(self.nums), min(self.nums))

	def test_max(self):
		self.assertEqual(get_max(self.nums), max(self.nums))
        
	def test_sum(self):
		self.assertEqual(get_sum(self.nums), sum(self.nums))
        
	def test_mul(self):
		self.assertEqual(get_mul(self.nums), math.prod(self.nums))

class BigSizeTest(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(BigSizeTest, self).__init__(*args, **kwargs)
		self.nums = gen_nums(10000)

	def test_min(self):
		self.assertEqual(get_min(self.nums), min(self.nums))

	def test_max(self):
		self.assertEqual(get_max(self.nums), max(self.nums))
        
	def test_sum(self):
		self.assertEqual(get_sum(self.nums), sum(self.nums))
        
	def test_mul(self):
		self.assertEqual(get_mul(self.nums), math.prod(self.nums))

class CommonNegativeTest(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(CommonNegativeTest, self).__init__(*args, **kwargs)
		self.nums = gen_negative_nums(1000)

	def test_min(self):
		self.assertEqual(get_min(self.nums), min(self.nums))

	def test_max(self):
		self.assertEqual(get_max(self.nums), max(self.nums))
        
	def test_sum(self):
		self.assertEqual(get_sum(self.nums), sum(self.nums))
        
	def test_mul(self):
		self.assertEqual(get_mul(self.nums), math.prod(self.nums))

class BigSizeNegativeTest(unittest.TestCase):
	def __init__(self, *args, **kwargs):
		super(BigSizeNegativeTest, self).__init__(*args, **kwargs)
		self.nums = gen_negative_nums(10000)

	def test_min(self):
		self.assertEqual(get_min(self.nums), min(self.nums))

	def test_max(self):
		self.assertEqual(get_max(self.nums), max(self.nums))
        
	def test_sum(self):
		self.assertEqual(get_sum(self.nums), sum(self.nums))
        
	def test_mul(self):
		self.assertEqual(get_mul(self.nums), math.prod(self.nums))

if __name__ == '__main__':
	unittest.main()