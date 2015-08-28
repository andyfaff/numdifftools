'''
Created on 28. aug. 2015

@author: pab
'''
import unittest
import numpy as np
from numpy.testing import assert_array_almost_equal, assert_allclose
from numdifftools.limits import Limit


class TestLimit(unittest.TestCase):

    def test_sinx_divx(self):
        def f(x):
            return np.sin(x)/x
        limf = Limit(f, full_output=True)
        lim, err = limf(0)
        assert_array_almost_equal(lim, 1)
        self.assertTrue(err.error_estimate < 1.77249444610966e-15)

    def test_derivative_of_cos(self):
        x0 = np.pi/2

        def g(x):
            return (np.cos(x0+x)-np.cos(x0))/x
        lim, err = Limit(g, full_output=True)(0)
        assert_allclose(lim, -1)
        self.assertTrue(err.error_estimate < 1e-14)

    def test_residue(self):

        def h(z):
            return -z/(np.expm1(2*z))
        lim, err = Limit(h, full_output=True)(0)
        assert_allclose(lim, -0.5)

        self.assertTrue(err.error_estimate < 1e-14)

    def test_difficult_limit(self):

        def k(x):
            return (x*np.exp(x)-np.exp(x)+1)/x**2
        lim, err = Limit(k, full_output=True)(0)
        assert_allclose(lim, 0.5)

        self.assertTrue(err.error_estimate < 1e-8)


if __name__ == "__main__":
    unittest.main()
