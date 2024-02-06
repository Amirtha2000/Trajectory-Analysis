# Trajectory-Analysis
Traj-alysis
# Programming Project README

## Introduction
This README provides an overview of the programming project for the course. The project focuses on solving tasks related to trajectory data processing and analysis using Python. The program is well-documented, tested, and implemented collaboratively in groups of 3 people.

## Project Structure
- The project contains basic model classes (trajectory, point, region) and a template for the functions and main class.
- Avoid changing the names of the main functions or the set of parameters they take.
- New inner functions can be added as needed.

## Tasks Overview
### Visualize (Basic Function)
- Visualize the imported trajectories, ensuring clarity and creativity.
- Additional features such as different colors for trajectories or a complete GUI are encouraged.

### Preprocessing - Data Reduction
- Implement the Douglas-Peucker algorithm to simplify a given trajectory (basic function).
- Implement the Sliding-Window-Algorithm (feature).
- Visualize one original and one simplified trajectory using the implemented methods (feature).

### Indexing
- Implement distance measures for trajectories:
  - Closest-Pair-Distance (basic function).
  - Dynamic-Time-Warping (feature).
- Implement an R-tree for a set of trajectories, with specified node constraints (basic function).

### Querying
- Regard an R-query for a set of trajectories:
  - Write a method to solve the R-query using the R-tree (basic function).
  - Write a method to solve the R-query without the R-tree (basic function).
  - Compare the time difference between the two implemented methods (feature).

