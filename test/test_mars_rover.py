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
        self.assertEqual(self.grid.getSize(), (100,100))

    def test_wrap_the_grid_N(self):
        self.grid = Grid()
        initial_position = self.mr.getPosition()
        for i in range(initial_position[1], self.grid.getSize()[1]):
            self.mr.moveN()
        self.assertEquals(self.mr.getPosition(), initial_position)

    def tearDown(self):
        pass
