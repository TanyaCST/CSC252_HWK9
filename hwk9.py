# Name:       Tanya Chen, Emily Wang
# Peers:      Maggie Hollis (CSC TA)
# References: Greedy Algotithm Lecture Note 
#             https://docs.python.org/3/library/csv.html
#             https://www.geeksforgeeks.org/python/load-csv-data-into-list-and-dictionary-using-python/
import csv

# with open('color-US-states.csv') as US_map:
#     map_reader = csv.reader(US_map, delimiter=' ', quotechar='|')
#     for row in map_reader:
#         pass

states: dict[str, str] = {}

with open("color-US-states.csv", 'r') as f:
    dict_reader = csv.DictReader(f)
    for row in dict_reader:
        key = row["STATE"]
        value = row["NEIGHBORS"]
        states[key] = value
    
print(states)

#### First Greedy Strategy ####
def strategy_1(states: dict[str, str]):
    states_1: dict[str, list[str]] = {}
    result_1: dict[str, int] = {} # Used to save states and their color

    # Convert the value into a list of string
    for key in states.keys():
        v_1 = states[key].split(",") # Can we use split there for string? I assume not?
        states_1[key] = v_1

    # Check the state with most neighbors first (highest length in value)
    # Sort the dictionary based on the number of neighbors (Use quick sort or merge sort)
    # Define a helper function

    # Start Coloring based on the state with highest
    # Define a set for colored states
    colored:list[str] = []

    # We are using integers to represent the color.
    # 1 represents the first color, 2 represents the 2nd color, etc.
    color:int = 1

    # Keep track of all different colors used in the map
    total_color:list[int] = []

    # Use for loop to loop through every state
    for state in states_1.keys():
        # Use a set to store colors for neighbors
        neighbor_colors: set[int] = set()

        # Check whether current state is colored or not
        # If the current state is not colored, check whether its neighbors are colored
        if state not in colored:
            # Find the color of neighbors
            for neighbor in states_1[state]:
                # pass through the neighbors not being colored
                if neighbor not in colored:
                    continue
                else:
                    neighbor_colors.add(result_1[neighbor])

            # 

        else:
            pass



#### Second Greedy Strategy ####
