import random
import math
import requests
import osmnx as ox
import json
# Define the number of cities
num_cities = 5

# Define the distance function between two cities using their coordinates
def dist(city1, city2):
    lat1, long1 = city1
    lat2, long2 = city2
    url = "http://router.project-osrm.org/route/v1/driving/{},{};{},{}?overview=false".format(long1, lat1, long2, lat2)
    result = requests.get(url).json()
    distance = result["routes"][0]["distance"]
    return distance/1000 

def get_coords(place):
    # url = "https://api.opencagedata.com/geocode/v1/json"
    # params = {
    #     "q": place,
    #     "key": "cad25f219794449ba17fcbf369468551"
    # }
    # response = requests.get(url, params=params).json()
    # coords = (response["results"][0]["geometry"]["lat"], response["results"][0]["geometry"]["lng"])
    # return coords
    coords=ox.geocode(place)
    return coords

# Example usage
city_names = ["Kozhikode Beach,Kozhikode",
"Tali Temple,Kozhikode",
"Mananchira Square,Kozhikode",
"Chevayur,Kozhikode",
"Hilite Mall,Kozhikode"]
city_coords = [get_coords(name) for name in city_names]
# Generate random coordinates for the cities
#city_coords = [(11.482524380683627, 75.99437153610091),(11.2697579, 75.82526455902655),(11.2052291,75.8122442),(11.80122, 76.00514),(11.66665, 75.7074935)]
#city_coords = [(11.482524380683627, 75.99437153610091),(11.66665, 75.7074935)]
# Generate a distance matrix using the coordinates
dist_matrix = [[dist(city_coords[i], city_coords[j]) for j in range(num_cities)] for i in range(num_cities)]

# Define the distance function between two cities
def dist(city1, city2):
    return dist_matrix[city1][city2]

# Define a function to compute the total distance of a tour
def tour_length(tour):
    return sum(dist(tour[i], tour[i+1]) for i in range(num_cities-1)) + dist(tour[-1], tour[0])

# Define the Lin-Kernighan algorithm
def lin_kernighan(start_city):
    # Generate a random tour starting from the given city
    tour = list(range(num_cities))
    tour.remove(start_city)
    random.shuffle(tour)
    tour.insert(0, start_city)
    
    # Define a function to compute the gain of a move
    def move_gain(tour, i, j):
        a, b, c, d = tour[i-1], tour[i], tour[j-1], tour[j % num_cities]
        return dist(a, b) + dist(c, d) - dist(a, c) - dist(b, d)
    
    # Define a function to apply a 3-opt move
    def apply_3opt(tour, i, j, k):
        new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:k+1][::-1] + tour[k+1:]
        return new_tour

    # Initialize the best tour and its cost
    best_tour, best_cost = tour[:], tour_length(tour)
    
    # Loop until no improvement can be made
    improved = True
    while improved:
        improved = False
        
        # Compute the candidate moves
        moves = [(i, j, k, move_gain(tour, i, k)) for i in range(num_cities-2) for j in range(i+1, num_cities-1) for k in range(j+1, num_cities)]
        moves.sort(key=lambda x: -x[3])
        
        # Try each move in turn
        for move in moves:
            i, j, k, gain = move
            new_tour = apply_3opt(tour, i, j, k)
            new_cost = tour_length(new_tour)
            if new_cost < best_cost:
                best_tour, best_cost = new_tour[:], new_cost
                tour = new_tour
                improved = True
                break

    return best_tour, best_cost
# Label the locations
locations = city_names

start_city =3

best_tour, least_cost = lin_kernighan(start_city)

# Print the optimal tour and its cost
print("Optimal tour starting from {}: ".format(locations[start_city]))
start_index = best_tour.index(start_city)
for i in range(num_cities):
    print("{} -> ".format(locations[best_tour[(start_index+i)%num_cities]]), end="")
print("{}\n".format(locations[best_tour[start_index]]))
print("Optimal cost: ", least_cost)
