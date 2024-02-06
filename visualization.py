#!/usr/bin/env python
# coding: utf-8

# In[1]:


# phase 1 imports
import point
import region
import utils
import functions_template as functions
import matplotlib
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display
listOfTrajectories = utils.importTrajectories("Trajectories")
print(len(listOfTrajectories))


# In[2]:


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
# vis(listOfTrajectories)


# In[4]:


def visGUI(trajectories):
    
    def number(user_1):
        l_index = -1
        for j, i in enumerate(listOfTrajectories):
            if user_1 == i.number:
                l_index = j
                break
        return l_index
    def plot_selected_trajectory(selected_trajectory):
        straj = number(selected_trajectory)
        traj = trajectories[straj]
        x = [point.X for point in traj.points]
        y = [point.Y for point in traj.points]

        plt.figure(figsize=(10, 8))
        plt.plot(x, y, label="Trajectory {}".format(traj.number))
        plt.xlabel('X Coordinate')
        plt.ylabel('Y Coordinate')
        plt.title('Trajectory Visualization')
        plt.legend()
        plt.show()

    # Create a list of trajectory numbers for the dropdown menu
    trajectory_numbers = [traj.number for traj in trajectories]
    dropdown_menu = widgets.Dropdown(
        options=trajectory_numbers,
        description='Select Trajectory:',
        disabled=False,
    )

    # Create an interactive widget
    interactive_plot = widgets.interactive(plot_selected_trajectory, selected_trajectory=dropdown_menu)

    # Display the widget and the interactive plot
    display(interactive_plot)

# Assuming listOfTrajectories is a list of objects with 'number' and 'points' attributes
# You can call the 'vis' function to display the interactive GUI for visualization
# visGUI(listOfTrajectories)


# In[ ]:




