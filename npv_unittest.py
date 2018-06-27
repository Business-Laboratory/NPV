import unittest
import numpy as np
from npv import NPV
from npv import generate_annuity

class TestNPVClass(unittest.TestCase):

	def setUp(self):
		self.rate_a = 0.000123456
		self.rate_b = 0
		self.rate_c = 0.1


	# test .shift_to() works
	# test .shift_to() checks type
	# shift_to formula: Price / ((1 + rate) ^ time)
	def test_shift_to(self):
		self.assertAlmostEqual(NPV(1, 100, self.rate_a).shift_to(0).value, 100 / (1+self.rate_a) ** 1)
		self.assertAlmostEqual(NPV(0, 100, self.rate_a).shift_to(1).value, 100 / (1 + self.rate_a) ** -1)
		self.assertRaises(TypeError, NPV(1, 100, self.rate_a).shift_to, "str")
		self.assertRaises(TypeError, NPV(1, 100, self.rate_a).shift_to, 1.1)

	# tests if 10 years of annuity payments of $15 were converted to a NPV
	# NPV of Annuity formula: Price((1 - (1 + rate)^(-Periods)) / rate)
	def test_generate_annuity(self):
		self.assertAlmostEqual(generate_annuity(10, 15, self.rate_c).value, 92.16850659)
		self.assertAlmostEqual(generate_annuity(0, 0, self.rate_a).value, 0)

	# test == works
	# test == checks types
	def test_eq_comparison(self):
		self.assertTrue(NPV(1, 100, self.rate_a) == NPV(1, 100.00000000001, self.rate_a))
		self.assertFalse(NPV(1, 100, self.rate_a) == NPV(0, 100, self.rate_a))
		self.assertRaises(TypeError, NPV(1,100, self.rate_a).__eq__, "str")
		self.assertRaises(TypeError, NPV(1,100, self.rate_a).__eq__, 1)

	# test != works
	# test != checks types
	def test_ne_comparison(self):
		self.assertFalse(NPV(1, 100, self.rate_a) != NPV(1, 100.00000000001, self.rate_a))
		self.assertTrue(NPV(1, 100, self.rate_a) != NPV(0, 100, self.rate_a))
		self.assertRaises(TypeError, NPV(1,100, self.rate_a).__ne__, "str")
		self.assertRaises(TypeError, NPV(1,100, self.rate_a).__ne__, 1)


	# test <= works
	# test <= checks types
	def test_le_comparison(self):
		self.assertTrue(NPV(1, 100, self.rate_a) <= NPV(1, 100.00000000001, self.rate_a))
		self.assertTrue(NPV(1, 100, self.rate_a) <= NPV(0, 100, self.rate_a))
		self.assertRaises(TypeError, NPV(1,100, self.rate_a).__le__, "str")
		self.assertRaises(TypeError, NPV(1,100, self.rate_a).__le__, 1)

	# test < works
	# test < checks types
	def test_lt_comparison(self):
		self.assertFalse(NPV(1, 100, self.rate_a) < NPV(1, 100.00000000001, self.rate_a))
		self.assertTrue(NPV(1, 100, self.rate_a) <= NPV(0, 100, self.rate_a))
		self.assertRaises(TypeError, NPV(1,100, self.rate_a).__lt__, "str")
		self.assertRaises(TypeError, NPV(1,100, self.rate_a).__lt__, 1)


	# test >= works
	# test >= checks types
	def test_ge_comparison(self):
		self.assertTrue(NPV(1, 100, self.rate_a) >= NPV(1, 100.00000000001, self.rate_a))
		self.assertFalse(NPV(1, 100, self.rate_a) >= NPV(0, 100, self.rate_a))
		self.assertRaises(TypeError, NPV(1,100, self.rate_a).__ge__, "str")
		self.assertRaises(TypeError, NPV(1,100, self.rate_a).__ge__, 1)

	# test > works
	# test > checks types
	def test_gt_comparison(self):
		self.assertFalse(NPV(1, 100, self.rate_a) > NPV(1, 100.00000000001, self.rate_a))
		self.assertFalse(NPV(1, 100, self.rate_a) > NPV(0, 100, self.rate_a))
		self.assertRaises(TypeError, NPV(1,100, self.rate_a).__gt__, "str")
		self.assertRaises(TypeError, NPV(1,100, self.rate_a).__gt__, 1)

	# test + works
	# test + checks types
	def test_add(self):
		self.assertEqual(NPV(1, 100, self.rate_a) + NPV(0, 100, self.rate_a), NPV(0, 100 + 100 / (1 + self.rate_a), self.rate_a))
		self.assertRaises(TypeError, NPV(1,100, self.rate_a).__add__, "str")
		self.assertRaises(TypeError, NPV(1,100, self.rate_a).__add__, 1)


	# test - (sub and neg) works
	# test - checks types
	def test_sub(self):
		self.assertEqual(NPV(1, 100, self.rate_a) - NPV(0, 100, self.rate_a), NPV(0, 100 / (1 + self.rate_a) - 100, self.rate_a))
		self.assertRaises(TypeError, NPV(1,100, self.rate_a).__add__, "str")
		self.assertRaises(TypeError, NPV(1,100, self.rate_a).__add__, 1)

	# test * works (rmul and mul)
	# test * checks types
	def test_mul(self):
		self.assertEqual(NPV(1, 100, self.rate_a) * 10, NPV(1, 100 * 10, self.rate_a))
		self.assertRaises(TypeError, NPV(1,100, self.rate_a).__mul__, "str")
		self.assertRaises(TypeError, NPV(1,100, self.rate_a).__mul__, NPV(1, 100, self.rate_a))

	def test_rmul(self):
		self.assertEqual(10 * NPV(1, 100, self.rate_a), NPV(1, 100 * 10, self.rate_a))
		self.assertEqual(10 * NPV(1, 100, self.rate_a), NPV(1, 100, self.rate_a) * 10)
		self.assertRaises(TypeError, NPV(1,100, self.rate_a).__rmul__, "str")
		self.assertRaises(TypeError, NPV(1,100, self.rate_a).__rmul__, NPV(1, 100, self.rate_a))

	# test / works
	# test / checks types
	# test division by zero
	def test_truediv(self):
		self.assertEqual(NPV(1, 100, self.rate_a) / 10, NPV(1, 100, self.rate_a) * (1/10))
		self.assertRaises(TypeError, NPV(1,100, self.rate_a).__truediv__, "str")
		self.assertRaises(TypeError, NPV(1,100, self.rate_a).__truediv__, NPV(1, 100, self.rate_a))
		self.assertRaises(ZeroDivisionError, NPV(1,1, self.rate_a).__truediv__, 0)

	def test_set_rate(self):
		self.assertEqual(NPV(1, 100, 1).set_rate(self.rate_b).rate , self.rate_b)
		self.assertRaises(TypeError, NPV(1,100, self.rate_b).set_rate, "str")
		
	
	def test_force_add(self):
		self.assertEqual(NPV(1, 100, self.rate_c).force_add(NPV(1, 100, 0.2)), NPV(0, 174.2424242424, 0))
		self.assertRaises(TypeError, NPV(1, 100, self.rate_a).force_add, NPV(1, 200, self.rate_a))

	def test_force_sub(self):
		self.assertEqual(NPV(1, 100, self.rate_c).force_sub(NPV(1, 100, 0.2)), NPV(1, 7.57575757, 0))
		self.assertRaises(TypeError, NPV(1, 100, self.rate_a).force_sub, NPV(1, 200, self.rate_a))

if __name__ == "__main__":
   unittest.main()