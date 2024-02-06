#!/usr/bin/env python
# coding: utf-8

# In[1]:


import unittest
import utils
import point
import region
import utils
import trajectory
import visualization
listOfTrajectories = utils.importTrajectories("Trajectories")

from functions_template import *

class TestMyFunctions(unittest.TestCase):

    def test_calculateDistance(self):
        p1 = Point(1, 1)
        p2 = Point(4, 5)
        p3 = Point(7, 2)
        # Test the calculateDistance function
        self.assertAlmostEqual(calculateDistance(p1, p2, p3), 4.949747 , places=2)

    def test_calculate_distance(self):
        p1 = Point(1, 1)
        p2 = Point(4, 5)
        # Test the calculate_distance function
        self.assertAlmostEqual(calculate_distance(p1, p2), 5.0, places=2)

    def test_douglasPeucker(self):
        traj = [Point(1, 1), Point(2, 2), Point(3, 3), Point(4, 4), Point(5, 5)]
        epsilon = 1.0
        # Test the douglasPeucker function
        simplified_traj = douglasPeucker(traj, epsilon)
        self.assertAlmostEqual(len(simplified_traj), 2)
       
    def test_euclidean_distance(self):
        p1 = Point(1, 1)
        p2 = Point(4, 5)
        # Test the euclidean_distance function
        distance = euclidean_distance(p1, p2)
        self.assertAlmostEqual(distance, 5.0, places=2)
        
    def test_slidingWindow(self):
        # Create a trajectory with points (0, 0), (1, 1), (2, 2), (3, 3), (4, 4)
        
        epsilon = 0.0001
        epsilon_sliding = 0.0001
        window_size = 3

        # Apply the sliding window algorithm to each simplified trajectory
        

        # Test the slidingWindow function
        for i in listOfTrajectories:
            approx_traj = slidingWindow(i.points, epsilon)
            m = len(approx_traj)

        self.assertEqual(m, 40)

    def test_closestPairDistance(self):
        
        
        # Create two trajectories with points (1, 1) and (4, 4)
        traj2 = [Point(1, 1), Point(2, 2), Point(3, 3), Point(4, 4)]
        traj3 = [Point(3, 3), Point(4, 4), Point(5, 5), Point(6, 6)]

        # Test the closestPairDistance function
        min_distance, closest_point_traj0, closest_point_traj1 = closestPairDistance(traj2, traj3)

        # The minimum distance should be 0, and the closest points should be (4, 4) and (4, 4)
        self.assertAlmostEqual(min_distance, 0.0, places=2)
        
        


    
    def test_solveQueryWithoutRTree(self):
        # Create a region with center at (0, 0) and radius 5.0
        listOfTrajectories = utils.importTrajectories("Trajectories")
        queryRegion = region.region(point.point(0.0012601754558545508, 0.0027251228043638775, 0.0), 0.00003)
        R_tree_without = solveQueryWithoutRTree(queryRegion, listOfTrajectories)
        for i in R_tree_without:
            self.assertIn((i.number), [43, 45, 50, 71, 83])

        
       
        
if __name__ == '__main__':
    unittest.main()


# In[ ]:




