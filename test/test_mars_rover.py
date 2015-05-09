import unittest
from app.mars_rover import MarsRover

class MarsRoverTester(unittest.TestCase):
    def setUp(self):
        self.mr = MarsRover()

    def test_initial_position(self):
        self.assertEqual(self.mr.position, (0,0))

    def test_initial_orientation(self):
        self.assertEqual(self.mr.orientation, "N")

    def test_move_N(self):
        self.assertEqual(self.mr.moveN().position, (0,1))

    def tearDown(self):
        pass
