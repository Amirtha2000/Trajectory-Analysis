#!/usr/bin/env python
# coding: utf-8

# In[11]:


# imports
import point
import region
import utils
import functions_template as functions
import trajectory
import visualization
listOfTrajectories = utils.importTrajectories("Trajectories")

# # Visualize trajectories
visualization.vis(listOfTrajectories)


# In[12]:


# GUI visual representation of the trajectories with a drop dow
visualization.visGUI(listOfTrajectories)


# In[13]:


# # Simplify at least one of the trajectories with Douglas Peucker and/or Sliding Window Algorithm

# #### Douglas
trajectories = functions.listTraj(listOfTrajectories)
epsilon = 0.0001
simplified_trajectories = functions.simplify_trajectories(trajectories, epsilon)    
functions.vis(simplified_trajectories)


###### Sliding Window Algorithm

epsilon_sliding = 0.0001
window_size = 3

# Apply the sliding window algorithm to each simplified trajectory
sliding_window_trajectories = []
for simplified_trajectory in simplified_trajectories:
    # Extract the points from the simplified trajectory (without the trajectory number)
    points_only = simplified_trajectory[0]
    
    # Apply the sliding window algorithm to the points
    sliding_window_points = functions.slidingWindow(points_only, epsilon_sliding)

    # Add the resulting approximate trajectory (with trajectory number) to the list
    sliding_window_trajectories.append([sliding_window_points, simplified_trajectory[1]])
    
# # Visualize the sliding window trajectories
functions.vis(sliding_window_trajectories)



# Visualize original trajectory and its two simplifications
print("visualizing the original and its simplifications:")
visualization.vis(listOfTrajectories)
functions.vis(simplified_trajectories)
functions.vis(sliding_window_trajectories)



# In[15]:


# Calculate the distance between at least two trajectories with Closest-Pair-Distance and/or Dynamic Time Warping


####Closest- Pair- Distance 

user_1 = int(input(f"Enter the first trajectory number : "))
user_2 = int(input(f"Enter the second trajectory number : "))
listOfTrajectories = utils.importTrajectories("Trajectories")

num_1 = functions.number(user_1)
num_2= functions.number(user_2)

# Example usage:
# Create two sample trajectories (represented as lists of Point objects)
trajectory_0 = []
trajectory_1 = []

for i in listOfTrajectories[num_1].points:
    trajectory_0.append(i)
for j in listOfTrajectories[num_2].points:
    trajectory_1.append(j)
# Call the CPD function to calculate the closest-pair distance between the two trajectories
cpd, closest_point_t0, closest_point_t1 = functions.closestPairDistance(trajectory_0, trajectory_1)
print("Closest-Pair Distance:", cpd)
print(num_1,num_2)
# Call the function to display the plot
functions.plot_trajectories_with_line(listOfTrajectories[num_1], listOfTrajectories[num_2], closest_point_t0, closest_point_t1)



####Dynamic Time Warping 

trajectory_0 = []
trajectory_1 = []

for i in listOfTrajectories[0].points:
    trajectory_0.append(i)  # Assuming i contains X, Y, and timestamp (T)
for j in listOfTrajectories[2].points:
    trajectory_1.append(j)  # Assuming j contains X, Y, and timestamp (T)

# Call the dynamic_time_warping function to calculate the DTW distance
dtw_distance = functions.dynamicTimeWarping(trajectory_0, trajectory_1)
print("Starting point of trajectory 0:", trajectory_0[0].X, trajectory_0[0].Y, trajectory_0[0].timestamp)
print("Starting point of trajectory 1:", trajectory_1[0].X, trajectory_1[0].Y, trajectory_1[0].timestamp)
print("Dynamic Time Warping Distance:", dtw_distance)


# In[ ]:


# Build R-tree with all given 62 trajectories

# Query the trajectories using the built R-tree and the region. Which trajectories lie in the given region?
# This query should return the trajectories with ids 43, 45, 50, 71, 83
# queryRegion = region.region(point.point(0.0012601754558545508,0.0027251228043638775,0.0),0.00003)
# foundTrajectories = functions.solveQueryWithRTree(queryRegion,listOfTrajectories)
# if foundTrajectories != None:
#     if len(foundTrajectories)==0:
#         print("No trajectories match the query.")
#     for t in foundTrajectories:
#         print(t)
import matplotlib.pyplot as plt
queryRegion = region.region(point.point(0.0012601754558545508, 0.0027251228043638775, 0.0), 0.00003)
R_tree_without = functions.solveQueryWithoutRTree(queryRegion, listOfTrajectories)
def vis(trajectories):
    plt.figure(figsize=(10,8))
    for trajec in trajectories:
        x = []
        y = []
        for traj in trajec.points:
            x.append(traj.X)
            y.append(traj.Y)
        plt.plot(x, y, label="Trajectory {}".format(trajec.number))
     
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('Trajectory Visualization')
    plt.legend()
    plt.show() 
vis(R_tree_without)
if R_tree_without:
    print("Trajectories within the query region:")
    for s in R_tree_without:
        print(s.number)
else:
    print("No trajectories match the query.")
    


# %%
