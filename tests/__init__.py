import unittest

from .test_average import TestAverage
from .test_extrema import TestExtrema
from .test_fundamental import TestFundamental
from .test_momentum import TestMomentum
from .test_order import TestOrder
from .test_statistics import TestStatistics


def run():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestAverage))
    test_suite.addTest(unittest.makeSuite(TestMomentum))
    test_suite.addTest(unittest.makeSuite(TestFundamental))
    test_suite.addTest(unittest.makeSuite(TestExtrema))
    test_suite.addTest(unittest.makeSuite(TestStatistics))
    test_suite.addTest(unittest.makeSuite(TestOrder))

    runner = unittest.TextTestRunner(verbosity=1)
    result = runner.run(test_suite)

    if result.wasSuccessful():
        exit(0)
    else:
        exit(1)
