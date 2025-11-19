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

states: dict[str, list[str]] = {}

with open("color-US-states.csv", 'r') as f:
    dict_reader = csv.DictReader(f)
    for row in dict_reader:
        key = row["STATE"]
        value = [n for n in row["NEIGHBORS"].split(',')] 
        states[key] = value
    
#print(states)


#### First Greedy Strategy ####


#### Second Greedy Strategy ####
# Emily: start w/ fewer neighbors
def color_fewest_neighbor(map: dict[str, list[str]]) -> dict[str,str]:
    """This function colors the map with different color for adjacent areas by coloring the area with fewest neighbor first. 
    BUT specifically the US states, because it has limited colors.
    
    param: (dict[str, list[str]]) map:

    """
    states_sets = set(states.keys())
    colored_states = {state: "" for state in states.keys()}
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"] 
    # it is actually terrible just having 7 colors of the rainbow defined
    # because this code cannot generalize to other complicated maps 
    # but I am only coloring the 50 states, so I want to use it :)

    while states_sets:

        fewest_key: str|None = None
        smallest_len = float('inf')

        for key in states_sets:
            num_neighbors = len(states[key])
            if num_neighbors < smallest_len:
                smallest_len = num_neighbors
                fewest_key = key
        
        if fewest_key is not None:
            if states[fewest_key] == []: 
                colored_states[fewest_key] = colors[0]
            else:
                for color in colors:
                    conflict = False
                    for neighbor in states[fewest_key]:
                        if colored_states[neighbor] == color:
                            conflict = True
                            break
                    if not conflict:
                        colored_states[fewest_key] = color
                        break

            states_sets.remove(fewest_key)

    return colored_states

# # some thoughts

# # find the states with fewest neighbor

# # some extra question: we can either color it one by one based on neighbor 
# # or we can color it first and continue coloring its neighbor?

# # process it
# # check if neighbor is colored in colored_states:
# #   yes: color w/ different color; 
# #   how to find this different color? current thought: we have to go in order: double for loop?
# #   no/else: color it with the first color in list colors, update colored_states

# # remove from states_sets