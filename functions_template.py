#!/usr/bin/env python
# coding: utf-8

# In[67]:


# imports
# phase 1 imports
import point
import region
import utils
import math
import matplotlib
import matplotlib.pyplot as plt
import trajectory
from datetime import datetime
from typing import List

listOfTrajectories = utils.importTrajectories("Trajectories")

class Point:
    def __init__(self, x, y):
        self.X = x
        self.Y = y
        
def number(user_1):
    l_index = -1
    listOfTrajectories = utils.importTrajectories("Trajectories")
    for j, i in enumerate(listOfTrajectories):
        if user_1 == i.number:
            l_index = j
            break
    return l_index

#For Douglas Pecker algorithm
def calculateDistance(point: Point, p1: Point, p2: Point):
    m = (p2.Y - p1.Y) / (p2.X - p1.X) if (p2.X - p1.X) != 0 else math.inf
    a = m
    b = -1
    c = -(m * p1.X - p1.Y)
    d = abs((a * point.X + b * point.Y + c)) / (math.sqrt(a * a + b * b))
    return d


# Calculate the Euclidean distance between two points (p1 and p2)
def calculate_distance(p1, p2):
    

    return math.sqrt((p2.X - p1.X)**2 + (p2.Y - p1.Y)**2)



def listTraj(listOfTrajectories):
    trajectories = []
    for traj in listOfTrajectories:
        trajectories += [[traj]]
    return trajectories


def simplify_trajectories(trajectories, epsilon):
    simplified_trajectories = []
    for trajectory in trajectories:
        simplified_points = douglasPeucker(trajectory[0].points, epsilon)
        simplified_trajectories.append([simplified_points,trajectory[0].number])
    return simplified_trajectories


def vis(trajectories):
    plt.figure(figsize=(10,8))
    for trajec in trajectories:
        x = []
        y = []
        for traj in trajec[0]:
            x.append(traj.X)
            y.append(traj.Y)
        plt.plot(x, y, label="Trajectory {}".format(str(trajec[1])))
     
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('Trajectory Visualization')
    plt.legend()
    plt.show() 



def plot_trajectories_with_line(T0, T1, closest_point_t0, closest_point_t1):
    x0 = []
    y0 = []   
    x1 = []
    y1 = []
   
    for traj in T0.points:
        x0.append(traj.X)
        y0.append(traj.Y)
        
    for traje in T1.points:
        x1.append(traje.X)
        y1.append(traje.Y)
        
    plt.figure(figsize=(10, 8))

    # Plot trajectory T0 in blue
    plt.plot(x0, y0, label='Trajectory T0', color='blue')

    # Plot trajectory T1 in red
    plt.plot(x1, y1, label='Trajectory T1', color='red')

    # Plot the closest points in the two trajectories as green points
    plt.scatter([closest_point_t0.X, closest_point_t1.X],
                [closest_point_t0.Y, closest_point_t1.Y], color='black')

    # Draw a dotted line between the closest points
    plt.plot([closest_point_t0.X, closest_point_t1.X],
             [closest_point_t0.Y, closest_point_t1.Y], color='green', linestyle='dotted')

    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('Trajectory Visualization with Closest Pair Line')
    plt.legend()
    plt.show()


def euclidean_distance(p1: point.point, p2: point.point) -> float:
    return math.sqrt((p1.X - p2.X) ** 2 + (p1.Y - p2.Y) ** 2)

def point_in_region(query_point: point.point, query_region: region.region) -> bool:
    distance = euclidean_distance(query_point, query_region.center)
    return distance <= query_region.radius



def douglasPeucker(traj:trajectory,epsilon) -> trajectory:
    dmax = 0
    index = 0
    end = len(traj)
    for i in range(1, end - 1):
        d = calculateDistance(traj[i], traj[0], traj[end - 1])
        if d > dmax:
            index = i
            dmax = d

    if dmax > epsilon:
        rec_results1 = douglasPeucker(traj[:index + 1], epsilon)
        rec_results2 = douglasPeucker(traj[index:end], epsilon)

        return rec_results1[:-1] + rec_results2

    return [traj[0], traj[end - 1]]

def slidingWindow(traj:trajectory,epsilon) -> trajectory:
    approximate_trajectory = []
    window_size = 3
    window = [traj[0]]  # Start with the first point as the anchor point
    for i in range(1, len(traj)):
        # Add the current point to the sliding window
        window.append(traj[i])

        # Apply Douglas-Peucker algorithm to the current window traj
        simplified_traj = douglasPeucker(window, epsilon)

        # If the window size is exceeded, remove the last point from the window
        # (which caused the highest error) and start a new window with the last point as the anchor
        if len(simplified_traj) > window_size:
            window.pop()
            approximate_trajectory.extend(simplified_traj[:-1])  # Add the simplified traj to the approximate trajectory
            window = [window[-1]]  # Start a new window with the last point as the anchor

    # After processing all traj, add the last window traj to the approximate trajectory
    approximate_trajectory.extend(window)
    
    return approximate_trajectory

    
def closestPairDistance(traj0:trajectory,traj1:trajectory) -> float:
    min_distance = float('inf')
    closest_point_traj0 = None
    closest_point_traj1 = None

    # Loop through all points in trajectory traj0
    for ai in traj0:
        # Loop through all points in trajectory traj1
        for bj in traj1:
            # Calculate the distance between the current pair of points
            dist = calculate_distance(ai, bj)
            # Update the minimum distance if the current distance is smaller
            if dist < min_distance:
                min_distance = dist
                closest_point_traj0 = ai
                closest_point_traj1 = bj
            if ai.X == bj.X and ai.Y == bj.Y:
                min_distance = 0
                closest_point_traj0 = ai
                closest_point_traj1 = bj
    return min_distance, closest_point_traj0, closest_point_traj1


