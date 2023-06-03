
# Travelling Salesman Problem Solver

This repository contains a Python program to solve the Travelling Salesman Problem (TSP) using the Lin-Kernighan algorithm. Given a set of cities and their coordinates, the program finds the optimal tour that visits each city exactly once and returns to the starting city.

## Usage

To use the program, follow these steps:

1. Install the required dependencies by running the following command:

pip install osmnx requests


2. Replace the `city_names` list with the names of the cities you want to visit. Make sure the names are in the format "Place Name, City". For example:
```python
city_names = [
    "Kozhikode Beach,Kozhikode",
    "Tali Temple,Kozhikode",
    "Mananchira Square,Kozhikode",
    "Chevayur,Kozhikode",
    "Hilite Mall,Kozhikode"
]

3. Run the program by executing the script:

python tsp_solver.py

4. The program will output the optimal tour starting from the specified city and its cost. For example:

Optimal tour starting from Chevayur, Kozhikode:
Chevayur, Kozhikode -> Kozhikode Beach, Kozhikode -> Tali Temple, Kozhikode -> Hilite Mall, Kozhikode -> Mananchira Square, Kozhikode -> Chevayur, Kozhikode

Optimal cost:  32.78

## Dependencies

The program relies on the following dependencies:

osmnx: Used to obtain the coordinates of the specified cities using OpenStreetMap data.
requests: Used to query the Open Source Routing Machine (OSRM) API to calculate the distances between cities.


