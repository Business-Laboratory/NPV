# test primes
import unittest
import numpy as np
from npv import NPV

# write the test first. The funtion will be called is_prime.
class TestNPVClass(unittest.TestCase):

	# test .shift_to() works
	# test .shift_to() checks type
	def test_shift_to(self):
		self.assertAlmostEqual(NPV(1, 100).shift_to(0).value, 100 / 1.1)
		self.assertAlmostEqual(NPV(0, 100).shift_to(1).value, 100 * 1.1)
		self.assertRaises(TypeError, NPV(1, 100).shift_to, "str")
		self.assertRaises(TypeError, NPV(1, 100).shift_to, 1.1)

	# test == works
	# test == checks types
	def test_eq_comparison(self):
		self.assertTrue(NPV(1, 100) == NPV(1, 100.00000000001))
		self.assertFalse(NPV(1, 100) == NPV(0, 100))
		self.assertRaises(TypeError, NPV(1,100).__eq__, "str")
		self.assertRaises(TypeError, NPV(1,100).__eq__, 1)

	# test != works
	# test != checks types
	def test_ne_comparison(self):
		self.assertFalse(NPV(1, 100) != NPV(1, 100.00000000001))
		self.assertTrue(NPV(1, 100) != NPV(0, 100))
		self.assertRaises(TypeError, NPV(1,100).__ne__, "str")
		self.assertRaises(TypeError, NPV(1,100).__ne__, 1)


	# test <= works
	# test <= checks types
	def test_le_comparison(self):
		self.assertTrue(NPV(1, 100) <= NPV(1, 100.00000000001))
		self.assertTrue(NPV(1, 100) <= NPV(0, 100))
		self.assertRaises(TypeError, NPV(1,100).__le__, "str")
		self.assertRaises(TypeError, NPV(1,100).__le__, 1)

	# test < works
	# test < checks types
	def test_lt_comparison(self):
		self.assertFalse(NPV(1, 100) < NPV(1, 100.00000000001))
		self.assertTrue(NPV(1, 100) <= NPV(0, 100))
		self.assertRaises(TypeError, NPV(1,100).__lt__, "str")
		self.assertRaises(TypeError, NPV(1,100).__lt__, 1)


	# test >= works
	# test >= checks types
	def test_ge_comparison(self):
		self.assertTrue(NPV(1, 100) >= NPV(1, 100.00000000001))
		self.assertFalse(NPV(1, 100) >= NPV(0, 100))
		self.assertRaises(TypeError, NPV(1,100).__ge__, "str")
		self.assertRaises(TypeError, NPV(1,100).__ge__, 1)

	# test > works
	# test > checks types
	def test_gt_comparison(self):
		self.assertFalse(NPV(1, 100) > NPV(1, 100.00000000001))
		self.assertFalse(NPV(1, 100) > NPV(0, 100))
		self.assertRaises(TypeError, NPV(1,100).__gt__, "str")
		self.assertRaises(TypeError, NPV(1,100).__gt__, 1)

	# test + works
	# test + checks types
	def test_add(self):
		self.assertEqual(NPV(1, 100) + NPV(0, 100), NPV(0, 100 + 100 / 1.1))
		self.assertRaises(TypeError, NPV(1,100).__add__, "str")
		self.assertRaises(TypeError, NPV(1,100).__add__, 1)


	# test - (sub and neg) works
	# test - checks types
	def test_sub(self):
		self.assertEqual(NPV(1, 100) - NPV(0, 100), NPV(0, 100 / 1.1 - 100))
		self.assertRaises(TypeError, NPV(1,100).__add__, "str")
		self.assertRaises(TypeError, NPV(1,100).__add__, 1)

	# test * works (rmul and mul)
	# test * checks types
	def test_mul(self):
		self.assertEqual(NPV(1, 100) * 10, NPV(1, 100 * 10))
		self.assertRaises(TypeError, NPV(1,100).__mul__, "str")
		self.assertRaises(TypeError, NPV(1,100).__mul__, NPV(1, 100))

	def test_rmul(self):
		self.assertEqual(10 * NPV(1, 100), NPV(1, 100 * 10))
		self.assertEqual(10 * NPV(1, 100), NPV(1, 100) * 10)
		self.assertRaises(TypeError, NPV(1,100).__rmul__, "str")
		self.assertRaises(TypeError, NPV(1,100).__rmul__, NPV(1, 100))

	# test / works
	# test / checks types
	# test division by zero
	def test_truediv(self):
		self.assertEqual(NPV(1, 100) / 10, NPV(1, 100) * (1/10))
		self.assertRaises(TypeError, NPV(1,100).__truediv__, "str")
		self.assertRaises(TypeError, NPV(1,100).__truediv__, NPV(1, 100))
		self.assertRaises(ZeroDivisionError, NPV(1,1).__truediv__, 0)

if __name__ == "__main__":
	unittest.main()
