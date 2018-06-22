import unittest
import numpy as np
from npv import NPV

class TestNPVClass(unittest.TestCase):

	# test .shift_to() works
	# test .shift_to() checks type
	def test_shift_to(self):
		self.assertAlmostEqual(NPV(1, 100, 0.1).shift_to(0).value, 100 / 1.1)
		self.assertAlmostEqual(NPV(0, 100, 0.1).shift_to(1).value, 100 * 1.1)
		self.assertRaises(TypeError, NPV(1, 100, 0.1).shift_to, "str")
		self.assertRaises(TypeError, NPV(1, 100, 0.1).shift_to, 1.1)

	def test_generate_annuity(self):
		self.assertAlmostEqual(NPV(1, 0, 0.1, 10, 15).generate_annuity().value, 92.16850659)

	# test == works
	# test == checks types
	def test_eq_comparison(self):
		self.assertTrue(NPV(1, 100, 0.1) == NPV(1, 100.00000000001, 0.1))
		self.assertFalse(NPV(1, 100, 0.1) == NPV(0, 100, 0.1))
		self.assertRaises(TypeError, NPV(1,100, 0.1).__eq__, "str")
		self.assertRaises(TypeError, NPV(1,100, 0.1).__eq__, 1)

	# test != works
	# test != checks types
	def test_ne_comparison(self):
		self.assertFalse(NPV(1, 100, 0.1) != NPV(1, 100.00000000001, 0.1))
		self.assertTrue(NPV(1, 100, 0.1) != NPV(0, 100, 0.1))
		self.assertRaises(TypeError, NPV(1,100, 0.1).__ne__, "str")
		self.assertRaises(TypeError, NPV(1,100, 0.1).__ne__, 1)


	# test <= works
	# test <= checks types
	def test_le_comparison(self):
		self.assertTrue(NPV(1, 100, 0.1) <= NPV(1, 100.00000000001, 0.1))
		self.assertTrue(NPV(1, 100, 0.1) <= NPV(0, 100, 0.1))
		self.assertRaises(TypeError, NPV(1,100, 0.1).__le__, "str")
		self.assertRaises(TypeError, NPV(1,100, 0.1).__le__, 1)

	# test < works
	# test < checks types
	def test_lt_comparison(self):
		self.assertFalse(NPV(1, 100, 0.1) < NPV(1, 100.00000000001, 0.1))
		self.assertTrue(NPV(1, 100, 0.1) <= NPV(0, 100, 0.1))
		self.assertRaises(TypeError, NPV(1,100, 0.1).__lt__, "str")
		self.assertRaises(TypeError, NPV(1,100, 0.1).__lt__, 1)


	# test >= works
	# test >= checks types
	def test_ge_comparison(self):
		self.assertTrue(NPV(1, 100, 0.1) >= NPV(1, 100.00000000001, 0.1))
		self.assertFalse(NPV(1, 100, 0.1) >= NPV(0, 100, 0.1))
		self.assertRaises(TypeError, NPV(1,100, 0.1).__ge__, "str")
		self.assertRaises(TypeError, NPV(1,100, 0.1).__ge__, 1)

	# test > works
	# test > checks types
	def test_gt_comparison(self):
		self.assertFalse(NPV(1, 100, 0.1) > NPV(1, 100.00000000001, 0.1))
		self.assertFalse(NPV(1, 100, 0.1) > NPV(0, 100, 0.1))
		self.assertRaises(TypeError, NPV(1,100, 0.1).__gt__, "str")
		self.assertRaises(TypeError, NPV(1,100, 0.1).__gt__, 1)

	# test + works
	# test + checks types
	def test_add(self):
		self.assertEqual(NPV(1, 100, 0.1) + NPV(0, 100, 0.1), NPV(0, 100 + 100 / 1.1, 0.1))
		self.assertRaises(TypeError, NPV(1,100, 0.1).__add__, "str")
		self.assertRaises(TypeError, NPV(1,100, 0.1).__add__, 1)


	# test - (sub and neg) works
	# test - checks types
	def test_sub(self):
		self.assertEqual(NPV(1, 100, 0.1) - NPV(0, 100, 0.1), NPV(0, 100 / 1.1 - 100, 0.1))
		self.assertRaises(TypeError, NPV(1,100, 0.1).__add__, "str")
		self.assertRaises(TypeError, NPV(1,100, 0.1).__add__, 1)

	# test * works (rmul and mul)
	# test * checks types
	def test_mul(self):
		self.assertEqual(NPV(1, 100, 0.1) * 10, NPV(1, 100 * 10, 0.1))
		self.assertRaises(TypeError, NPV(1,100, 0.1).__mul__, "str")
		self.assertRaises(TypeError, NPV(1,100, 0.1).__mul__, NPV(1, 100, 0.1))

	def test_rmul(self):
		self.assertEqual(10 * NPV(1, 100, 0.1), NPV(1, 100 * 10, 0.1))
		self.assertEqual(10 * NPV(1, 100, 0.1), NPV(1, 100, 0.1) * 10)
		self.assertRaises(TypeError, NPV(1,100, 0.1).__rmul__, "str")
		self.assertRaises(TypeError, NPV(1,100, 0.1).__rmul__, NPV(1, 100, 0.1))

	# test / works
	# test / checks types
	# test division by zero
	def test_truediv(self):
		self.assertEqual(NPV(1, 100, 0.1) / 10, NPV(1, 100, 0.1) * (1/10))
		self.assertRaises(TypeError, NPV(1,100, 0.1).__truediv__, "str")
		self.assertRaises(TypeError, NPV(1,100, 0.1).__truediv__, NPV(1, 100, 0.1))
		self.assertRaises(ZeroDivisionError, NPV(1,1, 0.1).__truediv__, 0)

	def test_set_rate(self):
		self.assertEqual(NPV(1, 100, 0).set_rate(0.1).rate , 0.1)
		self.assertRaises(TypeError, NPV(1,100, 0.1).set_rate, "str")
		
	def test_force_add(self):
		self.assertEqual(NPV(1, 100, 0.1).force_add(NPV(1, 100, 0.2)), NPV(0, 174.2424242424, 0))
		self.assertRaises(TypeError, NPV(1, 100, 0.1).force_add, NPV(1, 200, 0.1))

	def test_force_sub(self):
		self.assertEqual(NPV(1, 100, 0.1).force_sub(NPV(1, 100, 0.2)), NPV(1, 7.57575757, 0))
		self.assertRaises(TypeError, NPV(1, 100, 0.1).force_sub, NPV(1, 200, 0.1))

if __name__ == "__main__":
   unittest.main()