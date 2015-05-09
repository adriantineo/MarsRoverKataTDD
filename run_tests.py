import unittest
from test.test_mars_rover import MarsRoverTester

suite = unittest.TestLoader().loadTestsFromTestCase(MarsRoverTester)
unittest.TextTestRunner(verbosity=2).run(suite)