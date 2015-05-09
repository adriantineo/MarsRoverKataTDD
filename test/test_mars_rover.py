import unittest
from app.mars_rover import MarsRover

class MarsRoverTester(unittest.TestCase):
    def setUp(self):
        self.mr = MarsRover()

    def test_initial_position(self):
        self.assertEqual(self.mr.position, (0,0))

    def test_initial_orientation(self):
        self.assertEqual(self.orientation, "N")

    def tearDown(self):
        pass
