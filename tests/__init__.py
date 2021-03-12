import unittest

from .test_average import TestAverage
from .test_extrema import TestExtrema
from .test_functional import TestFunctional
from .test_fundamental import TestFundamental
from .test_momentum import TestMomentum
from .test_order import TestOrder
from .test_statistics import TestStatistics


def run():
    test_suite = unittest.TestSuite()

    items = [
        TestAverage,
        TestExtrema,
        TestFunctional,
        TestFundamental,
        TestMomentum,
        TestOrder,
        TestStatistics,
    ]

    for each in items:
        test_suite.addTest(unittest.makeSuite(each))

    runner = unittest.TextTestRunner(verbosity=1)
    result = runner.run(test_suite)

    if result.wasSuccessful():
        exit(0)
    else:
        exit(1)
