import unittest
from app.mars_rover import MarsRover
from app.grid import Grid

class MarsRoverTester(unittest.TestCase):
    def setUp(self):
        self.mr = MarsRover()

    def test_initial_position(self):
        self.assertEqual(self.mr.getPosition(), (0,0))

    def test_initial_orientation(self):
        self.assertEqual(self.mr.getOrientation(), "N")

    def test_move_N(self):
        self.mr.moveN()
        self.assertEqual(self.mr.getPosition(), (0,1))

    def test_size_of_grid(self):
        self.grid = Grid()
        self.assertEqual(self.grid.size, (100,100))

    def tearDown(self):
        pass