def dynamicTimeWarping(traj0:trajectory,traj1:trajectory) -> float:
    n = len(traj0)
    m = len(traj1)
    
    # Create a matrix to store the interim results
    dtw_matrix = [[float('inf') for _ in range(m+1)] for _ in range(n+1)]

    # Initialize the first row and column of the matrix
    dtw_matrix[0][0] = 0

    # Fill in the matrix using dynamic programming
    for i in range(1, n+1):
        for j in range(1, m+1):
            cost = calculate_distance(traj0[i-1], traj1[j-1])
            dtw_matrix[i][j] = cost + min(dtw_matrix[i-1][j], dtw_matrix[i][j-1], dtw_matrix[i-1][j-1])

    # The final value in the bottom-right cell of the matrix contains the DTW distance
    dtw_distance = dtw_matrix[n][m]
    
   # Parse the timestamp strings into datetime objects
    datetime_format = "%Y-%m-%d:%M:%S:%f"
    timestamp_traj0 = datetime.strptime(traj0[0].timestamp, datetime_format)
    timestamp_traj1 = datetime.strptime(traj1[0].timestamp, datetime_format)
    
    # Calculate the temporal distance between the starting points of the trajectories
    temporal_distance = abs((timestamp_traj0 - timestamp_traj1).total_seconds())
    
    # Add the temporal distance to the DTW distance
    dtw_distance += temporal_distance
    
    return dtw_distance


def solveQueryWithRTree(r:region,trajectories:list) -> list:
    return None

def solveQueryWithoutRTree(r:region,trajectories:list) -> list:
    inside_trajectories = []
    for i in trajectories:
        for p in i.points:
            if point_in_region(p, r):
                inside_trajectories.append(i)
                break  # Add the trajectory once and move to the next one

    return inside_trajectories


# In[44]:


# listOfTrajectories = utils.importTrajectories("Trajectories")

# trajectories = listTraj(listOfTrajectories)
# epsilon = 0.0001
# simplified_trajectories = simplify_trajectories(trajectories, epsilon)    
# vis(simplified_trajectories)

# # Set the threshold epsilon value and the sliding window size for the sliding window algorithm
# epsilon_sliding = 0.0001
# window_size = 3

# # Apply the sliding window algorithm to each simplified trajectory
# sliding_window_trajectories = []
# for simplified_trajectory in simplified_trajectories:
#     # Extract the points from the simplified trajectory (without the trajectory number)
#     points_only = simplified_trajectory[0]
    
#     # Apply the sliding window algorithm to the points
#     sliding_window_points = slidingWindow(points_only, epsilon_sliding)

#     # Add the resulting approximate trajectory (with trajectory number) to the list
#     sliding_window_trajectories.append([sliding_window_points, simplified_trajectory[1]])
    
# # # Visualize the sliding window trajectories
# vis(sliding_window_trajectories)


# In[40]:


# user_1 = int(input(f"Enter the first trajectory number : "))
# user_2 = int(input(f"Enter the second trajectory number : "))
# listOfTrajectories = utils.importTrajectories("Trajectories")

# num_1 = number(user_1)
# num_2= number(user_2)


# # Example usage:
# # Create two sample trajectories (represented as lists of Point objects)
# trajectory_0 = []
# trajectory_1 = []



# for i in listOfTrajectories[num_1].points:
#     trajectory_0.append(i)
# for j in listOfTrajectories[num_2].points:
#     trajectory_1.append(j)
# # Call the CPD function to calculate the closest-pair distance between the two trajectories
# cpd, closest_point_t0, closest_point_t1 = closestPairDistance(trajectory_0, trajectory_1)
# print("Closest-Pair Distance:", cpd)

# print(num_1,num_2)

# # Call the function to display the plot
# plot_trajectories_with_line(listOfTrajectories[num_1], listOfTrajectories[num_2], closest_point_t0, closest_point_t1)




# In[45]:


# trajectory_0 = []
# trajectory_1 = []

# for i in listOfTrajectories[0].points:
#     trajectory_0.append(i)  # Assuming i contains X, Y, and timestamp (T)
# for j in listOfTrajectories[2].points:
#     trajectory_1.append(j)  # Assuming j contains X, Y, and timestamp (T)

# # Call the dynamic_time_warping function to calculate the DTW distance
# dtw_distance = dynamicTimeWarping(trajectory_0, trajectory_1)
# print("Starting point of trajectory 0:", trajectory_0[0].X, trajectory_0[0].Y, trajectory_0[0].timestamp)
# print("Starting point of trajectory 1:", trajectory_1[0].X, trajectory_1[0].Y, trajectory_1[0].timestamp)
# print("Dynamic Time Warping Distance:", dtw_distance)


# In[69]:


# queryRegion = region.region(point.point(0.0012601754558545508, 0.0027251228043638775, 0.0), 0.00003)
# R_tree_without = solveQueryWithoutRTree(queryRegion, listOfTrajectories)
# def vis(trajectories):
#     plt.figure(figsize=(10,8))
#     for trajec in trajectories:
#         x = []
#         y = []
#         for traj in trajec.points:
#             x.append(traj.X)
#             y.append(traj.Y)
#         plt.plot(x, y, label="Trajectory {}".format(trajec.number))
     
#     plt.xlabel('X Coordinate')
#     plt.ylabel('Y Coordinate')
#     plt.title('Trajectory Visualization')
#     plt.legend()
#     plt.show() 
# vis(R_tree_without)
# if R_tree_without:
#     print("Trajectories within the query region:")
#     for s in R_tree_without:
#         print(s.number)
# else:
#     print("No trajectories match the query.")


# In[ ]:




