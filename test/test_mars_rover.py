import unittest
from app.mars_rover import MarsRover
from app.grid import Grid

class MarsRoverTester(unittest.TestCase):
    def setUp(self):
        self.grid = Grid()
        self.mr = MarsRover(self.grid)

    def test_initial_position(self):
        self.assertEqual(self.mr.getPosition(), (0,0))

    def test_initial_orientation(self):
        self.assertEqual(self.mr.getOrientation(), "N")

    def test_face_N(self):
        self.assertEqual(self.mr.getOrientation(), "N")

    def test_face_E(self):
        self.mr.turnRight()
        self.assertEqual(self.mr.getOrientation(), "E")

    def test_face_W(self):
        self.mr.turnLeft()
        self.assertEqual(self.mr.getOrientation(), "W")

    def test_move_F(self):
        self.mr.moveF()
        self.assertEqual(self.mr.getPosition(), (0,1))

    def test_size_of_grid(self):
        self.assertEqual(self.grid.getSize(), (100,100))

    def test_wrap_the_grid_N(self):
        initial_position = self.mr.getPosition()
        for i in range(initial_position[1], self.mr.getGrid().getSize()[1]):
            self.mr.moveF()
        self.assertEquals(self.mr.getPosition(), initial_position)

    def tearDown(self):
        pass
